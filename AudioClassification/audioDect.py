# -*- coding: UTF8 -*-
import sys
import GUI
import easyDLAPI
import audioRecord

APPKEY='Kxd9WK4FVCH0T9ImaBQoGEXe'
SECURET_KEY='5nf2rzzEjMrLKCl1YRYsrbUUEc1njwgT'
URL="https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/"


def RecordAudio():
    audioRecord.audioRecord('cache.wav',2)
    return
    
def DectAudio():
    audioType=''
    #audioType=easyDLAPI.audioDect(APPKEY,SECURET_KEY,
    #                    URL+"TZCL002",
    #                    '/home/pi/Desktop/AudioDect/cache.wav')
    #audioType=easyDLAPI.audioDect('Kxd9WK4FVCH0T9ImaBQoGEXe','5nf2rzzEjMrLKCl1YRYsrbUUEc1njwgT',
    #                    "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/CM001",
    #                    '/home/pi/Downloads/3.wav')
    #audioType=easyDLAPI.audioDect('Kxd9WK4FVCH0T9ImaBQoGEXe','5nf2rzzEjMrLKCl1YRYsrbUUEc1njwgT',
    #                    "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/CM001",
    #                    '/home/pi/Desktop/AudioDect/cache.wav')
    GUI.MainWidgetUI.updateLabel('a')
    return audioType
    


if __name__ == "__main__":
    
    app = GUI.QApplication(sys.argv)
    main_widget = GUI.MainWidgetUI('c')
    main_widget.show()
    sys.exit(app.exec_())
