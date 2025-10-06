import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ninja Game')

        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.player = pygame.image.load('data/images/entities/player.png')
        self.player.set_colorkey((0, 0, 0))
        self.player_position = [300, 200]
        self.movement = [0, 0, 0, 0]  
    
    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            self.screen.blit(self.player, self.player_position)
            self.player_position[1] += (self.movement[1] - self.movement[0]) * 2
            self.player_position[0] += (self.movement[3] - self.movement[2]) * 2
            self.screen.blit(self.player, self.player_position)
            
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
                    if event.key == pygame.K_UP:
                        self.movement[0] = 1
                    if event.key == pygame.K_DOWN:
                        self.movement [1] = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = 0
                    if event.key == pygame.K_DOWN:
                        self.movement [1] = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[2] = 1
                    if event.key == pygame.K_RIGHT:
                        self.movement [3] = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[2] = 0
                    if event.key == pygame.K_RIGHT:
                        self.movement [3] = 0
                # wasd movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = 1
                    if event.key == pygame.K_s:
                        self.movement [1] = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = 0
                    if event.key == pygame.K_s:
                        self.movement [1] = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[2] = 1
                    if event.key == pygame.K_d:
                        self.movement [3] = 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[2] = 0
                    if event.key == pygame.K_d:
                        self.movement [3] = 0

ninja_game = Game()
ninja_game.run()
            
        