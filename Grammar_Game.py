#!/usr/bin/python
import sys
import pygame
from Buttons import Buttons
from GameButton import GameButton
from MenuButton import MenuButton
from gi.repository import Gtk


class Grammar_Game:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0

        self.paused = True
        self.direction = 1
        self.bttnTestRect = pygame.Rect(self.x, self.y, 200, 100)
        self.bttnTest = Buttons(self.bttnTestRect.x, self.bttnTestRect.y, self.bttnTestRect, 200, 100)
        self.bttnlist = []
        self.window = "MainMenu"

    def set_ButtonList(self, bttnList):
        self.bttnlist = bttnList

    def add_to_ButtonList(self, button):
        if self.bttnlist == []:
            self.bttnlist = [button]
        elif self.bttnlist != []:
            self.bttnlist.append(button)

    def flush_ButtonList(self):
        self.bttnlist = []

    def Game_Screen(self, screen):
        self.flush_ButtonList()
        screen.fill((255, 255, 255))  # 255 for white
        answer_A = pygame.draw.rect(screen, (255, 0, 0), (000, 300, 1400, 100))
        answer_B = pygame.draw.rect(screen, (0, 255, 0), (000, 400, 1400, 100))
        answer_C = pygame.draw.rect(screen, (255, 0, 0), (000, 500, 1400, 100))
        answer_D = pygame.draw.rect(screen, (0, 255, 0), (000, 600, 1400, 100))
        quit_rect = pygame.draw.rect(screen, (0, 0, 255), (000, 000, 100, 100))
        bttnA = GameButton(answer_A.x, answer_A.y, answer_A, answer_A.width, answer_A.height, True)
        bttnB = GameButton(answer_B.x, answer_B.y, answer_B, answer_B.width, answer_B.height, False)
        bttnC = GameButton(answer_C.x, answer_C.y, answer_C, answer_C.width, answer_C.height, False)
        bttnD = GameButton(answer_D.x, answer_D.y, answer_D, answer_D.width, answer_D.height, False)
        bttnQuit = MenuButton(quit_rect.x, quit_rect.y, quit_rect, quit_rect.width, quit_rect.height, "MainMenu")
        self.add_to_ButtonList(bttnA)
        self.add_to_ButtonList(bttnB)
        self.add_to_ButtonList(bttnC)
        self.add_to_ButtonList(bttnD)
        self.add_to_ButtonList(bttnQuit)

    def Main_Menu(self, screen):
        self.flush_ButtonList()
        screen.fill((255, 255, 255))  # 255 for white
        Game = pygame.draw.rect(screen, (0, 255, 0), (000, 300, 1400, 100))
        HowToPlay = pygame.draw.rect(screen, (255, 0, 0), (000, 400, 1400, 100))
        TrophyCase = pygame.draw.rect(screen, (255, 255, 0), (000, 500, 1400, 100))
        Quit = pygame.draw.rect(screen, (0, 0, 255), (000, 600, 1400, 100))
        bttnA = MenuButton(Game.x, Game.y, Game, Game.width, Game.height, "GAMES")
        bttnB = MenuButton(HowToPlay.x, HowToPlay.y, HowToPlay, HowToPlay.width, HowToPlay.height, "HTP")
        bttnC = MenuButton(TrophyCase.x, TrophyCase.y, TrophyCase, TrophyCase.width, TrophyCase.height, "TC")
        bttnD = MenuButton(Quit.x, Quit.y, Quit, Quit.width, Quit.height, "RECTIFY")
        self.add_to_ButtonList(bttnA)
        self.add_to_ButtonList(bttnB)
        self.add_to_ButtonList(bttnC)
        self.add_to_ButtonList(bttnD)
        self.Title_Text(screen, "Main Menu")

    def Trophy_Case(self, screen):
        self.flush_ButtonList()
        screen.fill((255, 255, 255)) # 255 for white
        quit_rect = pygame.draw.rect(screen, (0, 0, 255), (000, 000, 100, 100))
        bttnQuit = MenuButton(quit_rect.x, quit_rect.y, quit_rect, quit_rect.width, quit_rect.height, "MainMenu")
        self.add_to_ButtonList(bttnQuit)
        self.Title_Text(screen, "Trophy Case")

    def How_To_Play(self, screen):
        self.flush_ButtonList()
        screen.fill((255, 255, 255)) # 255 for white
        quit_rect = pygame.draw.rect(screen, (0, 0, 255), (000, 000, 100, 100))
        bttnQuit = MenuButton(quit_rect.x, quit_rect.y, quit_rect, quit_rect.width, quit_rect.height, "MainMenu")
        self.add_to_ButtonList(bttnQuit)
        self.Title_Text(screen, "How To Play")
    
    # Load text somewhat in the upper middle of the screen
    def Title_Text(self, screen, text):
        Font = pygame.font.SysFont("monospace", 64)
        Title = Font.render(text, False, (0, 0, 0))
        screen.blit(Title, (400, 200))

    def set_paused(self, paused):
        self.paused = paused

    #def button to test events of things
    def EVENT_TEST_BUTTON(self):
        if self.paused:
            self.set_paused(False)
        elif self.paused == False:
            self.set_paused(True)

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass
    
    def Set_Screen(self, screen):
        if self.window == "MainMenu":
            self.Main_Menu(screen)
        if self.window == "GAMES":
            self.Game_Screen(screen)
        if self.window == "HTP":
            self.How_To_Play(screen)
        if self.window == "TC":
            self.Trophy_Case(screen)
        if self.window == "RECTIFY":
            sys.exit()

    def GameAnswer(self, answer):
        pass

    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                       #print(self.bttnlist)
                        for bttn in self.bttnlist:
                            result = bttn.EVENT_CLICK()
                            if result != False:
                                if result[0]:
                                    self.window = result[1]
                                elif result[0] == False:
                                    self.window = "GAMES"
                                    self.GameAnswer(result[1])

            # Move the ball
#           if not self.paused:
#               self.x += self.vx * self.direction
#               if self.direction == 1 and self.x > screen.get_width() + 100:
#                   self.x = -100
#               elif self.direction == -1 and self.x < -100:
#                   self.x = screen.get_width() + 100
#
#               self.y += self.vy
#               if self.y > screen.get_height() - 100:
#                   self.y = screen.get_height() - 100
#                   self.vy = -self.vy
#
#               self.vy += 5

            # Clear Display
            screen.fill((255, 255, 255))  # 255 for white
            self.Set_Screen(screen)

            #draw a rectangle
           #pygame.draw.rect(screen, (255, 0, 0), (000, 300, 1400, 100))
                        
            # Draw the ball
            #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)

#    def EVENT_CLICK():
#        pass

# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = Grammar_Game()
    game.run()

if __name__ == '__main__':
    main()
