
import ProcessData
import model
import globle_params
import  numpy as np
import tensorflow as tf

if __name__ == '__main__':
    X, val_x, y, val_y = ProcessData.data_preprocess(globle_params.MFCC_FEATURE)
    # model.dnn(X, val_x, y, val_y)
    print(X.shape)
    X=tf.reshape(X,[X.shape[0],10,10,-1])
    print(X.shape)
    val_x = tf.reshape(val_x, [val_x.shape[0],10, 10,-1])
    model.CNN(X, val_x, y, val_y)
    # models,history,nets=model.dnns(X, val_x, y, val_y)

    # # 可视化训练过程
    # model.process_show(history,nets)
    #
    # # 查看评价指标以及混淆矩阵
    # results = np.zeros( (val_x.shape[0],10) )
    # for j in range(nets):
    #   results = results  + models[j].predict(val_x)
    # results = np.argmax(results,axis = 1)
    # val_y_n = np.argmax(val_y,axis =1)
    # model.acc(val_y_n,results)