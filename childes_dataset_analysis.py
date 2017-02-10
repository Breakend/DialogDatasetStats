# coding: utf-8
import urllib2
from BeautifulSoup import BeautifulSoup
url = "http://childes.psy.cmu.edu/browser/index.php"
text = urllib2.urlopen(url).read()
soup = BeautifulSoup(text)
url = "http://childes.psy.cmu.edu/browser/index.php?url=Eng-NA/"

text = urllib2.urlopen(url).read()
soup = BeautifulSoup(text)
data = soup.findAll('li', attrs={'class' : 'dir'})
data
for d in data
for d in data:
    links = d.findAll('a')
    for a in links:
        print a
        
for d in data:
    links = d.findAll('a')
    for a in links:
        print a['href']
        
        
for d in data:
    links = d.findAll('a')
    for a in links:
        print a['href']
        
dirs = []
for d in data:
    links = d.findAll('a')
    for a in links:
        dirs.append(a['href'])
        
dirs
for d in dirs:   text = urllib2.urlopen().read()
for d in dirs:
    text = urllib2.urlopen(d).read()
    soup = BeautifulSoup(text)
    data = soup.findAll('li', attrs={'class' : 'dir'})
    cha = soup.findAll('li', attrs={'class' : 'cha'})
    print "Dirs %d" % len(data)
    print "Chas %d" % len(cha)
    
dialogs = []
for d in dirs:
    text = urllib2.urlopen(d).read()
    soup = BeautifulSoup(text)
    data = soup.findAll('li', attrs={'class' : 'dir'})
    cha = soup.findAll('li', attrs={'class' : 'cha'})
    print "Dirs %d" % len(data)
    print "Chas %d" % len(cha)
    
dialogs = 0
def search_dirs(dirs):
    chas = 0
    for d in dirs:
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(data)
        print "Chas %d" % len(cha)
        chas += search_dirs(data)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
dirs
chas = search_dirs(dirs)
def search_dirs(dirs):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(data)
        print "Chas %d" % len(cha)
        chas += search_dirs(data)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(data)
        print data
        print "Chas %d" % len(cha)
        chas += search_dirs(data)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for d in data:
            links = d.findAll('a')
            for a in links:
            links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
def search_dirs(dirs):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for d in data:
            links = d.findAll('a')
            for a in links:
                links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            links = l.findAll('a')
            for a in links:
                links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            links = l.findAll('a')
            for a in links:
                print a
                links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            links = l.findAll('a')
            import pdb; pdb.set_trace()
            for a in links:
                print a
                links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            import pdb; pdb.set_trace()
            for a in arefs:
                print a
                links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs, base_url="http://childes.psy.cmu.edu/browser/index.php?url=Eng-NA/"):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                if base_url in a:
                    links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs, base_url="index.php?url=Eng-NA"):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                if base_url in a:
                    links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs, base_url="index.php?url=Eng-NA"):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                print a
                if base_url in a:
                    links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs, base_url="index.php?url=Eng-NA"):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            import pdb; pdb.set_trace()
            for a in arefs:
                print a
                if base_url in a:
                    links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
def search_dirs(dirs, base_url="index.php?url=Eng-NA"):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                if base_url in a['href']:
                    links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs)
chas = search_dirs(dirs)
def search_dirs(dirs, base_url="index.php?url=Eng-NA", previous_links=[]):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                if base_url in a['href'] and a['href'] not in previous_links:
                    links.append(a['href'])
                    previous_links.append(h['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links, previous_links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs, previous_links = [x for x in dirs])
def search_dirs(dirs, base_url="index.php?url=Eng-NA", previous_links=[]):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                if base_url in a['href'] and a['href'] not in previous_links:
                    links.append(a['href'])
                    previous_links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links, previous_links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs, previous_links = [x for x in dirs])
def search_dirs(dirs, base_url="index.php?url=Eng-NA", previous_links=[]):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                if base_url in a['href'] and not (a['href'] in previous_links):
                    links.append(a['href'])
                    previous_links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links, previous_links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs, previous_links = [x for x in dirs])
def search_dirs(dirs, base_url="index.php?url=Eng-NA", previous_links=[]):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                import pdb; pdb.set_trace()
                if base_url in a['href'] and not (a['href'] in previous_links):
                    links.append(a['href'])
                    previous_links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links, previous_links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs, previous_links = [x for x in dirs])
def search_dirs(dirs, base_url="index.php?url=Eng-NA", previous_links=[]):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                import pdb; pdb.set_trace()
                if base_url in a['href'] and not (a['href'] in previous_links):
                    links.append(a['href'])
                    previous_links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links, previous_links = previous_links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs, previous_links = [x for x in dirs])
def search_dirs(dirs, base_url="index.php?url=Eng-NA", previous_links=[]):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                if base_url in a['href'] and not (a['href'] in previous_links):
                    links.append(a['href'])
                    previous_links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links, previous_links = previous_links)
        chas += len(cha)
    return chas
chas = search_dirs(dirs, previous_links = [x for x in dirs])
chas
url = "http://childes.psy.cmu.edu/browser/index.php?url=Eng-UK/"

text = urllib2.urlopen(url).read()
soup = BeautifulSoup(text)
chas
CHAS_NA = 7452
dirs = []
data = soup.findAll('li', attrs={'class' : 'dir'})
for d in data:
    links = d.findAll('a')
    for a in links:
        dirs.append(a['href'])
        
def get_orig_dirs(url):
    text = urllib2.urlopen(url).read()
    soup = BeautifulSoup(text)
    dirs = []
    data = soup.findAll('li', attrs={'class' : 'dir'})
    for d in data:
        links = d.findAll('a')
        for a in links:
            dirs.append(a['href'])
            
dirs = get_orig_dirs("http://childes.psy.cmu.edu/browser/index.php?url=Eng-UK/")
chas = search_dirs(dirs, "index.php?url=Eng-UK/", previous_links = [x for x in dirs])
dirs
def get_orig_dirs(url):
    text = urllib2.urlopen(url).read()
    soup = BeautifulSoup(text)
    dirs = []
    data = soup.findAll('li', attrs={'class' : 'dir'})
    for d in data:
        links = d.findAll('a')
        for a in links:
            dirs.append(a['href'])
    return dirs
dirs = get_orig_dirs("http://childes.psy.cmu.edu/browser/index.php?url=Eng-UK/")
chas = search_dirs(dirs, "index.php?url=Eng-UK/", previous_links = [x for x in dirs])
chas
CHAS_NA = 7452
CHAS_UK = 2610
dirs = get_orig_dirs("http://childes.psy.cmu.edu/browser/index.php?url=FluencyBank")
chas = search_dirs(dirs, "index.php?url=FluencyBank/", previous_links = [x for x in dirs])
dirs
dirs = get_orig_dirs("http://childes.psy.cmu.edu/browser/index.php?url=FluencyBank/")
dirs
chas = search_dirs(dirs, "index.php?url=FluencyBank/", previous_links = [x for x in dirs])
dirs
chas = search_dirs(dirs, "index.php?url=FluencyBank/", previous_links = [x for x in dirs])
prev_links = [x for x in dirs]; prev_links.append("http://childes.psy.cmu.edu/browser/index.php")
chas = search_dirs(dirs, "index.php?url=FluencyBank/", previous_links =prev_links)
prev_links = [x for x in dirs]; prev_links.append("http://childes.psy.cmu.edu/browser/index.php").append("http://childes.psy.cmu.edu/browser/index.php?url=FluencyBank/Voices/OASES/")
prev_links = [x for x in dirs]; prev_links.append("http://childes.psy.cmu.edu/browser/index.php");prev_links.append("http://childes.psy.cmu.edu/browser/index.php?url=FluencyBank/Voices/OASES/")
chas = search_dirs(dirs, "index.php?url=FluencyBank/", previous_links =prev_links)
chas
CHAS_UK = 2610
CHAS_FLUENCY = 15
def get_stuff_for_url(url):
    dirs = get_orig_dirs(url)
    prev_links = [x for x in dirs]; prev_links.append("http://childes.psy.cmu.edu/browser/index.php")
    chas = search_dirs(dirs, url, previous_links = prev_links)
    
def get_stuff_for_url(url):
    dirs = get_orig_dirs(url)
    prev_links = [x for x in dirs]; prev_links.append("http://childes.psy.cmu.edu/browser/index.php")
    chas = search_dirs(dirs, url, previous_links = prev_links)
    return chas
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Frogs/English-Miami/")
CHAS_FROGS = 89
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Frogs/English-Slobin/")
CHAS_FROGS += 59
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Frogs/English-WolfHemp/")
CHAS_FROGS += 89
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Frogs/EnglishSpanish-Miami/")
CHAS_FROGS += 176
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Clinical-MOR/")
def search_dirs(dirs, base_url, previous_links=[]):
    chas = 0
    for d in dirs:
        print d
        text = urllib2.urlopen(d).read()
        soup = BeautifulSoup(text)
        data = soup.findAll('li', attrs={'class' : 'dir'})
        links = []
        for l in data:
            arefs = l.findAll('a')
            for a in arefs:
                if base_url in a['href'] and not (a['href'] in previous_links):
                    links.append(a['href'])
                    previous_links.append(a['href'])
        cha = soup.findAll('li', attrs={'class' : 'cha'})
        print "Dirs %d" % len(links)
        print links
        print "Chas %d" % len(cha)
        chas += search_dirs(links, base_url, previous_links = previous_links)
        chas += len(cha)
    return chas
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Clinical-MOR/")
CHAS_CLINICAL_MOR = 3427
total = 3427
total += CHAS_FROGS
CHAS_FLUENCY = 15
total += CHAS_FLUENCY
CHAS_UK = 2610
total += CHAS_UK
total += CHAS_NA
total += CHAS_FLUENCY
total
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Biling/Watkins/")
total += 72
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Biling/Deuchar/Eng/")
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Biling/Deuchar/")
total += 11
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Biling/ProjectS/")
def get_stuff_for_url(url):
    dirs = get_orig_dirs(url)
    prev_links = [x for x in dirs]; prev_links.append("http://childes.psy.cmu.edu/browser/index.php")
    chas = search_dirs(dirs, url, previous_links)
    return chas
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Biling/ProjectS/")
def get_stuff_for_url(url):
    dirs = get_orig_dirs(url)
    prev_links = [x for x in dirs]; prev_links.append("http://childes.psy.cmu.edu/browser/index.php")
    chas = search_dirs(dirs, url)
    return chas
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Biling/ProjectS/")
total += 60 # Biling/ProjectS
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Biling/YipMatthews/Eng/")
total += 254
get_stuff_for_url("http://childes.psy.cmu.edu/browser/index.php?url=Biling/Singapore/")
total += 181 # Biling/Singapore
total
total -= CHAS_FROGS
total -= CHAS_CLINICAL
total -= CHAS_CLINICAL_MOR
get_ipython().magic(u'ls ')
total
