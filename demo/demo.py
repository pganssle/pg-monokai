#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Docstring

This is an example of a docstring
"""

import re
from os import path
import numpy as np

class ExampleClass(ExampleParent):
    def __init__(self):
        """
        Constructor
        """
        pass

    def method(self, parameter=None, numeric=1.0):
        print("This is a string.")          # Comments are bright so you can read them

        '''
        print("Use single-quoted multi-line strings to comment things out")
        if True:
            print("They are a darker color to be less noticeable")
        '''

class AnotherExample:
    """
    An example class
    """
    @property
    def exampleprop(self):
        return self._exampleprop
    @exampleprop.setter
    def exampleprop(self, value):
        self._exampleprop = value
    
    def run(self, edit):
        self.example_method(np.cos(3 * np.pi / 5))          # Syntax error!

        if self.test is not None:
            self.test = None
        else:
            raise ValueError('This program does nothing')