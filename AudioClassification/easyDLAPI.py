import requests
import File2Base64
import json
import GUI
import sys
import globleVar



def audioDect(APP_KEY,SECRET_KEY,URL,FILE):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
           '&client_id='+APP_KEY+'&client_secret='+SECRET_KEY
    response = requests.get(host)
    # if response:
    #     print(response.json())

    request_url = URL

    base64code=File2Base64.toBase64(FILE)

    # print(base64code)

    params = {'sound':base64code}

    access_token = str(response.json())
    request_url = request_url + "?access_token=" + response.json()['access_token']
    response = requests.post(url=request_url, data=json.dumps(params))
    print(response.json())
    result=response.json()['results']
    score=[result[0]['score'],result[1]['score'],result[2]['score']]
    name=[result[0]['name'],result[1]['name'],result[2]['name']]

    #print(name[score.index(max(score))])

    if name[score.index(max(score))]=='ambulance':
        result_string='救护车鸣笛'
    elif name[score.index(max(score))]=='police':
        result_string='警车鸣笛'
    else:
        result_string="无鸣笛"
    #result_string='检测出声音：' + ('GUzhang' if name[score.index(max(score))]=='true' else 'zhengcang')
    return result_string


if __name__ == "__main__":
    audioType=audioDect(globleVar.APPKEY,globleVar.SECURET_KEY,
                        globleVar.URL+"TZCL003",
                        './'+globleVar.AUDIO_FILE)
    #audioType=audioDect('Kxd9WK4FVCH0T9ImaBQoGEXe','5nf2rzzEjMrLKCl1YRYsrbUUEc1njwgT',
    #                    "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/CM001",
    #                    '/home/pi/Downloads/3.wav')
    #audioType=audioDect('Kxd9WK4FVCH0T9ImaBQoGEXe','5nf2rzzEjMrLKCl1YRYsrbUUEc1njwgT',
    #                    "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/CM001",
    #                    '/home/pi/Desktop/AudioDect/cache.wav')
    app = GUI.QApplication(sys.argv)
    main_widget = GUI.MainWidgetUI(audioType)
    main_widget.show()
    sys.exit(app.exec_())