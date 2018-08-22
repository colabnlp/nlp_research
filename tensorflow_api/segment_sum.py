# create by fanfan on 2018/3/10 0010
import tensorflow as tf
c = tf.constant([[1,2,3,4], [-1,-2,-3,-4], [5,6,7,8]])
sess = tf.Session()
result = tf.segment_sum(c, tf.constant([0, 0, 1]))#第二个参数长度必须为3
print("result")
print(sess.run(result))
result_ = tf.segment_sum(c, tf.constant([0, 1, 1]))
print("result_")
print(sess.run(result_))
result__ = tf.segment_sum(c, tf.constant([0, 1, 2]))
print("result__")
print(sess.run(result__))
result2 = tf.unsorted_segment_sum(c, tf.constant([2, 1, 1]),3)#第二个参数长度必须为3
print("result2")
print(sess.run(result2))
result3 = tf.unsorted_segment_sum(c, tf.constant([1, 0, 1]),2)
print("result3")
print(sess.run(result3))
#result4 = tf.unsorted_segment_sum(c, tf.constant([2, 0, 1]),2) #错误，segment_ids[0] = 2 is out of range [0, 2)
result4 = tf.unsorted_segment_sum(c, tf.constant([2, 0, 1]),3)
print("result4")
print(sess.run(result4))
result5 = tf.unsorted_segment_sum(c, tf.constant([3, 1, 0]),5)
print("result5")
print(sess.run(result5))