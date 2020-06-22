from tkinter import *
root = Tk()
root.title("Меню")
root.geometry("450x275")
root["bg"] = "midnight blue"
main_menu = Menu()

file_menu = Menu(font=("Times New Roman", 14),activebackground= "Coral", activeborderwidth= 3)
file_menu.add_command(label="Новый")
file_menu.add_command(label="Открыть...")
file_menu.add_command(label="Сохранить...")
file_menu.add_command(label="Выход")
file_menu.add_separator()

help_menu = Menu(font=("Times New Roman", 14),activebackground= "Coral", activeborderwidth= 3)
help_menu.add_command(label="Помощь")
help_menu.add_command(label="О программе")
help_menu.add_command(label="Поддержать автора денюжкой")
help_menu.add_separator()

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Справка" ,menu=help_menu)
root.config(menu=main_menu)
root.mainloop()