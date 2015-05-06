#!/usr/bin/python
import pygame
from gi.repository import Gtk

class Buttons:
    def __init__(self, pos, name, x, y):
        self.pos = pos
        self.name = name
        self.size = (x, y)

    def onButtons(self, pos):
        x, y = pos
        if (self.pos[0] < x and
            self.pos[0] + self.size[0] > x and
            self.pos[1] < y and
            self.pos[1] + self.size[1] > y
            ):
            return pos
        else: return None

    def EVENT_CLICK(self):
        mouseAt = pygame.mouse.get_pos();
        buttons_event = [
                            [self.bttnQuit ,self.EVENT_QUIT],
                            [self.bttnPlay , self.EVENT_PLAY],
                            [self.bttnHow ,self.EVENT_HELP],
                        ]
        for bttn,event in buttons_event:
            if bttn.onButtons(mouseAt):
                self.helperRaiseEvent(event)
                break
