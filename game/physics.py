from config.constants import *

class PhysicsEngine:
    def __init__(self):
        self.gravity = GRAVITY
        self.ground_y = GROUND_Y
        
    def apply_gravity(self, velocity_y):
        """Apply gravity to vertical velocity"""
        return velocity_y + self.gravity
        
    def update_position(self, x, y, velocity_x, velocity_y):
        """Update position based on velocity"""
        new_x = x + velocity_x
        new_y = y + velocity_y
        return new_x, new_y
        
    def check_ground_collision(self, y, height):
        """Check if object has hit the ground"""
        return y + height >= self.ground_y
        
    def clamp_to_ground(self, y, height):
        """Clamp object to ground level"""
        return self.ground_y - height
        
    def calculate_jump_velocity(self, jump_strength=JUMP_VELOCITY):
        """Calculate initial jump velocity"""
        return jump_strength
        
    def is_falling(self, velocity_y):
        """Check if object is falling"""
        return velocity_y > 0
        
    def is_rising(self, velocity_y):
        """Check if object is rising"""
        return velocity_y < 0
        
    def get_gravity(self):
        """Get current gravity value"""
        return self.gravity
        
    def set_gravity(self, gravity):
        """Set gravity value"""
        self.gravity = gravity
