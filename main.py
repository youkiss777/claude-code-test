#!/usr/bin/env python3
"""
Claude Code Test Project
簡単な計算機アプリケーション
"""

def add(a, b):
    """二つの数値を加算する"""
    return a + b

def subtract(a, b):
    """二つの数値を減算する"""
    return a - b

def multiply(a, b):
    """二つの数値を乗算する"""
    return a * b

def divide(a, b):
    """二つの数値を除算する"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculator_menu():
    """計算機のメニューを表示"""
    print("=== Claude Code Test Calculator ===")
    print("1. 加算 (+)")
    print("2. 減算 (-)")
    print("3. 乗算 (*)")
    print("4. 除算 (/)")
    print("5. 終了")
    
def main():
    """メイン関数"""
    while True:
        calculator_menu()
        choice = input("\n選択してください (1-5): ")
        
        if choice == '5':
            print("計算機を終了します。")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("無効な選択です。1-5を選んでください。")
            continue
            
        try:
            a = float(input("最初の数値を入力: "))
            b = float(input("二番目の数値を入力: "))
            
            if choice == '1':
                result = add(a, b)
                print(f"結果: {a} + {b} = {result}")
            elif choice == '2':
                result = subtract(a, b)
                print(f"結果: {a} - {b} = {result}")
            elif choice == '3':
                result = multiply(a, b)
                print(f"結果: {a} * {b} = {result}")
            elif choice == '4':
                result = divide(a, b)
                print(f"結果: {a} / {b} = {result}")
                
        except ValueError as e:
            print(f"エラー: {e}")
        except Exception as e:
            print(f"予期しないエラー: {e}")
            
        print("-" * 40)

if __name__ == "__main__":
    main()
