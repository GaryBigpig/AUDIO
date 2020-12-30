# -*- coding: utf-8 -*-
import pyaudio
import wave
import numpy as np
 
def audioRecord(filename, time=0):
    CHUNK = 512
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 48000
    RECORD_SECONDS = time 
    WAVE_OUTPUT_FILENAME = filename
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print('begin')
    frames = []
    if time > 0:
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
             data = stream.read(CHUNK)
             frames.append(data)
    print("stop")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    return
 
if __name__ == '__main__':
    audioRecord()