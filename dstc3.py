from dstc2_support import dataset_walker
import sys,os,argparse,shutil,glob,json,copy,time
import numpy as np
word_count = 0

turns = []

for dataset in ['dstc3_test', 'dstc3_seed']:
    # try:
    sessions = dataset_walker(dataset,dataroot='./data/',labels=True)
    # except:
    #     print('Skipping a thing')
    #     continue
    start_time = time.time()

    # import pdb; pdb.set_trace()

    for session in sessions:
        turn_count = 0
        for turn_index,(log_turn,labels) in enumerate(session):
            turn_count += 1
            if 'transcript' in log_turn['output']:
                word_count += len(log_turn['output']['transcript'].split(' '))
                # print()
            if 'transcription' in labels:
                word_count += len(labels['transcription'].split(' '))
        turns.append(turn_count)

    print word_count
    print np.mean(turns)
