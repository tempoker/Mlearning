import tensorflow as tf 
import input_data



def add_layer(inputs,in_size,out_size,activation_func = None):
	with tf.name_scope('layer'):
		with tf.name_scope('weights'):
			Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
		with tf.name_scope('biases'):
			biases = tf.Variable(tf.ones([1,out_size]),name='biases')
		with tf.name_scope('Wx_plus_b'):
			Wx_plus_b = tf.matmul(inputs,Weights) + biases
			Wx_plus_b = tf.nn.dropout(Wx_plus_b,keep_prob)
		if activation_func is None:
			outputs = Wx_plus_b
		else:
			outputs = activation_func(Wx_plus_b)
		#return Wx_plus_b if not activation_func  else activation_func(Wx_plus_b) 
		return outputs

def weight_init(shape):
	return tf.Variable(tf.truncated_normal(shape,stddev=0.1))

def bias_init(shape):
	return tf.Variable(tf.constant(0.1,shape=shape))

def conv2d(x,W):
	#stride [1,x_move,y_move,1]
	return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
	
def max_pool_2X2(x):
	#stride [1,x_move,y_move,1]
	return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

def accuracy(v_xs,v_ys):
	global pred
	y_pred = ses.run(pred,feed_dict={xs:v_xs,ys:v_ys,keep_prob:1})
	corect_pred = tf.equal(tf.argmax(y_pred,1),tf.argmax(v_ys,1))
	acc = tf.reduce_mean(tf.cast(corect_pred,tf.float32))
	return ses.run(acc,feed_dict={xs:v_xs,ys:v_ys,keep_prob:0.5})
if __name__ =="__main__":
	mnist = input_data.read_data_sets('data/',one_hot=True)

	xs = tf.placeholder(tf.float32,[None,784]) #28*28
	ys = tf.placeholder(tf.float32,[None,10])
	keep_prob = tf.placeholder(tf.float32)
	
	ximg = tf.reshape(xs,[-1,28,28,1])
	#conv1_layer
	W_conv1 = weight_init([5,5,1,32])
	b_conv1 = bias_init([32])
	h_conv1 = tf.nn.relu(conv2d(ximg,W_conv1) + b_conv1) #shape=28*28*32
	h_pool1 = max_pool_2X2(h_conv1) #14*14*32 
	#conv2_layer
	W_conv2 = weight_init([5,5,32,64])
	b_conv2 = bias_init([64])
	h_conv2 = tf.nn.relu(conv2d(h_pool1,W_conv2)+b_conv2)
	h_pool2 = max_pool_2X2(h_conv2)
	#w_fc1
	W_fc1 = weight_init([7*7*64,1024])
	b_fc1 = bias_init([1024])
	h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])
	h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1)+b_fc1)
	h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)
	#w_fc2
	W_fc2 = weight_init([1024,10])
	b_fc2 = bias_init([10])

	pred = tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2)+b_fc2)
	loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=ys,logits=pred))
	#loss = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(pred),reduction_indices=[1]))
	#optm = tf.train.GradientDescentOptimizer(4e-4).minimize(loss) #for test
	optm = tf.train.AdamOptimizer(3e-3).minimize(loss) #Adam:large data to choose
	correct_pred = tf.equal(tf.argmax(pred,1),tf.argmax(ys,1))
	acc = tf.reduce_mean(tf.cast(correct_pred,tf.float32))
	with tf.Session() as ses:
		writer = tf.summary.FileWriter(r'cnn_graph/',ses.graph)
		ses.run(tf.global_variables_initializer())
		for i in range(701):
			batch_xs,batch_ys = mnist.train.next_batch(128)	
			batch_xs_tes,batch_ys_tes = mnist.test.next_batch(128)
			ses.run([optm],feed_dict={xs:batch_xs,ys:batch_ys,keep_prob:0.5})
			if not i % 50 :
				print('Epochs=%03d***acc=%.3f' %(i,ses.run(acc,feed_dict={xs:batch_xs_tes,ys:batch_ys_tes,keep_prob:0.5}))) 
		writer.close()