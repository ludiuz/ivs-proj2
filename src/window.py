from tkinter import *
from calculator import Calculator


class Formula:
    def __init__(self):
        self._inp = StringVar()
        self._inp.set("")
        self.res = StringVar()
        self.res.set("")

    def btn_clicked(self, input):
        # print(input)
        # self._inp.set(input)
        # print(self._inp.get())

        if input == "del":
            a = self._inp.get()
            b = a[0 : len(a) - 1]
            self._inp.set(b)
            result = calc(self._inp.get())
            self.res.set(result)
        elif input == "=":
            pass

        else:
            self._inp.set(self._inp.get() + input)
            result = calc(self._inp.get())
            self.res.set(result)
            # self.res = self.res.set(calc(str(self._inp.get())))
            # print(res)


window = Tk()
form = Formula()
calc = Calculator()
window.geometry("360x800")
window.configure(bg="#fcfcfc")
entry = Entry(window, width=35, borderwidth=5)
entry.place(x=270, y=620, width=90, height=180)
canvas = Canvas(
    window,
    bg="#fcfcfc",
    height=800,
    width=360,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

img0 = PhotoImage(file=f"icons\img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("="),
    relief="flat",
)

b0.place(x=270, y=620, width=90, height=180)

img1 = PhotoImage(file=f"icons\img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("%"),
    relief="flat",
)

b1.place(x=0, y=710, width=90, height=90)

img2 = PhotoImage(file=f"icons\img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("0"),
    relief="flat",
)

b2.place(x=90, y=710, width=90, height=90)

img3 = PhotoImage(file=f"icons\img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("."),
    relief="flat",
)

b3.place(x=180, y=710, width=90, height=90)

img4 = PhotoImage(file=f"icons\img4.png")
b4 = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("1"),
    relief="flat",
)

b4.place(x=0, y=620, width=90, height=90)

img5 = PhotoImage(file=f"icons\img5.png")
b5 = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("2"),
    relief="flat",
)

b5.place(x=90, y=620, width=90, height=90)

img6 = PhotoImage(file=f"icons\img6.png")
b6 = Button(
    image=img6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("3"),
    relief="flat",
)

b6.place(x=180, y=620, width=90, height=90)

img7 = PhotoImage(file=f"icons\img7.png")
b7 = Button(
    image=img7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("4"),
    relief="flat",
)

b7.place(x=0, y=530, width=90, height=90)

img8 = PhotoImage(file=f"icons\img8.png")
b8 = Button(
    image=img8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("5"),
    relief="flat",
)

b8.place(x=90, y=530, width=90, height=90)

img9 = PhotoImage(file=f"icons\img9.png")
b9 = Button(
    image=img9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("6"),
    relief="flat",
)

b9.place(x=180, y=530, width=90, height=90)

img10 = PhotoImage(file=f"icons\img10.png")
b10 = Button(
    image=img10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("7"),
    relief="flat",
)

b10.place(x=0, y=440, width=90, height=90)

img11 = PhotoImage(file=f"icons\img11.png")
b11 = Button(
    image=img11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("8"),
    relief="flat",
)

b11.place(x=90, y=440, width=90, height=90)

img12 = PhotoImage(file=f"icons\img12.png")
b12 = Button(
    image=img12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("9"),
    relief="flat",
)

b12.place(x=180, y=440, width=90, height=90)

img13 = PhotoImage(file=f"icons\img13.png")
b13 = Button(
    image=img13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("("),
    relief="flat",
)

b13.place(x=0, y=350, width=90, height=90)

img14 = PhotoImage(file=f"icons\img14.png")
b14 = Button(
    image=img14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked(")"),
    relief="flat",
)

b14.place(x=90, y=350, width=90, height=90)

img15 = PhotoImage(file=f"icons\img15.png")
b15 = Button(
    image=img15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("/"),
    relief="flat",
)

b15.place(x=180, y=350, width=90, height=90)

img16 = PhotoImage(file=f"icons\img16.png")
b16 = Button(
    image=img16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("^"),
    relief="flat",
)

b16.place(x=0, y=260, width=90, height=90)

img17 = PhotoImage(file=f"icons\img17.png")
b17 = Button(
    image=img17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("odm"),
    relief="flat",
)

b17.place(x=90, y=260, width=90, height=90)

img18 = PhotoImage(file=f"icons\img18.png")
b18 = Button(
    image=img18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("!"),
    relief="flat",
)

b18.place(x=180, y=260, width=90, height=90)

img19 = PhotoImage(file=f"icons\img19.png")
b19 = Button(
    image=img19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("+"),
    relief="flat",
)

b19.place(x=270, y=530, width=90, height=90)

img20 = PhotoImage(file=f"icons\img20.png")
b20 = Button(
    image=img20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("-"),
    relief="flat",
)

b20.place(x=270, y=440, width=90, height=90)

img21 = PhotoImage(file=f"icons\img21.png")
b21 = Button(
    image=img21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("*"),
    relief="flat",
)

b21.place(x=270, y=350, width=90, height=90)

img22 = PhotoImage(file=f"icons\img22.png")
b22 = Button(
    image=img22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("del"),
    relief="flat",
)

b22.place(x=270, y=260, width=90, height=90)

entry0_img = PhotoImage(file=f"icons\img_textBox0.png")
entry0_bg = canvas.create_image(180.0, 218.5, image=entry0_img)

entry0 = Entry(bd=0, bg="#fcfcfc", textvariable=form.res, highlightthickness=0)

entry0.place(x=15, y=190, width=330, height=55)

entry1_img = PhotoImage(file=f"icons\img_textBox1.png")
entry1_bg = canvas.create_image(180.0, 137.5, image=entry1_img)

entry1 = Entry(bd=0, bg="#fcfcfc", textvariable=form._inp, highlightthickness=0)

entry1.place(x=15, y=85, width=330, height=103)

img23 = PhotoImage(file=f"icons\img23.png")
b23 = Button(
    image=img23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("hist"),
    relief="flat",
)

b23.place(x=0, y=46, width=181, height=41)

img24 = PhotoImage(file=f"icons\img24.png")
b24 = Button(
    image=img24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: form.btn_clicked("adv"),
    relief="flat",
)

b24.place(x=179, y=46, width=181, height=41)

window.resizable(False, False)
window.mainloop()
