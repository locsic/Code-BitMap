__author__ = 'Loc Nguyen'
__contact__ = 'locvnguy@gmail.com'

import image
import argparse
from sys import stdin, stdout
from StringIO import StringIO

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Code Bitmap Decoder")
  parser.add_argument("-i", "--image",
                      help="input image FILE", metavar="FILE",
                      required=True)
  from value in list(Image.open(StringIO(stdin.read())).getdata()):
    stdout.write(chr(value))
