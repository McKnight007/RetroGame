# Copyright 2023 Mark Muriuki
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario Game")

# Load the background image
background_image = pygame.image.load("Res/bg.jpg")


# Define the Platform sprite class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Define the Player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        sprite_sheet = pygame.image.load("Res/mario.png").convert_alpha()
        self.image = pygame.Surface((16, 16)).convert_alpha()
        self.image.blit(sprite_sheet, (0, 0), (0, 0, 16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 1
        self.y_velocity = 0.0
        self.gravity = 0.3

    def update(self):
        # Handle keyboard input for left/right movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.rect.left > 0:
                self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.rect.left < screen_width - 17:
                self.rect.x += self.speed

        # Handle keyboard input for up/down movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.jump()
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # Move down, but don't go out of bounds
            if self.rect.bottom < screen_height:
                self.rect.y += self.speed

        # Apply gravity to the player's y velocity
        self.y_velocity += self.gravity

        # Move the player's y position according to its velocity
        self.rect.y += self.y_velocity

        # Keep the player within the screen bounds
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.y_velocity = 0

            # Slow down the landing to make it smooth
            if abs(self.y_velocity) < 3:
                self.y_velocity = 0
            else:
                self.y_velocity *= -0.5

    def jump(self):
        # Only jump if the player is on the ground
        if self.rect.bottom == screen_height:
            # Set the player's y velocity to a negative value to make it jump
            self.y_velocity = -10


# Create a sprite group
all_sprites = pygame.sprite.Group()

# Create the player sprite and add it to the group
player = Player(5, screen_height / 2)
all_sprites.add(player)

# Create the platform sprites and add them to the group
platform1 = Platform(0, screen_height - 50)
all_sprites.add(platform1)

platform2 = Platform(200, 400)
all_sprites.add(platform2)

platform3 = Platform(500, 300)
all_sprites.add(platform3)

# Game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Update the sprites
    all_sprites.update()

    # Draw the background image
    game_display.blit(background_image, (0, 0))

    # Draw the sprites
    all_sprites.draw(game_display)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
