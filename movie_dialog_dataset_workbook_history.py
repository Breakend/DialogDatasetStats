# coding: utf-8
import os
get_ipython().magic('cd task1_qa')
get_ipython().magic('ls ')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            words = fil.split("\t")
            word_count += sum([len(thing.split(" ") for thing in words]))
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            words = fil.split("\t")
            word_count += sum([len(thing.split(" ")) for thing in words])
            
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            words = lines.split("\t")
            word_count += sum([len(thing.split(" ")) for thing in words])
            
word_count = 0
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words])
            
word_count
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd task2_recs/')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words])
            
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd task3_qarecs/')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words])
            
get_ipython().magic('cd ../task4_reddit/')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words])
            
word_count
get_ipython().magic('ls ')
vim README
word_count
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd task4_reddit/')
get_ipython().magic('ls ')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words])
            
get_ipython().magic('ls ')
word_count = 0
get_ipython().magic('ls ')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")[1:]
                word_count += sum([len(thing.split(" ")) for thing in words])
            
get_ipython().magic('cd ..')
get_ipython().magic('ls ')
get_ipython().magic('cd movie_dialog_dataset/')
get_ipython().magic('ls ')
get_ipython().magic('cd task1_qa/')
get_ipython().magic('ls ')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")[1:]
                word_count += sum([len(thing.split(" ")) for thing in words])
            
get_ipython().magic('cd ../task2_recs/')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")[1:]
                word_count += sum([len(thing.split(" ")) for thing in words])
            
get_ipython().magic('cd ../task3_qarecs/')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")[1:]
                word_count += sum([len(thing.split(" ")) for thing in words])
            
get_ipython().magic('ls ')
word_count
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                import pdb; pdb.set_trace()
            
                words = line.split("\t")[1:]
                word_count += sum([len(thing.split(" ")) for thing in words])
            
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                import pdb; pdb.set_trace()
            
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words])
            
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                import pdb; pdb.set_trace()
            
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words]) - 1 # -1 for start word being the id of the conversation
            
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words]) - 1 # -1 for start word being the id of the conversation
            
get_ipython().magic('ls ')
word_count = 0
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words]) - 1 # -1 for start word being the id of the conversation
            
get_ipython().magic('ls ')
get_ipython().magic('cd ../task2_recs/')
get_ipython().magic('ls ')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words]) - 1 # -1 for start word being the id of the conversation
            
get_ipython().magic('ls ')
get_ipython().magic('cd ../task1_qa/')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words]) - 1 # -1 for start word being the id of the conversation
            
get_ipython().magic('cd ../../task4_reddit/')
for dirpath, dnames, fnames in os.walk("./"):
    for f in fnames:
        with open(f) as fil:
            lines = fil.readlines()
            for line in lines:
                words = line.split("\t")
                word_count += sum([len(thing.split(" ")) for thing in words]) - 1 # -1 for start word being the id of the conversation
            
get_ipython().magic('ls ')
word_count
