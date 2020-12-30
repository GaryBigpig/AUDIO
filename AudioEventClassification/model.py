import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
import tensorflow as tf
from keras.optimizers import Adam
from keras.utils import np_utils
from sklearn import metrics
from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, \
    f1_score
from keras.callbacks import LearningRateScheduler
import matplotlib.pyplot as plt
import seaborn as sns
from keras.callbacks import ModelCheckpoint
import globle_params

def CNN(X, val_x, y, val_y):
    model=Sequential([
        # Convolution2D(filters=32,kernel_size=2,strides=1,padding='same',activation=tf.nn.relu),
        # MaxPooling2D((2,2),(2,2),padding='same'),
        Convolution2D(filters=16, kernel_size=3, strides=1, padding='same', activation=tf.nn.relu),
        MaxPooling2D((2, 2), (2, 2), padding='same'),
        # Convolution2D(filters=8, kernel_size=5, strides=1, padding='same', activation=tf.nn.relu),
        # MaxPooling2D((2, 2), (2, 2), padding='same'),
        Flatten(),
        Dense(500,activation=tf.nn.relu),
        Dense(300, activation=tf.nn.relu),
        tf.keras.layers.Dropout(rate=0.5),
        Dense(12, activation=tf.nn.softmax)
    ])

    checkpoint = ModelCheckpoint(globle_params.SAVED_MODEL, monitor='val_accuracy', verbose=1,
                                 save_best_only=True, mode='max', save_weights_only=False, period=1)
    callbacks_list = [checkpoint]

    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

    model.fit(X, y, batch_size=50, epochs=5000, validation_data=(val_x, val_y),callbacks=callbacks_list,verbose=2)
    return

def dnn(X, val_x, y, val_y):
    num_labels = y.shape[1]
    # print(num_labels)
    # num_labels1=val_y.shape[1]
    # print(num_labels1)

    # build model
    model = Sequential()
    model.add(Dense(1000, input_shape=(100,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(500))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(300))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(100))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(50))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(num_labels))
    model.add(Activation('softmax'))

    # filepath = "savemodel/weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
    checkpoint = ModelCheckpoint(globle_params.SAVED_MODEL, monitor='val_accuracy', verbose=1,
                                 save_best_only=True, mode='max',save_weights_only=False,period=1)
    callbacks_list = [checkpoint]

    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

    history=model.fit(X, y, batch_size=50, epochs=5000, validation_data=(val_x, val_y),callbacks=callbacks_list,verbose=2)

    name_title = ['Loss', 'Accuracy']
    fig = plt.figure(figsize=(10, 10))
    for i in range(0, 2):
        ax = fig.add_subplot(8, 8, i + 1)
        plt.plot(history.history[list(history.history.keys())[i]],
                 label=list(history.history.keys())[i])
        plt.plot(history.history[list(history.history.keys())[i + 2]],
                 label=list(history.history.keys())[i + 2])
        plt.xlabel('Epochs', fontsize=18)
        plt.ylabel(name_title[i], fontsize=18)
        plt.legend()
        plt.show()
    return

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