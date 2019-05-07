# coding=utf-8

import tkinter

import utils
import config

from .menu import RootMenu
from .mixins import WindowMinxin

logger = utils.get_logger()


class MainWindow(tkinter.Tk, WindowMinxin):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_scale_size()
        self.title("Musicsa")
        self.iconbitmap(config.ICON_FILENAME)
        self.geometry("800x600")
        self['menu'] = RootMenu(self)
