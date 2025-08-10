class GameSettings:
    def __init__(self):
        # Game settings
        self.sound_enabled = True
        self.music_enabled = True
        self.fullscreen = False
        self.vsync = True
        
        # Difficulty settings
        self.obstacle_frequency = 1.0
        self.speed_multiplier = 1.0
        
        # Control settings
        self.jump_key = 'SPACE'
        self.restart_key = 'R'
        
    def toggle_sound(self):
        """Toggle sound on/off"""
        self.sound_enabled = not self.sound_enabled
        
    def toggle_music(self):
        """Toggle music on/off"""
        self.music_enabled = not self.music_enabled
        
    def set_difficulty(self, difficulty):
        """Set game difficulty (easy, normal, hard)"""
        if difficulty == 'easy':
            self.obstacle_frequency = 0.7
            self.speed_multiplier = 0.8
        elif difficulty == 'normal':
            self.obstacle_frequency = 1.0
            self.speed_multiplier = 1.0
        elif difficulty == 'hard':
            self.obstacle_frequency = 1.3
            self.speed_multiplier = 1.2
