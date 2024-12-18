import pygame

class Gui():
    def __init__(self):
        self.root = pygame.init()
        self.clock = pygame.time.Clock()
        self.screen()
        self.loop()
    
    def screen(self):
        self.screen = pygame.display.set_mode((1280, 720))
        
    def loop(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
            self.screen.fill("black")
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

Gui()
