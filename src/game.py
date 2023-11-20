#importing everything
import pygame as py
import sys, os
from src.settings import window

class Game:
    def __init__(self): # object constructor for the game
        self.running = True
        self.window = py.display.set_mode((window.width,window.height))
    def init(self): # initialize settings
        py.display.set_caption(window.title)
    def update(self): # update each frame
        pass    
    def input(self): # take input 
        for event in py.event.get():
            if event.type == py.QUIT:
                self.running = False
    def draw(self): #draw graphics 
        pass
    def quit(self): # quit game 
        py.quit()
        sys.exit()

