from os import listdir
import os,shutil
from os.path import isfile

thedir = 'tmp'
if not os.path.exists(thedir):
    os.makedirs(thedir)
for f in listdir():
    if '.' not in f and isfile(f):
        shutil.move(f,thedir)
        # print(f)
