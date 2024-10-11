"""The 'parseNum' method parses a 'str' to a numeric type if possible."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations


def parseNum(*args) -> list:
  """The 'parseNum' receives any number of strings and returns them having
  cast them as a numeric type if possible."""
  out = []
  for arg in args:
    try:
      out.append(int(arg))
    except ValueError as intError:
      if 'invalid literal' in str(intError):
        try:
          out.append(float(arg))
        except ValueError as floatError:
          if 'could not convert' in str(floatError):
            try:
              out.append(complex(arg))
            except ValueError as complexError:
              if 'malformed string' in str(complexError):
                out.append(arg)
  return out
