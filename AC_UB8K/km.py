
import librosa
import numpy as np
import pandas as pd
import process_data
import globle_params
import os

def mfcc(wav_file):
    X, sample_rate = librosa.load(wav_file, res_type='kaiser_fast')
    value = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
    return value

def sample_feature(sample_path):
    result=[]
    for root,dirs,files in os.walk(sample_path):
        for name in files:
            feature=mfcc(os.path.join(root,name))
            # print(name.split('-')[0])
            # print(name.split('-')[1])
            label=name.split('-')[1]
            result.append([feature,label])
    return result

def eucliDist(A,B):
    return np.sqrt(sum(np.power((A - B), 2)))

def cosine_similarity(x, y, norm=False):
    """ 计算两个向量x和y的余弦相似度 """
    # assert len(x) == len(y), "len(x) != len(y)"
    # zero_list = [0] * len(x)
    # if x.all() == zero_list or y.all() == zero_list:
    #     return float(1) if x == y else float(0)

    # method 1
    res = np.array([[x[i] * y[i], x[i] * x[i], y[i] * y[i]] for i in range(len(x))])
    cos = sum(res[:, 0]) / (np.sqrt(sum(res[:, 1])) * np.sqrt(sum(res[:, 2])))

    # method 2
    # cos = bit_product_sum(x, y) / (np.sqrt(bit_product_sum(x, x)) * np.sqrt(bit_product_sum(y, y)))

    # method 3
    # dot_product, square_sum_x, square_sum_y = 0, 0, 0
    # for i in range(len(x)):
    #     dot_product += x[i] * y[i]
    #     square_sum_x += x[i] * x[i]
    #     square_sum_y += y[i] * y[i]
    # cos = dot_product / (np.sqrt(square_sum_x) * np.sqrt(square_sum_y))

    return 0.5 * cos + 0.5 if norm else cos  # 归一化到[0, 1]区间内

def predict_label(DataFeature,SampleFeature):
    minDistance=np.power(10,10)
    maxSimilarity=-1
    result=100
    label=('air_conditioner','car_horn','children_playing',
           'dog_bark','drilling','engin_idling','gun_shot','jackhammer','siren','street_music')
    for record in SampleFeature:
        Distance=eucliDist(record[0],DataFeature)
        Similarity=cosine_similarity(record[0],DataFeature)
        # if Distance<minDistance:
        #     minDistance=Distance
        if Similarity > maxSimilarity:
            maxSimilarity = Similarity
            result=record[1]

    # print(result)
    return label[int(result)]

def predict(SampleFeature,SampleData):
    predict_data=[]
    PredictLable=''
    i=0
    for record in SampleData:
        PredictLable=predict_label(record[0],SampleFeature)
        PredictResult=1 if PredictLable==record[1] else 0
        # print(PredictLable)
        print(PredictLable+"|"+record[1]+':'+str(PredictResult))
        predict_data.append([record[0],record[1],PredictLable,PredictResult])
        # print(predict_data)
        # exit()
        i+=1
        # print(str((i / (SampleData.shape[0])) * 100) + '%')
    return predict_data

def get_acc(data):
    data=np.array(data)
    # print(np.sum(data[:,3]))
    # print(data.shape[0])
    return np.sum(data[:,3])/data.shape[0]


if __name__ == '__main__':
    SampleFeature = sample_feature(globle_params.SAMPLE_PATH)
    SampleData = np.load(globle_params.MFCC_FEATURE, allow_pickle=True)

    # print(SampleFeature[:,0])
    PredictData=predict(SampleFeature,SampleData)
    print(np.shape(PredictData))
    # np.save(globle_params.MFCC_FEATURE, PredictData, allow_pickle=True)
    print(get_acc(PredictData))