import tensorflow as tf


def get_weight_variable(shape, regularizer):
    weights = tf.get_variable('weights', shape, initializer=tf.truncated_normal_initializer(mean=1, stddev=0.1))
    if regularizer is not None:
        tf.add_to_collection('losses', regularizer(weights))
    return weights


def layer(input_tensor, index, in_nodes_cnt, out_nodes_cnt, regularizer, use_action=True):
    with tf.variable_scope('layer{}'.format(index)):
        weights = get_weight_variable([in_nodes_cnt, out_nodes_cnt], regularizer)
        biases = tf.get_variable('biases', [out_nodes_cnt], initializer=tf.truncated_normal_initializer(mean=1, stddev=0.1))
        if use_action:
            return tf.nn.tanh(tf.matmul(input_tensor, weights) + biases)
        else:
            return tf.matmul(input_tensor, weights) + biases


def inference(input_tensor, shape, regularizer):
    temp_input_tensor = input_tensor
    for i in range(1, len(shape)):
        temp_input_tensor = layer(temp_input_tensor, i, shape[i-1], shape[i], regularizer, i!=len(shape)-1)
    return temp_input_tensor
