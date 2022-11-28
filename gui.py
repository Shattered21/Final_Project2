from tkinter import *

# Original link: https://www.youtube.com/watch?v=6CZB6VTy3Hg&list=PLl316cKxhMxtOWHa88kDqm42uWz1aqGfD
# I disabled text entry, color coded the design.
# I also made the input disappear if user clicks equal and then clicks another button other than clear.
# I created a new button and added it to the gui. It's a power button that clears the screen if powered off and disables all buttons.

class Calculator:

    def __init__(self, master):
        '''
        Method constructs the gui
        Methodd creates all buttons that are available for the user to use
        Method sets up the geometry and makes gui non-resizable
        '''
        master.title('Calculator')
        master.geometry('357x420+0+0')
        master.config(bg='black')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        self.__power = False
        Entry(width=14, bg='#ccddff', font=('Arial Bold', 28), state='disabled', textvariable=self.equation).place(x=0,
                                                                                                                   y=0)
        Button(width=7, height=3, text='ON/OFF', relief='flat', bg='Red', command=lambda: self.power()).place(x=299,
                                                                                                               y=0)

        Button(width=11, height=4, text='(', relief='flat', bg='purple', command=lambda: self.show('(')).place(x=0,
                                                                                                               y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='purple', command=lambda: self.show(')')).place(x=90,
                                                                                                               y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='orange', command=lambda: self.show('%')).place(x=180,
                                                                                                               y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='gray', command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='gray', command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='gray', command=lambda: self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='gray', command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='gray', command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='gray', command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='gray', command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='gray', command=lambda: self.show(8)).place(x=180, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='gray', command=lambda: self.show(9)).place(x=90, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='gray', command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='orange', command=lambda: self.show('.')).place(x=180,
                                                                                                               y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='orange', command=lambda: self.show('+')).place(x=270,
                                                                                                               y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='orange', command=lambda: self.show('-')).place(x=270,
                                                                                                               y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='orange', command=lambda: self.show('/')).place(x=270,
                                                                                                               y=50)
        Button(width=11, height=4, text='x', relief='flat', bg='orange', command=lambda: self.show('*')).place(x=270,
                                                                                                               y=125)
        Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='Clear', relief='flat', bg='yellow', command=self.clear).place(x=0, y=350)

    def show(self, value):
        '''
        Method shows the calculation on the gui screen
        '''
        if self.__power:
            self.entry_value += str(value)
            self.equation.set(self.entry_value)

    def clear(self):
        '''
        Method clears the calculation on the gui screen
        '''
        if self.__power:
            self.entry_value = ''
            self.equation.set(self.entry_value)

    def solve(self):
        '''
        Method solves the equation entered by the user
        '''
        if self.__power:
            eval(self.entry_value)
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = ''

    def power(self):
        '''
        Method checks if the power is on
        if power is turned off method clears the screen
        '''
        if self.__power == False:
            self.__power = True
        else:
            self.__power = False
            self.entry_value = ''
            self.equation.set(self.entry_value)




