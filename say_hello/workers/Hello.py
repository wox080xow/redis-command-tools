from django.conf import settings
from interface.worker import IWorker
# from dataclasses import dataclass

HELLO = settings.HELLO
# @dataclass
class Worker(IWorker):
    def _setup(self):
        self.helloText = HELLO
    def run(self):
        self._setup()
        print(self.helloText)
    def finish(self):
        print("The job is done.")