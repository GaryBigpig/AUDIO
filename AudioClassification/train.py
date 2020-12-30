import utils
import torch
from torch import nn
from torchvision.datasets import CIFAR10,ImageFolder
from torchvision import transforms as T
import numpy as np
import vggnet
import globleVar




def data_tf(x):
    x = np.array(x, dtype='float32') / 255
    x = (x - 0.5) / 0.5  # 标准化，这个技巧之后会讲到
    x = x.transpose((2, 0, 1))  # 将 channel 放到第一维，只是 pytorch 要求的输入方式
    x = torch.from_numpy(x)
    return x

def train():
    # transform = T.Compose([T.Resize((512,256)),T.ToTensor(), T.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])])
    # train_set = CIFAR10('./CIFARData', train=True, transform=data_tf, download=1)
    train_set = ImageFolder(globleVar.TRAIN_PATH, transform=data_tf)
    train_data = torch.utils.data.DataLoader(train_set, batch_size=5, shuffle=True)
    # test_set = CIFAR10('./CIFARData', train=False, transform=data_tf, download=1)
    test_set = ImageFolder(globleVar.EVALUATION_PATH, transform=data_tf)
    test_data = torch.utils.data.DataLoader(test_set, batch_size=5, shuffle=False)
    # create_spectrogram
    # utils.create_spectrogram(globleVar.SHELL_FILE)
    # predict_set
    predict_set = ImageFolder(globleVar.PREDICT_PATH, transform=data_tf)
    predict_data = torch.utils.data.DataLoader(predict_set, batch_size=1, shuffle=False)

    net = vggnet.vgg()
    optimizer = torch.optim.SGD(net.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    # print(train_data)
    # for im,label in train_data:
    #     # print(im.size())
    #     print(label)

    # utils.train(net, train_data, test_data, 20000, optimizer, criterion)
    # utils.predict(globleVar.MODEL_PATH + '_mingdi_1.0.pt', predict_data,'mingdi')
    # utils.delete_file(globleVar.PREDICT_PATH + '/ambulance/*.jpg')
    # utils.predict(globleVar.MODEL_PATH + '_zhuanxiang_1.0.pt', predict_data, 'zhuanxiang')
    # utils.predict(globleVar.MODEL_PATH + '_chemen_1.0.pt', predict_data,'chemen')
    utils.predict(globleVar.MODEL_PATH + '_steps_1.0.pt', predict_data, 'mingdi')

   