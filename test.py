

import tkinter as tk
from tkinter import messagebox



label_font = ('ArialBlack', 11, 'bold')
entry_font = ('ArialBlack', 12, 'bold')
btn_font = ('Elephant', 12, 'bold')

class OnlineRestaruant(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        self.frames = {}
        for F in (LoginPage, MainPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#41588E')


        username_label = tk.Label(self, text='Имя пользователя', font=label_font,
                                  bg='#AC1876',fg='#F0EAD6')
        username_label.place(x=30,y=100,width=150,height=20)
        self.controller.configure(background='#334353')

        self.username_entry = tk.Entry(self, bg='#E8F48C', fg='#536872', font=entry_font)
        self.username_entry.place(x=190,y=100,width=150,height=20)


        password_label = tk.Label(self, text='Пароль', font=label_font,
                                  bg='#AC1876',fg='#F0EAD6')
        password_label.place(x=30,y=200,width=150,height=20)


        self.password_entry = tk.Entry(self, show='*', bg='#E8F48C', fg='#536872', font=entry_font)
        self.password_entry.place(x=190,y=200,width=150,height=20)


        self.send_btn = tk.Button(self, text='Войти', bg='#FF003F',
                                  activebackground='#F4CA16',
                                  command=lambda: self.check_password(),
                                  font=btn_font)
        self.send_btn.place(x=100,y=250,width=200,height=25)

    def check_password(self):
        if self.password_entry.get() == "0" and self.username_entry.get() == "0":
            self.controller.show_frame("MainPage")
        else:
            messagebox.showinfo("ERROR", "Неверный пароль или логин")


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#035278')

        self.samsa_lbl = tk.Label(self,text='Самса', font=label_font,
                                  bg='#CD5C5C')
        self.samsa_lbl.place(x=160, y=30,height=25)

        self.samsa_btn1 = tk.Button(self, text='С Говядиной', font='bold',  bg='#AC1876',
                                  activebackground='#9C7CF4', width=10,
                                  command=lambda: self.basket_ent.insert(0, "С Говядиной "))
        self.samsa_btn2 = tk.Button(self, text='С Курицей', font='bold',  bg='#AC1876',
                                  activebackground='#9C7CF4', width=10,
                                  command=lambda: self.basket_ent.insert(0, "С Курицей "))
        self.samsa_btn3 = tk.Button(self, text='С Картошкой', font='bold',  bg='#AC1876',
                                  activebackground='#9C7CF4', width=10,
                                  command=lambda: self.basket_ent.insert(0, "С Картошкой "))

        self.samsa_btn1.place(x=20,y=70,width=120,height=25)
        self.samsa_btn2.place(x=145,y=70,width=120,height=25)
        self.samsa_btn3.place(x=270,y=70,width=120,height=25)

        self.vech_lbl = tk.Label(self,text='Блюда', font=label_font,
                                  bg='#CD5C5C')
        self.vech_lbl.place(x=160, y=100,height=25)
        self.vech_btn4 = tk.Button(self, text='Плов', font='bold',  bg='#AC1876',
                                  activebackground='#9C7CF4', width=10,
                                   command=lambda: self.basket_ent.insert(0, "Плов "))
        self.vech_btn5 = tk.Button(self, text='Шурпа', font='bold', bg='#AC1876',
                                  activebackground='#9C7CF4', width=10,
                                   command=lambda: self.basket_ent.insert(0, "Шурпа "))
        self.vech_btn6 = tk.Button(self, text='Манты', font='bold', bg='#AC1876',
                                  activebackground='#9C7CF4', width=10,
                                   command=lambda: self.basket_ent.insert(0, "Манты "))

        self.vech_btn4.place(x=30,y=130,width=100,height=25)
        self.vech_btn5.place(x=140, y=130, width=100, height=25)
        self.vech_btn6.place(x=250, y=130, width=100, height=25)



        self.basket_lbl = tk.Label(self,text='Корзина', font=label_font,
                                  bg='#E884CD')
        self.basket_lbl.place(x=150, y=200,height=25)

        self.location_lbl = tk.Label(self, text='Введите свое место положение', font=label_font,
                                   bg='#02AEC3',fg='#F0EAD6')
        self.location_lbl.place(x=90, y=325, height=25)

        self.order_btn = tk.Button(self, text="Заказать", font='bold',  bg='#FF003F',
                                  activebackground='#F4CA16', width=20,
                                   command=lambda: self.MsgBox())
        self.order_btn.place(x=150, y=420, width=100, height=25)
        self.delet_btn = tk.Button(self, text="Удалить", font='bold',  bg='#3591CD',
                                  activebackground='#20B2AA', width=20,
                                   command=lambda: self.Delete())
        self.delet_btn.place(x=150, y=290, width=100, height=25)

        self.basket_ent = tk.Entry(self,  font=label_font,
                                  bg='#3591CD')
        self.basket_ent.place(x=20,y=230,width=350,height=50)

        self.location_ent = tk.Entry(self,  font=label_font,
                                  bg='#E8F48C', fg='#536872')
        self.location_ent.place(x=20,y=360,width=350,height=50)

    def MsgBox(self):
        messagebox.showinfo("Заказ принят!",  self.location_ent.get())

    def Delete(self):
        self.basket_ent.delete(0, tk.END)


if __name__ == "__main__":
    app = OnlineRestaruant()


    app.geometry("400x500")
    app.resizable(False, False)

    app.grid_columnconfigure(0, minsize=100)
    app.mainloop()