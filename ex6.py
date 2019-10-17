#x ^ y = (x | y) & ~(x & y)
import tensorflow
import tensorflow as tf
def logical_xor(x, y):
  x = tf.constant([True, True, False, False], dtype = tf.bool)
  y = tf.constant([True, False, True, True], dtype = tf.bool)
  z = tf.logical_xor(x, y)   


