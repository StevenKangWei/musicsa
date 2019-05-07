# coding=utf-8

import config


class WindowMinxin(object):

    def set_scale_size(self, scaling=None):
        if scaling is None:
            scaling = config.WINDOW_SCALING
        self.tk.call('tk', 'scaling', scaling)

    def center_window(self):
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        width = 800
        height = 600

        size = '{width}x{height}+{x}+{y}'.format(
            width=width,
            height=height,
            x=int((screenwidth - width) / 2),
            y=int((screenheight - height) / 2)
        )
        self.geometry(size)
