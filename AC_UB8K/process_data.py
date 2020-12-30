import pandas as pd
import os
import globle_params
import wave
import matplotlib.pyplot as plt
import numpy as np
import progressbar
import librosa
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.utils import np_utils

def analyseData(metaFile):
    print("Reading configure file: "+metaFile+"...")
    metadatas=pd.read_csv(metaFile,sep=',')
    # print(metadata.head())

    # 查看各个文件夹中的各类声音分布情况
    appended = []
    for i in range(1, 11):
        appended.append(metadatas[metadatas.fold == i]['classID'].value_counts())
    class_distribution = pd.DataFrame(appended)
    class_distribution = class_distribution.reset_index()
    class_distribution['index'] = ["fold" + str(x) for x in range(1, 11)]
    # print(class_distribution)

def audio_path_class(metaFile,audioFileName):
    metadatas = pd.read_csv(metaFile, sep=',')
    metadata = metadatas[metadatas['slice_file_name'] == audioFileName]
    path_name = os.path.join(globle_params.UB8K_PATH+'/audio', 'fold' + str(metadata.fold.values[0]), audioFileName)
    return path_name, metadata['class'].values[0]

def audio_show(audioFile,classID):
    wav_stream = wave.open(audioFile, "rb")
    num_frame = wav_stream.getnframes()  # 获取帧数
    num_channel = wav_stream.getnchannels()  # 获取声道数
    print(num_channel)
    framerate = wav_stream.getframerate()  # 获取帧速率
    num_sample_width = wav_stream.getsampwidth()  # 获取实例的比特宽度，即每一帧的字节数
    str_data = wav_stream.readframes(num_frame)  # 读取全部的帧
    wav_stream.close()  # 关闭流
    wave_data = np.fromstring(str_data, dtype=np.short)  # 将声音文件数据转换为数组矩阵形式
    wave_data.shape = -1, num_channel  # 按照声道数将数组整形，单声道时候是一列数组，双声道时候是两列的矩阵
    wave_data = wave_data.T  # 将矩阵转置
    wave_data = wave_data
    time = np.arange(0, len(wave_data)) * (1.0 / framerate)  # 计算声音的播放时间，单位为秒
    # 画声音波形
    plt.plot(time, wave_data)
    plt.show()
    return wave_data

def MFCC_Feature(metaFile):
    # 读取wav声音文件，并提取器mfcc特征，以及label标签，将其保存

    metadatas = pd.read_csv(metaFile, sep=',')
    bar = progressbar.ProgressBar(maxval=metadatas.shape[0],
                                  widgets=[progressbar.Bar('$', '||', '||'), ' ', progressbar.Percentage()])
    bar.start()
    dataset = [[1 for k in range(2)] for m in range(metadatas.shape[0])]
    print(np.shape(dataset))
    # [[1 for j in range(1, 5)] for i in range(1, 4)]
    for i in range(metadatas.shape[0]):

        file, class_id = audio_path_class(metaFile, metadatas.slice_file_name[i])
        try:
            X, sample_rate = librosa.load(file, res_type='kaiser_fast')
            target_path=os.path.join(globle_params.SAMPLE_PATH,class_id)
            if os.path.exists(target_path) is not True:
                os.makedirs(target_path)
            os.system('cp '+file + ' ' + target_path)
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        except Exception:
            print("Error encountered while parsing file: ", file)
            mfccs, class_id = None, None
        feature = mfccs
        label = class_id
        dataset[i][0], dataset[i][1] = feature, label
        print(str((i/(metadatas.shape[0]))*100)+'%')
        bar.update(i + 1)
    bar.finish()
    # 将声音文件的mfcc特征以及label保存，便于之后的导入
    # np.save(globle_params.MFCC_FEATURE, dataset, allow_pickle=True)
    return


def Read_MFCC_Feature(MFCCFeatureFile):
    data_feature = np.load(MFCCFeatureFile, allow_pickle=True)
    # 查看npy文件的信息共有8732个文件信息以及2列，第一类是mfcc特征，第二列是label标签
    # print(data_feature.shape)
    # print(data_feature[0,0])
    # print(data_feature[0, 1])
    return data_feature

def data_preprocess(MFCCFeatureFile):
    # 导入数据
    data = pd.DataFrame(np.load(MFCCFeatureFile, allow_pickle=True))
    data.columns = ['feature', 'label','test']
    # data.columns = ['feature', 'label']
    # print(data['test'])

    X = np.array(data.feature.tolist())
    y = np.array(data.label.tolist())

    # 数据分割
    X, val_x, y, val_y = train_test_split(X, y)
    print(y)

    # 对标签进行one-hot处理
    lb = LabelEncoder()

    print(lb.fit_transform(y))
    y=lb.fit_transform(y)
    val_y = lb.fit_transform(val_y)
    # y = np_utils.to_categorical(lb.fit_transform(y))
    # val_y = np_utils.to_categorical(lb.fit_transform(val_y))

    return X, val_x, y, val_y


if __name__ == '__main__':
    # analyseData(globle_params.UB8K_METAFILE)
    # path,label=audio_path_class(globle_params.UB8K_METAFILE,'7061-6-0-0.wav')
    # audio_show(path,label)
    MFCC_Feature(globle_params.UB8K_METAFILE)
    # Read_MFCC_Feature(globle_params.MFCC_FEATURE)
    # X, val_x, y, val_y=data_preprocess(globle_params.MFCC_FEATURE)
    # print(y)



