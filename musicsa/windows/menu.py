# coding=utf-8

import tkinter

from .mixins import WindowMinxin


class RootMenu(tkinter.Menu):

    def __init__(self, root):
        super().__init__(root)
        self.add_command(label='File')
