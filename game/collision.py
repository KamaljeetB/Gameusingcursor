import pygame

class CollisionManager:
    def __init__(self):
        self.collision_tolerance = 5  # Pixel tolerance for collision detection
        
    def check_collisions(self, labubu, obstacles):
        """Check for collisions between Labubu and obstacles"""
        labubu_rect = labubu.get_rect()
        
        for obstacle in obstacles:
            obstacle_rect = obstacle.get_rect()
            
            if self.check_rect_collision(labubu_rect, obstacle_rect):
                return True
                
        return False
        
    def check_rect_collision(self, rect1, rect2):
        """Check collision between two rectangles"""
        return rect1.colliderect(rect2)
        
    def check_point_collision(self, point, rect):
        """Check if a point is inside a rectangle"""
        return rect.collidepoint(point)
        
    def get_collision_side(self, rect1, rect2):
        """Determine which side of rect1 collided with rect2"""
        # Calculate overlap on each axis
        overlap_x = min(rect1.right, rect2.right) - max(rect1.left, rect2.left)
        overlap_y = min(rect1.bottom, rect2.bottom) - max(rect1.top, rect2.top)
        
        if overlap_x > 0 and overlap_y > 0:
            # Determine primary collision side
            if overlap_x < overlap_y:
                # Horizontal collision
                if rect1.centerx < rect2.centerx:
                    return "right"
                else:
                    return "left"
            else:
                # Vertical collision
                if rect1.centery < rect2.centery:
                    return "bottom"
                else:
                    return "top"
                    
        return None
        
    def check_collision_with_tolerance(self, rect1, rect2, tolerance=0):
        """Check collision with pixel tolerance"""
        # Create slightly smaller rectangles for more precise collision
        adjusted_rect1 = rect1.inflate(-tolerance, -tolerance)
        adjusted_rect2 = rect2.inflate(-tolerance, -tolerance)
        
        return adjusted_rect1.colliderect(adjusted_rect2)
        
    def get_collision_rect(self, rect1, rect2):
        """Get the intersection rectangle of two rectangles"""
        return rect1.clip(rect2)
        
    def is_collision_imminent(self, labubu, obstacles, frames_ahead=10):
        """Predict if a collision will occur in the next few frames"""
        # This could be used for advanced AI or visual warnings
        labubu_rect = labubu.get_rect()
        
        for obstacle in obstacles:
            obstacle_rect = obstacle.get_rect()
            
            # Move obstacle forward to simulate future position
            future_obstacle_rect = obstacle_rect.copy()
            future_obstacle_rect.x -= frames_ahead * 5  # Assuming 5 pixels per frame movement
            
            if self.check_rect_collision(labubu_rect, future_obstacle_rect):
                return True
                
        return False
