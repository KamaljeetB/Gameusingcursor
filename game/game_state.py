class GameState:
    """Game state management class"""
    
    # Game states
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    HIGH_SCORE = "high_score"
    
    def __init__(self):
        self.current_state = self.PLAYING
        self.previous_state = None
        
    def set_state(self, new_state):
        """Change the current game state"""
        if new_state in [self.MENU, self.PLAYING, self.PAUSED, self.GAME_OVER, self.HIGH_SCORE]:
            self.previous_state = self.current_state
            self.current_state = new_state
            
    def get_state(self):
        """Get current game state"""
        return self.current_state
        
    def is_playing(self):
        """Check if game is in playing state"""
        return self.current_state == self.PLAYING
        
    def is_paused(self):
        """Check if game is paused"""
        return self.current_state == self.PAUSED
        
    def is_game_over(self):
        """Check if game is over"""
        return self.current_state == self.GAME_OVER
        
    def pause_game(self):
        """Pause the game"""
        if self.current_state == self.PLAYING:
            self.set_state(self.PAUSED)
            
    def resume_game(self):
        """Resume the game"""
        if self.current_state == self.PAUSED:
            self.set_state(self.PLAYING)
            
    def restart_game(self):
        """Restart the game"""
        self.set_state(self.PLAYING)
        
    def go_to_menu(self):
        """Go to main menu"""
        self.set_state(self.MENU)
