# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe
# scirpt para que tus programas en con tkinter o otrs sean un ejecutable
setup(name='suma',
      version="1.0",
      description="programa para sumar dos numeros",
      author="Mxcat",
      author_email="mxcat.xxtremxx@gmail.com",
      url="none",
      license="Libre",
      scripts=["suma.py"],
      windows=["suma.py"],
      options={"py2exe":{"bundle_files": 3,"compressed": True}},
      zipfile="none",
)