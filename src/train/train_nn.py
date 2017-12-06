import src.nn.network as network
import src.config as config
import tensorflow as tf
import src.data.data_getter as data_getter

CNT_EPOCH = 100
REGULARIZATION_RATE = 0.0001
MOVING_AVERAGE_DECAY = 0.99
LEARNING_RATE_BASE = 0.1
LEARNING_RATE_DECAY = 0.99
BATCH_SIZE = 16

if __name__ == "__main__":

    training_features, training_labels = data_getter.get_training_data_set(weeks=config.CNT_PERIOD)
    test_features, test_labels = data_getter.get_test_data_set(config.CNT_PERIOD)

    x = tf.placeholder(tf.float32, [None, config.N_INPUT], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, config.N_OUTPUT])
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)

    y = network.inference(x, config.SHAPE, regularizer)
    global_step = tf.Variable(0, trainable=False)

    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    variable_averages_op = variable_averages.apply(tf.trainable_variables())
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.argmax(y_, 1), logits=y)
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    loss = cross_entropy_mean + tf.add_n(tf.get_collection('losses'))
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        len(training_labels)/BATCH_SIZE,
        LEARNING_RATE_DECAY
    )
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(loss, global_step=global_step)
    train_op = tf.group(train_step, variable_averages_op)

    correction_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correction_prediction, tf.float32))

    with tf.name_scope("summary"):
        tf.summary.scalar("train_loss", loss)
        merged_summary = tf.summary.merge_all()

    saver = tf.train.Saver()
    with tf.Session() as sess:
        init_op = tf.global_variables_initializer()
        sess.run(init_op)

        train_writer = tf.summary.FileWriter(config.SUMMARY_PATH + "train/", sess.graph)
        test_writer = tf.summary.FileWriter(config.SUMMARY_PATH + "test/", sess.graph)

        for i in range(CNT_EPOCH):
            for n_batch in range(len(training_labels) // BATCH_SIZE):
                xs = training_features[n_batch * BATCH_SIZE: (n_batch+1) * BATCH_SIZE]
                ys = training_labels[n_batch * BATCH_SIZE: (n_batch+1) * BATCH_SIZE]
                _, train_summary, step = sess.run([train_op, merged_summary, global_step]
                                                  , feed_dict={x: xs, y_: ys})
                train_writer.add_summary(train_summary, global_step=step)

                loss_value, test_summary, accuracy_value = sess.run([loss, merged_summary, accuracy], feed_dict={
                    x: test_features,
                    y_: test_labels
                })
                test_writer.add_summary(test_summary, global_step=step)

                if step % 1000 == 0:
                    print('step# {}, loss = {}, accuracy = {}'.format(step, loss_value, accuracy_value))
                    saver.save(sess, config.MODEL_PATH, global_step=global_step)

