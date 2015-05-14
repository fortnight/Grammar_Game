#!/usr/bin/python
import pygame
from gi.repository import Gtk

class MenuButton:
    def __init__(self, x, y, rect, w, h, screen):
        self.x = x
        self.y = y
        self.rect = rect
        self.size = (w, h)
        self.screen = screen

    # Method to see if the current positon is on a button
    def onButtons(self, pos):
        x, y = pos
        if (self.x < x and
            self.x + self.size[0] > x and
            self.y < y and
            self.y + self.size[1] > y
            ):
            return pos
        else: return False

    @staticmethod
    def helperRaiseEvent(events):
        for e in events: e();

    # The event to call when things get clicked on
    def EVENT_CLICK(self):
        # see where the mouse currently is
        mouseAt = pygame.mouse.get_pos();   
        # an array of buttons and their events
        #buttons_event = [                   
        #                    [self.bttnQuit ,self.EVENT_QUIT],
        #                    [self.bttnPlay , self.EVENT_PLAY],
        #                    [self.bttnHow ,self.EVENT_HELP],
        #                     [self.bttnTest ,self.EVENT_TEST_BUTTON]
        #                ]
        #for bttn,event in buttons_event:    
            # see if the mouse is on the button when called
        if self.onButtons(mouseAt):     
            # call the event in that place of the array
            #self.helperRaiseEvent(event)
            # only call one event at any click (no button overlap)
            return True, self.screen #self.EVENT_TEST_BUTTON()
                #break
        elif self.onButtons(mouseAt) == False:
            return False

   # def EVENT_TEST_BUTTON(self):
   #     screen = pygame.display.get_surface()
   #     pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, 200, 100))

