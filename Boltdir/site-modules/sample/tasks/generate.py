#!/usr/bin/env python
import os, sys, json
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'python_task_helper', 'files'))
from task_helper import TaskHelper


hosts_file = open("/etc/hosts", "r").read()
resolv_file = open("/etc/resolv.conf", "r").read()

output = hosts_file + resolv_file

class Generate(TaskHelper):
    def task(self, args):
        return {'result': output}

if __name__ == '__main__':
    Generate().run()