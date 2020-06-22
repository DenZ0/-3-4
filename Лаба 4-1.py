from tkinter import *
root = Tk()
root["bg"] = "midnight blue"
label_color = "royal blue"
root.minsize(660, 420)
root.title('Парикмахерская')

surname = StringVar()
surname_to_delete = StringVar()
surname_to_find = StringVar()
date = StringVar()
date_to_find = StringVar()
service = StringVar()
price = IntVar()
dropdown_key = StringVar(root)
dropdown_key.set('Фамилия')
dropdown_value = StringVar(root)
dropdown_value.set('Услуга')
variables = [('Фамилия', surname), ('Дата', date), ('Услуга', service), ('Цена', price)]
variables2 = [('Поиск по фамилии', surname_to_find), ('Поиск по дате', date_to_find)]
def create_form(*attributes):
    label, var, row_count = attributes
    Label(text=label, bg=label_color).grid(row=row_count, column=0, sticky='w')
    Entry(textvariable=var).grid(row=row_count,column=1, padx=5, pady=5)
row_count = 0
for label, var in variables:
    create_form(label, var, row_count)
    row_count += 1
Button(text="Добавить клиента", font=("Times New Roman", 11)).grid(row=4,column=0, padx=5, pady=5, sticky="e")
Button(text="Добавить значение клиенту",font=("Times New Roman", 11)).grid(row=4,column=1, padx=5, pady=5, sticky="e")

Label(text=variables[0][0], bg=label_color).grid(row=0, column=3, sticky='w')
Entry(textvariable=surname_to_delete).grid(row=0,column=4, padx=5, pady=5)
Button(text="Удалить клиента",font=("Times New Roman", 11)).grid(row=1,column=4, padx=5, pady=5, sticky="e")

row_count = 5
for label, var in variables2:
    create_form(label, var, row_count)
    row_count += 1

Button(text="Найти",font=("Times New Roman", 11)).grid(row=10,column=0, padx=5, pady=5, sticky="e")
OptionMenu(root, dropdown_key, '').grid(row=2,column=3, padx=5, pady=5)
OptionMenu(root, dropdown_value, '').grid(row=2,column=4, padx=5, pady=5)
Button(text="Удалить запись",font=("Times New Roman", 11)).grid(row=3,column=4, padx=5, pady=5, sticky="e")
Label(text="Клиенты за сутки", bg=label_color,font=("Times New Roman", 11)).grid(row=4, column=4, sticky='e')
Button(text="Показать",font=("Times New Roman", 11)).grid(row=5,column=4, padx=5, pady=5, sticky="e")
root.mainloop()