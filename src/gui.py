from tkinter import *
from calculator import Calculator
import os


def run_gui():
    """
    This function initialiazes the calculator GUI, by creating new class Formula and setting
    up new window with entry field and buttons. This class handles all the button clicks and key
    presses by updating the input and result field accordingly.

    :return: None 
    """
    # Create new class
    class Formula:
        def __init__(self):
            """
            Initialization of variables self._inp and self.res
            """
            self._inp = StringVar()
            self._inp.set("")
            self.res = StringVar()
            self.res.set("")

        def btn_clear(self):
            """
            Clears entry after holding clear button in GUI
            """
            self.res.set("")
            self._inp.set("")

        def btn_clicked(self, input):
            """
            This method handles button clicks and updates the input field and result field accordingly.
    
            :param input: str, the value of the button that was clicked
            """
            if input == "del":
                pom = self._inp.get()
                cursor_pos = entry1.index(INSERT)
                if cursor_pos == 0:
                    return
                self._inp.set(pom[: cursor_pos - 1] + pom[cursor_pos:])
                entry1.icursor(cursor_pos - 1)
                if pom == "":
                    self.res.set("")
                    return
                result = calc(self._inp.get())
                self.res.set(result)
            elif input == "=":
                result = calc(self._inp.get())
                self._inp.set(result)
                self.res.set("")
                entry1.icursor(END)
            elif input == "odm":
                pom = self._inp.get()
                pom = "(" + pom + ")^(1/)"
                self._inp.set(pom)
                result = calc(self._inp.get())
                self.res.set(result)

            else:
                cursor_pos = entry1.index(INSERT)
                pom = self._inp.get()
                self._inp.set(pom[:cursor_pos] + input + pom[cursor_pos:])
                entry1.icursor(cursor_pos + 1)
                result = calc(self._inp.get())
                self.res.set(result)

        def on_key_press(self, event):
            """
            Updates the formula input and result based on the current input
            
            :param event: The key press event.
            :type event: tkinter.Event
            """
            self._inp.set(self._inp.get())
            result = calc(self._inp.get())
            self.res.set(result)

    window = Tk()
    # create an instance of the Formula class
    form = Formula()
    # create an instance of the Calculator class
    calc = Calculator()
    res = calc("5+*-")

    # create an interface of GUI
    window.geometry("360x800")
    window.title("Calculator")
    icon = PhotoImage(file="./src/icons/icon64x64.png")
    window.iconphoto(True, icon)
    #window.iconbitmap("./src/icons/icon64x64.ico")
    window.configure(bg="#fcfcfc")
    window.resizable(False, False)
    

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

    # create a label to display the calculation result
    label_resoult = Label(
        anchor="e",
        font=("Arial", 18),
        bd=0,
        bg="#fcfcfc",
        textvariable=form.res,
        highlightthickness=0,
    )
    # disable label to user input
    label_resoult.config(state="disabled")
    label_resoult.place(x=15, y=190, width=330, height=55)

    # create an image for input
    entry1_img = PhotoImage(file="./src/icons/img_textBox1.png")
    entry1_bg = canvas.create_image(180.0, 137.5, image=entry1_img)

    entry1 = Entry(
        font=("Arial", 22),
        justify="right",
        bd=0,
        bg="#fcfcfc",
        textvariable=form._inp,
        highlightthickness=0,
    )

    entry1.place(x=15, y=85, width=330, height=103)
    # Bind the "Key" event to the "on_key_press" method of the form object using a lambda function
    entry1.bind("<Key>", lambda event: window.after(10, form.on_key_press, event))
    # Create a background image for the entry box
    entry0_img = PhotoImage(file="./src/icons/img_textBox0.png")
    entry0_bg = canvas.create_image(180.0, 218.5, image=entry0_img)

    # Create a background image for '='
    img0 = PhotoImage(file="./src/icons/img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("="),
        relief="flat",
    )

    b0.place(x=270, y=620, width=90, height=180)

    # Create a background image for '%'
    img1 = PhotoImage(file="./src/icons/img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("%"),
        relief="flat",
    )

    b1.place(x=0, y=710, width=90, height=90)

    # Create a background image for '0'
    img2 = PhotoImage(file="./src/icons/img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("0"),
        relief="flat",
    )

    b2.place(x=90, y=710, width=90, height=90)

    # Create a background image for '.'
    img3 = PhotoImage(file="./src/icons/img3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("."),
        relief="flat",
    )

    b3.place(x=180, y=710, width=90, height=90)

    # Create a background image for '1'
    img4 = PhotoImage(file="./src/icons/img4.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("1"),
        relief="flat",
    )

    b4.place(x=0, y=620, width=90, height=90)

    # Create a background image for '2'
    img5 = PhotoImage(file="./src/icons/img5.png")
    b5 = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("2"),
        relief="flat",
    )

    b5.place(x=90, y=620, width=90, height=90)

    # Create a background image for '3'
    img6 = PhotoImage(file="./src/icons/img6.png")
    b6 = Button(
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("3"),
        relief="flat",
    )

    b6.place(x=180, y=620, width=90, height=90)

    # Create a background image for '4'
    img7 = PhotoImage(file="./src/icons/img7.png")
    b7 = Button(
        image=img7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("4"),
        relief="flat",
    )

    b7.place(x=0, y=530, width=90, height=90)

    # Create a background image for '5'
    img8 = PhotoImage(file="./src/icons/img8.png")
    b8 = Button(
        image=img8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("5"),
        relief="flat",
    )

    b8.place(x=90, y=530, width=90, height=90)

    # Create a background image for '6'
    img9 = PhotoImage(file="./src/icons/img9.png")
    b9 = Button(
        image=img9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("6"),
        relief="flat",
    )

    b9.place(x=180, y=530, width=90, height=90)

    # Create a background image for '7'
    img10 = PhotoImage(file="./src/icons/img10.png")
    b10 = Button(
        image=img10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("7"),
        relief="flat",
    )

    b10.place(x=0, y=440, width=90, height=90)

    # Create a background image for '8'
    img11 = PhotoImage(file="./src/icons/img11.png")
    b11 = Button(
        image=img11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("8"),
        relief="flat",
    )

    b11.place(x=90, y=440, width=90, height=90)

    # Create a background image for '9'
    img12 = PhotoImage(file="./src/icons/img12.png")
    b12 = Button(
        image=img12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("9"),
        relief="flat",
    )

    b12.place(x=180, y=440, width=90, height=90)

    # Create a background image for '('
    img13 = PhotoImage(file="./src/icons/img13.png")
    b13 = Button(
        image=img13,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("("),
        relief="flat",
    )

    b13.place(x=0, y=350, width=90, height=90)

    # Create a background image for ')'
    img14 = PhotoImage(file="./src/icons/img14.png")
    b14 = Button(
        image=img14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked(")"),
        relief="flat",
    )

    b14.place(x=90, y=350, width=90, height=90)

    # Create a background image for '/'
    img15 = PhotoImage(file="./src/icons/img15.png")
    b15 = Button(
        image=img15,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("/"),
        relief="flat",
    )

    b15.place(x=180, y=350, width=90, height=90)

    # Create a background image for '^'
    img16 = PhotoImage(file="./src/icons/img16.png")
    b16 = Button(
        image=img16,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("^"),
        relief="flat",
    )

    b16.place(x=0, y=260, width=90, height=90)

    # Create a background image for 'sqr'
    img17 = PhotoImage(file="./src/icons/img17.png")
    b17 = Button(
        image=img17,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("odm"),
        relief="flat",
    )

    b17.place(x=90, y=260, width=90, height=90)

    # Create a background image for '!'
    img18 = PhotoImage(file="./src/icons/img18.png")
    b18 = Button(
        image=img18,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("!"),
        relief="flat",
    )

    b18.place(x=180, y=260, width=90, height=90)

    # Create a background image for '+'
    img19 = PhotoImage(file="./src/icons/img19.png")
    b19 = Button(
        image=img19,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("+"),
        relief="flat",
    )

    b19.place(x=270, y=530, width=90, height=90)

    # Create a background image for '-'
    img20 = PhotoImage(file="./src/icons/img20.png")
    b20 = Button(
        image=img20,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("-"),
        relief="flat",
    )

    b20.place(x=270, y=440, width=90, height=90)

    # Create a background image for 'X'
    img21 = PhotoImage(file="./src/icons/img21.png")
    b21 = Button(
        image=img21,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("*"),
        relief="flat",
    )

    b21.place(x=270, y=350, width=90, height=90)

    def on_button_pressed():
        """
        This function is called when a button is pressed, and checks whether the button is still being pressed after one second.

        :return: None
        """
        if button_pressed:
            form.btn_clear()

    def on_button_release(event):
        """
        This function will be called when the button is released.

        :param event: The event triggered by the button release.
        :type event: tkinter.Event
        """
        global button_pressed
        button_pressed = False

    def on_button_click(event):
        """
        This function will be called when the button is clicked.

        :param event: The event that triggered the button click.
        :type event: tkinter.Event
        """
        global button_pressed
        button_pressed = True
        window.after(1000, on_button_pressed)

    # Create a background image for 'clear'
    img22 = PhotoImage(file="./src/icons/img22.png")
    b22 = Button(
        image=img22,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: form.btn_clicked("del"),
        relief="flat",
    )
    button_pressed = False
    b22.bind("<Button-1>", on_button_click)
    b22.bind("<ButtonRelease-1>", on_button_release)

    b22.place(x=270, y=260, width=90, height=90)

    # Create a background image for 'history'
    img23 = PhotoImage(file="./src/icons/img23.png")
    b23 = Button(image=img23, borderwidth=0, highlightthickness=0, relief="flat")

    b23.place(x=0, y=46, width=181, height=41)

    # Create a background image for 'advanced'
    img24 = PhotoImage(file="./src/icons/img24.png")
    b24 = Button(image=img24, borderwidth=0, highlightthickness=0, relief="flat")

    b24.place(x=179, y=46, width=181, height=41)

    window.resizable(False, False)
    window.mainloop()
