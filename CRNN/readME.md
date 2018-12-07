# process the dataset mjsynth for pre-train the crnn

### 1.Download and unzip the dataset by
```
tar xf mjsynth.tar.gz
```

### 2.Move the get_listtxt.py to the same dir as mnt (unzip from mjsynth.tar.gz)
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

open to_lmdb/tolmdb.py and set the *file_list* and *image_root* to your path 

Then run with python2:
```
cd to_lmdb
python2 tolmdb.py
```
