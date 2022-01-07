import os
from os import listdir
from os.path import join, isdir, basename
import sys

base_dir = 'CTFS-2021'
prefix = '/ctf-writeups-2021'
ctf_path = sys.argv[1]

full_path = join(prefix,base_dir,ctf_path)

def link(path):
    full_path = join(prefix,base_dir,path)
    return f'## [{basename(path)}]({full_path})  \n'


rootfile = 'CTFS-2021/README.md'
with open(rootfile,'a') as f:
    f.write(link(ctf_path))
    

def make_links(path):
    print(path)
    directories = ['..']
    for i in listdir(join(base_dir,path)):
        if isdir(join(base_dir,path,i)):
            directories.append(i)
    with open(join(base_dir,path,'README.md'),'a') as f:
        for i in directories:
            f.write(link(join(path,i)))
    for i in directories[1:]:
        print(i)
        make_links(join(path,i))

make_links(ctf_path)




