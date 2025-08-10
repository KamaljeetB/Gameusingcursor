import pygame
import math
import numpy as np

class SimpleAudioManager:
    def __init__(self):
        pygame.mixer.init(22050, -16, 2, 512)
        
        # Audio settings
        self.sound_enabled = True
        self.music_enabled = True
        self.sound_volume = 0.7
        self.music_volume = 0.3  # Lower volume for background music
        
        # Sound effects
        self.sounds = {}
        
        # Background music
        self.background_music = None
        self.music_playing = False
        
        # Initialize sounds and music
        self.create_sounds()
        self.create_background_music()
        
    def create_sounds(self):
        """Create simple sound effects"""
        try:
            self.sounds['jump'] = self.create_jump_sound()
            self.sounds['coin'] = self.create_coin_sound()
            self.sounds['gem'] = self.create_gem_sound()
            self.sounds['death'] = self.create_death_sound()
            print("✅ Simple audio manager initialized successfully")
        except Exception as e:
            print(f"⚠️ Audio initialization warning: {e}")
            self.sound_enabled = False
            
    def create_background_music(self):
        """Create upbeat background music"""
        try:
            self.background_music = self.create_upbeat_music()
            print("🎵 Background music created successfully")
        except Exception as e:
            print(f"⚠️ Background music creation warning: {e}")
            self.music_enabled = False
            
    def create_jump_sound(self):
        """Create a simple jump sound"""
        sample_rate = 22050
        duration = 0.3
        samples = int(sample_rate * duration)
        
        # Create ascending tone
        sound_data = []
        for i in range(samples):
            # Frequency increases from 200Hz to 400Hz
            freq = 200 + (i / samples) * 200
            sample = math.sin(2 * math.pi * freq * i / sample_rate)
            # Add some harmonics for richer sound
            sample += 0.3 * math.sin(2 * math.pi * freq * 2 * i / sample_rate)
            # Apply envelope (fade out)
            envelope = 1.0 - (i / samples) * 0.5
            sample_value = int(sample * 32767 * 0.3 * envelope)
            # Create stereo sample (left and right channel)
            sound_data.append([sample_value, sample_value])
            
        # Convert to pygame sound (2D array for stereo)
        sound_array = np.array(sound_data, dtype=np.int16)
        return pygame.sndarray.make_sound(sound_array)
        
    def create_coin_sound(self):
        """Create a coin collection sound"""
        sample_rate = 22050
        duration = 0.2
        samples = int(sample_rate * duration)
        
        sound_data = []
        for i in range(samples):
            # Simple ding sound at 800Hz
            freq = 800
            sample = math.sin(2 * math.pi * freq * i / sample_rate)
            # Add harmonics
            sample += 0.2 * math.sin(2 * math.pi * freq * 3 * i / sample_rate)
            # Apply envelope
            envelope = 1.0 - (i / samples) * 0.8
            sample_value = int(sample * 32767 * 0.4 * envelope)
            # Create stereo sample (left and right channel)
            sound_data.append([sample_value, sample_value])
            
        sound_array = np.array(sound_data, dtype=np.int16)
        return pygame.sndarray.make_sound(sound_array)
        
    def create_gem_sound(self):
        """Create a gem collection sound"""
        sample_rate = 22050
        duration = 0.4
        samples = int(sample_rate * duration)
        
        sound_data = []
        for i in range(samples):
            # Sparkle sound with multiple frequencies
            freq1 = 1200
            freq2 = 800
            sample = (math.sin(2 * math.pi * freq1 * i / sample_rate) + 
                     math.sin(2 * math.pi * freq2 * i / sample_rate))
            # Add some modulation
            sample += 0.1 * math.sin(2 * math.pi * 5 * i / sample_rate)
            # Apply envelope
            envelope = 1.0 - (i / samples) * 0.6
            sample_value = int(sample * 32767 * 0.3 * envelope)
            # Create stereo sample (left and right channel)
            sound_data.append([sample_value, sample_value])
            
        sound_array = np.array(sound_data, dtype=np.int16)
        return pygame.sndarray.make_sound(sound_array)
        
    def create_death_sound(self):
        """Create a death sound"""
        sample_rate = 22050
        duration = 0.8
        samples = int(sample_rate * duration)
        
        sound_data = []
        for i in range(samples):
            # Descending crash sound
            freq = 400 - (i / samples) * 300
            sample = math.sin(2 * math.pi * freq * i / sample_rate)
            # Add noise for crash effect
            noise = (math.sin(2 * math.pi * 100 * i / sample_rate) + 
                    math.sin(2 * math.pi * 200 * i / sample_rate)) * 0.3
            sample = sample * 0.7 + noise * 0.3
            # Apply envelope
            envelope = 1.0 - (i / samples) * 0.5
            sample_value = int(sample * 32767 * 0.5 * envelope)
            # Create stereo sample (left and right channel)
            sound_data.append([sample_value, sample_value])
            
        sound_array = np.array(sound_data, dtype=np.int16)
        return pygame.sndarray.make_sound(sound_array)
        
    def create_upbeat_music(self):
        """Create energetic adventure background music with multiple layers"""
        sample_rate = 22050
        duration = 6.0  # 6-second loop for more variety
        samples = int(sample_rate * duration)
        
        # Define adventure-themed melody (A minor pentatonic for more dramatic feel)
        melody_notes = [220, 246, 277, 329, 370, 415, 466, 523]  # A, B, C#, E, F#, G#, A
        bass_notes = [110, 123, 138, 164, 185, 207, 233, 261]   # Lower octave
        
        # Create rhythm pattern (6/8 time for more dynamic feel)
        beats_per_bar = 6
        samples_per_beat = samples // (beats_per_bar * 4)  # 24 beats total
        
        music_data = []
        
        for i in range(samples):
            sample = 0.0
            
            # Main melody layer (plays every 3 beats for more dramatic timing)
            beat_position = (i // samples_per_beat) % 24
            if beat_position % 3 == 0:
                note_index = (beat_position // 3) % len(melody_notes)
                freq = melody_notes[note_index]
                # Add vibrato for more character
                vibrato = 0.02 * math.sin(2 * math.pi * 6 * i / sample_rate)
                sample += 0.25 * math.sin(2 * math.pi * freq * (1 + vibrato) * i / sample_rate)
                # Add harmonics for richer sound
                sample += 0.08 * math.sin(2 * math.pi * freq * 2 * i / sample_rate)
                sample += 0.04 * math.sin(2 * math.pi * freq * 3 * i / sample_rate)
            
            # Counter-melody layer (plays on off-beats)
            if beat_position % 3 == 1:
                note_index = ((beat_position // 3) + 2) % len(melody_notes)
                freq = melody_notes[note_index] * 1.5  # Higher octave
                sample += 0.15 * math.sin(2 * math.pi * freq * i / sample_rate)
            
            # Bass layer (plays on every beat with walking bass pattern)
            if beat_position % 1 == 0:
                note_index = (beat_position // 2) % len(bass_notes)
                freq = bass_notes[note_index]
                sample += 0.18 * math.sin(2 * math.pi * freq * i / sample_rate)
            
            # Enhanced percussion layer
            if beat_position in [0, 6, 12, 18]:  # Kick drum on strong beats
                sample += 0.35 * math.sin(2 * math.pi * 50 * i / sample_rate) * math.exp(-i / (sample_rate * 0.15))
            if beat_position in [3, 9, 15, 21]:  # Snare on backbeats
                sample += 0.25 * (math.sin(2 * math.pi * 180 * i / sample_rate) + 
                                math.sin(2 * math.pi * 360 * i / sample_rate)) * math.exp(-i / (sample_rate * 0.08))
            
            # Hi-hat pattern (more complex rhythm)
            if beat_position % 2 == 0:
                sample += 0.08 * math.sin(2 * math.pi * 900 * i / sample_rate) * math.exp(-i / (sample_rate * 0.03))
            if beat_position % 3 == 0:
                sample += 0.12 * math.sin(2 * math.pi * 1200 * i / sample_rate) * math.exp(-i / (sample_rate * 0.02))
            
            # Add some adventure-style effects
            if beat_position % 12 == 0:  # Every 2 bars
                # Cymbal crash effect
                sample += 0.2 * (math.sin(2 * math.pi * 2000 * i / sample_rate) + 
                               math.sin(2 * math.pi * 3000 * i / sample_rate)) * math.exp(-i / (sample_rate * 0.5))
            
            # Apply overall envelope with smoother transitions
            envelope = 1.0
            if i < sample_rate * 0.2:  # Longer fade in
                envelope = i / (sample_rate * 0.2)
            elif i > samples - sample_rate * 0.2:  # Longer fade out
                envelope = (samples - i) / (sample_rate * 0.2)
            
            # Clamp and convert to stereo
            sample = max(-1.0, min(1.0, sample * envelope))
            sample_value = int(sample * 32767 * 0.5)  # Slightly lower volume for better balance
            music_data.append([sample_value, sample_value])
        
        music_array = np.array(music_data, dtype=np.int16)
        return pygame.sndarray.make_sound(music_array)
        
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
        
    def set_sound_volume(self, volume):
        """Set sound effects volume (0.0 to 1.0)"""
        self.sound_volume = max(0.0, min(1.0, volume))
        
    def toggle_sound(self):
        """Toggle sound effects on/off"""
        self.sound_enabled = not self.sound_enabled
        
    def play_background_music(self):
        """Start playing background music"""
        if self.music_enabled and self.background_music and not self.music_playing:
            try:
                self.background_music.set_volume(self.music_volume)
                self.background_music.play(-1)  # Loop indefinitely
                self.music_playing = True
                print("🎵 Background music started")
            except Exception as e:
                print(f"Music play error: {e}")
                
    def stop_background_music(self):
        """Stop background music"""
        if self.music_playing:
            try:
                pygame.mixer.stop()
                self.music_playing = False
                print("🔇 Background music stopped")
            except Exception as e:
                print(f"Music stop error: {e}")
                
    def toggle_music(self):
        """Toggle background music on/off"""
        if self.music_playing:
            self.stop_background_music()
        else:
            self.play_background_music()
            
    def set_music_volume(self, volume):
        """Set background music volume (0.0 to 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
        if self.background_music:
            self.background_music.set_volume(self.music_volume)
        
    def cleanup(self):
        """Clean up audio resources"""
        pygame.mixer.quit()
