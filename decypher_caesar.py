from helpers import rotate_character   

def undo_encrypt(text, rot):
    encrypted = ""
    for each_char in text:
        if each_char == " ":
            encrypted = encrypted + " "
        else:
            encrypted = encrypted + rotate_character(each_char, -rot)       
    return encrypted

def main():
    user_text = input("Type a message encrypted with the Caesar Cypher: \n")
    user_rotation_used = input("Characters Rotated by: \n")
    print(undo_encrypt(user_text, int(user_rotation_used)))

if __name__ == "__main__":
    main()
