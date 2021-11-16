import tkinter as tk
from tkinter import *
from tkinter import ttk


from tkinter import messagebox

import requests


root = tk.Tk()
root.geometry("700x270")
root.title("Currency Converter")

root.maxsize(700,350)

def show_data():
    try:
        amount = E1.get()
        from_currency = c1.get()
        to_currency = c2.get()
        url = 'http://api.currencylayer.com/live?access_key=4273d2c37f738367f08780b934ce7dda&format=1'

        if amount == '':
            messagebox.showerror("Currency Converter", "please Fill the Amount")

        elif to_currency == '':
            messagebox.showerror("Currency Converter", "please choose the Currency")

        else:
            data = requests.get(url).json() 
            currency = from_currency.strip()+to_currency.strip()
            amount = int(amount) 
            cc = data['quotes'][currency]
            cur_conv = cc*amount 
            E2.insert(0,cur_conv)

            text.insert('end',f'{amount} united state Dollar Equals {cur_conv} {to_currency} \n\n ')
    except requests.ConnectionError:
        messagebox.showerror("Error", "No internet Connection!!!")
    
    except:
        messagebox.showerror("Error", "Opps!!! Something went wrong:(.")

def clear():
     E1.delete(0,'end')
     E2.delete(0,'end')
     text.delete(1.0,'end')

l1 = Label(root,text="USD Currency Converter Using Python", font=('verdana',10,'bold'))
l1.place(x=150,y=15)

amt = Label(root,text="Amount",font=('roboto',10,'bold'))
amt.place(x=20,y=15)
E1 = Entry(root,width=20,borderwidth=1,font=('roboto',10,'bold'))
E1.place(x=20,y=40)

c1 = tk.StringVar()
c2 = tk.StringVar()
currencychoose1 = ttk.Combobox(root, width = 20, textvariable = c1, state = 'readonly',font=('verdana',10,'bold'))

currencychoose1['values'] = ('USD',)

currencychoose1.place(x=300,y=40)

currencychoose1.current(0)

E2 = Entry(root,width=20,borderwidth=1,font=('roboto',10,'bold'))
E2.place(x=20,y=80)

currencychoose2 = ttk.Combobox(root, width = 20, textvariable = c2, state = 'readonly',font=('verdana',10,'bold'))

currencychoose2['values'] = ('INR',
                             'EUR',
                             'CAD',
                             'AFN',
                                  )

currencychoose2.place(x=300,y=80)

currencychoose2.current()

text = Text(root,height=7,width=52,font=('verdana','10','bold'))

text.place(x=100,y=120)

B = Button(root,text="Search",command=show_data,font=('verdana','10','bold'),activeforeground='#0CF566',bg="#0CF566",activebackground="white",fg="white")
B.place(x=20,y=120)

clear = Button(root,text="clear",command=clear,font=('verdana',10,'bold'),activebackground='red',)
clear.place(x=20,y=170)

root.mainloop()