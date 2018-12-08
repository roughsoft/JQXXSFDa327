import os
import lmdb # install lmdb by "pip install lmdb"
import cv2
import re
from PIL import Image
import numpy as np
import imghdr


def checkImageIsValid(imageBin):
    if imageBin is None:
        return False
    try:
        imageBuf = np.fromstring(imageBin, dtype=np.uint8)
        img = cv2.imdecode(imageBuf, cv2.IMREAD_GRAYSCALE)
        imgH, imgW = img.shape[0], img.shape[1]
    except:
        return False
    else:
        if imgH * imgW == 0:
            return False		
    return True


def writeCache(env, cache):
    with env.begin(write=True) as txn:
        for k, v in cache.items():
            txn.put(k, v)
			
def createDataset(outputPath, imagePathList, labelList, lexiconList=None, checkValid=True):
    """
    Create LMDB dataset for CRNN training.
    ARGS:
        outputPath    : LMDB output path
        imagePathList : list of image path
        labelList     : list of corresponding groundtruth texts
        lexiconList   : (optional) list of lexicon lists
        checkValid    : if true, check the validity of every image
    """
    assert(len(imagePathList) == len(labelList))
    nSamples = len(imagePathList)
    env = lmdb.open(outputPath, map_size=1099511627776)
    cache = {}
    cnt = 1
    for i in range(nSamples):   

        imagePath = ''.join(imagePathList[i]).split()[0].replace('\n','').replace('\r\n','')
        #print(imagePath)
        label = ''.join(labelList[i])
        #print(label)
        # if not os.path.exists(imagePath):
        #     print('%s does not exist' % imagePath)
        #     continue	
		
        with open(imagePath, 'rb') as f:
            imageBin = f.read()


        if checkValid:
            if not checkImageIsValid(imageBin):
                print('%s is not a valid image' % imagePath)
                continue
        imageKey = 'image-%09d' % cnt
        labelKey = 'label-%09d' % cnt
        cache[imageKey] = imageBin
        cache[labelKey] = label
        if lexiconList:
            lexiconKey = 'lexicon-%09d' % cnt
            cache[lexiconKey] = ' '.join(lexiconList[i])
        if cnt % 1000 == 0:
            writeCache(env, cache)
            cache = {}
            print('Written %d / %d' % (cnt, nSamples))
        cnt += 1
        #print(cnt)
    nSamples = cnt-1
    cache['num-samples'] = str(nSamples)
    writeCache(env, cache)
    print('Created dataset with %d samples' % nSamples)


file_list=["test_list.txt",
           "train_list.txt",
           "val_list.txt"]
image_root = "mnt/ramdisk/max/90kDICT32px"
import os.path as osp
if __name__ == '__main__':
    for file in file_list:

        dir_path = osp.dirname(file)
        name = osp.basename(file).split('_')[0]
        outputPath = osp.join(dir_path, name)
        imgdata = open(file)
        imageList = list(imgdata)
        imagePathList = []
        labelList = []
        for line in imageList:
            word = line.split()[1]
            labelList.append(word)
            imagePathList.append(osp.join(image_root, line[2:]))
        createDataset(outputPath, imagePathList, labelList)        


