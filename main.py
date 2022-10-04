from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operator = ''
food_price = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_price = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_price = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_button(character):
    global operator
    operator = operator + character
    calculator_display.delete(0,END)
    calculator_display.insert(END,operator)

def delete_all():
    global operator
    operator =''
    calculator_display.delete(0,END)

def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0,END)
    calculator_display.insert(0,result)
    operator = ''

def review_check():
    x = 0
    for b in food_box:
        if food_variables[x].get() ==1:
            food_box[x].config(state=NORMAL)
            if food_box[x].get() == 0:
                food_box.delete(0,END)
            food_box[x].focus()
        else:
            food_box[x].config(state=DISABLED)
            food_text[x].set('0')
        x += 1

    x = 0
    for b in drink_box:
        if drink_variables[x].get() == 1:
            drink_box[x].config(state=NORMAL)
            if drink_box[x].get() == 0:
                drink_box.delete(0, END)
            drink_box[x].focus()
        else:
            drink_box[x].config(state=DISABLED)
            drink_text[x].set('0')
        x += 1

    x = 0
    for b in dessert_box:
        if dessert_variables[x].get() == 1:
            dessert_box[x].config(state=NORMAL)
            if dessert_box[x].get() == 0:
                dessert_box.delete(0, END)
            dessert_box[x].focus()
        else:
            dessert_box[x].config(state=DISABLED)
            dessert_text[x].set('0')
        x += 1


def total_calculation():
    food_subtotal = 0
    p = 0
    for unit in food_text:
        food_subtotal = food_subtotal + (float(unit.get()) * food_price[p])
        p += 1


    drink_subtotal = 0
    p = 0
    for unit in drink_text:
        drink_subtotal = drink_subtotal + (float(unit.get()) * drink_price[p])
        p += 1


    dessert_subtotal = 0
    p = 0
    for unit in dessert_text:
        dessert_subtotal = dessert_subtotal + (float(unit.get()) * dessert_price[p])
        p += 1

    my_subtotal = food_subtotal + drink_subtotal + dessert_subtotal
    my_taxes = my_subtotal * 0.11
    my_total = my_subtotal + my_taxes

    food_cost_var.set(f'£ {round(food_subtotal,2)}')
    drink_cost_var.set(f'£ {round(drink_subtotal,2)}')
    dessert_cost_var.set(f'£ {round(dessert_subtotal,2)}')
    subtotal_var.set(f'£ {round(my_subtotal,2)}')
    taxes_var.set(f'£ {round(my_taxes,2)}')
    total_var.set(f'£ {round(my_total,2)}')

def create_invoice():
    invoice_text.delete(1.0, END)
    invoice_number = f'N# - {random.randint(1000,9999)}'
    my_date = datetime.datetime.now()
    invoice_date = f'{my_date.day}/{my_date.month}/{my_date.year} - {my_date.hour}:{my_date.minute}'
    invoice_text.insert(END, f'Information: \t{invoice_number}\t\t{invoice_date}\n')
    invoice_text.insert(END, f'*' * 63 + '\n')
    invoice_text.insert(END, f'Items\t\tQuantity\t\tItems Cost\n')
    invoice_text.insert(END, f'-' * 75 + '\n')

    x = 0
    for f in food_text:
        if f.get() != '0':
            invoice_text.insert(END,f'{food_list[x]}\t\t{f.get()}\t\t£ {int(f.get()) * food_price[x]}\n')
        x += 1

    x = 0
    for d in drink_text:
        if d.get() != '0':
            invoice_text.insert(END,f'{drink_list[x]}\t\t{d.get()}\t\t£ {int(d.get()) * drink_price[x]}\n')
        x += 1

    x = 0
    for de in dessert_text:
        if de.get() != '0':
            invoice_text.insert(END, f'{dessert_list[x]}\t\t{de.get()}\t\t£ {int(de.get()) * dessert_price[x]}\n')
        x += 1
    invoice_text.insert(END, f'*' * 63 + '\n')
    invoice_text.insert(END,f'Food Subtotal: \t\t\t{food_cost_var.get()}\n')
    invoice_text.insert(END, f'Drink Subtotal: \t\t\t{drink_cost_var.get()}\n')
    invoice_text.insert(END, f'Dessert Subtotal: \t\t\t{dessert_cost_var.get()}\n')
    invoice_text.insert(END, f'-' * 75 + '\n')
    invoice_text.insert(END, f'Subtotal: \t\t\t{subtotal_var.get()}\n')
    invoice_text.insert(END, f'Taxes: \t\t\t{taxes_var.get()}\n')
    invoice_text.insert(END, f'Total: \t\t\t{total_var.get()}\n')
    invoice_text.insert(END, f'*' * 63 + '\n')
    invoice_text.insert(END, f'See you soon')

def save_invoice():
    invoice_info = invoice_text.get(1.0, END)
    my_file = filedialog.asksaveasfile(mode= 'w', defaultextension='.txt')
    my_file.write(invoice_info)
    my_file.close()
    messagebox.showinfo('Notification', ' Your invoice has been saved!')

def reset_all():
    invoice_text.delete(0.1,END)

    for text in food_text:
        text.set('0')
    for text in drink_text:
        text.set('0')
    for text in dessert_text:
        text.set('0')

    for box in food_box:
        box.config(state=DISABLED)
    for box in drink_box:
        box.config(state=DISABLED)
    for box in dessert_box:
        box.config(state=DISABLED)

    for var in food_variables:
        var.set(0)
    for var in drink_variables:
        var.set(0)
    for var in dessert_variables:
        var.set(0)

    food_cost_var.set('')
    drink_cost_var.set('')
    dessert_cost_var.set('')
    subtotal_var.set('')
    taxes_var.set('')
    total_var.set('')




#Initialise tkinter
application = Tk()

application.geometry('1020x720+0+0')

application.resizable(True, True)

#Set title
application.title('My Restaurant - Invoicing system')

#Background colorr
application.config(bg='burlywood2')

#top panel
top_panel = Frame(application, bd=1, relief=FLAT)

top_panel.pack(side=TOP)

#Title tag
title_tag = Label(top_panel,
                  text='Invoicing System',
                  fg='azure4',
                  font=('Dosis', 58),
                  bg='burlywood',
                  width=27)
title_tag.grid(row=0, column=0)

left_panel = Frame(application,bd=1,relief=FLAT)
left_panel.pack(side=LEFT)

cost_panel = Frame(left_panel,bd=1,relief=FLAT, bg='azure4',padx=115)
cost_panel.pack(side=BOTTOM)

food_panel = LabelFrame(left_panel,text='Food',font = ('Dosis',19,'bold'),bd=1,relief=FLAT,fg='azure4')
food_panel.pack(side=LEFT)

drink_panel = LabelFrame(left_panel,text='Drink',font = ('Dosis',19,'bold'),bd=1,relief=FLAT,fg='azure4')
drink_panel.pack(side=LEFT)

dessert_panel = LabelFrame(left_panel,text='Dessert',font = ('Dosis',19,'bold'),bd=1,relief=FLAT,fg='azure4')
dessert_panel.pack(side=LEFT)

right_panel = Frame(application,bd=1,relief=FLAT)
right_panel.pack(side=RIGHT)

calculator_panel = Frame(right_panel,bd=1,relief=FLAT,bg='burlywood')
calculator_panel.pack()

invoice_panel = Frame(right_panel,bd=1,relief=FLAT,bg='burlywood')
invoice_panel.pack()

buttons_panel = Frame(right_panel,bd=1,relief=FLAT,bg='burlywood')
buttons_panel.pack()

food_list = ['Chicken','Lamb','Salmon','Hake','Kebab','Pizza1','Pizza2','Pizza3']
drink_list = ['Apple Juice','Orange Juice','Lemonade','Sprite','Coke','Vimto','Tango','Water']
dessert_list = ['Pear','Ice cream','Fruit','Brownies','Pudding','Cheesecake','Cake1','Cake2']


#Create the drink items
drink_variables = []
drink_box = []
drink_text =[]
counter = 0
for drink in drink_list:
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel,text= drink.title(),font=('Dosis',19,'bold'),
                       onvalue=1,offvalue=0,variable=drink_variables[counter],command=review_check)
    drink.grid(row= counter,column=0, sticky=W)

    drink_box.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_box[counter] = Entry(drink_panel,
                              font=('Dosis', 18, 'bold'),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=drink_text[counter])
    drink_box[counter].grid(row=counter,
                           column=1)
    counter += 1

food_variables = []
food_box = []
food_text =[]
counter = 0
for food in food_list:
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel,text= food.title(),font=('Dosis',19,'bold'),
                       onvalue=1,offvalue=0,variable=food_variables[counter],command=review_check)
    food.grid(row= counter,column=0, sticky=W)

    food_box.append('')
    food_text.append('')
    food_text[counter]=StringVar()
    food_text[counter].set('0')
    food_box[counter] = Entry(food_panel,
                              font=('Dosis',18,'bold'),
                              bd=1,
                              width = 6,
                              state = DISABLED,
                              textvariable = food_text[counter])
    food_box[counter].grid(row=counter,
                           column=1)
    counter += 1

dessert_variables = []
dessert_box = []
dessert_text =[]
counter = 0
for dessert in dessert_list:
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel,text= dessert.title(),font=('Dosis',19,'bold'),
                       onvalue=1,offvalue=0,variable=dessert_variables[counter],command=review_check)
    dessert.grid(row= counter,column=0, sticky=W)

    dessert_box.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_box[counter] = Entry(dessert_panel,
                              font=('Dosis', 18, 'bold'),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=dessert_text[counter])
    dessert_box[counter].grid(row=counter,
                           column=1)
    counter += 1

subtotal_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()
food_cost_var = StringVar()
food_cost_label = Label(cost_panel,
                        text='Food Cost',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
food_cost_label.grid(row=0,column=0)
food_cost_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=food_cost_var)
food_cost_text.grid(row=0,column=1,padx=41)


drink_cost_var = StringVar()
drink_cost_label = Label(cost_panel,
                        text='Drink Cost',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
drink_cost_label.grid(row=1,column=0)
drink_cost_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=drink_cost_var)
drink_cost_text.grid(row=1,column=1,padx=41)


dessert_cost_var = StringVar()
dessert_cost_label = Label(cost_panel,
                        text='Dessert Cost',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
dessert_cost_label.grid(row=2,column=0)
dessert_cost_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2,column=1,padx=41)

subtotal_label = Label(cost_panel,
                        text='Subtotal',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
subtotal_label.grid(row=0,column=2)
subtotal_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=subtotal_var)
subtotal_text.grid(row=0,column=3, padx=41)

taxes_label = Label(cost_panel,
                        text='Taxes',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
taxes_label.grid(row=1,column=2)
taxes_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=taxes_var)
taxes_text.grid(row=1,column=3, padx=41)

total_label = Label(cost_panel,
                        text='Total',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
total_label.grid(row=2,column=2)
total_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=total_var)
total_text.grid(row=2,column=3, padx=41)

#Buttons
buttons = ['total','invoice','save','reset']
created_buttons = []
column = 0
for button in buttons:
    button = Button(buttons_panel,
                    text=button.title(),
                    font = ('Dosis',13,'bold'),
                    fg = 'white',
                    bg='azure4',
                    bd=1,
                    width=9)

    created_buttons.append(button)
    button.grid(row=0,column=column)
    column +=1

created_buttons[0].config(command=total_calculation)
created_buttons[1].config(command=create_invoice)
created_buttons[2].config(command=save_invoice)
created_buttons[3].config(command=reset_all)

invoice_text = Text(invoice_panel,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=42,
                    height=10)
invoice_text.grid(row=0,column=0)


#Calculator
calculator_display = Entry(calculator_panel,
                           font=('Dosis',16,'bold'),
                           width =32,
                           bd=1)
calculator_display.grid(row=0,columnspan=4)

calculator_buttons = ['7','8','9','+',
                      '4','5','6','-',
                      '1','2','3','x',
                      'CE','Delete','0','/']

stored_buttons = []

my_row=1
my_column = 0

for button in calculator_buttons:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=('Dosis',16,'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=8)

    stored_buttons.append(button)

    button.grid(row=my_row,
                column=my_column)
    if my_column == 3:
        my_row +=1

    my_column +=1
    if my_column == 4:
        my_column=0

stored_buttons[0].config(command=lambda: click_button('7'))
stored_buttons[1].config(command=lambda: click_button('8'))
stored_buttons[2].config(command=lambda: click_button('9'))
stored_buttons[3].config(command=lambda: click_button('+'))
stored_buttons[4].config(command=lambda: click_button('4'))
stored_buttons[5].config(command=lambda: click_button('5'))
stored_buttons[6].config(command=lambda: click_button('6'))
stored_buttons[7].config(command=lambda: click_button('-'))
stored_buttons[8].config(command=lambda: click_button('1'))
stored_buttons[9].config(command=lambda: click_button('2'))
stored_buttons[10].config(command=lambda: click_button('3'))
stored_buttons[11].config(command=lambda: click_button('*'))
stored_buttons[12].config(command=lambda: get_result())
stored_buttons[13].config(command=lambda: delete_all())
stored_buttons[14].config(command=lambda: click_button('0'))
stored_buttons[15].config(command=lambda: click_button('/'))




#Prevent window closing
application.mainloop()