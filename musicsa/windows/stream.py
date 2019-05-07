# coding=utf-8

import tkinter
import threading

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

import utils

logger = utils.get_logger()


class StreamForm(object):

    def __init__(self, master):
        self.master = master
        self.stream = self.master.stream
        self.chunk = self.stream.chunk
        self.create_figure()
        self.draw_thread = threading.Thread(target=self.draw_task)
        self.draw_thread.setDaemon(True)
        self.draw_thread.start()

    def draw_task(self):
        while self.stream.running:
            logger.info('get data from stream')
            data = self.stream.get_data()
            if data is None:
                continue
            logger.info('draw data...')
            self.line.set_ydata(data)
            self.canvas.draw()
            self.canvas.flush_events()

    def create_figure(self):
        plt.ion()
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.axes.grid()
        self.axes.set_ylim(-40000, 40000)
        self.axes.set_xlim(0, self.chunk)
        self.line, = self.axes.plot(np.arange(0, self.chunk), np.zeros(self.chunk))

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
