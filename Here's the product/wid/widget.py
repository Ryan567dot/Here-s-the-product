from tkinter import *

window = Tk()
window.title("Super Market")
window.config(bg="lightblue")
window.geometry("400x450")

number1 = Label(window, text="Enter your first number:").grid(row=1, column=1)
number2 = Label(window, text="Enter your second number:").grid(row=2, column=1)








window.mainloop()