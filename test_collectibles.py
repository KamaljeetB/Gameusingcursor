#!/usr/bin/env python3
"""
Test script to demonstrate collectibles system
"""

import pygame
import sys
from game.collectibles import CollectibleManager, Coin, Gem
from game.player import Labubu
from config import constants

def test_collectibles():
    """Test collectibles spawning and collection"""
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Collectibles Test")
    clock = pygame.time.Clock()
    
    collectible_manager = CollectibleManager()
    labubu = Labubu()
    
    print("💰 Collectibles Test")
    print("Watch for coins and gems spawning")
    print("Move Labubu with arrow keys to collect them")
    print("Press ESC to exit")
    
    running = True
    frame_count = 0
    total_collected = 0
    
    while running and frame_count < 600:  # Run for 10 seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    labubu.jump()
        
        # Handle continuous key presses for Labubu movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and labubu.x > 50:
            labubu.x -= 3
        if keys[pygame.K_RIGHT] and labubu.x < 700:
            labubu.x += 3
        
        # Update Labubu
        labubu.update()
        
        # Update collectibles
        collectible_manager.update(constants.INITIAL_GAME_SPEED)
        
        # Check for collection
        collected_items = collectible_manager.check_collisions(labubu)
        if collected_items:
            total_collected += len(collected_items)
            print(f"Collected {len(collected_items)} items! Total: {total_collected}")
            for item in collected_items:
                if isinstance(item, Coin):
                    print(f"  - Coin worth {item.value} points")
                elif isinstance(item, Gem):
                    print(f"  - {item.gem_type.capitalize()} gem worth {item.value} points")
        
        # Render
        screen.fill(constants.SKY_COLOR)
        pygame.draw.rect(screen, constants.GROUND_COLOR, 
                        (0, constants.GROUND_Y, 800, 400 - constants.GROUND_Y))
        
        labubu.draw(screen)
        collectible_manager.draw(screen)
        
        # Draw info
        font = pygame.font.Font(None, 24)
        info_text = [
            f"Frame: {frame_count}",
            f"Collectibles: {len(collectible_manager.collectibles)}",
            f"Total Collected: {total_collected}",
            f"Total Score: {collectible_manager.total_score}",
            "Use ARROW KEYS to move, SPACE to jump"
        ]
        
        for i, text in enumerate(info_text):
            text_surface = font.render(text, True, constants.BLACK)
            screen.blit(text_surface, (10, 10 + i * 25))
        
        pygame.display.flip()
        clock.tick(60)
        frame_count += 1
        
        # Print collectible info every 120 frames
        if frame_count % 120 == 0:
            print(f"Frame {frame_count}: {len(collectible_manager.collectibles)} collectibles on screen")
            for i, collectible in enumerate(collectible_manager.collectibles):
                if isinstance(collectible, Coin):
                    print(f"  Collectible {i}: Coin at ({collectible.x:.1f}, {collectible.y:.1f})")
                elif isinstance(collectible, Gem):
                    print(f"  Collectible {i}: {collectible.gem_type} gem at ({collectible.x:.1f}, {collectible.y:.1f})")
    
    pygame.quit()
    print(f"Test completed. Total items collected: {total_collected}")
    print(f"Total score from collectibles: {collectible_manager.total_score}")

if __name__ == "__main__":
    test_collectibles()
