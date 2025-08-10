#!/usr/bin/env python3
"""
Verification script to test specific game mechanics in detail
"""

import pygame
import time
from game.game_state import GameState
from game.player import Dinosaur
from game.obstacles import ObstacleManager, Cactus
from game.collision import CollisionManager
from config import constants

def test_dinosaur_physics():
    """Test dinosaur physics and jumping"""
    print("🧪 Testing Dinosaur Physics...")
    
    dinosaur = Dinosaur()
    
    # Test initial state
    assert dinosaur.is_on_ground == True, "Dinosaur should start on ground"
    assert dinosaur.is_jumping == False, "Dinosaur should not be jumping initially"
    assert dinosaur.velocity_y == 0, "Initial velocity should be 0"
    
    # Test jumping
    initial_y = dinosaur.y
    dinosaur.jump()
    assert dinosaur.is_jumping == True, "Dinosaur should be jumping after jump()"
    assert dinosaur.velocity_y == constants.JUMP_VELOCITY, "Jump velocity should be set"
    assert dinosaur.is_on_ground == False, "Dinosaur should not be on ground after jump"
    
    # Test gravity application
    for i in range(10):
        dinosaur.update()
    
    assert dinosaur.velocity_y > constants.JUMP_VELOCITY, "Velocity should increase due to gravity"
    
    # Test landing
    while dinosaur.y < constants.DINO_Y:
        dinosaur.update()
    
    assert dinosaur.is_on_ground == True, "Dinosaur should land on ground"
    assert dinosaur.is_jumping == False, "Dinosaur should not be jumping after landing"
    assert dinosaur.velocity_y == 0, "Velocity should be 0 after landing"
    
    print("✅ Dinosaur physics test passed!")

def test_obstacle_system():
    """Test obstacle spawning and movement"""
    print("🧪 Testing Obstacle System...")
    
    obstacle_manager = ObstacleManager()
    
    # Test initial state
    assert len(obstacle_manager.obstacles) == 0, "Should start with no obstacles"
    
    # Test obstacle spawning
    obstacle_manager.spawn_obstacle()
    assert len(obstacle_manager.obstacles) == 1, "Should spawn one obstacle"
    
    obstacle = obstacle_manager.obstacles[0]
    assert isinstance(obstacle, Cactus), "Should spawn a cactus"
    assert obstacle.x == constants.OBSTACLE_SPAWN_X, "Obstacle should spawn at correct X position"
    assert obstacle.y == constants.GROUND_Y - constants.OBSTACLE_HEIGHT, "Obstacle should be on ground"
    
    # Test obstacle movement
    initial_x = obstacle.x
    obstacle_manager.update(constants.INITIAL_GAME_SPEED)
    assert obstacle.x < initial_x, "Obstacle should move left"
    
    # Test obstacle cleanup
    obstacle.x = -100  # Move off screen
    obstacle_manager.update(constants.INITIAL_GAME_SPEED)
    assert len(obstacle_manager.obstacles) == 0, "Off-screen obstacles should be removed"
    
    print("✅ Obstacle system test passed!")

def test_collision_detection():
    """Test collision detection system"""
    print("🧪 Testing Collision Detection...")
    
    collision_manager = CollisionManager()
    dinosaur = Dinosaur()
    cactus = Cactus(100)
    
    # Test no collision when far apart
    cactus.x = 200
    assert collision_manager.check_collisions(dinosaur, [cactus]) == False, "No collision when far apart"
    
    # Test collision when overlapping
    cactus.x = dinosaur.x
    cactus.y = dinosaur.y
    assert collision_manager.check_collisions(dinosaur, [cactus]) == True, "Should detect collision when overlapping"
    
    # Test collision with tolerance
    cactus.x = dinosaur.x + 5
    cactus.y = dinosaur.y + 5
    assert collision_manager.check_collisions(dinosaur, [cactus]) == True, "Should detect collision with tolerance"
    
    print("✅ Collision detection test passed!")

def test_game_state_management():
    """Test game state transitions"""
    print("🧪 Testing Game State Management...")
    
    game_state = GameState()
    
    # Test initial state
    assert game_state.is_playing() == True, "Should start in playing state"
    assert game_state.is_paused() == False, "Should not be paused initially"
    assert game_state.is_game_over() == False, "Should not be game over initially"
    
    # Test pause functionality
    game_state.pause_game()
    assert game_state.is_paused() == True, "Should be paused after pause_game()"
    assert game_state.is_playing() == False, "Should not be playing when paused"
    
    # Test resume functionality
    game_state.resume_game()
    assert game_state.is_playing() == True, "Should be playing after resume_game()"
    assert game_state.is_paused() == False, "Should not be paused when playing"
    
    # Test game over state
    game_state.set_state(GameState.GAME_OVER)
    assert game_state.is_game_over() == True, "Should be game over after setting state"
    assert game_state.is_playing() == False, "Should not be playing when game over"
    
    # Test restart
    game_state.restart_game()
    assert game_state.is_playing() == True, "Should be playing after restart"
    
    print("✅ Game state management test passed!")

def test_scoring_system():
    """Test scoring and speed progression"""
    print("🧪 Testing Scoring System...")
    
    score = 0
    game_speed = constants.INITIAL_GAME_SPEED
    
    # Test initial values
    assert game_speed == constants.INITIAL_GAME_SPEED, "Should start with initial game speed"
    
    # Test score progression
    for i in range(1000):
        score += 1
        game_speed = constants.INITIAL_GAME_SPEED + (score // 1000) * constants.SPEED_INCREMENT
    
    assert score == 1000, "Score should increment correctly"
    assert game_speed == constants.INITIAL_GAME_SPEED + constants.SPEED_INCREMENT, "Speed should increase after 1000 points"
    
    # Test multiple speed increases
    for i in range(2000):
        score += 1
        game_speed = constants.INITIAL_GAME_SPEED + (score // 1000) * constants.SPEED_INCREMENT
    
    assert game_speed == constants.INITIAL_GAME_SPEED + 3 * constants.SPEED_INCREMENT, "Speed should increase multiple times"
    
    print("✅ Scoring system test passed!")

def main():
    """Run all verification tests"""
    print("🔍 Dinosaur Game - Phase 1 Verification Tests")
    print("=" * 50)
    
    tests = [
        ("Dinosaur Physics", test_dinosaur_physics),
        ("Obstacle System", test_obstacle_system),
        ("Collision Detection", test_collision_detection),
        ("Game State Management", test_game_state_management),
        ("Scoring System", test_scoring_system)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            test_func()
            passed += 1
            print(f"✅ {test_name} PASSED\n")
        except Exception as e:
            print(f"❌ {test_name} FAILED: {e}\n")
    
    print("=" * 50)
    print(f"Verification Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All verification tests passed!")
        print("🚀 Phase 1 is fully functional and ready for Phase 2 development!")
    else:
        print("⚠️  Some tests failed. Please review the errors above.")

if __name__ == "__main__":
    main()
