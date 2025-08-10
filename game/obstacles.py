import pygame
import random
from config.constants import *

class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0
        
    def update(self, game_speed):
        """Update obstacle position"""
        self.x -= game_speed
        
    def draw(self, screen):
        """Draw the obstacle"""
        pygame.draw.rect(screen, OBSTACLE_COLOR, (self.x, self.y, self.width, self.height))
        
    def get_rect(self):
        """Get obstacle collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)
        
    def is_off_screen(self):
        """Check if obstacle is off the left side of the screen"""
        return self.x + self.width < 0

class Cactus(Obstacle):
    def __init__(self, x, height=None, cactus_type=None):
        # Random height between min and max
        if height is None:
            height = random.randint(OBSTACLE_MIN_HEIGHT, OBSTACLE_MAX_HEIGHT)
        
        # Random cactus type if not specified
        if cactus_type is None:
            cactus_type = random.choice(['simple', 'double', 'triple'])
        
        super().__init__(x, GROUND_Y - height, OBSTACLE_WIDTH, height)
        self.cactus_type = cactus_type
        self.create_cactus_shape()
        
    def create_cactus_shape(self):
        """Create a cactus shape based on type"""
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        if self.cactus_type == 'simple':
            self.create_simple_cactus()
        elif self.cactus_type == 'double':
            self.create_double_cactus()
        elif self.cactus_type == 'triple':
            self.create_triple_cactus()
        
    def create_simple_cactus(self):
        """Create a simple single cactus"""
        # Main cactus body
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (10, 0, 10, self.height))
        
        # Cactus arms
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (5, 15, 8, 8))
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (17, 25, 8, 8))
        
        # Cactus spikes
        for i in range(3):
            y_pos = 10 + i * 15
            pygame.draw.polygon(self.surface, OBSTACLE_COLOR, 
                              [(8, y_pos), (12, y_pos-3), (16, y_pos)])
    
    def create_double_cactus(self):
        """Create a double cactus (two connected)"""
        # Left cactus
        left_height = self.height * 0.8
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (5, self.height - left_height, 8, left_height))
        
        # Right cactus
        right_height = self.height
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (17, self.height - right_height, 8, right_height))
        
        # Connecting arm
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (10, self.height - 20, 10, 5))
        
        # Spikes on both cacti
        for i in range(2):
            y_pos = self.height - 15 - i * 10
            pygame.draw.polygon(self.surface, OBSTACLE_COLOR, 
                              [(3, y_pos), (7, y_pos-2), (11, y_pos)])
            pygame.draw.polygon(self.surface, OBSTACLE_COLOR, 
                              [(15, y_pos), (19, y_pos-2), (23, y_pos)])
    
    def create_triple_cactus(self):
        """Create a triple cactus (three connected)"""
        # Left cactus
        left_height = self.height * 0.6
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (3, self.height - left_height, 6, left_height))
        
        # Middle cactus
        middle_height = self.height
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (12, self.height - middle_height, 6, middle_height))
        
        # Right cactus
        right_height = self.height * 0.7
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (21, self.height - right_height, 6, right_height))
        
        # Connecting arms
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (8, self.height - 15, 8, 3))
        pygame.draw.rect(self.surface, OBSTACLE_COLOR, (17, self.height - 12, 8, 3))
        
        # Spikes
        for i in range(2):
            y_pos = self.height - 10 - i * 8
            pygame.draw.polygon(self.surface, OBSTACLE_COLOR, 
                              [(1, y_pos), (5, y_pos-2), (9, y_pos)])
            pygame.draw.polygon(self.surface, OBSTACLE_COLOR, 
                              [(10, y_pos), (14, y_pos-2), (18, y_pos)])
            pygame.draw.polygon(self.surface, OBSTACLE_COLOR, 
                              [(19, y_pos), (23, y_pos-2), (27, y_pos)])
        
    def draw(self, screen):
        """Draw the cactus"""
        screen.blit(self.surface, (self.x, self.y))

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.spawn_timer = 0
        self.spawn_delay = 60  # Frames between obstacle spawns
        
    def update(self, game_speed):
        """Update all obstacles and spawn new ones"""
        # Update existing obstacles
        for obstacle in self.obstacles[:]:
            obstacle.update(game_speed)
            
            # Remove obstacles that are off screen
            if obstacle.is_off_screen():
                self.obstacles.remove(obstacle)
        
        # Spawn new obstacles
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_obstacle()
            self.spawn_timer = 0
            
            # Adjust spawn delay based on game speed and add randomness
            base_delay = max(30, 60 - (game_speed - INITIAL_GAME_SPEED) * 2)
            self.spawn_delay = base_delay + random.randint(-10, 10)  # Add randomness to spacing
    
    def spawn_obstacle(self):
        """Spawn a new obstacle"""
        # Check if there's enough space to spawn
        if not self.obstacles or self.obstacles[-1].x < SCREEN_WIDTH - OBSTACLE_MIN_DISTANCE:
            # Random spacing between obstacles
            spacing = random.randint(OBSTACLE_MIN_DISTANCE, OBSTACLE_MAX_DISTANCE)
            spawn_x = OBSTACLE_SPAWN_X + random.randint(-50, 50)  # Add some randomness to spawn position
            
            obstacle = Cactus(spawn_x)
            self.obstacles.append(obstacle)
    
    def draw(self, screen):
        """Draw all obstacles"""
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset(self):
        """Reset obstacle manager"""
        self.obstacles.clear()
        self.spawn_timer = 0
        self.spawn_delay = 60
    
    def get_obstacles(self):
        """Get list of all obstacles"""
        return self.obstacles
