import pygame

class InputHandler:
    def __init__(self):
        self.jump_pressed = False
        self.jump_cooldown = 0
        self.jump_cooldown_max = 5  # Prevent rapid jumping
        
    def handle_jump(self, dinosaur):
        """Handle jump input for the dinosaur"""
        if not self.jump_pressed and self.jump_cooldown <= 0:
            dinosaur.jump()
            self.jump_pressed = True
            self.jump_cooldown = self.jump_cooldown_max
            
    def update(self):
        """Update input handler state"""
        # Update jump cooldown
        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1
            
        # Reset jump pressed state
        self.jump_pressed = False
        
    def handle_keydown(self, event, dinosaur, game_state):
        """Handle key down events"""
        if event.key == pygame.K_SPACE:
            if game_state.is_playing():
                self.handle_jump(dinosaur)
        elif event.key == pygame.K_p:
            if game_state.is_playing():
                game_state.pause_game()
            elif game_state.is_paused():
                game_state.resume_game()
        elif event.key == pygame.K_r:
            if game_state.is_game_over():
                return "restart"
        elif event.key == pygame.K_ESCAPE:
            return "quit"
            
        return None
        
    def handle_keyup(self, event):
        """Handle key up events"""
        if event.key == pygame.K_SPACE:
            self.jump_pressed = False
            
    def is_jump_pressed(self):
        """Check if jump key is currently pressed"""
        return self.jump_pressed
        
    def get_jump_cooldown(self):
        """Get current jump cooldown"""
        return self.jump_cooldown
