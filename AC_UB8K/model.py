import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import Adam
from keras.utils import np_utils
from sklearn import metrics
from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, \
    f1_score
from keras.callbacks import LearningRateScheduler
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb


def xgboost(X, val_x, y, val_y):
    print(X.shape)
    print(y.shape)
    xgb_train = xgb.DMatrix(X, label=y)
    xgb_test = xgb.DMatrix(val_x, label=val_y)

    params = {
        'objective': 'multi:softmax',
        'eta': 0.05,
        'max_depth': 5,
        'num_class': 10
    }

    watchlist = [(xgb_train, 'train'), (xgb_test, 'test')]
    num_round = 6000
    bst = xgb.train(params, xgb_train, num_round, watchlist)

    pred = bst.predict(xgb_test)

    error_rate = np.sum(pred != val_y) / val_y.shape[0]

    print('测试集错误率(softmax):{}'.format(error_rate))

    accuray = 1 - error_rate
    print('测试集准确率：%.4f' % accuray)

    return


def dnn(X, val_x, y, val_y):
    num_labels = y.shape[1]
    filter_size = 3

    # build model
    model = Sequential()
    model.add(Dense(512, input_shape=(40,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(num_labels))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

    model.fit(X, y, batch_size=64, epochs=5000, validation_data=(val_x, val_y))


def dnns(X, val_x, y, val_y):
    num_labels = y.shape[1]
    nets = 5

    model = [0] * nets
    # model = [0 for k in range(5)]

    # build model
    for net in range(nets):
        model[net] = Sequential()

        model[net].add(Dense(512, input_shape=(40,)))
        model[net].add(Activation('relu'))
        model[net].add(Dropout(0.45))

        model[net].add(Dense(256))
        model[net].add(Activation('relu'))
        model[net].add(Dropout(0.45))

        model[net].add(Dense(num_labels))
        model[net].add(Activation('softmax'))

        model[net].compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='RMSprop')

    # 训练网络
    history = [0] * nets
    epochs = 132
    for j in range(nets):
        X_train2, X_val2, Y_train2, Y_val2 = X, val_x, y, val_y
        history[j] = model[j].fit(X, Y_train2, batch_size=256,
                                  epochs=epochs,
                                  validation_data=(X_val2, Y_val2), verbose=0)
        # score = model[j].evaluate(X_val2, Y_val2, batch_size=256)
        # print("processing model # "+str(j) + " _ " + str(score))
        # for key in history[j].history.keys():
        #     print(key)

        print("DNN {0:d}: Epochs={1:d}, Train accuracy={2:.5f}, Validation accuracy={3:.5f}".format(
            j + 1, epochs, max(history[j].history['accuracy']), max(history[j].history['val_accuracy'])))


    return model,history,nets

def process_show(history,nets):
    # 图示训练过程
    net = -1
    name_title = ['Loss', 'Accuracy']
    fig = plt.figure(figsize=(64, 64))
    for j in range(nets):
        for i in range(0, 2):
            ax = fig.add_subplot(8, 8, i + 1)
            plt.plot(history[j].history[list(history[j].history.keys())[i]],
                     label=list(history[j].history.keys())[i])
            plt.plot(history[j].history[list(history[j].history.keys())[i + 2]],
                     label=list(history[j].history.keys())[i + 2])
            plt.xlabel('Epochs', fontsize=18)
            plt.ylabel(name_title[i], fontsize=18)
            plt.legend()
            plt.show()

# 定义评价指标
def acc(y_test, prediction):
    ### PRINTING ACCURACY OF PREDICTION
    ### RECALL
    ### PRECISION
    ### CLASIFICATION REPORT
    ### CONFUSION MATRIX
    cm = confusion_matrix(y_test, prediction)
    recall = np.diag(cm) / np.sum(cm, axis=1)
    precision = np.diag(cm) / np.sum(cm, axis=0)

    print('Recall:', recall)
    print('Precision:', precision)
    print('\n clasification report:\n', classification_report(y_test, prediction))
    print('\n confussion matrix:\n', confusion_matrix(y_test, prediction))

    ax = sns.heatmap(confusion_matrix(y_test, prediction), linewidths=0.5, cmap="YlGnBu")