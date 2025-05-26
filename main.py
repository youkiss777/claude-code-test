#!/usr/bin/env python3
"""
Claude Code Test Project - Advanced Calculator
簡単な計算機アプリケーション（拡張版）
"""

import math
import json
from datetime import datetime

class CalculatorHistory:
    """計算履歴を管理するクラス"""
    
    def __init__(self):
        self.history = []
    
    def add_calculation(self, operation, operand1, operand2, result):
        """計算結果を履歴に追加"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "operand1": operand1,
            "operand2": operand2,
            "result": result
        }
        self.history.append(entry)
    
    def get_history(self):
        """履歴を取得"""
        return self.history
    
    def clear_history(self):
        """履歴をクリア"""
        self.history.clear()
    
    def save_to_file(self, filename="calculator_history.json"):
        """履歴をファイルに保存"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"履歴保存エラー: {e}")
            return False

class AdvancedCalculator:
    """拡張計算機クラス"""
    
    def __init__(self):
        self.history = CalculatorHistory()
    
    def add(self, a, b):
        """二つの数値を加算する"""
        result = a + b
        self.history.add_calculation("add", a, b, result)
        return result

    def subtract(self, a, b):
        """二つの数値を減算する"""
        result = a - b
        self.history.add_calculation("subtract", a, b, result)
        return result

    def multiply(self, a, b):
        """二つの数値を乗算する"""
        result = a * b
        self.history.add_calculation("multiply", a, b, result)
        return result

    def divide(self, a, b):
        """二つの数値を除算する"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.add_calculation("divide", a, b, result)
        return result
    
    def power(self, a, b):
        """べき乗計算"""
        result = a ** b
        self.history.add_calculation("power", a, b, result)
        return result
    
    def square_root(self, a):
        """平方根計算"""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = math.sqrt(a)
        self.history.add_calculation("sqrt", a, None, result)
        return result
    
    def factorial(self, n):
        """階乗計算"""
        if n < 0 or not isinstance(n, int):
            raise ValueError("Factorial is only defined for non-negative integers")
        result = math.factorial(n)
        self.history.add_calculation("factorial", n, None, result)
        return result
    
    def sin(self, angle_degrees):
        """サイン（度数法）"""
        angle_radians = math.radians(angle_degrees)
        result = math.sin(angle_radians)
        self.history.add_calculation("sin", angle_degrees, None, result)
        return result
    
    def cos(self, angle_degrees):
        """コサイン（度数法）"""
        angle_radians = math.radians(angle_degrees)
        result = math.cos(angle_radians)
        self.history.add_calculation("cos", angle_degrees, None, result)
        return result
    
    def tan(self, angle_degrees):
        """タンジェント（度数法）"""
        angle_radians = math.radians(angle_degrees)
        result = math.tan(angle_radians)
        self.history.add_calculation("tan", angle_degrees, None, result)
        return result

def calculator_menu():
    """計算機のメニューを表示"""
    print("=== Claude Code Advanced Calculator ===")
    print("基本演算:")
    print("1. 加算 (+)")
    print("2. 減算 (-)")
    print("3. 乗算 (*)")
    print("4. 除算 (/)")
    print("拡張演算:")
    print("5. べき乗 (^)")
    print("6. 平方根 (√)")
    print("7. 階乗 (!)")
    print("8. サイン (sin)")
    print("9. コサイン (cos)")
    print("10. タンジェント (tan)")
    print("その他:")
    print("11. 履歴表示")
    print("12. 履歴保存")
    print("13. 履歴クリア")
    print("14. 終了")

def main():
    """メイン関数"""
    calc = AdvancedCalculator()
    
    while True:
        calculator_menu()
        choice = input("\n選択してください (1-14): ")
        
        if choice == '14':
            print("計算機を終了します。")
            break
        
        try:
            if choice in ['1', '2', '3', '4', '5']:
                # 二項演算
                a = float(input("最初の数値を入力: "))
                b = float(input("二番目の数値を入力: "))
                
                if choice == '1':
                    result = calc.add(a, b)
                    print(f"結果: {a} + {b} = {result}")
                elif choice == '2':
                    result = calc.subtract(a, b)
                    print(f"結果: {a} - {b} = {result}")
                elif choice == '3':
                    result = calc.multiply(a, b)
                    print(f"結果: {a} * {b} = {result}")
                elif choice == '4':
                    result = calc.divide(a, b)
                    print(f"結果: {a} / {b} = {result}")
                elif choice == '5':
                    result = calc.power(a, b)
                    print(f"結果: {a} ^ {b} = {result}")
            
            elif choice in ['6', '7', '8', '9', '10']:
                # 単項演算
                a = float(input("数値を入力: "))
                
                if choice == '6':
                    result = calc.square_root(a)
                    print(f"結果: √{a} = {result}")
                elif choice == '7':
                    if not a.is_integer() or a < 0:
                        print("階乗は非負の整数でのみ定義されます。")
                        continue
                    result = calc.factorial(int(a))
                    print(f"結果: {int(a)}! = {result}")
                elif choice == '8':
                    result = calc.sin(a)
                    print(f"結果: sin({a}°) = {result}")
                elif choice == '9':
                    result = calc.cos(a)
                    print(f"結果: cos({a}°) = {result}")
                elif choice == '10':
                    result = calc.tan(a)
                    print(f"結果: tan({a}°) = {result}")
            
            elif choice == '11':
                # 履歴表示
                history = calc.history.get_history()
                if not history:
                    print("履歴がありません。")
                else:
                    print("\n=== 計算履歴 ===")
                    for i, entry in enumerate(history[-10:], 1):  # 最新10件
                        timestamp = entry['timestamp'][:19]  # 秒まで表示
                        op = entry['operation']
                        op1 = entry['operand1']
                        op2 = entry['operand2']
                        result = entry['result']
                        
                        if op2 is None:
                            print(f"{i}. [{timestamp}] {op}({op1}) = {result}")
                        else:
                            print(f"{i}. [{timestamp}] {op}({op1}, {op2}) = {result}")
            
            elif choice == '12':
                # 履歴保存
                if calc.history.save_to_file():
                    print("履歴をcalculator_history.jsonに保存しました。")
                else:
                    print("履歴の保存に失敗しました。")
            
            elif choice == '13':
                # 履歴クリア
                calc.history.clear_history()
                print("履歴をクリアしました。")
            
            else:
                print("無効な選択です。1-14を選んでください。")
                continue
                
        except ValueError as e:
            print(f"エラー: {e}")
        except Exception as e:
            print(f"予期しないエラー: {e}")
            
        print("-" * 50)

# 後方互換性のために元の関数も残す
def add(a, b):
    """二つの数値を加算する（後方互換性）"""
    return a + b

def subtract(a, b):
    """二つの数値を減算する（後方互換性）"""
    return a - b

def multiply(a, b):
    """二つの数値を乗算する（後方互換性）"""
    return a * b

def divide(a, b):
    """二つの数値を除算する（後方互換性）"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    main()
