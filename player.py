import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.spritesheet = pygame.image.load('Res/mario.png')
        self.image = self.get_image(0, 0, 16, 16)  # Extract the first sprite from the sheet
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_image(self, x, y, width, height):
        # Extract a sprite from the sprite sheet
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))  # Set the background color of the sprite to transparent
        return image

    def update(self):
        # Define the player's movement
        pass


# Set up the game window
screen_width = 800
screen_height = 600
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario Game")

# Create a sprite group
all_sprites = pygame.sprite.Group()

# Create a player sprite and add it to the group
player = Player(0, 0)
all_sprites.add(player)

# Game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Update the sprites
    all_sprites.update()

    # Draw the sprites
    game_display.fill((255, 255, 255))
    all_sprites.draw(game_display)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
