import sys
from os.path import abspath, dirname, join as path_join

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(abspath(path_join(dirname(__file__), 'log.txt')), 'w')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(
            str(message)
            .replace('\033[0;32m', '')
            .replace('\033[0m', '')
            .replace('\033[0;30;44m', '')
            .replace('\033[0;34m', '')
            .replace('\033[0;30;43m', '')
            .replace('\033[0;33m', '')
            .replace('\033[0;30;41m', '')
            .replace('\033[0;31m', '')
        )

    def flush(self):
        pass