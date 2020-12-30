
# -*- coding: utf-8 -*-


import time


TRAIN_CONFIG_FILE= "/home/fenggang/Desktop/Files/Data/TAU Urban Acoustic Scenes 2019 Mobile Development dataset/TAU-urban-acoustic-scenes-2019-mobile-development/evaluation_setup/fold1_train.csv"
TEST_CONFIG_FILE= "/home/fenggang/Desktop/Files/Data/TAU Urban Acoustic Scenes 2019 Mobile Development dataset/TAU-urban-acoustic-scenes-2019-mobile-development/evaluation_setup/fold1_test.csv"
EVALUATION_CONFIG_FILE= "/home/fenggang/Desktop/Files/Data/TAU Urban Acoustic Scenes 2019 Mobile Development dataset/TAU-urban-acoustic-scenes-2019-mobile-development/evaluation_setup/fold1_evaluate.csv"

SOURCE_PATH = "/home/fenggang/Desktop/Files/Data/TAU Urban Acoustic Scenes 2019 Mobile Development dataset/TAU-urban-acoustic-scenes-2019-mobile-development/"
SOURCE_TRAIN_PATH = "/home/fenggang/Desktop/Files/Data/TAU Urban Acoustic Scenes 2019 Mobile Development dataset/TAU-urban-acoustic-scenes-2019-mobile-development/train_source/"
SOURCE_TEST_PATH = "/home/fenggang/Desktop/Files/Data/TAU Urban Acoustic Scenes 2019 Mobile Development dataset/TAU-urban-acoustic-scenes-2019-mobile-development/test_source/"
SOURCE_EVALUATION_PATH = "/home/fenggang/Desktop/Files/Data/TAU Urban Acoustic Scenes 2019 Mobile Development dataset/TAU-urban-acoustic-scenes-2019-mobile-development/evaluate_source/"


TRAIN_PATH = "/home/fenggang/Desktop/Files/Data/TAU Urban Acoustic Scenes 2019 Mobile Development dataset/TAU-urban-acoustic-scenes-2019-mobile-development/train/"
PREDICT_PATH = "/home/fenggang/Desktop/Files/Data/TAU Urban Acoustic Scenes 2019 Mobile Development dataset/TAU-urban-acoustic-scenes-2019-mobile-development/predict/"
EVALUATION_PATH = "/home/fenggang/Desktop/Files/Data/TAU Urban Acoustic Scenes 2019 Mobile Development dataset/TAU-urban-acoustic-scenes-2019-mobile-development/evaluate/"

MODEL_PATH='/home/fenggang/Desktop/Projects/AudioClassification/model/'

APPKEY='Kxd9WK4FVCH0T9ImaBQoGEXe'
SECURET_KEY='5nf2rzzEjMrLKCl1YRYsrbUUEc1njwgT'
URL="https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/"
AUDIO_FILE='cache.wav'
SPEECH_FILE='speech.mp3'


TTS_URL = 'http://tsn.baidu.com/text2audio'
TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'

LOG_FILE = (
    "log/logfile_" + time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + ".log"
)



