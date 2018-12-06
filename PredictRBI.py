import tensorflow as tf
import sys
print(sys.argv)
inputList=[[float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])]]
sess=tf.Session()
save=tf.train.import_meta_graph('models/RBIModels/model.ckpt-1000.meta')
save.restore(sess,tf.train.latest_checkpoint("./models/RBIModels"))
inputs=sess.graph.get_operation_by_name('inputs').outputs[0]
output=sess.graph.get_tensor_by_name('output_layer/Relu:0')
print('Prediction: ',sess.run(output,feed_dict={inputs:inputList}))
