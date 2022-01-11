#!/usr/bin/env python3 

import datetime 
import os 

def do_magic():
    now = datetime.datetime.now()
    return "Hello! {0}".format(now)

if __name__ == "__main__":
    print("Content-type: text/html\n\n") 
    print(do_magic()) 
    print(os.enriron)

