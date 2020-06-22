from tkinter import *

OPTIONS = [
"Мажитэль Арбуз-Дыня",
"Мажитэль Персик-Маракуйя",
"Мажитэль Клубника",
"Мажитэль Мульти-Фрукт",
"Мажитэль Груша-Манго",
"Мажитэль Пина-Колада",
] #etc

master = Tk()
master.title("Выбор вкуса")
master.geometry("450x275")
master["bg"] = "midnight blue"
variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

mainloop()