
# coding: utf-8

# In[1]:


# -*- encoding: utf-8 -*-
from __future__ import division

#get_ipython().run_line_magic('matplotlib', 'inline')
import tensorflow as tf
import numpy as np
import pandas as pd
import math
import warnings
warnings.filterwarnings('ignore')
batch_size = 16


# In[2]:


def prelu(x, name):
    with tf.variable_scope(name):
        alpha = tf.get_variable(
            'alpha', x.get_shape()[-1],
            initializer=tf.constant_initializer(0.25))
        return tf.maximum(x, 0.0) + alpha * tf.minimum(x, 0.0)


# In[3]:


def inference(input_tensor, regularizer=None, keep_prob=None):

    with tf.variable_scope('layer1') as vc:
        weights = tf.get_variable(
            name='weight',
            shape=[5,1024],
            initializer=tf.random_normal_initializer(stddev=0.02)
        )
        biases = tf.get_variable(
            name='bias',
            shape=[1024],
            initializer=tf.constant_initializer(0.)
        )

        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(weights))
        fc1 = tf.matmul(input_tensor, weights) + biases
        fc1 = tf.nn.relu(fc1, 'layer1')

    with tf.variable_scope('layer2') as vc:
        weights = tf.get_variable(name='weights',
                                  shape=[1024, 1024],
                                  initializer=tf.random_normal_initializer(stddev=0.02))
        biases = tf.get_variable(name='biases',
                                 shape=[1024],
                                 initializer=tf.constant_initializer(0.))
        fc2 = tf.nn.relu(tf.matmul(fc1, weights) + biases, 'layer2')
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(weights))

    with tf.variable_scope('layer3') as vc:
        weights = tf.get_variable(name='weights',
                                  shape=[1024, 1024],
                                  initializer=tf.random_normal_initializer(0.02))
        biases = tf.get_variable(name='biases',
                                 shape=[1024],
                                 initializer=tf.constant_initializer(0.))
        fc3 = tf.nn.relu(tf.matmul(fc2, weights) + biases, 'layer3')
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(weights))

    with tf.variable_scope('layer4') as vc:
        weights = tf.get_variable(
            name='weights',
            shape=[1024, 1024],
            initializer=tf.random_normal_initializer(0.02)
        )
        biases = tf.get_variable(
            name='bias',
            shape=[1024],
            initializer=tf.constant_initializer(0.)
        )

        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(weights))
        fc4 = tf.matmul(fc3, weights) + biases
        fc4 = tf.nn.relu(fc4, 'layer4')

    with tf.variable_scope('layer5') as vc:
        weights = tf.get_variable(
            name='weight',
            shape=[1024, 1024],
            initializer=tf.random_normal_initializer(stddev=0.02)
        )
        biases = tf.get_variable(
            name='biases',
            shape=[1024],
            initializer=tf.constant_initializer(0.)
        )
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(weights))
        fc5 = tf.matmul(fc4, weights) + biases
        fc5 = tf.nn.relu(fc5, 'layer5')

    with tf.variable_scope('layer6') as vc:
        weights = tf.get_variable(
            name='weight',
            shape=[1024, 1024],
            initializer=tf.random_normal_initializer(stddev=0.02)
        )
        biases = tf.get_variable(
            name='biases',
            shape=[1024],
            initializer=tf.constant_initializer(0.)
        )
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(weights))
        fc6 = tf.matmul(fc5, weights) + biases
        fc6 = tf.nn.relu(fc6, 'layer6')
        #fc6 = tf.nn.dropout(fc6, keep_prob=keep_prob)
    # additional layers
    additional_layer = 10
    for i in range(additional_layer):
        with tf.variable_scope('layer%s'%str(i+100)) as vc:
            weights = tf.get_variable(name='weights', shape=[1024, 1024], initializer=tf.random_normal_initializer(stddev=0.02))
            biases = tf.get_variable(name='biases', shape=[1024], initializer=tf.constant_initializer(0.))
            fc6 = tf.nn.relu(tf.matmul(fc6, weights) + biases)
            if regularizer is not None:
                tf.add_to_collection('losses', regularizer(weights))

    with tf.variable_scope('layer7') as vc:
        weights = tf.get_variable(
            name='weights',
            shape=[1024, 6],
            initializer=tf.random_normal_initializer(stddev=0.02)
        )
        biases = tf.get_variable(
            name='biases',
            shape=[6],
            initializer=tf.constant_initializer(0.)
        )

        fc7 = tf.matmul(fc6, weights) + biases
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(weights))
    return fc7



# In[4]:


with tf.name_scope('input') as ns:
    x = tf.placeholder(
        dtype=tf.float32,
        shape=[None, 5],
        name='x-input'
    )

    y = tf.placeholder(
        dtype=tf.float32,
        shape=[None, 6],
        name='y-input'
    )

    keep_prob = tf.placeholder(
        dtype=tf.float32,
        name='is_training'
    )


# In[5]:


with tf.name_scope('regularizer') as ns:
    regularizer = tf.contrib.layers.l2_regularizer(0.01)


# In[6]:

with tf.device('/gpu:0'):
    with tf.name_scope('inference') as ns:
        y_out = inference(x, regularizer=regularizer, keep_prob=keep_prob)


# In[7]:


#loss = tf.losses.huber_loss(y, y_out, delta=10) + tf.add_n(tf.get_collection('losses'))
loss_sq = tf.losses.mean_squared_error(y, y_out)
loss = loss_sq + tf.add_n(tf.get_collection('losses'))
tf.summary.scalar('loss', loss)
# In[8]:


with tf.name_scope('train_step') as ns:
    global_step = tf.Variable(0, trainable=False)
    learning_rate = tf.train.exponential_decay(
        0.001,
        global_step,
        1000,
        0.95,
        staircase=True
    )
    tf.summary.scalar('learning_rate', learning_rate)
    update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss, global_step)


merged_summary_op = tf.summary.merge_all()
saver = tf.train.Saver()
# In[9]:
config = tf.ConfigProto(log_device_placement=True, allow_soft_placement=True)
config.gpu_options.allow_growth = True

sess = tf.Session(config=config)
#init_op = tf.global_variables_initializer()
#sess.run(init_op)
ckpt = tf.train.latest_checkpoint('./model')
if ckpt:
    saver.restore(sess, ckpt)
else:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
summary_writer = tf.summary.FileWriter('./log', sess.graph)
# In[10]:


#from sklearn.model_selection import train_test_split

raw_data = pd.read_csv('./csv_9k/norm_train.csv', header=None)
data = raw_data.values
data_test = pd.read_csv('./csv_9k/norm_test.csv', header=None)
data_test = data_test.values
target_test = pd.read_csv('./csv_9k/w_l_test.csv', header=None)
target_test = target_test.values
target = pd.read_csv('./csv_9k/w_l_train.csv', header=None)
target = target.values
#X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=2333)
shuffle_idx = np.random.permutation(data.shape[0])
data = data[shuffle_idx, :]
target = target[shuffle_idx]
data_csv = pd.DataFrame(data)
#data_csv.to_csv('./norm_train.csv', header=None)
# In[11]:


#data.shape


# In[12]:


#X_train.shape


# In[ ]:


epochs = 100
for epoch in range(epochs):
    start = 0
    for i in range(int(data.shape[0]/batch_size)):
        end = min(start+batch_size, 9000)
        #batch_idx = np.random.choice(49556, 128, replace=True)
        batch_idx = np.random.choice(9000, batch_size, replace=True)
        xs_batch = data[start: end]
        ys_batch = target[start: end]
        start = end
        #xs_batch = data[batch_idx]
        #ys_batch = target[batch_idx]
        feed_dict_batch = {x: xs_batch, y: ys_batch, keep_prob: 1.0}
        _, loss_value, lr_value, summary, global_step_value = sess.run([train_step, loss, learning_rate, merged_summary_op, global_step],
                                 feed_dict=feed_dict_batch)
        summary_writer.add_summary(summary, global_step_value)
        print('epochs: {0}, iterations: {1}, loss: {2}'.format(epoch, i, loss_value))

saver.save(sess, './model/model.ckpt', global_step=global_step)
# In[ ]:


feed_train = {x: data, keep_prob: 1.0}
answer_train = sess.run(y_out, feed_dict=feed_train)
feed_test = {x: data_test, keep_prob: 1.0}
answer_test = sess.run(y_out, feed_dict=feed_test)
loss_test = sess.run(loss, feed_dict={x: data_test, y: target_test, keep_prob: 1.0})
#print('loss_on_test', loss_test)
loss_train = sess.run(loss, feed_dict={x: data, y: target, keep_prob: 1.0})
print('loss_on_train', loss_train)
print(sess.run(learning_rate))

# In[ ]:


# In[ ]:


#sess.run(loss, feed_dict={x: X_test, y: y_test, is_training: False})


# In[ ]:


answer_train = pd.DataFrame(answer_train)
answer_test = pd.DataFrame(answer_test)

# In[ ]:

answer_test.to_csv('./w_l_test.csv', header=None)
#answer_train.to_csv('./w_l_train.csv', header=None)
