# -*- coding: UTF8 -*-
import io, shutil, sys, os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import audioRecord
import easyDLAPI
import globleVar
import SpeechSynthesis


class MainWidgetUI(QDialog):
    def __init__(self,value):  
        super().__init__()
        self.resize(300,200)
        self.setWindowTitle('鸣笛检测')
        self.setWindowIcon(QtGui.QIcon("favicon.ico"))

        Layout = QVBoxLayout()

        self.Label1=QLabel(self)
        self.Label1.setText(value)
        self.Label1.setAlignment(Qt.AlignCenter)
        self.Label1.resize(300,30)

        self.pushButton1 = QPushButton("检测")
        # self.pushButton2 = QPushButton("To file")
        Layout.addWidget(self.pushButton1)  # addWidget 添加一个挂件
        # Layout.addSpacing(100)  # 添加一个100px的空间距离 且不带弹性
        #Layout.addWidget(self.pushButton2)
        self.setLayout(Layout)  # setLayout设置 QVBoxLayout()垂直 与QHBoxLayout() 水平布局, 查看布局请移步CURL-api.py
        #self.pushButton1.clicked.connect(audioDect.DectAudio)
        self.pushButton1.clicked.connect(self.dectAudio)
        
    
    def dectAudio(self):
        self.Label1.setText("开始检测......")
        self.Label1.repaint()
        audioRecord.audioRecord(globleVar.AUDIO_FILE,3)
        #audioType=easyDLAPI.audioDect('Kxd9WK4FVCH0T9ImaBQoGEXe','5nf2rzzEjMrLKCl1YRYsrbUUEc1njwgT',
        #                "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/TZCL003",
        #                '/home/pi/Desktop/AudioDect/cache.wav')
        audioType=easyDLAPI.audioDect(globleVar.APPKEY,globleVar.SECURET_KEY,
                        globleVar.URL+"TZCL003",
                        './'+globleVar.AUDIO_FILE)
        print(audioType)
        self.Label1.setText(audioType)
        self.Label1.repaint()
        SpeechSynthesis.SpeechSynthesis(globleVar.APPKEY,globleVar.SECURET_KEY,globleVar.TOKEN_URL,audioType,globleVar.TTS_URL)
        os.system("omxplayer -o local /home/pi/Desktop/AudioDect/speech.mp3")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_widget = MainWidgetUI('')
    main_widget.show()
    sys.exit(app.exec_())