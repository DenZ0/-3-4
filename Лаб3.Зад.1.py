from tkinter import *
languages = [("Молоко",1 ), ("Масло Подсолнечное", 2), 
("Чай", 3), ("Шоколад", 4),
("Порошок", 5), ("Пиво", 6)]
def select():
    l = language.get()
    if l == 1:
     sel.config(text="Цена: 60 руб.")
    elif l == 2:
     sel.config(text="Цена: 100 руб.")
    elif l == 3:
     sel.config(text="Цена: 110 руб.")
    elif l == 4:
     sel.config(text="Цена: 90 руб.")
    elif l == 5:
     sel.config(text="Цена: 320 руб.")
    elif l == 6:
     sel.config(text="Цена: 150 руб.") 

root = Tk()
root.title("Список товаров")
root.geometry("520x385")
root["bg"] = "Snow"
header = Label(text="Выберите товар", padx=15, pady=10,  bg='Snow',font= "10",)
header.grid(row=0, column=0, sticky=W)
language = IntVar()
row = 1
for txt, val in languages:
	Radiobutton(text=txt, value=val, variable=language, padx=15, pady=10, bg='Snow', command=select)\
    	.grid(row=row, sticky=W)
	row += 1
sel = Label(padx=15, pady=10 )
sel.grid(row=row, sticky=W)

root.mainloop()