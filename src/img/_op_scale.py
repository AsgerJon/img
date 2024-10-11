"""OPScale encapsulates the image rescaling in a class exposing the
overloading capabilities inherited from BaseObject. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from icecream import ic
from worktoy.base import BaseObject, overload
from worktoy.desc import AttriBox, THIS
from worktoy.text import typeMsg, monoSpace

from img import ImgTool

ic.configureOutput(includeContext=True)


class OPScale(BaseObject):
  """OPScale encapsulates the image rescaling in a class exposing the
  overloading capabilities inherited from BaseObject. """

  @overload(str, str, int, int)
  def __init__(self, *args) -> None:
    ic()
    src, tgt, w, h = args
    tool = ImgTool()
    tool.load(src)
    tool.resize(w, h)
    tool.save(tgt)
    self.validate(tool, w, h)

  @overload(str, int, int)
  def __init__(self, *args) -> None:
    ic()
    src, w, h = args
    tool = ImgTool()
    tool.load(src)
    tool.resize(w, h)
    tool.save()
    self.validate(tool, w, h)

  @overload(str, str, tuple)
  def __init__(self, *args) -> None:
    ic()
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
    self.validate(tool, w, h)

  @overload(str, tuple)
  def __init__(self, *args) -> None:
    ic()
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
    self.validate(tool, w, h)

  @staticmethod
  def validate(tool: ImgTool, w: int, h: int) -> None:
    """Validate the tool."""
    if not isinstance(tool, ImgTool):
      e = typeMsg('tool', tool, ImgTool)
      raise TypeError(e)
    resizedFile = tool.targetFile
    newTool = ImgTool()
    newTool.load(resizedFile)
    w0, h0 = newTool.sourceImage.size
    tol = int(w / 20 + h / 20)  # 10 % averaged
    if w < 0:
      w = h * tool.aspect
    elif h < 0:
      h = w / tool.aspect
    if (w0 - w) ** 2 + (h0 - h) ** 2 > tol ** 2:
      e = """The difference between actual and expected size exceeds the 
      allowable tolerance!"""
      raise ValueError(monoSpace(e))
