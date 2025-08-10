#!/usr/bin/env python3
"""
Test script to demonstrate varied cactus obstacles
"""

import pygame
import sys
from game.obstacles import ObstacleManager, Cactus
from config import constants

def test_varied_obstacles():
    """Test varied obstacle spawning"""
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Varied Obstacles Test")
    clock = pygame.time.Clock()
    
    obstacle_manager = ObstacleManager()
    
    print("🌵 Varied Obstacles Test")
    print("Watch for different cactus types and heights")
    print("Press ESC to exit")
    
    running = True
    frame_count = 0
    
    while running and frame_count < 600:  # Run for 10 seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update obstacles
        obstacle_manager.update(constants.INITIAL_GAME_SPEED)
        
        # Render
        screen.fill(constants.SKY_COLOR)
        pygame.draw.rect(screen, constants.GROUND_COLOR, 
                        (0, constants.GROUND_Y, 800, 400 - constants.GROUND_Y))
        
        obstacle_manager.draw(screen)
        
        # Draw info
        font = pygame.font.Font(None, 24)
        info_text = [
            f"Frame: {frame_count}",
            f"Obstacles: {len(obstacle_manager.obstacles)}",
            f"Spawn Timer: {obstacle_manager.spawn_timer}",
            f"Spawn Delay: {obstacle_manager.spawn_delay}"
        ]
        
        for i, text in enumerate(info_text):
            text_surface = font.render(text, True, constants.BLACK)
            screen.blit(text_surface, (10, 10 + i * 25))
        
        # Draw obstacle details
        for i, obs in enumerate(obstacle_manager.obstacles):
            if hasattr(obs, 'cactus_type'):
                detail_text = f"Obstacle {i}: {obs.cactus_type}, h={obs.height}"
                detail_surface = font.render(detail_text, True, constants.BLACK)
                screen.blit(detail_surface, (10, 150 + i * 20))
        
        pygame.display.flip()
        clock.tick(60)
        frame_count += 1
        
        # Print obstacle info every 120 frames
        if frame_count % 120 == 0:
            print(f"Frame {frame_count}: {len(obstacle_manager.obstacles)} obstacles")
            for i, obs in enumerate(obstacle_manager.obstacles):
                if hasattr(obs, 'cactus_type'):
                    print(f"  Obstacle {i}: {obs.cactus_type}, height={obs.height}, x={obs.x:.1f}")
    
    pygame.quit()
    print(f"Test completed. Total obstacles spawned: {len(obstacle_manager.obstacles)}")

if __name__ == "__main__":
    test_varied_obstacles()
