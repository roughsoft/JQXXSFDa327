############

#author yunpeng zhai, PKU univ.

############

#project dir
#./
#./mnt
#./get_list.py

#run 
#python3 get_list.py

############
import os.path as osp

file_list=["mnt/ramdisk/max/90kDICT32px/annotation_test.txt",
           "mnt/ramdisk/max/90kDICT32px/annotation_train.txt",
           "mnt/ramdisk/max/90kDICT32px/annotation_val.txt"]

def main():
    for file in file_list:
        filename = osp.basename(file)
        txt_type = filename.split('_')[1].split('.')[0]
        out_name = txt_type+"_list.txt"#test_list.txt  train_list.txt  val_list.txt
        outfile = open(out_name,"w")
        lines = open(file, "r").readlines()
        for line in lines:
            path = line.strip().split(' ')[0]
            label = osp.basename(path).split('_')[1]
            outfile.write(path+" "+label+"\n")

if __name__ == '__main__':
    main()