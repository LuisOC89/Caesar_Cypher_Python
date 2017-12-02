from helpers import rotate_character   

def encrypt(text, rot):
    encrypted = ""
    for each_char in text:
        if each_char == " ":
            encrypted = encrypted + " "
        else:
            encrypted = encrypted + rotate_character(each_char, rot)       
    return encrypted

def main():
    user_text = input("Type a message: \n")
    user_rotation = input("Rotate by: \n")
    print(encrypt(user_text, int(user_rotation)))

if __name__ == "__main__":
    main()
