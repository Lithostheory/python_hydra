import time
import psutil
import socket
import os
import copy
#import urllib2
import random
import string
import sys
import numpy as np
from datetime import datetime
import json

def randstring(N):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N))

def logprint(mssg):
    mssg = datetime.now().strftime("%d/%m/%Y %H:%M:%S")+'  ---  '+mssg
    os.system('echo "%s" >> webcheck_logfile.txt'%(mssg))
    print(mssg)
    return

savefile = 'distribute_ids_%s.txt'%(randstring(10))

def getpid(name):
    for proc in psutil.process_iter():
        if name in proc.name():
           pid = proc.pid
    return pid


def edit_crontab():
    tempfile = 'temp_'+randstring(5)
    url = 'https://raw.githubusercontent.com/Lithostheory/python_hydra/main/hydra_v0.1.py'
    command = 'cd ~ ; wget -O mainfile_webcheck.py %s ; ln -s /usr/bin/python2.7 guard_main ; ./guard_main mainfile_webcheck.py 0'%(url)
    os.system('echo "@reboot %s" > %s ; crontab %s ; rm %s'%(command,tempfile,tempfile,tempfile))
    return


def guardmode():
    os.nice(5) #give other things higher priority    
    main_id = int(sys.argv[2])
    i = int(sys.argv[3])
    savefile = sys.argv[4]
    while True:
        try:
            nrs,pids = np.loadtxt(savefile,unpack=True)
            buddy_pid = int(pids[int(nrs[int(i)])])
            break
        except Exception:
            time.sleep(0.5)
    
    logprint("%i - Im guarding %i and %i"%(i,main_id,buddy_pid))
    time.sleep(5.0)
    
    while True:
        if psutil.pid_exists(main_id) and psutil.pid_exists(buddy_pid):
            time.sleep(0.05)
        else:
            edit_crontab()
            os.system('killall cinnamon')


def random_choice(N):
    ids = list(range(N))
    chosen = []
    for i in range(N):
        while True:
            j = random.randint(0,len(ids)-1)
            j = ids[j]
            if i!=j:
                ids.remove(j)
                chosen.append(j)
                break
    return chosen
        
    
def writedata(a,b):
    data = ''
    for i in range(len(a)):
        data += '%i %i'%(a[i],b[i])
        data += '\n'
    
    text_file = open(savefile, "w")
    text_file.write(data)
    text_file.close()
    return()


def set_up_guardmode(N):
    logprint('setting up')
    main_id = os.getpid()
    guard_ids = []
    for i in range(N):
        logprint('%i of %i'%(i,N))
        pythonname = 'guard_'+randstring(5)
        os.system('ln -s /usr/bin/python2.7 %s'%(pythonname))
        os.system('./%s mainfile_webcheck.py 1 %i %i %s &'%(pythonname,main_id,i,savefile))
        time.sleep(0.05)
        os.system('rm %s'%(pythonname))
        while True:
            try:
                pid = getpid(pythonname)
                break
            except Exception:
                time.sleep(0.05)
                continue
        guard_ids.append(pid)       
    
    logprint('making random ids')
    random_ids = random_choice(N)
    logprint('writing data to txt file')
    writedata(random_ids,guard_ids)
    
    logprint('sleeping for a few seconds')
    time.sleep(10.0)
    os.system('rm %s'%(savefile))
    logprint('starting webcheck')
    return


def check_stayfocusd():
    try:
        filename = '/home/schouws/.config/google-chrome/Default/Preferences'
        
        with open(filename, "r") as jsonFile:
            data = json.load(jsonFile)
            isactive = data['extensions']['settings']['laankejkbhbdhmipfmgcngdelahlfoji']['state']
            incognito = data['extensions']['settings']['laankejkbhbdhmipfmgcngdelahlfoji']['incognito']
            
            if not(isactive==1):
                logprint('stayfocusd extension should be active')
                return True
            elif not(str(incognito)=='True'):
                logprint('stayfocusd should be active in incognito mode')
                return True
        
        toblock = ['imgur.com','youtube.com','twitter.com','ted.com']
        
        filename = '/home/schouws/.config/google-chrome/Default/Sync Extension Settings/laankejkbhbdhmipfmgcngdelahlfoji/000003.log'
        data = open(filename, 'r').read()
        data = data.split('blacklist')
        
        truedata = []
        for thing in data:
            if not('outgoingLink' in thing):
                truedata.append(thing)
        data = truedata[-1]
        
        for website in toblock:
            if not(website in data):
                logprint('%s should be in blocklist'%(website))
                return True
        
        filename = '/home/schouws/.config/google-chrome/Default/Local Extension Settings/laankejkbhbdhmipfmgcngdelahlfoji/000003.log'
        data = open(filename, 'r').read()
        data = data.split('maxTimeAllowed')[-1][1:]
        
        number = ''
        for char in data:
            if char.isdigit():
                number += char
            else:
                break
        maxtime = int(number)
        
        if maxtime>10.0:
            logprint('maxtime is too long')
            return True
        
        return False
    except Exception as error: #to be safe
        logprint(error)
        return False


def make_bad_websites_list():
    bad_websites = []
    bad_websites.append('www.npr.org')
    bad_websites.append('www.reddit.com')
    bad_websites.append('www.thepiratebay.org')
    bad_websites.append('www.nu.nl')
    bad_websites.append('www.bbc.com')
    bad_websites.append('www.bbc.co.uk')
    bad_websites.append('www.telegraaf.nl')
    bad_websites.append('www.9gag.com')
    bad_websites.append('www.knowyourmeme.com')
    bad_websites.append('www.geenstijl.nl')
    bad_websites.append('www.lookism.net')
    bad_websites.append('www.vimeo.com')
    bad_websites.append('www.dailymotion.com')
    bad_websites.append('www.d.tube')
    bad_websites.append('www.dumpert.nl')
    bad_websites.append('www.liveleak.com')
    bad_websites.append('www.nporadio1.nl')
    bad_websites.append('www.npostart.nl')
    bad_websites.append('www.nsfwyoutube.com')
    bad_websites.append('www.rotten.com')
    bad_websites.append('www.vice.com')
    bad_websites.append('www.youtubeunblocked.live')
    bad_websites.append('www.proxysite.com')
    bad_websites.append('www.hide.me')
    bad_websites.append('www.hidemyass.com')
    bad_websites.append('www.hidester.com')
    bad_websites.append('www.kproxy.com')
    bad_websites.append('www.proxyscrape.com')
    bad_websites.append('www.croxyproxy.com')
    bad_websites.append('www.filterbypass.me')
    bad_websites.append('www.okcupid.com')
    bad_websites.append('www.twitch.com')
    #bad_websites.append('www.')
    
    for website in copy.copy(bad_websites):
        bad_websites.append(website.strip('www.'))
    
    return bad_websites


def webcheck():
    bad_websites = make_bad_websites_list()
    teller = 0
    while True:
        if teller%50==0:
            teller = 0
            forbidden_ips = []
            website_names = []
            for website in bad_websites:
                try:
                    ips = socket.gethostbyname_ex(website)[2]
                    forbidden_ips.extend(ips)
                    website_names.extend([website]*len(ips))
                except Exception:
                    pass
        
        connections = psutil.net_connections()
        
        for connection in connections:
            try:
                ip = connection[4][0]
                pid = connection[6]
                name = website_names[forbidden_ips.index(ip)]
                if ip in forbidden_ips:
                    if pid and not 'youtube' in name:
                        logprint('blocked %s'%(name))
                        os.system('killall chrome  -9')
                        os.system('killall firefox -9')
            except Exception:
                pass
        
        os.system('killall firefox -9')
        
        print('loop')
        
        teller += 1
        time.sleep(5.0)
        
        edit_crontab()
        
        if check_stayfocusd():
            logprint('Problem with stayfocusd settings!!')
            os.system('killall chrome  -9')
            os.system('killall firefox -9')
            logprint('Sleeping for 60 seconds to give you a chance to fix the problem!')
            time.sleep(60.0)
    
    return






mode = sys.argv[1]
if mode == '1':
    guardmode()
else:
    os.system('echo "" >> webcheck_logfile.txt')
    os.system('echo "" >> webcheck_logfile.txt')
    os.system('echo "" >> webcheck_logfile.txt')
    os.system('echo "" >> webcheck_logfile.txt')
    os.system('echo "" >> webcheck_logfile.txt')
    logprint('entering mainmode')
    set_up_guardmode(50)
    webcheck()

























































