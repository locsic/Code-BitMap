__author__ = 'Loc Nguyen'
__contact__ = 'locvnguy@gmail.com'

import Image
from sys import stdin, stdout
from StringIO import StringIO

for value in list(Image.open(StringIO(stdin.read())).getdata()):
  stdout.write(chr(value))
