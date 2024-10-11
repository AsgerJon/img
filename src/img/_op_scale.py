"""OPScale encapsulates the image rescaling in a class exposing the
overloading capabilities inherited from BaseObject. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from worktoy.base import BaseObject, overload
from worktoy.desc import AttriBox, THIS
from worktoy.text import typeMsg, monoSpace

from img import ImgTool


class OPScale(BaseObject):
  """OPScale encapsulates the image rescaling in a class exposing the
  overloading capabilities inherited from BaseObject. """

  @overload(str, str, int, int)
  def __init__(self, *args) -> None:
    src, tgt, w, h = args
    tool = ImgTool()
    tool.load(src)
    tool.resize(w, h)
    tool.save(tgt)

  @overload(str, int, int)
  def __init__(self, *args) -> None:
    src, w, h = args
    tool = ImgTool()
    tool.load(src)
    tool.resize(w, h)
    tool.save()

  @overload(str, str, tuple)
  def __init__(self, *args) -> None:
    src, tgt, dim = args
    if len(dim) == 2:
      if any([not isinstance(i, int) for i in dim]):
        e = typeMsg('dim', dim, int)
        raise TypeError
      w, h = dim
    else:
      e = """The 'dim' tuple must have exactly two elements, but received: 
      '%s'!"""
      raise ValueError(monoSpace(e % str(dim)))
    tool = ImgTool()
    tool.load(src)
    tool.resize(w, h)
    tool.save(tgt)

  @overload(str, tuple)
  def __init__(self, *args) -> None:
    src, dim = args
    if len(dim) == 2:
      if any([not isinstance(i, int) for i in dim]):
        e = typeMsg('dim', dim, int)
        raise TypeError
      w, h = dim
    else:
      e = """The 'dim' tuple must have exactly two elements, but received: 
      '%s'!"""
      raise ValueError(monoSpace(e % str(dim)))
    tool = ImgTool()
    tool.load(src)
    tool.resize(w, h)
    tool.save()
