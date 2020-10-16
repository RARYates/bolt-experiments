#!/usr/bin/env python
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'python_task_helper', 'files'))
from task_helper import TaskHelper

#print(os.environ.get(PT_contents))

class read(TaskHelper):
    def task(self,args):
        f = open("test.txt", "a")
        #f.write(os.environ[PT_contents])
        for x in args:
            f.write(x)
        f.close

if __name__ == '__main__':
    read().run()