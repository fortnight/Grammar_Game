#!/usr/bin/python
import pygame
from gi.repository import Gtk

class Buttons:
    def __init__(self, pos, name, w, h):
        self.pos = pos
        self.name = name
        self.size = (w, h)

    # Method to see if the current positon is on a button
    def onButtons(self, pos):
        x, y = pos
        if (self.pos[0] < x and
            self.pos[0] + self.size[0] > x and
            self.pos[1] < y and
            self.pos[1] + self.size[1] > y
            ):
            return pos
        else: return None

    # The event to call when things get clicked on
    def EVENT_CLICK(self):
        mouseAt = pygame.mouse.get_pos();   # see where the mouse currently is
        buttons_event = [                   # an array of buttons and their events
                            [self.bttnQuit ,self.EVENT_QUIT],
                            [self.bttnPlay , self.EVENT_PLAY],
                            [self.bttnHow ,self.EVENT_HELP],
                        ]
        for bttn,event in buttons_event:    
            if bttn.onButtons(mouseAt):     # see if the mouse is on the button when called
                self.helperRaiseEvent(event)# call the event in that place of the array
                break                       # only call one event at any click (no button overlap)
