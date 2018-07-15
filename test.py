import tensorflow as tf
import scipy
print('scipy: %s' % scipy.__version__)
hello = tf.constant('Charles')
sess = tf.Session()
print(sess.run(hello).decode())
