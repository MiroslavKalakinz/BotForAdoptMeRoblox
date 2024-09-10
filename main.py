# version 0.8
import pydirectinput
import time
import datetime
import tkinter
import playsound


time.sleep(3)
print('Made by MIROSXWBR')

playsound.playsound('start.mp3', True)





# Служебные
def respawn():
    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, respawn"
    print(cur_time)
    time.sleep(3)
    pydirectinput.press('esc')
    pydirectinput.press('r')
    pydirectinput.press('enter')


def tonnel():
    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, tonnel"
    print(cur_time)

    pydirectinput.keyDown('s')
    time.sleep(0.5)
    pydirectinput.press('e')
    pydirectinput.keyUp('s')
    time.sleep(1)
    pydirectinput.keyDown('w')
    time.sleep(2)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(5.5)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep(5.5)
    pydirectinput.keyUp('s')
    pydirectinput.keyDown('d')
    time.sleep(3)
    pydirectinput.keyUp('d')
    time.sleep(8)


# Задания

def drink():
    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, drink"
    print(cur_time)
    pydirectinput.keyDown('w')
    time.sleep(1)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(0.3)
    pydirectinput.keyUp('d')
    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(10)
    respawn()


def eat():
    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, eat"
    print(cur_time)
    pydirectinput.keyDown('w')
    time.sleep(1)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(0.5)
    pydirectinput.keyUp('a')
    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(10)
    respawn()


def sleep():
    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, sleep"
    print(cur_time)
    pydirectinput.keyDown('a')
    time.sleep(0.5)
    pydirectinput.keyUp('a')
    time.sleep(0.5)
    pydirectinput.press('e')
    time.sleep(15)
    respawn()


def bath():
    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, bath"
    print(cur_time)
    pydirectinput.keyDown('w')
    time.sleep(0.4)
    pydirectinput.keyUp('w')
    time.sleep(0.2)
    pydirectinput.keyDown('d')
    time.sleep(0.4)
    pydirectinput.keyUp('d')
    pydirectinput.press('e')
    pydirectinput.press('2')
    time.sleep(12)
    respawn()


def pizza():
    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, pizza"
    print(cur_time)

    tonnel()

    pydirectinput.keyDown('w')
    time.sleep(5)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(8)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(5.2)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(1)
    pydirectinput.keyUp('a')

    time.sleep(50)

    respawn()


def hospital():
    tonnel()

    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, hospital"
    print(cur_time)

    pydirectinput.keyDown('w')
    time.sleep(21)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(4)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(3.5)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(1)
    pydirectinput.keyUp('a')

    time.sleep(2)

    pydirectinput.keyDown('a')
    time.sleep(1)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('w')
    time.sleep(5)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(1.5)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(0.4)
    pydirectinput.keyUp('s')
    pydirectinput.press('e')
    pydirectinput.click(1851, 823)

    time.sleep(10)

    respawn()


def playGround():
    tonnel()

    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, playground"
    print(cur_time)

    pydirectinput.keyDown('w')
    time.sleep(6)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(9)
    pydirectinput.keyUp('d')
    time.sleep(50)

    respawn()


def school():
    tonnel()

    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, school"
    print(cur_time)

    pydirectinput.keyDown('w')
    time.sleep(20)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(9)
    pydirectinput.keyUp('d')
    time.sleep(50)

    respawn()


def beach():
    tonnel()

    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, beach"
    print(cur_time)

    pydirectinput.keyDown('w')
    time.sleep(21)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(3)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('d')
    time.sleep(3)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(1.17)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(16)
    pydirectinput.keyUp('d')

    time.sleep(52)

    respawn()


def salon():
    tonnel()

    d = datetime.datetime.now()
    cur_time = f"{d.hour}:{d.minute}:{d.second}, salon"
    print(cur_time)

    pydirectinput.keyDown('w')
    time.sleep(5)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(7.7)
    pydirectinput.keyUp('a')
    pydirectinput.keyDown('s')
    time.sleep(2)
    pydirectinput.keyUp('s')
    time.sleep(52)

    respawn()


def commands():
    time.sleep(3)
    while True:

        time.sleep(2)
        drink()

        time.sleep(2)
        eat()

        time.sleep(2)
        sleep()

        time.sleep(2)
        bath()

        time.sleep(2)
        pizza()

        time.sleep(2)
        playGround()

        time.sleep(2)
        school()

        time.sleep(2)
        beach()

        time.sleep(2)
        salon()



root = tkinter.Tk()
root.title("MIROSXWBR'S BOT")
root.geometry("500x150")

btn = tkinter.Button(text="Запустить бота", command=commands, width=100, height=5)
btn.pack(padx=120, pady=50)

root.mainloop()