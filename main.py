"""
Project: OTP Detection System
Author: B. Lakshmi Vara Prasad
GitHub: https://github.com/prasad-ai18
Description: Detects OTP codes from messages using Python and regular expressions.
"""
import re

otp_history = []

def detect_otp(message):
    pattern = r'\b\d{4,6}\b'
    otp = re.findall(pattern, message)

    if otp:
        print("\nOTP Found:", otp[0])
        otp_history.append(otp[0])
    else:
        print("\nNo OTP detected")


def check_multiple_messages():
    n = int(input("\nHow many messages do you want to check? "))

    for i in range(n):
        message = input(f"\nEnter message {i+1}: ")
        detect_otp(message)


def view_history():
    if otp_history:
        print("\nDetected OTP History:")
        for i, otp in enumerate(otp_history, 1):
            print(f"{i}. {otp}")
    else:
        print("\nNo OTPs detected yet.")


def validate_otp():
    user_otp = input("\nEnter OTP to validate: ")

    if re.fullmatch(r'\d{4,6}', user_otp):
        print("Valid OTP format")
    else:
        print("Invalid OTP format")


def menu():
    while True:
        print("\n===== OTP Detection System =====")
        print("1. Detect OTP from a message")
        print("2. Detect OTP from multiple messages")
        print("3. Validate OTP format")
        print("4. View detected OTP history")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            message = input("\nEnter the message: ")
            detect_otp(message)

        elif choice == "2":
            check_multiple_messages()

        elif choice == "3":
            validate_otp()

        elif choice == "4":
            view_history()

        elif choice == "5":
            print("\nExiting OTP Detection System...")
            break

        else:
            print("\nInvalid choice. Try again.")


print("Welcome to OTP Detection System")
menu()
