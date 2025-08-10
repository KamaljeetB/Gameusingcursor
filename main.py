import pygame
import sys
from game.game_state import GameState
from game.player import Labubu
from game.obstacles import ObstacleManager
from game.collectibles import CollectibleManager
from game.physics import PhysicsEngine
from game.input_handler import InputHandler
from game.collision import CollisionManager
from utils.simple_audio import SimpleAudioManager
from config.constants import *
from config.settings import GameSettings

class LabubuObstacleCourse:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Labubu Obstacle Course")
        self.clock = pygame.time.Clock()
        
        # Initialize game components
        self.settings = GameSettings()
        self.game_state = GameState()
        self.input_handler = InputHandler()
        self.physics_engine = PhysicsEngine()
        self.collision_manager = CollisionManager()
        self.audio_manager = SimpleAudioManager()
        
        # Initialize game objects
        self.labubu = Labubu()
        self.obstacle_manager = ObstacleManager()
        self.collectible_manager = CollectibleManager()
        
        # Game variables
        self.score = 0
        self.collectible_score = 0
        self.game_speed = INITIAL_GAME_SPEED
        
        # Start background music
        self.audio_manager.play_background_music()
        
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.game_state.is_playing():
                    # Direct jump call for immediate response
                    self.labubu.jump()
                    self.audio_manager.play_jump()
                elif event.key == pygame.K_r and self.game_state.current_state == GameState.GAME_OVER:
                    self.restart_game()
                elif event.key == pygame.K_m:
                    self.audio_manager.toggle_sound()
                elif event.key == pygame.K_b:
                    self.audio_manager.toggle_music()
                elif event.key == pygame.K_ESCAPE:
                    # Toggle pause/resume
                    if self.game_state.is_playing():
                        self.pause_game()
                    elif self.game_state.is_paused():
                        self.resume_game()
                    
        return True
    
    def pause_game(self):
        """Pause the game and stop background music"""
        if self.game_state.is_playing():
            self.game_state.pause_game()
            # Pause background music
            if self.audio_manager.music_playing:
                self.audio_manager.stop_background_music()
            print("⏸️ Game paused - music stopped")
    
    def resume_game(self):
        """Resume the game and restart background music"""
        if self.game_state.is_paused():
            self.game_state.resume_game()
            # Resume background music
            if not self.audio_manager.music_playing:
                self.audio_manager.play_background_music()
            print("▶️ Game resumed - music restarted")
    
    def update(self):
        """Update game logic"""
        if self.game_state.current_state == GameState.PLAYING:
            # Update Labubu
            self.labubu.update()
            
            # Update obstacles
            self.obstacle_manager.update(self.game_speed)
            
            # Update collectibles
            self.collectible_manager.update(self.game_speed)
            
            # Check obstacle collisions
            if self.collision_manager.check_collisions(self.labubu, self.obstacle_manager.obstacles):
                self.audio_manager.play_death()
                # Stop background music when game over
                if self.audio_manager.music_playing:
                    self.audio_manager.stop_background_music()
                self.game_state.set_state(GameState.GAME_OVER)
            
            # Check collectible collisions
            collected_items = self.collectible_manager.check_collisions(self.labubu)
            if collected_items:
                self.collectible_score += sum(item.value for item in collected_items)
                # Play appropriate sound for each collected item
                for item in collected_items:
                    if hasattr(item, 'gem_type'):  # It's a gem
                        self.audio_manager.play_gem()
                    else:  # It's a coin
                        self.audio_manager.play_coin()
            
            # Update score and speed
            self.score += 1
            self.game_speed = INITIAL_GAME_SPEED + (self.score // 1000) * SPEED_INCREMENT
    
    def render(self):
        """Render the game"""
        # Clear screen
        self.screen.fill(SKY_COLOR)
        
        # Draw ground
        pygame.draw.rect(self.screen, GROUND_COLOR, (0, GROUND_Y, SCREEN_WIDTH, SCREEN_HEIGHT - GROUND_Y))
        
        # Draw game objects
        self.labubu.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.collectible_manager.draw(self.screen)
        
        # Draw UI
        self.draw_ui()
        
        # Draw pause screen if paused
        if self.game_state.is_paused():
            self.draw_pause_screen()
        
        # Update display
        pygame.display.flip()
    
    def draw_ui(self):
        """Draw user interface elements"""
        font = pygame.font.Font(None, 36)
        font_small = pygame.font.Font(None, 24)
        
        # Draw scores
        score_text = font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        
        collectible_text = font.render(f"Coins: {self.collectible_score}", True, BLACK)
        self.screen.blit(collectible_text, (10, 30))
        
        # Draw controls info
        controls_text = font_small.render("SPACE: Jump | M: Sound | B: Music | ESC: Pause", True, BLACK)
        self.screen.blit(controls_text, (10, 60))
        
        # Draw game over screen
        if self.game_state.current_state == GameState.GAME_OVER:
            self.draw_game_over_screen()
    
    def draw_pause_screen(self):
        """Draw pause screen overlay"""
        font_large = pygame.font.Font(None, 72)
        font_medium = pygame.font.Font(None, 48)
        font_small = pygame.font.Font(None, 36)
        
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = font_large.render("PAUSED", True, WHITE)
        text_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
        self.screen.blit(pause_text, text_rect)
        
        # Current scores
        score_text = font_medium.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        self.screen.blit(score_text, score_rect)
        
        collectible_text = font_medium.render(f"Coins: {self.collectible_score}", True, WHITE)
        collectible_rect = collectible_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        self.screen.blit(collectible_text, collectible_rect)
        
        # Resume instruction
        resume_text = font_medium.render("Press ESC to Resume", True, WHITE)
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(resume_text, resume_rect)
        
        # Additional controls
        controls_text = font_small.render("M: Toggle Sound | B: Toggle Music", True, WHITE)
        controls_rect = controls_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 90))
        self.screen.blit(controls_text, controls_rect)
    
    def draw_game_over_screen(self):
        """Draw game over screen"""
        font_large = pygame.font.Font(None, 72)
        font_medium = pygame.font.Font(None, 48)
        
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = font_large.render("GAME OVER", True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(game_over_text, text_rect)
        
        # Final scores
        final_score_text = font_medium.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        self.screen.blit(final_score_text, score_rect)
        
        collectible_score_text = font_medium.render(f"Coins Collected: {self.collectible_score}", True, WHITE)
        collectible_rect = collectible_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
        self.screen.blit(collectible_score_text, collectible_rect)
        
        # Restart instruction
        restart_text = font_medium.render("Press R to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70))
        self.screen.blit(restart_text, restart_rect)
    
    def restart_game(self):
        """Restart the game"""
        self.labubu = Labubu()
        self.obstacle_manager = ObstacleManager()
        self.collectible_manager = CollectibleManager()
        self.score = 0
        self.collectible_score = 0
        self.game_speed = INITIAL_GAME_SPEED
        self.game_state.set_state(GameState.PLAYING)
        
        # Start background music
        self.audio_manager.play_background_music()
        print("🔄 Game restarted - music started")
    
    def cleanup(self):
        """Clean up game resources"""
        self.audio_manager.cleanup()
    
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            # Handle events
            running = self.handle_events()
            
            # Update game logic
            self.update()
            
            # Render
            self.render()
            
            # Cap the frame rate
            self.clock.tick(FPS)
        
        self.cleanup()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = LabubuObstacleCourse()
    game.run()
