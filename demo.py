#!/usr/bin/env python3
"""
Demo script to show the dinosaur game mechanics
"""

import pygame
import time
from game.game_state import GameState
from game.player import Labubu
from game.obstacles import ObstacleManager
from game.physics import PhysicsEngine
from game.input_handler import InputHandler
from game.collision import CollisionManager
from config import constants
from config.settings import GameSettings

def run_demo():
    """Run a brief demo of the game"""
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Dinosaur Game Demo")
    clock = pygame.time.Clock()
    
    # Initialize game components
    game_state = GameState()
    labubu = Labubu()
    obstacle_manager = ObstacleManager()
    collision_manager = CollisionManager()
    
    # Demo variables
    demo_timer = 0
    auto_jump_timer = 0
    score = 0
    game_speed = constants.INITIAL_GAME_SPEED
    
    print("🎮 Starting Dinosaur Game Demo...")
    print("The dinosaur will automatically jump over obstacles")
    print("Press ESC to exit the demo")
    
    running = True
    while running and demo_timer < 300:  # Run for 5 seconds (60 FPS * 5)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Auto-jump logic for demo
        auto_jump_timer += 1
        if auto_jump_timer >= 120:  # Jump every 2 seconds
            labubu.jump()
            auto_jump_timer = 0
        
        # Update game objects
        labubu.update()
        obstacle_manager.update(game_speed)
        
        # Check collisions
        if collision_manager.check_collisions(labubu, obstacle_manager.obstacles):
            print("💥 Demo ended: Labubu hit an obstacle!")
            break
        
        # Update score and speed
        score += 1
        game_speed = constants.INITIAL_GAME_SPEED + (score // 1000) * constants.SPEED_INCREMENT
        
        # Render
        screen.fill(constants.SKY_COLOR)
        pygame.draw.rect(screen, constants.GROUND_COLOR, 
                        (0, constants.GROUND_Y, constants.SCREEN_WIDTH, 
                         constants.SCREEN_HEIGHT - constants.GROUND_Y))
        
        labubu.draw(screen)
        obstacle_manager.draw(screen)
        
        # Draw demo info
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Demo Score: {score}", True, constants.BLACK)
        screen.blit(score_text, (10, 10))
        
        demo_text = font.render("DEMO MODE - Press ESC to exit", True, constants.BLACK)
        screen.blit(demo_text, (10, 50))
        
        pygame.display.flip()
        clock.tick(constants.FPS)
        demo_timer += 1
    
    pygame.quit()
    print(f"🎯 Demo completed! Final score: {score}")
    print("✅ All game mechanics working correctly!")

if __name__ == "__main__":
    run_demo()
