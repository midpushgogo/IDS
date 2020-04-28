import pandas as pd
import  numpy as np

traindata = pd.read_csv('train.txt', header=None)
testdata = pd.read_csv('test.txt', header=None)

trainlen=len(traindata)
all=pd.concat([traindata,testdata],ignore_index=True)
class_map={'normal':0,
           'ipsweep':1,'mscan':1,'nmap':1,'portsweep':1,'saint':1,'satan':1,
           'apache2':2,'back':2,'land':2,'mailbomb':2,'neptune':2,'pod':2,'processtable':2,'smurf':2,'teardrop':2,'udpstorm':2,
           'buffer_overflow':3,'httptunnel':3,'loadmodule':3,'perl':3,'ps':3,'rootkit':3,'sqlattack':3,'xterm':3,
           'ftp_write':4,'guess_passwd':4,'imap':4,'multihop':4,'named':4,'phf':4,'sendmail':4,'snmpgetattack':4,'snmpguess':4,'spy':4,'warezclient':4,'warezmaster':4,'worm':4,'xlock':4,'xsnoop':4}

for i in [1,2,3]:

    a1 = pd.factorize(all[i])
    all[i] = a1[0]

all= all.iloc[:,0:42]


all[41]=all[41].map(class_map)




traindata=all.iloc[:trainlen,]
testdata=all.iloc[trainlen:,]

traindata.to_csv('train_factorize.csv',header=None,index=False)
testdata.to_csv('test_factorize.csv',header=None,index=False)
