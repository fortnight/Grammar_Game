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

        self.cur_game = None
        self.cur_question = 'Question1'
        self.space_height = 300
        self.space_width = 1200
        self.paused = True
        self.direction = 1
        self.bttnTestRect = pygame.Rect(self.x, self.y, 200, 100)
        self.bttnTest = Buttons(self.bttnTestRect.x, self.bttnTestRect.y, self.bttnTestRect, 200, 100)
        self.bttnlist = []
        self.trophyList = []
        self.window = "MainMenu"

    def set_TrophyList(self, bttnList):
        self.trophyList = bttnList

    def add_to_TrophyList(self, button):
        if self.trophyList == []:
            self.trophyList = [button]
        elif self.trophyList != []:
            self.trophyList.append(button)

    def flush_TrophyList(self):
        self.trophyList = []

    def set_ButtonList(self, bttnList):
        self.bttnlist = bttnList

    def add_to_ButtonList(self, button):
        if self.bttnlist == []:
            self.bttnlist = [button]
        elif self.bttnlist != []:
            self.bttnlist.append(button)

    def flush_ButtonList(self):
        self.bttnlist = []

    def Game_question(self, screen, gamefile):
        self.Title_Text(screen, gamefile.readline()[:-1])
        self.Button_Text(screen, gamefile.readline()[:-1], self.bttnlist[0])
        self.Button_Text(screen, gamefile.readline()[:-1], self.bttnlist[1])
        self.Button_Text(screen, gamefile.readline()[:-1], self.bttnlist[2])
        self.Button_Text(screen, gamefile.readline()[:-1], self.bttnlist[3])
        #self.curline += 5

    def Game_Screen(self, screen):
        if self.cur_question == 'Trophy':
            self.add_to_TrophyList(self.cur_game)
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
        bttnQuit = MenuButton(quit_rect.x, quit_rect.y, quit_rect, quit_rect.width, quit_rect.height, "GAMES")
        self.add_to_ButtonList(bttnA)
        self.add_to_ButtonList(bttnB)
        self.add_to_ButtonList(bttnC)
        self.add_to_ButtonList(bttnD)
        self.add_to_ButtonList(bttnQuit)
        self.Button_Text(screen, "Quit", bttnQuit)
        gamefile = file(self.cur_game + '/' + self.cur_question + '.txt')
        self.Game_question(screen, gamefile)

    def Game_Menu(self, screen):
        self.flush_ButtonList()
        screen.fill((255, 255, 255))  # 255 for white
        RP = pygame.draw.rect(screen, (0, 255, 0), (565, 290, 463, 111))
        PP  = pygame.draw.rect(screen, (255, 0, 0), (565, 416, 463, 111))
        CS = pygame.draw.rect(screen, (255, 255, 0), (565, 542, 463, 111))
        quit_rect = pygame.draw.rect(screen, (0, 0, 255), (535, 668, 463, 111))
        bttnA = MenuButton(RP.x, RP.y, RP, RP.width, RP.height, "GAME_RP")
        bttnB = MenuButton(PP.x, PP.y, PP, PP.width, PP.height, "GAME_PP")
        bttnC = MenuButton(CS.x, CS.y, CS, CS.width, CS.height, "GAME_CS")
        bttnQuit = MenuButton(quit_rect.x, quit_rect.y, quit_rect, quit_rect.width, quit_rect.height, "MainMenu")
        self.add_to_ButtonList(bttnA)
        self.add_to_ButtonList(bttnB)
        self.add_to_ButtonList(bttnC)
        self.add_to_ButtonList(bttnQuit)
        TS = pygame.image.load(file('images/gamescreen.jpg.png'))
        screen.blit(TS, (0, 0))
       #self.Title_Text(screen, "Main Menu")
       #self.Button_Text(screen, "Games", bttnA)
       #self.Button_Text(screen, "Trophy Case", bttnB)
       #self.Button_Text(screen, "Credits", bttnC)
       #self.Button_Text(screen, "Exit", bttnD)

    def Main_Menu(self, screen):
        self.flush_ButtonList()
        screen.fill((255, 255, 255))  # 255 for white
        Game = pygame.draw.rect(screen, (0, 255, 0), (565, 290, 463, 111))
        TrophyCase = pygame.draw.rect(screen, (255, 0, 0), (565, 416, 463, 111))
        Credits = pygame.draw.rect(screen, (255, 255, 0), (565, 542, 463, 111))
        Quit = pygame.draw.rect(screen, (0, 0, 255), (565, 668, 463, 111))
        NinjaBear = pygame.draw.rect(screen, (255, 255, 255), (1300, 000, 100, 100))
        bttnA = MenuButton(Game.x, Game.y, Game, Game.width, Game.height, "GAMES")
        bttnB = MenuButton(TrophyCase.x, TrophyCase.y, TrophyCase, TrophyCase.width, TrophyCase.height, "TC")
        bttnC = MenuButton(Credits.x, Credits.y, Credits, Credits.width, Credits.height, "CR")
        bttnD = MenuButton(Quit.x, Quit.y, Quit, Quit.width, Quit.height, "RECTIFY")
        bttnE = MenuButton(NinjaBear.x, NinjaBear.y, NinjaBear, NinjaBear.width, NinjaBear.height, "NB")
        self.add_to_ButtonList(bttnA)
        self.add_to_ButtonList(bttnB)
        self.add_to_ButtonList(bttnC)
        self.add_to_ButtonList(bttnD)
        self.add_to_ButtonList(bttnE)
        self.Title_Text(screen, "Main Menu")
        self.Button_Text(screen, "Games", bttnA)
        self.Button_Text(screen, "Trophy Case", bttnB)
        self.Button_Text(screen, "Credits", bttnC)
        self.Button_Text(screen, "Exit", bttnD)
        TS = pygame.image.load(file('images/titlescreen.jpg.png'))
        screen.blit(TS, (0, 0))

    def Trophy_Case(self, screen):
        self.flush_ButtonList()
        quit_rect = pygame.draw.rect(screen, (0, 0, 255), (000, 000, 100, 100))
        bttnQuit = MenuButton(quit_rect.x, quit_rect.y, quit_rect, quit_rect.width, quit_rect.height, "MainMenu")
        self.add_to_ButtonList(bttnQuit)
        self.Title_Text(screen, "Trophy Case")
        self.Button_Text(screen, "Quit", bttnQuit)
        for trophy in self.trophyList:
            if trophy == 'games/RP':
                Banana = pygame.image.load(file('images/banana.png'))
                screen.blit(Banana, (100, 300))
            if trophy == 'games/PP':
                Watermelon = pygame.image.load(file('images/watermelon.png'))
                screen.blit(Watermelon, (300, 500))
            if trophy == 'games/CS':
                Strawberry = pygame.image.load(file('images/Strawberry.png'))
                screen.blit(Strawberry, (700, 300))

    def Credits(self, screen):
        self.flush_ButtonList()
        screen.fill((255, 255, 255)) # 255 for white
        quit_rect = pygame.draw.rect(screen, (0, 0, 255), (000, 000, 100, 100))
        bttnQuit = MenuButton(quit_rect.x, quit_rect.y, quit_rect, quit_rect.width, quit_rect.height, "MainMenu")
        self.add_to_ButtonList(bttnQuit)
        self.Title_Text(screen, "Credits")
        self.Button_Text(screen, "Quit", bttnQuit)

    def Ninja_Bear(self, screen):
        self.flush_ButtonList()
        screen.fill((255, 255, 255)) # 255 for white
        quit_rect = pygame.draw.rect(screen, (0, 0, 255), (000, 000, 100, 100))
        bttnQuit = MenuButton(quit_rect.x, quit_rect.y, quit_rect, quit_rect.width, quit_rect.height, "MainMenu")
        self.add_to_ButtonList(bttnQuit)
        NB = pygame.image.load(file('images/Ninja-bear.png'))
        center_x = (1400-159)/2
        center_y = (400-228)/2
        screen.blit(NB, (center_x, center_y + 300))
        self.Title_Text(screen, "Ninja Bear")
        self.Button_Text(screen, "Quit", bttnQuit)
    
    # Load text somewhat in the upper middle of the screen
    def Title_Text(self, screen, text):
        Font = pygame.font.SysFont("monospace", 64)
        Title = Font.render(text, False, (0, 0, 0))
        center_x = (self.space_width - Title.get_rect().width)/2
        center_y = (self.space_height - Title.get_rect().height)/2
        screen.blit(Title, (center_x, center_y))

    def Button_Text(self, screen, text, button):
        Font = pygame.font.SysFont("monospace", 40)
        Title = Font.render(text, False, (0, 0, 0))
        center_x = (button.size[0] - Title.get_rect().width)/2
        center_y = (button.size[1] - Title.get_rect().height)/2
        screen.blit(Title, (button.x + center_x, button.y + center_y))

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
        screen.fill((255, 255, 255)) # 255 for white
        if self.window == "MainMenu":
            self.cur_question = 'Question1'
            self.Main_Menu(screen)
        if self.window == "GAMES":
            self.cur_question = 'Question1'
            self.Game_Menu(screen)
        if self.window == "CR":
            self.Credits(screen)
        if self.window == "TC":
            self.Trophy_Case(screen)
        if self.window == "NB":
            self.Ninja_Bear(screen)
        if self.window == "GAME_RP":
            self.cur_game = 'games/RP'
            self.Game_Screen(screen)
        if self.window == "GAME_PP":
            self.cur_game = 'games/PP'
            self.Game_Screen(screen)
        if self.window == "GAME_CS":
            self.cur_game = 'games/CS'
            self.Game_Screen(screen)
        if self.window == "RECTIFY":
            sys.exit()

    def Next_Question(self):
        if self.cur_question == 'Question5':
            self.cur_question = 'Trophy'
        if self.cur_question == 'Question4':
            self.cur_question = 'Question5'
        if self.cur_question == 'Question3':
            self.cur_question = 'Question4'
        if self.cur_question == 'Question2':
            self.cur_question = 'Question3'
        if self.cur_question == 'Question1':
            self.cur_question = 'Question2'


    def GameAnswer(self, screen, answer):
        if answer:
            self.Next_Question()

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
                                    self.GameAnswer(screen, result[1])

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
