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
batch_size = 10
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

def eval_noguard(sess, x, keep_prob, predictions, x_list, wl_infile, norm_infile, euc_infile):
    wl_list = []
    norm_list = []

    for item in wl_infile:
        item = item.strip().split(",")
        item_tmp = []
        for ind in item:
            item_tmp.append(float(ind))
        wl_list.append(item_tmp)
    for item in norm_infile:
        item = item.strip().split(",")
        item_tmp = []
        for ind in item:
            item_tmp.append(float(ind))
        norm_list.append(item_tmp)

    euc_dis = 0
    #for item in x_list:
        #euc_dis += item**2
    euc_dis = (x_list[0]/10.0)**2 + (x_list[1]/1e7)**2 + (x_list[2]/10.0)**2 + (x_list[3]/1e2)**2 + (x_list[4]/1e2)**2
    euc_dis = sqrt(euc_dis)
    i = 0
    restore = 0
    bst_step = 9999999999
    flag = 0
    
    for item in euc_infile:
        i += 1
        euc_from_file = float(item.strip())
        #print("============")
        #print euc_from_file
        #print("++++++++++++")
        #print restore
        nstep = euc_from_file - restore
        #print nstep
        #print("++++++++")
        if 1e-8 < nstep < bst_step:
            bst_step = nstep
        if euc_from_file > euc_dis and i != 1:
            euc1 = float(euc_infile[i - 2].strip())
            euc2 = euc_from_file
            input_list = []
            #print ("in1")
            if fabs(euc1 - euc_dis) < fabs(euc2 - euc_dis):
                #print ("in2")
                for k in range(i - 1 - timesteps, i - 1):
                    input_list.append(wl_list[k])
                input_list = np.array(input_list)
                feed_dict = {x:input_list.reshape([-1, timesteps, ydimen]), keep_prob:1.0}
                result = sess.run(predictions, feed_dict = feed_dict)[0]
                return result
            else:
                #print ("in3")
                for k in range(i - timesteps, i):
                    input_list.append(wl_list[k])
                input_list = np.array(input_list)
                feed_dict = {x:input_list.reshape([-1, timesteps, ydimen]), keep_prob:1.0}
                result = sess.run(predictions, feed_dict = feed_dict)[0]
                return result
        elif euc_from_file > euc_dis and i == 1:
            #print ("in4")
            return float(wl_infile[0].strip())
        elif euc_from_file < euc_dis and i == len(euc_infile):
            print ("in5")
            flag = 1
            break
        restore = euc_from_file
    
    input_list = []
    for j in range(len(wl_list) - timesteps, len(wl_list)):
        exist_item_list = wl_list[j]
        input_list.append(exist_item_list)
    input_list = np.array(input_list)
    feed_dict = {x:input_list.reshape([-1, timesteps, ydimen]), keep_prob:1.0}
    result = sess.run(predictions, feed_dict = feed_dict)[0]
    return result

def test2():
    euc_infile = open("./csv_train/euc_dataset_sorted_eucsqrt.csv", "r").readlines()
    wl_infile = open("./csv_train/w_l_dataset_ratio_sorted_eucsqrt.csv", "r").readlines()
    norm_infile = open("./csv_train/norm_dataset_sorted_eucsqrt.csv", "r").readlines()
    tst_norm_infile = open("./csv_test/norm_dataset.csv", "r").readlines()
    tst_wl_infile = open("./csv_test/w_l_dataset_ratio.csv", "r").readlines()
    set_A = wl_infile
    set_B = norm_infile
    set_C = euc_infile
    tst_norm_set = tst_norm_infile
    tst_wl_set = tst_wl_infile
    outfile = open("./check/RNN_tst/wl_rnn.csv", "w")
    csv_write = csv.writer(outfile, dialect = "excel")
    x = tf.placeholder(tf.float32, [None, timesteps, ydimen], name='input_x')
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

    predictions = tf.contrib.layers.fully_connected(outputs, ydimen, activation_fn=tf.nn.relu)
    saver = tf.train.Saver()
    with tf.Session(config = tf.ConfigProto(gpu_options = tf.GPUOptions(allow_growth = True)))  as sess:
        ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            i = 0
            for x_item in tst_norm_set:
                splited_x = x_item.split(",")
                x_list = []
                for ind in splited_x:
                    x_list.append(float(ind))
                result = eval_noguard(sess, x, keep_prob, predictions, np.array(x_list), set_A, set_B, set_C)
                
                csv_write.writerow(result)
               
                tmp_list = tst_wl_set[i].split(",")
                y_list = []
                for ind in tmp_list:
                    y_list.append(float(ind))
                cost = tf.reduce_mean(tf.square(result - y_list))
                
                
                #print(sqrt(cost.eval()))
                i += 1
            outfile.close()

if __name__ == "__main__":
    test2()
