import librosa
import cv2
from scipy.io import wavfile
import os
import numpy as np
from pydub import AudioSegment
import matplotlib.pyplot as plt
import IPython.display as ipd
import wave


def audio_mix(inputFile1,inputFile2,outputFile):
    sound1 = AudioSegment.from_mp3(inputFile1)
    sound2 = AudioSegment.from_mp3(inputFile2)

    # mix sound2 with sound1, starting at 0ms into sound1)
    output = sound1.overlay(sound2)

    # save the result
    output.export(outputFile, format="wav")

def audio_time_stretch(input_audio, out_path,rates):
    y, sr = librosa.load(input_audio, sr=None)
    for rate in rates:  # 拉伸速率 [0.81, 0.93, 1.07, 1.23]
        y_shift = librosa.effects.time_stretch(y, rate=rate)  # 使用TS生成新数据
        # 数据导出为文件  replace('.ogg', '_no-{}.wav'.format(step)))  (old,new)
        librosa.output.write_wav(os.path.join(out_path,
                                              os.path.basename(input_audio).replace('.wav', '_ts-{}.wav'.format(rate))),
                                 y_shift, sr)

def audio_pitch_shift(input_audio, output_audio,steps):
    y, sr = librosa.load(input_audio, sr=None)
    for step in steps:
        y_shift = librosa.effects.pitch_shift(y, sr, n_steps=step)          # 使用PS1生成新数据 [-2, -1, 1, 2]
        librosa.output.write_wav(os.path.join(out_path,
            os.path.basename(input_audio).replace('.wav', '_ps-{}.wav'.format(step))), y_shift, sr)

def audio_add_noise(input_audio, output_audio,steps):
    y, sr = librosa.load(input_audio, sr=None)
    for step in steps:
        wn = np.random.normal(0, 1, len(y))                         # 从高斯分布（正态分布）提取样本 [1, 2, 3, 4]
        y_noise = np.where(y != 0.0, y.astype('float64') + 0.02 * wn, 0.0).astype(np.float32)
        librosa.output.write_wav(os.path.join(out_path,
            os.path.basename(input_audio).replace('.wav', "_no-{}.wav".format(step))),  y_noise, sr)

def print_wav(file,pic):
    # 读取音频文件
    print(file)
    audio_file=wave.open(file)
    print(type(audio_file))
    # 读取音频数据
    nf = audio_file.getnframes()
    audio_data = audio_file.readframes(nf)
    print(type(audio_data))
    # 把data转化为数组：
    w = np.fromstring(audio_data, dtype=np.int16)
    # 除以最大值，使得所有的数字介于 - 1到1之间：
    w = w * 1.0 / (max(abs(w)))
    # 这个时候的数据类型，就是数组的形式：
    print(type(w))
    # 画图
    plt.plot(w, '-', c='g')
    plt.show()
    # 保存
    plt.savefig(pic)



if __name__ == '__main__':
    index = 0
    # print(os.getcwd())
    file_path = "./data/input/"       # 输入文件夹路径
    out_path = "./data/output/"               # 增强后数据(输出)文件夹路径[无文件夹会自动创建]
    file_path = "./data/output/"
    if not os.path.isdir(out_path):  # 判断目标路径是否存在，不存在则创建
        os.mkdir(out_path)

    # audio_mix(file_path+"dog.wav",file_path+"police.mp3",save_path+"dog_police.wav")

    for filename in os.listdir(r"./" + file_path):
        print(filename[-4:])
        if filename[-4:]=='.wav':
            in_path = file_path + filename
            # wav, sr = librosa.load(in_path, sr=None)
            print_wav(in_path,out_path+filename+'.png')

        # audio_time_stretch(in_path, out_path,[0.5, 1.8])
        # audio_pitch_shift(in_path, out_path, [-2, -1, 1, 2])
        # audio_pitch_shift(in_path, out_path, [-3.5, -2.5, 2.5, 3.5])
        # audio_add_noise(in_path, out_path, [1, 2, 3, 4])
        # index = index + 1
        # print(index)
        # print()
        # cv2.waitKey(200)
