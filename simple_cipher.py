#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
簡單的加密解密程式
使用 Caesar Cipher (凱薩加密法)
"""


def encrypt(text, shift=3):
    """
    加密文字

    Args:
        text: 要加密的文字
        shift: 偏移量 (預設為 3)

    Returns:
        加密後的文字
    """
    result = ""

    for char in text:
        if char.isalpha():
            # 判斷是大寫還是小寫
            ascii_offset = 65 if char.isupper() else 97
            # 加密並保持在字母範圍內
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += encrypted_char
        else:
            # 非字母字元保持不變
            result += char

    return result


def decrypt(text, shift=3):
    """
    解密文字

    Args:
        text: 要解密的文字
        shift: 偏移量 (預設為 3)

    Returns:
        解密後的文字
    """
    # 解密就是反向偏移
    return encrypt(text, -shift)


def main():
    """主程式"""
    print("=== 簡單加密程式 ===\n")

    # 示範加密
    original_text = "Hello World"
    shift_value = 3

    print(f"原始文字: {original_text}")

    encrypted = encrypt(original_text, shift_value)
    print(f"加密後: {encrypted}")

    decrypted = decrypt(encrypted, shift_value)
    print(f"解密後: {decrypted}")

    print("\n--- 互動模式 ---")
    while True:
        print("\n請選擇操作:")
        print("1. 加密")
        print("2. 解密")
        print("3. 結束")

        choice = input("請輸入選項 (1/2/3): ").strip()

        if choice == "3":
            print("程式結束")
            break

        if choice not in ["1", "2"]:
            print("無效的選項，請重新選擇")
            continue

        text = input("請輸入文字: ")
        shift = input("請輸入偏移量 (預設為 3): ").strip()
        shift = int(shift) if shift.isdigit() else 3

        if choice == "1":
            result = encrypt(text, shift)
            print(f"加密結果: {result}")
        else:
            result = decrypt(text, shift)
            print(f"解密結果: {result}")


if __name__ == "__main__":
    main()
