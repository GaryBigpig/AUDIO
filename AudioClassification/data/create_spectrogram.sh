echo '>> START : Audio to Spectrogram creation <<'

for audioFile in /home/fenggang/Desktop/Projects/AudioClassification/data/predict/ambulance/*.wav; do
        echo $audioFile
        ffmpeg -i $audioFile -lavfi showspectrumpic=s=32x32:legend=disabled $audioFile.jpg
    done
    
echo '>> END : Audio to Spectrogram creation <<'
