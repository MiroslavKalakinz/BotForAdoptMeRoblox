# version 0.9
import time
import tkinter
import playsound
import tasks

# Запуск
time.sleep(3)
print('Made by MIROSXWBR')

# playsound.playsound('start.mp3', True)




root = tkinter.Tk()
root.title("MIROSXWBR'S BOT")
root.geometry("500x150")

btn = tkinter.Button(text="Запустить бота", command=tasks.commands, width=100, height=5)
btn.pack(padx=120, pady=50)

root.mainloop()
