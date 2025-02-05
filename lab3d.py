#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space '''
# Author ID: [seneca_id]

import subprocess

def free_space():
    p = subprocess.Popen("df -h / | awk 'NR==2 {print $4}'", stdout=subprocess.PIPE, shell=True)
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())
