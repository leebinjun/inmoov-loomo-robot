from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
 
import tensorflow as tf
import numpy as np
 
w = np.int32(28)
h = np.int32(28)
 
def weight_variable(shape, name):
    '''Define weight
    Args:
      shape: The shape of weight.
      name: The name of weight.
    Returns:
      The Variable object
    '''
    return tf.Variable(tf.truncated_normal(shape, stddev=0.1), name=name)
 
def bias_variable(shape, name):
    '''Define bias
    Args:
      shape: The shape of bias
      name: The name of bias
    Returns:
      The Variable object
    '''
    return tf.Variable(tf.constant(0.1, shape=shape), name=name)
 
def model(x, keep_prob):
    '''Build the MNIST model
    Args:
      x: Input, tf.placeholder, the dimension is [-1, 784]
      keep_prob: 
    Returns:
      y: Classification probability
    '''
    
    x_image = tf.reshape(x, [-1, w, h, 1])
 
    # Conv1
    with tf.name_scope('conv1'):
        W_conv1 = weight_variable([3, 3, 1, 16], name="weight")
        b_conv1 = bias_variable([16], name='bias')
        h_conv1 = tf.nn.relu(
            tf.nn.conv2d(x_image, W_conv1, strides=[1,1,1,1], padding="SAME", name='conv')
            + b_conv1)
        h_pool1 = tf.nn.max_pool(h_conv1, ksize=[1,2,2,1], strides=[1,2,2,1],
                                 padding="SAME", name="pool")
 
    # Conv2
    with tf.name_scope('conv2'):
        W_conv2 = weight_variable([3, 3, 16, 32], name="weight")
        b_conv2 = bias_variable([32], name='bias')
        h_conv2 = tf.nn.relu(
            tf.nn.conv2d(h_pool1, W_conv2, strides=[1,1,1,1], padding="SAME", name='conv')
            + b_conv2)
        h_pool2 = tf.nn.max_pool(h_conv2, ksize=[1,2,2,1], strides=[1,2,2,1],
                                 padding="SAME", name="pool")
 
    # fc1
    with tf.name_scope('fc1'):
        W_fc1 = weight_variable([7*7*32, 256], name="weight")
        b_fc1 = bias_variable([256], name='bias')
        h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*32])
        h_fc1 = tf.nn.relu(
            tf.matmul(h_pool2_flat, W_fc1)+b_fc1)
 
    # Dropout
    #keep_prob = tf.placeholder(tf.float32)
    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
 
    # fc2
    with tf.name_scope('fc2'):
        W_fc2 = weight_variable([256, 4], name="weight")
        b_fc2 = bias_variable([4], name='bias')
        y = tf.nn.softmax(
            tf.matmul(h_fc1_drop, W_fc2)+b_fc2, name="output")
 
    return y
