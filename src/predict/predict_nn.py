import src.nn.network as network
import tensorflow as tf
import src.config as config
import src.train.train_nn as train_nn
import src.data.data_getter as data_getter


def predict(features, labels):
    x = tf.placeholder(tf.float32, [None, config.N_INPUT], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, config.N_OUTPUT])
    y = network.inference(x, config.SHAPE, None)

    correction_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correction_prediction, tf.float32))

    variable_averages = tf.train.ExponentialMovingAverage(train_nn.MOVING_AVERAGE_DECAY)
    variables_to_restore = variable_averages.variables_to_restore()
    saver = tf.train.Saver(variables_to_restore)

    with tf.Session() as sess:
        saver.restore(sess, '/home/liuzhf/workspace/projects/Toothless-Forth/model/toothless.ckpt-14000')
        out, accuracy_score = sess.run([y, accuracy], feed_dict={
            x: features,
            y_: labels
        })
        return out, accuracy_score


def main(argv=None):
    features, labels = data_getter.get_all_data_set(config.CNT_PERIOD)
    out, accuracy_score = predict(features, labels)
    print(out[0:100])
    print("accuracy = {}".format(accuracy_score))


if __name__ == '__main__':
    tf.app.run()
