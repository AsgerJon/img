"""The 'parseContainer' function parses a 'str' to a list, a dict or a
set. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.text import typeMsg, stringList


def parseContainer(data: str) -> object:
  """The 'parseContainer' function parses a 'str' to a list, a dict or a
  set. """
  if not isinstance(data, str):
    e = typeMsg('data', data, str)
    raise TypeError(e)
  data = data.strip()
  if data.startswith('[') and data.endswith(']'):
    return [i.strip() for i in data.split(',')]
  if data.startswith('{') and data.endswith('}'):
    entries = data[1:-1].split(',')
    maybeDict = []
    for entry in entries:
      if len(entry.split(':')) == 2:
        maybeDict.append(entry)
        continue
      break
    else:
      return {k: v for (k, v) in maybeDict}
    return set(*entries)
  if data.startswith('(') and data.endswith(')'):
    return tuple(i.strip() for i in data.split(','))
