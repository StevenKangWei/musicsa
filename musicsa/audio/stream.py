# coding=utf-8

import struct
from queue import Queue
import threading

import pyaudio
import numpy as np

import config
import utils

logger = utils.get_logger()


class Stream(object):

    def __init__(self):
        self.chunk = 1024
        self.channels = config.AUDIO_CHANNELS
        self.bit = config.AUDIO_BIT
        self.bit_width = config.AUDIO_BIT_WIDTH
        self.rate = config.AUDIO_SAMPLE_RATE
        self.input = False
        self.output = False

        self.pyaudio = None
        self.stream = None

        self.buffer = Queue()
        self.running = False

    def read_frames(self):
        if not self.stream:
            return None
        frames = self.stream.read(self.chunk)
        return frames

    def get_frames(self):
        frames = self.buffer.get(block=True)
        with self.buffer.mutex:
            self.buffer.queue.clear()
        return frames

    def get_data(self, frames=None):
        if not frames:
            frames = self.get_frames()
        data = struct.unpack(str(self.chunk) + "h", frames)
        data = np.array(data)
        return data

    def close_stream(self):
        pass

    def close_pyaudio(self):
        if not self.pyaudio:
            return
        logger.info('terminate pyaudio...')
        self.pyaudio.terminate()
        self.pyaudio = None

    def close(self):
        self.running = False
        self.close_stream()
        self.close_pyaudio()

    def __del__(self):
        self.close()


class WireStream(Stream):

    def __init__(self):
        super().__init__()
        self.input = True
        self.output = True
        self.play_thread = threading.Thread(target=self.play_task)
        self.play_thread.setDaemon(True)

    def start(self):
        self.running = True
        self.play_thread.start()
        if self.pyaudio is None:
            logger.info('start create pyaudio...')
            self.pyaudio = pyaudio.PyAudio()
        if self.input and self.stream is None:
            logger.info('start create stream...')
            self.stream = self.pyaudio.open(
                format=pyaudio.get_format_from_width(self.bit_width),
                channels=self.channels,
                rate=self.rate,
                input=self.input,
                output=self.output,
                frames_per_buffer=self.chunk,
            )

    def play_task(self):
        while self.running:
            frames = self.read_frames()
            if not frames:
                continue
            self.buffer.put(frames)
            self.stream.write(frames)

    def close_stream():
        if not self.stream:
            return
        logger.info('close stream...')
        self.stream.stop_stream()
        self.stream.close()
        self.stream = None
