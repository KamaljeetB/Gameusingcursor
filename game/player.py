import pygame
from config.constants import *

class Labubu:
    def __init__(self):
        self.x = DINO_X
        self.y = DINO_Y
        self.width = DINO_WIDTH
        self.height = DINO_HEIGHT
        
        # Physics variables
        self.velocity_y = 0
        self.is_jumping = False
        self.is_on_ground = True
        
        # Animation variables
        self.animation_frame = 0
        self.animation_timer = 0
        
        # Create cute Labubu shape
        self.create_labubu_shape()
        
    def create_labubu_shape(self):
        """Create a cute grey Labubu character using pygame drawing"""
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        # Grey color for Labubu
        LABUBU_GREY = (128, 128, 128)
        LABUBU_DARK_GREY = (80, 80, 80)
        LABUBU_LIGHT_GREY = (180, 180, 180)
        
        # Main body (round)
        pygame.draw.ellipse(self.surface, LABUBU_GREY, (8, 25, 24, 30))
        
        # Head (large round)
        pygame.draw.circle(self.surface, LABUBU_GREY, (20, 18), 15)
        
        # Ears (pointed)
        pygame.draw.polygon(self.surface, LABUBU_GREY, [(10, 8), (15, 2), (20, 8)])
        pygame.draw.polygon(self.surface, LABUBU_GREY, [(20, 8), (25, 2), (30, 8)])
        
        # Inner ears (lighter)
        pygame.draw.polygon(self.surface, LABUBU_LIGHT_GREY, [(12, 8), (15, 4), (18, 8)])
        pygame.draw.polygon(self.surface, LABUBU_LIGHT_GREY, [(22, 8), (25, 4), (28, 8)])
        
        # Eyes (large and cute)
        pygame.draw.circle(self.surface, WHITE, (16, 15), 4)
        pygame.draw.circle(self.surface, WHITE, (24, 15), 4)
        pygame.draw.circle(self.surface, BLACK, (16, 15), 2)
        pygame.draw.circle(self.surface, BLACK, (24, 15), 2)
        pygame.draw.circle(self.surface, WHITE, (15, 14), 1)
        pygame.draw.circle(self.surface, WHITE, (23, 14), 1)
        
        # Nose (small triangle)
        pygame.draw.polygon(self.surface, LABUBU_DARK_GREY, [(19, 18), (20, 20), (21, 18)])
        
        # Mouth (cute smile)
        pygame.draw.arc(self.surface, LABUBU_DARK_GREY, (17, 18, 6, 4), 0, 3.14, 2)
        
        # Arms (round)
        pygame.draw.circle(self.surface, LABUBU_GREY, (12, 35), 6)
        pygame.draw.circle(self.surface, LABUBU_GREY, (28, 35), 6)
        
        # Legs (round)
        pygame.draw.circle(self.surface, LABUBU_GREY, (15, 50), 5)
        pygame.draw.circle(self.surface, LABUBU_GREY, (25, 50), 5)
        
    def jump(self):
        """Make the Labubu jump"""
        if self.is_on_ground and not self.is_jumping:
            self.velocity_y = JUMP_VELOCITY
            self.is_jumping = True
            self.is_on_ground = False
            
    def update(self):
        """Update Labubu physics and animation"""
        # Apply gravity
        self.velocity_y += GRAVITY
        
        # Update position
        self.y += self.velocity_y
        
        # Check ground collision
        if self.y >= DINO_Y:
            self.y = DINO_Y
            self.velocity_y = 0
            self.is_jumping = False
            self.is_on_ground = True
            
        # Update animation
        self.update_animation()
        
    def update_animation(self):
        """Update Labubu animation"""
        self.animation_timer += 1
        
        if self.animation_timer >= 10:  # Change animation every 10 frames
            self.animation_timer = 0
            self.animation_frame = (self.animation_frame + 1) % 2
            
            # Recreate Labubu shape with different leg positions for running animation
            self.create_labubu_shape()
            
            if self.animation_frame == 1:
                # Move legs slightly for running effect
                self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                
                # Grey color for Labubu
                LABUBU_GREY = (128, 128, 128)
                LABUBU_DARK_GREY = (80, 80, 80)
                LABUBU_LIGHT_GREY = (180, 180, 180)
                
                # Main body (round)
                pygame.draw.ellipse(self.surface, LABUBU_GREY, (8, 25, 24, 30))
                
                # Head (large round)
                pygame.draw.circle(self.surface, LABUBU_GREY, (20, 18), 15)
                
                # Ears (pointed)
                pygame.draw.polygon(self.surface, LABUBU_GREY, [(10, 8), (15, 2), (20, 8)])
                pygame.draw.polygon(self.surface, LABUBU_GREY, [(20, 8), (25, 2), (30, 8)])
                
                # Inner ears (lighter)
                pygame.draw.polygon(self.surface, LABUBU_LIGHT_GREY, [(12, 8), (15, 4), (18, 8)])
                pygame.draw.polygon(self.surface, LABUBU_LIGHT_GREY, [(22, 8), (25, 4), (28, 8)])
                
                # Eyes (large and cute)
                pygame.draw.circle(self.surface, WHITE, (16, 15), 4)
                pygame.draw.circle(self.surface, WHITE, (24, 15), 4)
                pygame.draw.circle(self.surface, BLACK, (16, 15), 2)
                pygame.draw.circle(self.surface, BLACK, (24, 15), 2)
                pygame.draw.circle(self.surface, WHITE, (15, 14), 1)
                pygame.draw.circle(self.surface, WHITE, (23, 14), 1)
                
                # Nose (small triangle)
                pygame.draw.polygon(self.surface, LABUBU_DARK_GREY, [(19, 18), (20, 20), (21, 18)])
                
                # Mouth (cute smile)
                pygame.draw.arc(self.surface, LABUBU_DARK_GREY, (17, 18, 6, 4), 0, 3.14, 2)
                
                # Arms (round)
                pygame.draw.circle(self.surface, LABUBU_GREY, (12, 35), 6)
                pygame.draw.circle(self.surface, LABUBU_GREY, (28, 35), 6)
                
                # Legs in different position for running animation
                pygame.draw.circle(self.surface, LABUBU_GREY, (13, 50), 5)
                pygame.draw.circle(self.surface, LABUBU_GREY, (27, 50), 5)
                
    def draw(self, screen):
        """Draw the Labubu on the screen"""
        screen.blit(self.surface, (self.x, self.y))
        
    def get_rect(self):
        """Get the Labubu's collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
        
    def reset(self):
        """Reset Labubu to initial state"""
        self.x = DINO_X
        self.y = DINO_Y
        self.velocity_y = 0
        self.is_jumping = False
        self.is_on_ground = True
        self.animation_frame = 0
        self.animation_timer = 0
        self.create_labubu_shape()
