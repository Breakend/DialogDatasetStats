# coding: utf-8
import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('smsCorpus_en_2015.03.09_all.xml').getroot()
e
e.items()
e = xml.etree.ElementTree.parse('smsCorpus_en_2015.03.09_all.xml')
e
e.get_root()
root = e.getroot()
for child in root:
    print(child)
    
root[0]
root[0].text
root[0]
e.tostringlist()
e.tostringlist(root[0])
ElementTree.tostringlist(root)
root[0].items()
root[0].keys()
root[0].attrib
root[1].attrib
root[2].attrib
root[0].get_children()
list(root[0])
list(root[0])[0]
list(root[0])[0].text
list(root[0])[1]
list(root[0])[1].text
list(root[0])[1].attrib
list(list(root[0])[1])
list(list(root[0])[1])[0]
list(list(root[0])[1])[0].text
def get_source_dest_pairs(root):
    dialog_pairs = {}
    all_messages = list(root)
    for message in all_messages:
        message_attrs = list(message)
        source = message_attrs[1]
        source = list(source)[0]
        dest = message_attrs[2]
        dest = list(dest)[0]
        if source not in dialog_pairs:
            dialog_pairs[source] = {}
            dialog_pairs[source][dest] = 1
        else:
            if dest not in dialog_pairs[source]:
                dialog_pairs[source][dest] = 1
            else:
                dialog_pairs[source][dest] += 1
    return dialog_pairs
get_source_dest_pairs(root)
def get_source_dest_pairs(root):
    dialog_pairs = {}
    all_messages = list(root)
    for message in all_messages:
        message_attrs = list(message)
        source = message_attrs[1]
        source = list(source)[0].text
        dest = message_attrs[2]
        dest = list(dest)[0].text
        if source not in dialog_pairs:
            dialog_pairs[source] = {}
            dialog_pairs[source][dest] = 1
        else:
            if dest not in dialog_pairs[source]:
                dialog_pairs[source][dest] = 1
            else:
                dialog_pairs[source][dest] += 1
    return dialog_pairs
get_source_dest_pairs(root)
def get_source_dest_pairs(root):
    dialog_pairs = {}
    all_messages = list(root)
    for message in all_messages:
        message_attrs = list(message)
        source = message_attrs[1]
        source = list(source)[0]
        dest = message_attrs[2]
        dest = list(dest)[0]
        import pdb; pdb.set_trace()
        
        if source not in dialog_pairs:
            dialog_pairs[source] = {}
            dialog_pairs[source][dest] = 1
        else:
            if dest not in dialog_pairs[source]:
                dialog_pairs[source][dest] = 1
            else:
                dialog_pairs[source][dest] += 1
    return dialog_pairs
get_source_dest_pairs(root)
def get_source_dest_pairs(root):
    dialog_pairs = {}
    all_messages = list(root)
    for message in all_messages:
        message_attrs = list(message)
        source = message_attrs[1]
        source = list(source)[0].text
        dest = message_attrs[2]
        dest = list(dest)[0].text
        import pdb; pdb.set_trace()
        
        if source not in dialog_pairs:
            dialog_pairs[source] = {}
            dialog_pairs[source][dest] = 1
        else:
            if dest not in dialog_pairs[source]:
                dialog_pairs[source][dest] = 1
            else:
                dialog_pairs[source][dest] += 1
    return dialog_pairs
get_source_dest_pairs(root)
c
get_source_dest_pairs(root)
get_source_dest_pairs(root)
def get_source_dest_pairs(root):
    dialog_pairs = {}
    all_messages = list(root)
    for message in all_messages:
        message_attrs = list(message)
        source = message_attrs[1]
        source = list(source)[0].text
        dest = message_attrs[2]
        dest = list(dest)[0].text
        
        if source not in dialog_pairs:
            dialog_pairs[source] = {}
            dialog_pairs[source][dest] = 1
        else:
            if dest not in dialog_pairs[source]:
                dialog_pairs[source][dest] = 1
            else:
                dialog_pairs[source][dest] += 1
    return dialog_pairs
get_source_dest_pairs(root)
dialogs = get_source_dest_pairs(root)
dialogs
dialogs.keys()
total_dialogs = []
for source, ds in dialogs.iteritems():
    total_dialogs += len(ds.keys())
    
total_dialogs = 0
for source, ds in dialogs.iteritems():
    total_dialogs += len(ds.keys())
    
total_dialogs
turns_per_dialog = []
for source, ds in dialogs.iteritems():
    turns_per_dialog.extend(ds.values())
    
turns_per_dialog
np.mean(turns_per_dialog)
import numpy as np
np.mean(turns_per_dialog)
