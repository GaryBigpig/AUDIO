import sys
sys.path.append('..')

import numpy as np
import torch
from torch import nn
from torch.autograd import Variable



def vgg_block(num_convs, in_channels, out_channels):
    # net = [nn.Conv2d(in_channels, out_channels, kernel_size=12,stride=2, padding=1), nn.ReLU(True)]  # 定义第一层 252  124
    # net = [nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1), nn.ReLU(True)]
    net = [nn.Conv2d(in_channels, out_channels, kernel_size=4,stride=2, padding=1), nn.ReLU(True)] # 定义第一层 16  16
    if num_convs>0:
        for i in range(num_convs - 1):  # 定义后面的很多层
            net.append(nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1))
            net.append(nn.ReLU(True))

    net.append(nn.MaxPool2d(8, 8))  # 定义池化层
    # net.append(nn.Dropout(p=0.5, inplace=True))
    return nn.Sequential(*net)

def vgg_stack(num_convs, channels):
    net = []
    layers=0
    for n, c in zip(num_convs, channels):
        if layers==1:
            break
        print(layers)
        layers+=1
        in_c = c[0]
        out_c = c[1]
        net.append(vgg_block(n, in_c, out_c))
    return nn.Sequential(*net)

# vgg_net = vgg_stack((1, 1, 2, 2, 2), ((3, 64), (64, 128), (128, 256), (256, 512), (512, 512)))
vgg_net = vgg_stack((0, 0), ((3, 16), (64, 128)))
print(vgg_net)
class vgg(nn.Module):
    def __init__(self):
        super(vgg, self).__init__()
        # self.feature = vgg_net
        self.feature = vgg_net
        self.fc = nn.Sequential(
            nn.Linear(64, 30),
            nn.Dropout(p=0.5, inplace=True),
            nn.ReLU(True),
            nn.Linear(30, 3)
        )
        print(self.fc)
    def forward(self, x):
        x = self.feature(x)
        x = x.view(x.shape[0], -1)
        x = self.fc(x)
        return x



