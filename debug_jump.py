#!/usr/bin/env python3
"""
Debug script to test jumping mechanism
"""

import pygame
import sys
from game.player import Labubu
from game.game_state import GameState
from config import constants

def debug_jump():
    """Test jumping mechanism in isolation"""
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Jump Debug Test")
    clock = pygame.time.Clock()
    
    labubu = Labubu()
    game_state = GameState()
    
    print("🔍 Jump Debug Test")
    print("Press SPACE to jump")
    print("Press ESC to exit")
    print(f"Initial position: ({labubu.x}, {labubu.y})")
    print(f"On ground: {labubu.is_on_ground}")
    print(f"Jumping: {labubu.is_jumping}")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print(f"SPACE pressed! Current state: on_ground={labubu.is_on_ground}, jumping={labubu.is_jumping}")
                    labubu.jump()
                    print(f"After jump: on_ground={labubu.is_on_ground}, jumping={labubu.is_jumping}, velocity={labubu.velocity_y}")
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        # Update Labubu
        labubu.update()
        
        # Render
        screen.fill(constants.SKY_COLOR)
        pygame.draw.rect(screen, constants.GROUND_COLOR, 
                        (0, constants.GROUND_Y, 800, 400 - constants.GROUND_Y))
        
        labubu.draw(screen)
        
        # Draw debug info
        font = pygame.font.Font(None, 24)
        debug_text = [
            f"Position: ({labubu.x:.1f}, {labubu.y:.1f})",
            f"Velocity: {labubu.velocity_y:.1f}",
            f"On Ground: {labubu.is_on_ground}",
            f"Jumping: {labubu.is_jumping}",
            "Press SPACE to jump"
        ]
        
        for i, text in enumerate(debug_text):
            text_surface = font.render(text, True, constants.BLACK)
            screen.blit(text_surface, (10, 10 + i * 25))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("Debug test completed")

if __name__ == "__main__":
    debug_jump()
