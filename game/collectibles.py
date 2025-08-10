import pygame
import random
from config.constants import *

class Collectible:
    def __init__(self, x, y, width, height, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = value
        self.collected = False
        self.animation_frame = 0
        self.animation_timer = 0
        
    def update(self, game_speed):
        """Update collectible position and animation"""
        self.x -= game_speed
        
        # Update animation
        self.animation_timer += 1
        if self.animation_timer >= 8:  # Change animation every 8 frames
            self.animation_timer = 0
            self.animation_frame = (self.animation_frame + 1) % 4
            
    def draw(self, screen):
        """Draw the collectible"""
        pass  # Override in subclasses
        
    def get_rect(self):
        """Get collectible collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
        
    def is_off_screen(self):
        """Check if collectible is off the left side of the screen"""
        return self.x + self.width < 0
        
    def collect(self):
        """Mark collectible as collected"""
        self.collected = True

class Coin(Collectible):
    def __init__(self, x, y):
        super().__init__(x, y, 20, 20, 10)  # 10 points per coin
        self.create_coin_shape()
        
    def create_coin_shape(self):
        """Create a coin shape"""
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        # Coin colors
        COIN_GOLD = (255, 215, 0)
        COIN_DARK_GOLD = (218, 165, 32)
        
        # Draw coin circle
        pygame.draw.circle(self.surface, COIN_GOLD, (10, 10), 10)
        pygame.draw.circle(self.surface, COIN_DARK_GOLD, (10, 10), 8)
        
        # Draw coin center
        pygame.draw.circle(self.surface, COIN_GOLD, (10, 10), 6)
        
        # Draw dollar sign or star pattern
        if self.animation_frame % 2 == 0:
            # Dollar sign
            font = pygame.font.Font(None, 16)
            text = font.render("$", True, COIN_DARK_GOLD)
            text_rect = text.get_rect(center=(10, 10))
            self.surface.blit(text, text_rect)
        else:
            # Star pattern
            pygame.draw.circle(self.surface, COIN_DARK_GOLD, (10, 10), 2)
            
    def draw(self, screen):
        """Draw the coin with animation"""
        self.create_coin_shape()  # Recreate with current animation frame
        screen.blit(self.surface, (self.x, self.y))

class Gem(Collectible):
    def __init__(self, x, y, gem_type=None):
        if gem_type is None:
            gem_type = random.choice(['red', 'blue', 'green', 'purple'])
            
        super().__init__(x, y, 25, 25, 50)  # 50 points per gem
        self.gem_type = gem_type
        self.create_gem_shape()
        
    def create_gem_shape(self):
        """Create a gem shape"""
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        # Gem colors based on type
        gem_colors = {
            'red': ((255, 0, 0), (139, 0, 0)),
            'blue': ((0, 0, 255), (0, 0, 139)),
            'green': ((0, 255, 0), (0, 139, 0)),
            'purple': ((128, 0, 128), (75, 0, 130))
        }
        
        primary_color, secondary_color = gem_colors[self.gem_type]
        
        # Draw gem diamond shape
        points = [
            (12, 2),   # Top
            (20, 12),  # Right
            (12, 22),  # Bottom
            (4, 12)    # Left
        ]
        
        pygame.draw.polygon(self.surface, primary_color, points)
        pygame.draw.polygon(self.surface, secondary_color, points, 2)
        
        # Draw gem facets
        inner_points = [
            (12, 6),   # Top inner
            (18, 12),  # Right inner
            (12, 18),  # Bottom inner
            (6, 12)    # Left inner
        ]
        
        pygame.draw.polygon(self.surface, secondary_color, inner_points)
        
        # Draw sparkle effect
        if self.animation_frame % 2 == 0:
            pygame.draw.circle(self.surface, (255, 255, 255), (12, 12), 2)
            
    def draw(self, screen):
        """Draw the gem with animation"""
        self.create_gem_shape()  # Recreate with current animation frame
        screen.blit(self.surface, (self.x, self.y))

class CollectibleManager:
    def __init__(self):
        self.collectibles = []
        self.spawn_timer = 0
        self.spawn_delay = 30  # Spawn collectibles more frequently than obstacles
        self.total_collected = 0
        self.total_score = 0
        
    def update(self, game_speed):
        """Update all collectibles and spawn new ones"""
        # Update existing collectibles
        for collectible in self.collectibles[:]:
            collectible.update(game_speed)
            
            # Remove collectibles that are off screen or collected
            if collectible.is_off_screen() or collectible.collected:
                self.collectibles.remove(collectible)
        
        # Spawn new collectibles
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_collectible()
            self.spawn_timer = 0
            
            # Adjust spawn delay based on game speed
            base_delay = max(20, 30 - (game_speed - INITIAL_GAME_SPEED))
            self.spawn_delay = base_delay + random.randint(-5, 5)
    
    def spawn_collectible(self):
        """Spawn a new collectible"""
        # Check if there's enough space to spawn
        if not self.collectibles or self.collectibles[-1].x < SCREEN_WIDTH - 100:
            # Random position
            x = OBSTACLE_SPAWN_X + random.randint(-30, 30)
            y = random.randint(GROUND_Y - 100, GROUND_Y - 30)  # Above ground
            
            # 70% chance for coin, 30% chance for gem
            if random.random() < 0.7:
                collectible = Coin(x, y)
            else:
                collectible = Gem(x, y)
                
            self.collectibles.append(collectible)
    
    def check_collisions(self, labubu):
        """Check for collisions between Labubu and collectibles"""
        labubu_rect = labubu.get_rect()
        collected_items = []
        
        for collectible in self.collectibles:
            if not collectible.collected:
                collectible_rect = collectible.get_rect()
                if labubu_rect.colliderect(collectible_rect):
                    collectible.collect()
                    collected_items.append(collectible)
                    self.total_collected += 1
                    self.total_score += collectible.value
                    
        return collected_items
    
    def draw(self, screen):
        """Draw all collectibles"""
        for collectible in self.collectibles:
            if not collectible.collected:
                collectible.draw(screen)
    
    def reset(self):
        """Reset collectible manager"""
        self.collectibles.clear()
        self.spawn_timer = 0
        self.spawn_delay = 30
        self.total_collected = 0
        self.total_score = 0
    
    def get_collectibles(self):
        """Get list of all collectibles"""
        return self.collectibles
