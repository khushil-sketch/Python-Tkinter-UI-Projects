from tkinter import *

root = Tk()
root.title('Cool Calc')

# ENTRY WIDGET
input1 = Entry(root, width=15, font='Calibri 30', bg='#a6a6a6', fg='white')
# input1.grid(row=0,column=0,columnspan=4, padx=20,pady=20)  #padx doesnt increase the height of the Entry Widget. It adjusts its position in the grid.
input1.grid(row=0, column=0, columnspan=3, sticky=W + E)


# BUTTON-ENTRY LINK FUNCTION
def calc_button(cur_number):
    previous = input1.get()  # This grabs the data currently in the text box befoe it is deleted by the method on the next line
    input1.delete(0, END)  # Deletes any value from the 0th index to the last index.
    input1.insert(0, str(previous) + str(
        cur_number))  # Once the data is grabbed, we can now arrange and output it in the correct way.


# CLEAR FUNCTION
def clear_func():
    input1.delete(0, END)


# ADD FUNCTION
def add_func(add):
    global num1
    num1 = input1.get()
    input1.delete(0, END)


# EQUAL FUNCTION
def equal_func(equal):
    global num2
    num2 = input1.get()
    input1.delete(0, END)
    input1.insert(0, int(num1) + int(num2))
    # label=Label(text=)


# BUTTON WIDGETS
button1 = Button(root, text='1', padx=40, pady=15, border=0.5, bg='#333333', fg='white', font='Calibri 15',
                 command=lambda: calc_button(1))
button2 = Button(root, text='2', padx=40, pady=15, border=0.5, bg='#333333', fg='white', font='Calibri 15',
                 command=lambda: calc_button(2))
button3 = Button(root, text='3', padx=40, pady=15, border=0.5, bg='#333333', fg='white', font='Calibri 15',
                 command=lambda: calc_button(3))
button4 = Button(root, text='4', padx=40, pady=15, border=0.5, bg='#333333', fg='white', font='Calibri 15',
                 command=lambda: calc_button(4))
button5 = Button(root, text='5', padx=40, pady=15, border=0.5, bg='#333333', fg='white', font='Calibri 15',
                 command=lambda: calc_button(5))
button6 = Button(root, text='6', padx=40, pady=15, border=0.5, bg='#333333', fg='white', font='Calibri 15',
                 command=lambda: calc_button(6))
button7 = Button(root, text='7', padx=40, pady=15, border=0.5, bg='#333333', fg='white', font='Calibri 15',
                 command=lambda: calc_button(7))
button8 = Button(root, text='8', padx=40, pady=15, border=0.5, bg='#333333', fg='white', font='Calibri 15',
                 command=lambda: calc_button(8))
button9 = Button(root, text='9', padx=40, pady=15, border=0.5, bg='#333333', fg='white', font='Calibri 15',
                 command=lambda: calc_button(9))
button0 = Button(root, text='0', padx=40, pady=15, border=0.5, bg='#333333', fg='white', font='Calibri 15',
                 command=lambda: calc_button(0))
clear_b = Button(root, text='DEL', padx=80, pady=15, border=0.5, bg='#4d4d4d', fg='white', font='Calibri 15',
                 command=clear_func)  # No need for lambda since no parameter being given
equal_b = Button(root, text='=', padx=90, pady=15, border=0.5, bg='#cc0000', fg='white', font='Calibri 15',
                 command=lambda: equal_func('='))
add_b = Button(root, text='+', padx=40, pady=15, border=0.5, bg='#4d4d4d', fg='white', font='Calibri 15',
               command=lambda: add_func('+'))
###################
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
clear_b.grid(row=4, column=1, columnspan=2)
equal_b.grid(row=5, column=1, columnspan=2)
add_b.grid(row=5, column=0)

# Leave it
root.mainloop()
