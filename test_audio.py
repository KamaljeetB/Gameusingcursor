#!/usr/bin/env python3
"""
Test script to demonstrate the audio system
"""

import pygame
import sys
from utils.simple_audio import SimpleAudioManager

def test_audio():
    """Test all audio features"""
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Audio Test")
    clock = pygame.time.Clock()
    
    audio_manager = SimpleAudioManager()
    
    print("🔊 Audio System Test")
    print("Press keys to test sounds:")
    print("  J - Jump sound")
    print("  C - Coin sound")
    print("  G - Gem sound")
    print("  D - Death sound")
    print("  M - Toggle sound on/off")
    print("  ESC - Exit")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_j:
                    print("Playing jump sound...")
                    audio_manager.play_jump()
                elif event.key == pygame.K_c:
                    print("Playing coin sound...")
                    audio_manager.play_coin()
                elif event.key == pygame.K_g:
                    print("Playing gem sound...")
                    audio_manager.play_gem()
                elif event.key == pygame.K_d:
                    print("Playing death sound...")
                    audio_manager.play_death()
                elif event.key == pygame.K_m:
                    audio_manager.toggle_sound()
                    status = "ON" if audio_manager.sound_enabled else "OFF"
                    print(f"Sound toggled: {status}")
        
        # Render
        screen.fill((135, 206, 235))  # Sky blue
        
        # Draw instructions
        font = pygame.font.Font(None, 24)
        instructions = [
            "Audio System Test",
            "",
            "Press J - Jump sound",
            "Press C - Coin sound", 
            "Press G - Gem sound",
            "Press D - Death sound",
            "Press M - Toggle sound",
            "Press ESC - Exit",
            "",
            f"Sound: {'ON' if audio_manager.sound_enabled else 'OFF'}",
            f"Volume: {audio_manager.sound_volume:.1f}"
        ]
        
        for i, text in enumerate(instructions):
            text_surface = font.render(text, True, (0, 0, 0))
            screen.blit(text_surface, (50, 50 + i * 25))
        
        pygame.display.flip()
        clock.tick(60)
    
    audio_manager.cleanup()
    pygame.quit()
    print("Audio test completed!")

if __name__ == "__main__":
    test_audio()
