import pygame
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ninja Game')

        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.movement = [0, 0]
        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
    
    def run(self):
        while True:
            #background color
            self.screen.fill((14, 219, 248))           
            
            self.player.update(self.movement[1] - self.movement[0], 0)
            self.player.render(self.screen)




            # frame rate
            pygame.display.update()
            self.clock.tick(60)
            
            # Event handler
            for event in pygame.event.get():
                
                # exit game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = 1
                    if event.key == pygame.K_RIGHT:
                        self.movement [1] = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = 0
                    if event.key == pygame.K_RIGHT:
                        self.movement [1] = 0
                # wasd movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = 1
                    if event.key == pygame.K_d:
                        self.movement [1] = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = 0
                    if event.key == pygame.K_d:
                        self.movement [1] = 0

ninja_game = Game()
ninja_game.run()