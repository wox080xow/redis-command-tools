import sys

from django.conf import settings
from interface.worker import IWorker
from utils.functions import shcmd
# from dataclasses import dataclass

HELLO = settings.HELLO
# @dataclass
class Worker(IWorker):
    def run(self):
        output=shcmd("brah_brah")
        # output=shcmd("mkdir testdir")
        try:
            print("len(): ", len(output))
        except:
            # 跳出才會觸發SHFunctionTest裡的try except
            sys.exit(1)
            
            # 直接pass except就好像什麼錯誤都沒發生一樣
            # pass
        
        print("type(): ", type(output))
        print("output: ", output)
    def end(self):
        print("The job is ended.")