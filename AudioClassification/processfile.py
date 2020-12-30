

import pandas as pd
import os


def cpFIle(sourcePath,targetPath,configFile,type):
    print("Reading configure file: "+configFile+"...")
    configs=pd.read_csv(configFile,sep='\t')

    for row in range(len(configs)):
        print('Copying file ' + configs.iloc[row,0] + '...')
        # print("cp '" + sourcePath + configs.iloc[row,0] + "' '" + targetPath + "'")
        if type=="wav":
            os.system("cp -f '" + sourcePath + configs.iloc[row,0] + "' '" + targetPath + "'")
        else:
            os.system("cp -f '" + sourcePath + configs.iloc[row, 0][6:] + ".jpg' '" + targetPath + "/" + configs.iloc[row, 1]+ "/'")





