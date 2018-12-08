# process the dataset mjsynth for pre-train the crnn

### 1.Download and unzip the dataset by
```
tar xf mjsynth.tar.gz
```

### 2.Move the mnt (unzip from mjsynth.tar.gz) to the dir *JQXXSFDa327/CRNN*
```
python3 get_listtxt.py
```
And You will get three xxx_list.txt which will be used for lmdb transformation.
```
test_list.txt
train_list.txt
val_list.txt
```
### 3.Convert img to lmdb

open tolmdb.py and set the *file_list* and *image_root* to your path 

Then run with python2:
```
python2 tolmdb.py
```
