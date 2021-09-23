import tensorflow as tf
from numpy.random import RandomState

#定义训练数据的batch大小
batch_size = 8

#定义神经网络的参数
w1 = tf.Variable(tf.random_normal([2,3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3,1], stddev=1, seed=1))

#定义None是为了适应不同的batch_size
x = tf.placeholder(tf.float32, shape=(None,2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None,1), name='y-input')

#定义神经网络的前向传播过程
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

#定义损失函数和反向传播的算法
y = tf.sigmoid(y)
cross_entropy = -tf.reduce_mean(
    y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))
    + (1-y_) *  tf.log(tf.clip_by_value(1-y, 1e-10, 1.0)))
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

#通过随机数生成一个模拟数据集
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size,2)
Y = [[int(x1+x2 < 1)] for (x1, x2) in X]

#创建一个会话来运行TensorFlow程序
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    #初始化变量
    sess.run(init_op)

    print(sess.run(w1))
    print(sess.run(w2))

    STEP = 5000
    for i in range(STEP):
        start = (i * batch_size) % dataset_size
        end = min(start+batch_size, dataset_size)

        sess.run(
            train_step, feed_dict={x:X[start:end], y_:Y[start:end]}
        )
        if(i % 1000 == 0):
            total_cross_entropy = sess.run(
                cross_entropy, feed_dict={x:X, y_:Y}
            )
            print("After %d training step(s), cross entropy on all data is %g"%(i, total_cross_entropy))

    print(sess.run(w1))
    print(sess.run(w2))
