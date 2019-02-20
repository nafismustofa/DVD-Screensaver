import pygame , random

class Display:
    def __init__(self):
        #Variables
        self.__is_running = True
        self.__FPS = 60
        self.__screen_size = (self.__screen_width , self.__screen_height) = (800 , 600)
        
        #Colors
        self.__color_black = (0 , 0 , 0)
        self.__color_white = (255 , 255 , 255)

        #DVD Icon Variables
        self.__dvd_x = self.__screen_width // 2
        self.__dvd_y = self.__screen_height // 2
        self.__dvd_speed = [random.choice([5 , -5]) , random.choice([5 , -5])]

        #Objects
        self.__game_display = None
        self.__icon = pygame.image.load("./assets/DVD_icon.png")
        self.__clock = pygame.time.Clock()

    #Display DVD
    def __dvd(self):
        dvd = pygame.image.load("./assets/DVD_logo.png")

        self.__game_display.blit(dvd , [(self.__dvd_x - 40) , (self.__dvd_y - 40)])

    #Main Display Function
    def display(self):
        #Pygame Initialization
        pygame.init()

        #Display Setup
        self.__game_display = pygame.display.set_mode(self.__screen_size)
        pygame.display.set_caption("DVD Sreensaver Hits The Corner!")
        pygame.display.set_icon(self.__icon)

        #Main Loop
        while self.__is_running:
            #Event Handlers
            for event in pygame.event.get():
                #Quitting Event
                if event.type == pygame.QUIT:
                    self.__is_running = False

            #Set Background Color
            self.__game_display.fill(self.__color_black)

            #Display DVD Icon
            self.__dvd()

            #Display Update
            pygame.display.update()

            #Set FPS
            self.__clock.tick(self.__FPS)
        
        #Quitting Functions
        pygame.quit()
        quit()