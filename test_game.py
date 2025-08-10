#!/usr/bin/env python3
"""
Test script to verify all game components work correctly
"""

def test_imports():
    """Test that all modules can be imported"""
    try:
        import pygame
        print("✓ Pygame imported successfully")
        
        from game.game_state import GameState
        print("✓ GameState imported successfully")
        
        from game.player import Labubu
        print("✓ Labubu imported successfully")
        
        from game.obstacles import ObstacleManager, Cactus
        print("✓ Obstacles imported successfully")
        
        from game.physics import PhysicsEngine
        print("✓ PhysicsEngine imported successfully")
        
        from game.input_handler import InputHandler
        print("✓ InputHandler imported successfully")
        
        from game.collision import CollisionManager
        print("✓ CollisionManager imported successfully")
        
        from config import constants
        print("✓ Constants imported successfully")
        
        from config.settings import GameSettings
        print("✓ GameSettings imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_game_objects():
    """Test that game objects can be created"""
    try:
        from game.game_state import GameState
        from game.player import Labubu
        from game.obstacles import ObstacleManager
        from game.physics import PhysicsEngine
        from game.input_handler import InputHandler
        from game.collision import CollisionManager
        from config.settings import GameSettings
        
        # Create game objects
        game_state = GameState()
        labubu = Labubu()
        obstacle_manager = ObstacleManager()
        physics_engine = PhysicsEngine()
        input_handler = InputHandler()
        collision_manager = CollisionManager()
        settings = GameSettings()
        
        print("✓ All game objects created successfully")
        
        # Test basic functionality
        assert game_state.is_playing() == True
        assert labubu.is_on_ground == True
        assert len(obstacle_manager.obstacles) == 0
        
        print("✓ Basic functionality tests passed")
        
        return True
        
    except Exception as e:
        print(f"✗ Object creation error: {e}")
        return False

def test_game_mechanics():
    """Test basic game mechanics"""
    try:
        from game.player import Labubu
        from game.obstacles import Cactus
        from game.collision import CollisionManager
        from config import constants
        
        # Test Labubu jumping
        labubu = Labubu()
        initial_y = labubu.y
        labubu.jump()
        assert labubu.is_jumping == True
        assert labubu.velocity_y == constants.JUMP_VELOCITY
        print("✓ Labubu jumping mechanics work")
        
        # Test obstacle creation
        cactus = Cactus(100)
        assert cactus.x == 100
        assert cactus.y == constants.GROUND_Y - constants.OBSTACLE_HEIGHT
        print("✓ Obstacle creation works")
        
        # Test collision detection
        collision_manager = CollisionManager()
        labubu_rect = labubu.get_rect()
        cactus_rect = cactus.get_rect()
        
        # Move cactus to Labubu position to test collision
        cactus.x = labubu.x
        cactus.y = labubu.y
        cactus_rect = cactus.get_rect()
        
        collision = collision_manager.check_rect_collision(labubu_rect, cactus_rect)
        assert collision == True
        print("✓ Collision detection works")
        
        return True
        
    except Exception as e:
        print(f"✗ Game mechanics error: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing Dinosaur Game Components...")
    print("=" * 40)
    
    tests = [
        ("Import Test", test_imports),
        ("Object Creation Test", test_game_objects),
        ("Game Mechanics Test", test_game_mechanics)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nRunning {test_name}...")
        if test_func():
            passed += 1
            print(f"✓ {test_name} PASSED")
        else:
            print(f"✗ {test_name} FAILED")
    
    print("\n" + "=" * 40)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The game is ready to run.")
        print("\nTo play the game, run: python3 main.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()
