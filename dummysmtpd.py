#!/usr/bin/env python
"""
Dummy SMTP server accepting everything and storing message to disk.
Useful for unit testing.
"""

import asyncore
import time
import os
import os.path

from argparse import ArgumentParser
from itertools import count
from smtpd import SMTPServer


class DummySMTP(SMTPServer):
    """SMTP server storing received emails to disk"""

    def __init__(self, path, *args, **kwargs):
        self.path = path
        self.counter = count(1)
        # smtpd.SMTPServer is still on old-school class on 2.7
        SMTPServer.__init__(self, *args, **kwargs)

    def process_message(self, peer, mailfrom, rcpttos, data):
        filename = '{}.{}.eml'.format(time.time(), self.counter.next())
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        path = os.path.join(self.path, filename)
        with open(path, 'w') as f:
            f.write(data)


def main():
    """Parse arguments and start server"""
    parser = ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('-h', '--host', dest='host', action='store',
            default='localhost', help='IP or hostname to bind to')
    parser.add_argument('-p', '--port', dest='port', action='store', type=int,
            default=1025, help='Port to bind to')
    parser.add_argument('-d', dest='path', action='store',
            default=os.getcwd(), help='Folder to store emails to')
    parser.add_argument('--help', dest='help', action='store_true',
            help='Display this help')
    args = parser.parse_args()
    if args.help:
        parser.print_help()
        return
    _ = DummySMTP(args.path, (args.host, args.port), None)
    asyncore.loop()

if __name__ == '__main__':
    main()
