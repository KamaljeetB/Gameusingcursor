import pygame
import os
import random
from config import constants

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        
        # Audio settings
        self.sound_enabled = True
        self.music_enabled = True
        self.sound_volume = 0.7
        self.music_volume = 0.5
        
        # Sound effects dictionary
        self.sounds = {}
        self.music_tracks = []
        self.current_music = None
        
        # Initialize sounds
        self.load_sounds()
        
    def load_sounds(self):
        """Load all sound effects"""
        try:
            # Create simple sound effects using pygame's built-in sound generation
            self.create_sound_effects()
            print("✅ Audio manager initialized successfully")
        except Exception as e:
            print(f"⚠️ Audio initialization warning: {e}")
            self.sound_enabled = False
            
    def create_sound_effects(self):
        """Create simple sound effects programmatically"""
        # Jump sound (ascending tone)
        self.sounds['jump'] = self.create_jump_sound()
        
        # Coin collection sound (ding)
        self.sounds['coin'] = self.create_coin_sound()
        
        # Gem collection sound (sparkle)
        self.sounds['gem'] = self.create_gem_sound()
        
        # Death sound (crash)
        self.sounds['death'] = self.create_death_sound()
        
        # Power-up sound (power)
        self.sounds['powerup'] = self.create_powerup_sound()
        
        # Background music
        self.create_background_music()
        
    def create_jump_sound(self):
        """Create a jump sound effect"""
        # Generate a simple ascending tone
        sample_rate = 22050
        duration = 0.3  # seconds
        samples = int(sample_rate * duration)
        
        # Create a simple ascending sine wave
        import math
        sound_array = []
        for i in range(samples):
            # Frequency increases from 200Hz to 400Hz
            freq = 200 + (i / samples) * 200
            sample = math.sin(2 * math.pi * freq * i / sample_rate)
            sound_array.append(int(sample * 32767 * 0.3))  # Reduce volume
            
        return pygame.sndarray.make_sound(pygame.surfarray.pixels3d(
            pygame.Surface((len(sound_array), 1))
        ))
        
    def create_coin_sound(self):
        """Create a coin collection sound"""
        sample_rate = 22050
        duration = 0.2
        samples = int(sample_rate * duration)
        
        import math
        sound_array = []
        for i in range(samples):
            # Simple ding sound (800Hz with decay)
            freq = 800
            decay = 1.0 - (i / samples) * 0.8
            sample = math.sin(2 * math.pi * freq * i / sample_rate) * decay
            sound_array.append(int(sample * 32767 * 0.4))
            
        return pygame.sndarray.make_sound(pygame.surfarray.pixels3d(
            pygame.Surface((len(sound_array), 1))
        ))
        
    def create_gem_sound(self):
        """Create a gem collection sound"""
        sample_rate = 22050
        duration = 0.4
        samples = int(sample_rate * duration)
        
        import math
        sound_array = []
        for i in range(samples):
            # Sparkle sound (multiple frequencies)
            freq1 = 1200 + math.sin(i * 0.1) * 200
            freq2 = 800 + math.sin(i * 0.15) * 100
            decay = 1.0 - (i / samples) * 0.6
            sample = (math.sin(2 * math.pi * freq1 * i / sample_rate) + 
                     math.sin(2 * math.pi * freq2 * i / sample_rate)) * decay * 0.3
            sound_array.append(int(sample * 32767 * 0.3))
            
        return pygame.sndarray.make_sound(pygame.surfarray.pixels3d(
            pygame.Surface((len(sound_array), 1))
        ))
        
    def create_death_sound(self):
        """Create a death sound effect"""
        sample_rate = 22050
        duration = 0.8
        samples = int(sample_rate * duration)
        
        import math
        sound_array = []
        for i in range(samples):
            # Descending crash sound
            freq = 400 - (i / samples) * 300
            decay = 1.0 - (i / samples) * 0.5
            sample = math.sin(2 * math.pi * freq * i / sample_rate) * decay
            sound_array.append(int(sample * 32767 * 0.5))
            
        return pygame.sndarray.make_sound(pygame.surfarray.pixels3d(
            pygame.Surface((len(sound_array), 1))
        ))
        
    def create_powerup_sound(self):
        """Create a power-up sound effect"""
        sample_rate = 22050
        duration = 0.5
        samples = int(sample_rate * duration)
        
        import math
        sound_array = []
        for i in range(samples):
            # Power-up sound (ascending with harmonics)
            freq = 300 + (i / samples) * 400
            decay = 1.0 - (i / samples) * 0.3
            sample = (math.sin(2 * math.pi * freq * i / sample_rate) +
                     math.sin(2 * math.pi * freq * 2 * i / sample_rate) * 0.5) * decay
            sound_array.append(int(sample * 32767 * 0.4))
            
        return pygame.sndarray.make_sound(pygame.surfarray.pixels3d(
            pygame.Surface((len(sound_array), 1))
        ))
        
    def create_background_music(self):
        """Create simple background music"""
        # For now, we'll create a simple looping melody
        # In a real implementation, you'd load actual music files
        self.music_tracks = ['simple_loop']
        
    def play_sound(self, sound_name):
        """Play a sound effect"""
        if self.sound_enabled and sound_name in self.sounds:
            try:
                self.sounds[sound_name].set_volume(self.sound_volume)
                self.sounds[sound_name].play()
            except Exception as e:
                print(f"Sound play error: {e}")
                
    def play_jump(self):
        """Play jump sound"""
        self.play_sound('jump')
        
    def play_coin(self):
        """Play coin collection sound"""
        self.play_sound('coin')
        
    def play_gem(self):
        """Play gem collection sound"""
        self.play_sound('gem')
        
    def play_death(self):
        """Play death sound"""
        self.play_sound('death')
        
    def play_powerup(self):
        """Play power-up sound"""
        self.play_sound('powerup')
        
    def start_background_music(self):
        """Start background music"""
        if self.music_enabled:
            try:
                # Create a simple looping background melody
                self.create_simple_background_music()
            except Exception as e:
                print(f"Music start error: {e}")
                
    def create_simple_background_music(self):
        """Create a simple background melody"""
        # This is a placeholder - in a real game you'd load actual music files
        # For now, we'll just indicate that music is playing
        self.current_music = "playing"
        
    def stop_background_music(self):
        """Stop background music"""
        if self.current_music:
            pygame.mixer.music.stop()
            self.current_music = None
            
    def set_sound_volume(self, volume):
        """Set sound effects volume (0.0 to 1.0)"""
        self.sound_volume = max(0.0, min(1.0, volume))
        
    def set_music_volume(self, volume):
        """Set music volume (0.0 to 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
        if self.current_music:
            pygame.mixer.music.set_volume(self.music_volume)
            
    def toggle_sound(self):
        """Toggle sound effects on/off"""
        self.sound_enabled = not self.sound_enabled
        
    def toggle_music(self):
        """Toggle background music on/off"""
        self.music_enabled = not self.music_enabled
        if not self.music_enabled:
            self.stop_background_music()
        elif not self.current_music:
            self.start_background_music()
            
    def cleanup(self):
        """Clean up audio resources"""
        pygame.mixer.quit()
