# coding=utf-8

import tkinter

from .mixins import WindowMinxin


class RootMenu(tkinter.Menu):

    def __init__(self, master):
        super().__init__(master)
        self.add_command(label='File')
