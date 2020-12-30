import os
import globle_params
import AudioSetDownload
import pandas as pd
import librosa
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import LabelBinarizer

def search_file(path):
    result=[]
    for root,dirs,files in os.walk(path):
        for name in files:
            if name[-4:]=='.csv':
                result.append(os.path.join(root,name))
    return result

def MFCC_Feature(path):
    # 读取wav声音文件，并提取器mfcc特征，以及label标签，将其保存
    # path=path+'baby crying'
    dataset=[]
    for root,dirs,files in os.walk(path):
        i = 0
        # print(len(files))
        for name in files:
            record=[]
            # print(name)
            print(root.split('/')[-1])
            file = os.path.join(root, name)
            class_id = root.split('/')[-1]
            try:
                X, sample_rate = librosa.load(file, res_type='kaiser_fast')
                mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=100).T, axis=0)
            except Exception:
                print("Error encountered while parsing file: ", file)
                mfccs, class_id = None, None
            if mfccs is not None:
                record.append(mfccs)
                record.append(class_id)
                # print(record)
                dataset.append(record)
            print(str((i / (len(files))) * 100) + '%')
            i += 1
    print(dataset)
    # 将声音文件的mfcc特征以及label保存，便于之后的导入
    np.save(globle_params.MFCC_FEATURE, dataset, allow_pickle=True)

    return

def MFCC_Feature1(metadatas):
    # 读取wav声音文件，并提取器mfcc特征，以及label标签，将其保存
    dataset = [[1 for k in range(2)] for m in range(len(metadatas))]
    print(np.shape(dataset))
    i=0
    for key,value in metadatas.items():
        file=os.path.join(globle_params.SAMPLE_DATA_PATH,key)
        class_id = value
        try:
            X, sample_rate = librosa.load(file, res_type='kaiser_fast')
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        except Exception:
            print("Error encountered while parsing file: ", file)
            mfccs, class_id = None, None
        feature = mfccs
        label = class_id
        dataset[i][0], dataset[i][1] = feature, label
        print(str((i/(len(metadatas)))*100)+'%')
        i += 1

    # 将声音文件的mfcc特征以及label保存，便于之后的导入
    np.save(globle_params.MFCC_FEATURE, dataset, allow_pickle=True)
    return

def build_metadata(metapath):
    source_files = search_file(metapath)
    meta_data = {}
    if len(source_files) > 0:
        for i in range(len(source_files)):
            print(source_files[i])
            csv_data = AudioSetDownload.read_file(source_files[i])
            csv_data = csv_data[2:][:]
            for re in csv_data:
                sample_file=os.path.join(globle_params.SAMPLE_DATA_PATH, re[0] + '.wav')
                if os.path.exists(sample_file):
                    if len([val for val in re[3:] if val in globle_params.LABELS])==1:
                        label=globle_params.LABEL_DICT[[val for val in re[3:] if val in globle_params.LABELS][0]]
                        target_path=os.path.join(globle_params.SAMPLE_DATA_PATH, label)
                        if os.path.exists(target_path) is not True:
                            os.makedirs(target_path)
                        os.system('cp ' + sample_file + ' '+target_path+'/'+re[0] + '.wav')
                        meta_data[re[0] + '.wav'] = label
                        print(re[0] + '.wav')
                    else:
                        print("alarm")
                        print(re[0] + '.wav')
                        meta_data[re[0] + '.wav'] = [val for val in re[3:] if val in globle_params.LABELS]
    return meta_data

def Read_MFCC_Feature(MFCCFeatureFile):
    data_feature = np.load(MFCCFeatureFile, allow_pickle=True)

    return data_feature

def data_preprocess(MFCCFeatureFile):
    # 导入数据
    data = pd.DataFrame(np.load(MFCCFeatureFile, allow_pickle=True))
    data.columns = ['feature', 'label']
    # print(data['label'])

    X = np.array(data.feature.tolist())
    y = np.array(data.label.tolist())
    # print(y)

    # 数据分割
    X, val_x, y, val_y = train_test_split(X, y)
    # print(y)
    # 对标签进行one-hot处理
    encoder = LabelBinarizer()
    y = encoder.fit_transform(y)
    val_y = encoder.fit_transform(val_y)

    return X, val_x, y, val_y

def dense_to_one_hot(labels_dense, num_classes):
   """Convert class labels from scalars to one-hot vectors."""
   num_labels = labels_dense.shape[0]
   index_offset = np.arange(num_labels) * num_classes
   labels_one_hot = np.zeros((num_labels, num_classes))
   labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
   return labels_one_hot

if __name__ == '__main__':
    MFCC_Feature(globle_params.SAMPLE_DATA_PATH)
    # metadatas=build_metadata(globle_params.SOURCE_META_DATA)
    # MFCC_Feature(metadatas)
    # data_feature=Read_MFCC_Feature(globle_params.MFCC_FEATURE)
    # print(data_feature)

    # X, val_x, y, val_y=data_preprocess(globle_params.MFCC_FEATURE)
    # print(y)
    # print(len(y))
    # y=list(y)
    #
    # for i in y:
    #     print(i)
    #     while y.count(i)>1:
    #         del y[y.index(i)]
    # print(len(y))
    # cls = DecisionTreeClassifier()
    # cls.fit(X, y)
    # Y_pred = cls.predict(val_x)
    # print(Y_pred)