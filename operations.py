import math
from tkinter import *
import calculator
    
#Function
class Calc():
    def __init__(self, tk):
        self.calculator = calculator
        self.total=0
        self.current=''
        self.input=True
        self.check_sum=False
        self.op=''
        self.result=False
    #When numbers are entered
    def number(self, num):
        self.result=False
        num1 =self.calculator.value.get()
        num2 = str(num)
        if self.input:
            self.current=num2
            self.input=False
        else:
            if num2 == '+/-': #Change positive or negative
                if '-' in num1:
                    self.current=num1.removeprefix('-')
                else:
                    self.current=-(float(self.calculator.value.get()))
            elif num2 == '%': #Change to percent by dividing by 100
                self.current = float((self.calculator.value.get()))/100
            elif num2 == '.': #Change to decimal
                if num2 in num1:
                    return
                self.current=num1+num2
        self.display(self.current)
    #Display screen
    def display(self, num):
        self.calculator.value.insert(0, num)
        self.calculator.value.delete(0, END)
    #assigned appropriate operator
    def operator(self, op):
        self.current=float(self.current)
        if self.check_sum:
            self.function()
        elif not self.result:
            self.total=self.current
            self.input=True
        self.check_sum=True
        self.op=op
        self.result=False
    def function(self):
        self.current=float(self.current)
        if self.op == 'add':
            self.total += self.current
        if self.op == 'sub':
            self.total -= self.current
        if self.op == 'mul':
            self.total *= self.current
        if self.op == 'div':
            self.total /= self.current
        self.input = False
        self.check_sum = False
        self.display(self.total)
    #Display when press equal
    def equal(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.function()
        else:
            self.total=float(self.calculator.value.get())
    #Clear entry
    def clear(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input = True
    #Clear all
    def clearAll(self):
        self.clear()
        self.total = 0
        
            
            