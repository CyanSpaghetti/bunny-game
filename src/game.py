#importing everything
import pygame as py
import sys, os
from src.settings import window

class Game:
    def __init__(self):
        self.running = True
        self.window = py.display.set_mode((window.width,window.height))
    def init(self):
        py.display.set_caption(window.title)
    def update(self):
        pass    
    def input(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.running = False
    def draw(self):
        pass
    def quit(self):
        py.quit()
        sys.exit()

