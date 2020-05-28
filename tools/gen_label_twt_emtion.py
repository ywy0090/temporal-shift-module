# Code for "TSM: Temporal Shift Module for Efficient Video Understanding"
# arXiv:1811.08383
# Ji Lin*, Chuang Gan, Song Han
# {jilin, songhan}@mit.edu, ganchuang@csail.mit.edu
# ------------------------------------------------------
# Code adapted from https://github.com/metalbubble/TRN-pytorch/blob/master/process_dataset.py

import os
import json


root_path = '/home/ywy/dataset/Emotion_twt/'
dataset_path = '/media/ywy/56e860d6-987d-4855-af6c-25a5fb0fb64d/ywy/Dataset/EmotionTwt/'
categories_file = 'categories.json'
train_file = 'train_gold.json'
if __name__ == '__main__':
    with open(root_path+categories_file) as f:
        categories = json.load(f)
    categories = [c for c in categories]
    dict_categories = {}
    for i, category in enumerate(categories):
        dict_categories[category] = i

    print(dict_categories)
    output = []
    train_file = root_path + train_file
    train_output = dataset_path + 'train_label.txt'
    with open(train_file) as f:
        for line in f:
            json_dict = json.loads(line)
            idx = json_dict['idx']
            text = json_dict['text']
            reply = json_dict['reply']
            mp4 = json_dict['mp4']
            category = json_dict['categories'][0]
            output.append('%d\t%s\t%s\t%s\t%s' % (idx, text, reply, mp4, category))
    with open(train_output,'w') as f:
        f.write('\n'.join(output))
