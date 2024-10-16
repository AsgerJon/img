"""ImgTool encapsulates image editing in a class. """
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from PIL.Image import Image
from PIL.Image import open as imgOpen
from worktoy.base import BaseObject, overload
from worktoy.desc import AttriBox, Field


class ImgTool(BaseObject):
  """ImgTool encapsulates image editing in a class. """

  sourceFile = AttriBox[str]()
  targetFile = AttriBox[str]()

  sourceImage = AttriBox[Image]()
  tempImage = AttriBox[Image]()

  aspect = Field()

  @overload(str)
  def load(self, filePath: str) -> None:
    """Load image from file."""
    self.sourceFile = filePath
    return self.load()

  @overload()
  def load(self) -> None:
    """Load image from the source file."""
    with imgOpen(self.sourceFile) as img:
      self.sourceImage = img.copy()
      self.tempImage = img.copy()

  def saveAs(self, filePath: str) -> None:
    """Save image as"""
    self.targetFile = filePath
    self.save()

  @overload(str)
  def save(self, filePath: str) -> None:
    """Save the image to a file."""
    self.targetFile = filePath
    self.save()

  @overload()
  def save(self) -> None:
    """Save the image to the target file."""
    if not self.targetFile:
      self.targetFile = self._generateGenericName()
    Image.save(self.tempImage, self.targetFile, format='PNG')

  def resize(self, width: int, height: int, ) -> None:
    """Resize the image."""
    if width < 0:
      return self.resize(int(height * self.aspect), height, )
    if height < 0:
      return self.resize(width, int(width / self.aspect), )
    self.tempImage = Image.resize(self.sourceImage, (width, height))
    if not self.targetFile:
      self.targetFile = self._generateResizedName()
    self.save()

  def _generateResizedName(self) -> str:
    """Generates a file name for the resized image."""
    baseName = os.path.abspath(self.sourceFile)
    name, ext = os.path.splitext(baseName)
    return f'{name}_resized{ext}'

  def _generateGenericName(self) -> str:
    """Generates a file name for the resized image."""
    baseName = os.path.abspath(self.sourceFile)
    name, ext = os.path.splitext(baseName)
    return f'{name}_generic{ext}'

  @aspect.GET
  def _getAspect(self, ) -> float:
    """Get the aspect ratio of the image."""
    return self.sourceImage.width / self.sourceImage.height
