import easygui

from sign_to_text import sign_to_text
from voice_to_sign import voice_to_sign

def main_menu():
    while True:
        image = "assets/logo.png"  # make sure this path is correct

        choice = easygui.buttonbox(
            title="Gesture Bridge",
            image=image,
            msg="Welcome to Gesture Bridge, Choose the mode you want to use",
            choices=["Sign to Text", "Voice to Sign", "Exit"],
        )

        if choice == "Sign to Text":
            sign_to_text()

        elif choice == "Voice to Sign":
            voice_to_sign()

        elif choice == "Exit" or choice is None:
            easygui.msgbox("Thank you for using the application!")
            break

if __name__ == "__main__":
    main_menu()
