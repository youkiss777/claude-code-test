"""
Claude Code Test Project - Unit Tests
計算機アプリケーションのテスト
"""

import unittest
import sys
import os

# テスト対象のモジュールをインポート
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from main import add, subtract, multiply, divide

class TestCalculatorFunctions(unittest.TestCase):
    """計算機関数のテストクラス"""
    
    def test_add(self):
        """加算のテスト"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10.5, 5.5), 16.0)
    
    def test_subtract(self):
        """減算のテスト"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(10.5, 5.5), 5.0)
    
    def test_multiply(self):
        """乗算のテスト"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        """除算のテスト"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(15, 3), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-10, 2), -5)
    
    def test_divide_by_zero(self):
        """ゼロ除算のテスト"""
        with self.assertRaises(ValueError):
            divide(10, 0)
        with self.assertRaises(ValueError):
            divide(-5, 0)

class TestEdgeCases(unittest.TestCase):
    """エッジケースのテストクラス"""
    
    def test_large_numbers(self):
        """大きな数値のテスト"""
        self.assertEqual(add(1e10, 1e10), 2e10)
        self.assertEqual(multiply(1e6, 1e6), 1e12)
    
    def test_small_numbers(self):
        """小さな数値のテスト"""
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)
        self.assertAlmostEqual(subtract(1.0, 0.9), 0.1, places=10)

if __name__ == '__main__':
    # テストスイートを実行
    print("=== Claude Code Test - Unit Tests ===")
    unittest.main(verbosity=2)
