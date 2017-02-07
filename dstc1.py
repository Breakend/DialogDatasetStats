from dstc1_support import dataset_walker
import sys,os,argparse,shutil,glob,json,copy,time

word_count = 0



for dataset in ['train1a', 'train1b', 'train1c', 'train2', 'train3', 'test1', 'test2', 'test3', 'test4']:
    try:
        sessions = dataset_walker(dataset,dataroot='./data/',labels=True)
    except:
        print('Skipping a thing')
        continue
    start_time = time.time()

    # import pdb; pdb.set_trace()

    for session in sessions:
        for turn_index,(log_turn,labels) in enumerate(session):
            if 'transcript' in log_turn['output']:
                word_count += len(log_turn['output']['transcript'].split(' '))
                # print()
            if 'transcription' in labels:
                word_count += len(labels['transcription'].split(' '))

    print word_count
