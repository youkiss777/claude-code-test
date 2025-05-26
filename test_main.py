"""
Claude Code Test Project - Advanced Unit Tests
拡張計算機アプリケーションのテスト
"""

import unittest
import sys
import os
import math
import json
import tempfile

# テスト対象のモジュールをインポート
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from main import add, subtract, multiply, divide, AdvancedCalculator, CalculatorHistory

class TestBasicCalculatorFunctions(unittest.TestCase):
    """基本計算機関数のテストクラス（後方互換性）"""
    
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

class TestAdvancedCalculator(unittest.TestCase):
    """拡張計算機のテストクラス"""
    
    def setUp(self):
        """テスト前の準備"""
        self.calc = AdvancedCalculator()
    
    def test_basic_operations(self):
        """基本演算のテスト"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.divide(10, 2), 5)
    
    def test_power(self):
        """べき乗のテスト"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
        self.assertEqual(self.calc.power(2, -1), 0.5)
    
    def test_square_root(self):
        """平方根のテスト"""
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(0), 0)
        self.assertAlmostEqual(self.calc.square_root(2), math.sqrt(2), places=10)
        
        # 負の数のテスト
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_factorial(self):
        """階乗のテスト"""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)
        
        # 無効な入力のテスト
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
    
    def test_trigonometric_functions(self):
        """三角関数のテスト"""
        # 特定角度での値をテスト
        self.assertAlmostEqual(self.calc.sin(0), 0, places=10)
        self.assertAlmostEqual(self.calc.sin(90), 1, places=10)
        self.assertAlmostEqual(self.calc.cos(0), 1, places=10)
        self.assertAlmostEqual(self.calc.cos(90), 0, places=10)
        self.assertAlmostEqual(self.calc.tan(0), 0, places=10)
        self.assertAlmostEqual(self.calc.tan(45), 1, places=10)
    
    def test_divide_by_zero_advanced(self):
        """拡張計算機でのゼロ除算テスト"""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

class TestCalculatorHistory(unittest.TestCase):
    """計算履歴のテストクラス"""
    
    def setUp(self):
        """テスト前の準備"""
        self.history = CalculatorHistory()
        self.calc = AdvancedCalculator()
    
    def test_add_calculation(self):
        """計算記録の追加テスト"""
        self.history.add_calculation("add", 2, 3, 5)
        history_list = self.history.get_history()
        
        self.assertEqual(len(history_list), 1)
        self.assertEqual(history_list[0]['operation'], 'add')
        self.assertEqual(history_list[0]['operand1'], 2)
        self.assertEqual(history_list[0]['operand2'], 3)
        self.assertEqual(history_list[0]['result'], 5)
    
    def test_clear_history(self):
        """履歴クリアのテスト"""
        self.history.add_calculation("add", 2, 3, 5)
        self.history.add_calculation("multiply", 4, 5, 20)
        
        self.assertEqual(len(self.history.get_history()), 2)
        
        self.history.clear_history()
        self.assertEqual(len(self.history.get_history()), 0)
    
    def test_save_to_file(self):
        """ファイル保存のテスト"""
        self.history.add_calculation("add", 2, 3, 5)
        self.history.add_calculation("multiply", 4, 5, 20)
        
        # 一時ファイルにテスト
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as temp_file:
            temp_filename = temp_file.name
        
        try:
            # ファイルに保存
            result = self.history.save_to_file(temp_filename)
            self.assertTrue(result)
            
            # ファイルから読み込んで確認
            with open(temp_filename, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
            
            self.assertEqual(len(loaded_data), 2)
            self.assertEqual(loaded_data[0]['operation'], 'add')
            self.assertEqual(loaded_data[1]['operation'], 'multiply')
            
        finally:
            # 一時ファイルを削除
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)
    
    def test_calculation_with_history(self):
        """計算実行時の履歴記録テスト"""
        # 計算実行
        self.calc.add(10, 5)
        self.calc.multiply(3, 7)
        self.calc.square_root(16)
        
        history = self.calc.history.get_history()
        self.assertEqual(len(history), 3)
        
        # 各計算の確認
        self.assertEqual(history[0]['operation'], 'add')
        self.assertEqual(history[0]['result'], 15)
        
        self.assertEqual(history[1]['operation'], 'multiply')
        self.assertEqual(history[1]['result'], 21)
        
        self.assertEqual(history[2]['operation'], 'sqrt')
        self.assertEqual(history[2]['result'], 4)

class TestEdgeCases(unittest.TestCase):
    """エッジケースのテストクラス"""
    
    def setUp(self):
        self.calc = AdvancedCalculator()
    
    def test_large_numbers(self):
        """大きな数値のテスト"""
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)
        self.assertEqual(self.calc.multiply(1e6, 1e6), 1e12)
    
    def test_small_numbers(self):
        """小さな数値のテスト"""
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)
        self.assertAlmostEqual(self.calc.subtract(1.0, 0.9), 0.1, places=10)
    
    def test_negative_numbers(self):
        """負の数のテスト"""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.divide(-10, 2), -5)
    
    def test_zero_operations(self):
        """ゼロを含む計算のテスト"""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.power(0, 5), 0)
        self.assertEqual(self.calc.power(5, 0), 1)

class TestPerformance(unittest.TestCase):
    """パフォーマンステストクラス"""
    
    def setUp(self):
        self.calc = AdvancedCalculator()
    
    def test_large_factorial(self):
        """大きな階乗の計算テスト"""
        # 20!まではすぐに計算できるはず
        result = self.calc.factorial(20)
        expected = math.factorial(20)
        self.assertEqual(result, expected)
    
    def test_many_calculations(self):
        """多数の計算実行テスト"""
        # 1000回の計算を実行
        for i in range(1000):
            self.calc.add(i, i + 1)
        
        history = self.calc.history.get_history()
        self.assertEqual(len(history), 1000)
        
        # 最後の計算を確認
        last_calc = history[-1]
        self.assertEqual(last_calc['operand1'], 999)
        self.assertEqual(last_calc['operand2'], 1000)
        self.assertEqual(last_calc['result'], 1999)

if __name__ == '__main__':
    # テストスイートを実行
    print("=== Claude Code Advanced Test - Unit Tests ===")
    print("Testing basic functions, advanced calculator, history, and edge cases...")
    print("=" * 60)
    
    # より詳細なテスト出力
    unittest.main(verbosity=2, buffer=True)
