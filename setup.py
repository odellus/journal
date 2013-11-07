#! /usr/bin/env python

import os, shutil, subprocess

name = raw_input('What is your name?\n -->')
#position = raw_input('What is your position at work?\n--> ')
#company = raw_input('What company do your work for?\n--> ')
#email = raw_input('What is your email address?\n-- ')

print 'So to double-check your name is '+name+'.'

#position_pre = '# Position\t: '+position
#company_pre = '# Company\t: '+company
#email_pre = '# E-mail\t: '+email

journal_preheader = name#+'\n'+position_pre+'\n'+company_pre+'\n'+email_pre
writ_str = "\nJOURNAL_PREHEADER = ['"+journal_preheader+"']\n"

fh = open(os.environ.get('HOME')+'/.twsetup_defaults.py','a')
fh.write(writ_str)
fh.close()

#fh= open(os.environ.get('HOME')+'/.twsetup_defaults.py','a')
#fh.write(writ_str)
#fh.close()

apt_depen_lst = ['couchdb','python-setuptools','emacs','python-dev']
# Installing dependencies
print "Installing CouchDB..."
print "You will be asked to input your password."
p = subprocess.Popen('sudo apt-get install '+' '.join(apt_depen_lst),shell=True)
p.communicate()

p = subprocess.Popen('sudo easy_install pip',shell=True)
p.communicate()

pip_depen_lst = ['couchdbkit','python-dateutil','restkit', 'socketpool']

print "Installing CouchDBKit..."
p = subprocess.Popen('sudo pip install '+' '.join(pip_depen_lst),shell=True)
p.communicate()


p = subprocess.Popen('sudo chmod +x ./journal',shell=True)
p.communicate()

print "Copying to /usr/bin/journal"
p = subprocess.Popen('sudo cp ./journal /usr/bin/journal',shell=True)
p.communicate()

p = subprocess.Popen('sudo couchdb -b',shell=True)
p.communicate()

print "To use journal now, simply type 'journal' on the command line."
print "Have a nice day."
