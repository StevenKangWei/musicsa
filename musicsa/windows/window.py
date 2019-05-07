# coding=utf-8

import tkinter

import utils
import config

from .menu import RootMenu
from .mixins import WindowMinxin
from .stream import StreamForm
from audio.stream import WireStream

logger = utils.get_logger()


class MainWindow(tkinter.Tk, WindowMinxin):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_scale_size()
        self.title("Musicsa")
        self.iconbitmap(config.ICON_FILENAME)
        self.geometry("800x600")
        self['menu'] = RootMenu(self)

        logger.info('create wirestream')
        self.stream = WireStream()
        self.stream.start()
        logger.info('create stream form')
        self.stream_form = StreamForm(self)
