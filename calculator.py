from tkinter import *
import operations

class Calculator_UI:
    def __init__(self, master):
        #Initialize application
        master.geometry("320x568")
        master.resizable(False, False)
        master.title("CALCULATOR")
        master.config(background = 'black')
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=2)
        display_box= Frame(master, bg='white', width=320, bd=0, highlightthickness=0, relief="ridge")
        display_box.grid(row=0)

        value = Entry(display_box, font=('calibre', 35, 'normal'), bg='white', fg='white', justify=RIGHT)
        value.insert(0,"0")

        option = operations.Calc(self)
        
def main():
    root = Tk()
    app = Calculator_UI(root)
    root.mainloop()
    
if __name__ == '__main__' :
    main()
        
        

    


    






