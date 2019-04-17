import tensorflow as tf
import numpy as np
import os
#import matplotlib.pyplot as plt
from math import fabs, sqrt
import random
import csv

#training_examples = 10000
#testing_examples = 1000
#sample_gap = 0.01
MODEL_SAVE_PATH = './RNNmodel/'
MODEL_NAME = 'model.ckpt'
ydimen = 6
timesteps = 3
lstm_size = 4096
lstm_layers = 2
batch_size = 3
epochs = 50
norm_infile = open("./csv_train/norm_dataset_sorted_eucsqrt.csv", "r").readlines()
wl_infile = open("./csv_train/w_l_dataset_ratio_sorted_eucsqrt.csv", "r").readlines()

def generate_data2(train_percent):
    norm_train = []
    norm_test = []
    wl_train = []
    wl_test = []
    i = 0
    for item in norm_infile:
        i += 1
        item_list = []
        item = item.strip().split(",")
        for ind in item:
            item_list.append(float(ind))
        if i < len(norm_infile)*train_percent:
            norm_train.append(item_list)
        else:
            norm_test.append(item_list)
    i = 0
    for item in wl_infile:
        i += 1
        item_list = []
        item = item.strip().split(",")
        for ind in item:
            item_list.append(ind)
        if i < len(wl_infile)*train_percent:
            wl_train.append(item_list)
        else:
            wl_test.append(item_list)
    return norm_train, wl_train, norm_test, wl_test


def generate_data(seq):
    X = []
    y = []

    for i in range(len(seq) - timesteps -1):
        X.append(seq[i : i+timesteps])
        y.append(seq[i+timesteps])

    return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)


def get_batches(X, y, batch_size=64):
    for i in range(0, len(X), batch_size):
        begin_i = i
        end_i = i + batch_size if (i+batch_size) < len(X) else len(X)
        yield X[begin_i:end_i], y[begin_i:end_i]

norm_train, wl_train, norm_test, wl_test = generate_data2(0.99)
train_x, train_y = generate_data(wl_train)
test_x, test_y = generate_data(wl_test)

def train():
    outfile = open("train_cost.log", "w")
  
    global_step = tf.Variable(0, trainable=False)
    learning_rate = tf.train.exponential_decay(0.0001, global_step, 5000, 0.5, staircase=True)
    #learning_rate = 0.01
    tf.summary.scalar('learning_rate', learning_rate)
    variable_averages = tf.train.ExponentialMovingAverage(0.99, global_step)
    variable_averages_op = variable_averages.apply(tf.trainable_variables())

    x = tf.placeholder(tf.float32, [None, timesteps, ydimen], name='input_x')
    y_ = tf.placeholder(tf.float32, [None, ydimen], name='input_y')
    keep_prob = tf.placeholder(tf.float32, name='keep_prob')


    lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)
    drop = tf.contrib.rnn.DropoutWrapper(lstm, output_keep_prob=keep_prob)
    def lstm_cell():
        lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)
        lstm = tf.contrib.rnn.DropoutWrapper(lstm, output_keep_prob=keep_prob)
        return lstm
    cell = tf.contrib.rnn.MultiRNNCell([ lstm_cell() for _ in range(lstm_layers)])


    outputs, final_state = tf.nn.dynamic_rnn(cell, x, dtype=tf.float32)
    outputs = outputs[:,-1]

    predictions = tf.contrib.layers.fully_connected(outputs, ydimen, activation_fn=None)
    #cost = tf.losses.mean_squared_error(y_, predictions)
    cost = tf.reduce_mean(tf.square(y_ - predictions))
    tf.summary.scalar('loss', tf.sqrt(cost))
    #optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)
    train_step=tf.train.AdamOptimizer(learning_rate).minimize(cost, global_step = global_step)
    with tf.control_dependencies([train_step, variable_averages_op]):
        train_op = tf.no_op(name="train")

    saver = tf.train.Saver()
    merged_summary_op = tf.summary.merge_all()
    with tf.Session(config = tf.ConfigProto(gpu_options = tf.GPUOptions(allow_growth = True)))  as sess:
        tf.global_variables_initializer().run()
        summary_writer = tf.summary.FileWriter('logs_lstm', tf.get_default_graph())

        iteration = 1
        train_cost_list = []
        train_axi = []
        loss = 0
        for e in range(epochs):
            for xs, ys in get_batches(train_x, train_y, batch_size):
                #print xs
                feed_dict = { x:xs, y_:ys, keep_prob:.5 }
                sess.run(train_step, feed_dict = {x:xs, y_:ys, keep_prob:0.5})
                summary = sess.run(merged_summary_op, feed_dict = {x:xs, y_:ys, keep_prob:0.5})
                summary_writer.add_summary(summary, iteration)
                loss = sess.run(cost, feed_dict={x:xs, y_:ys, keep_prob:1.0})
                pred = sess.run(predictions, feed_dict = {x:xs, y_:ys, keep_prob:1.0})
                #print pred
                loss = sqrt(loss)
                outfile.write(str(loss))
                outfile.write(" ")
                
                if iteration % 100 == 0:
                    print('Epochs:{}/{}'.format(e, epochs),
                          'Iteration:{}'.format(iteration),
                          'Train loss: {:.8f}'.format(loss))
                    
                    
                    print (pred[:10])
                    print ("++++++++++++++++++++++++++++++++++++++")
                    print (ys[:10])
                    print ("======================================")
                    
                iteration += 1
            
            saver.save(
                        sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME),
                        global_step=global_step
                    )
            train_cost_list.append(loss)
            train_axi.append(e)
        outfile.close()
    


if __name__ == "__main__":
    train()
    
