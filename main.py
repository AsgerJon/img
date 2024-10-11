"""Main Tester Script"""
#  AGPL-3.0 license
#  Copyright (c) 2023-2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys

from worktoy.meta import CallMeMaybe
from worktoy.text import typeMsg, stringList

from img import ImgTool
from moreworktoy import parseNum
from yolo import yolo


def tester00() -> int:
  """Hello World!"""
  stuff = ['hello world!', os, sys, frozenset]
  for item in stuff:
    print(item)
  return 0


def tester01() -> int:
  """Testing zshpy"""

  for item in sys.argv:
    print(item)
  return 0


def tester02() -> int:
  """Testing file stuff"""
  print(__file__)
  here = os.path.abspath(__file__)
  print(here)
  baseName = os.path.basename(here)
  print('os.path.basename: %s' % baseName)
  name, ext = os.path.splitext(baseName)
  print('name: %s' % name)
  print('ext: %s' % ext)
  return 0


def func(*args) -> int:
  """The default function"""
  print(sys.argv[1], 'func')
  return 0


def scale(*args) -> int:
  """Resizes the image"""


def main() -> int:
  """Main entry point"""
  args = [*sys.argv, ]
  sysFile = args.pop(0)
  hostDir = args.pop(0)
  funcKey = args.pop(0)
  self = os.path.basename(os.path.dirname(__file__))
  if __file__ != sysFile:
    print("""file and sys.argv mismatch!""")
    return 1
  if self not in funcKey.split('.'):
    print("""script name and sys.argv mismatch:""")
    print(self, funcKey, sysFile)
    return 2
  key = 'func' if '.' not in funcKey else funcKey.split('.')[1]
  target = globals().get(key, None)
  if not isinstance(target, CallMeMaybe):
    print(typeMsg('target', target, CallMeMaybe))
    return 3
  return target(*args, hostDir)


if __name__ == '__main__':
  yolo(main)
