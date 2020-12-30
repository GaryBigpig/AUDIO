
SOURCE_META_DATA='./source_meta_data'
META_DATA_FILE='./meta_data/meta_data.csv'
SAMPLE_DATA_PATH='./sample_data/'
MFCC_FEATURE='./mfcc_feature/mfcc_feature.npy'
# SAVED_MODEL='./saved_model/1'
SAVED_MODEL='./saved_model/model-improvement-{epoch:02d}-{val_accuracy:.2f}'


# LABEL_DICT={'/m/02mfyn':1,"/m/04cvmfc":2,"/m/03qc9zr":3,"/m/07qw_06":4,"/m/07pjjrj":5,
#        "/m/07pws3f":6,"/m/0dgbq":7,"/m/01y3hg":8,"/m/0c3f7m":8,"/m/07sr1lc":10,"/m/07s2xch":11,
#             "/m/039jq":12,"/m/07qnq_y":13,"/m/032s66":14,"/m/014zdl":0}

# LABEL_DICT={'/m/02mfyn':'Car_alarm',"/m/04cvmfc":"Roar","/m/03qc9zr":"Screaming","/m/07qw_06":"Wail|moan","/m/07pjjrj":"Smash|crash",
#        "/m/07pws3f":"Bang","/m/0dgbq":"Civil_defense|siren","/m/01y3hg":"Smoke_detector|smoke_alarm","/m/0c3f7m":"Fire_alarm","/m/07sr1lc":"Yell","/m/07s2xch":"Groan",
#           "/m/039jq":"Glass","/m/07qnq_y":"Thump|thud","/m/032s66":"Gunshot|gunfire","/m/014zdl":"Explosion"}

LABEL_DICT={'/m/02mfyn':'Car_alarm',"/m/04cvmfc":"Roar","/m/03qc9zr":"Screaming","/m/07qw_06":"Wail_Moan","/m/07pjjrj":"Smash_Crash",
       "/m/07pws3f":"Bang","/m/0dgbq":"Civil_defense_Siren","/m/01y3hg":"Smoke_detector_Smoke_alarm","/m/0c3f7m":"Fire_alarm","/m/07sr1lc":"Yell","/m/07s2xch":"Groan",
          "/m/039jq":"Glass","/m/07qnq_y":"Thump_Thud","/m/032s66":"Gunshot_Gunfire","/m/014zdl":"Explosion"}

LABELS=["/m/02mfyn","/m/04cvmfc","/m/03qc9zr","/m/07qw_06","/m/07pjjrj","/m/07pws3f","/m/0dgbq",
         "/m/01y3hg","/m/0c3f7m","/m/07sr1lc","/m/07s2xch","/m/039jq","/m/07qnq_y","/m/032s66","/m/014zdl"]



