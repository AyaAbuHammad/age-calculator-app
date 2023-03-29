import datetime
import tkinter as tk
from PIL import Image ,ImageTk
from tkinter import messagebox

window = tk.Tk()
window.title('Age Calculator')
window.geometry('620x700')

name = tk.Label(text='name')
name.grid(row=1, column=0)

year = tk.Label(text='year')
year.grid(row=2 , column=0)

month = tk.Label(text='month')
month.grid(row=3 , column=0)

day = tk.Label(text='day')
day.grid(row=4 , column=0)

nameEntry = tk.Entry()
nameEntry.grid(row=1 , column=1)

yearEntry = tk.Entry()
yearEntry.grid(row=2 , column=1)

monthEntry = tk.Entry()
monthEntry.grid(row=3 , column=1)

dayEntry = tk.Entry()
dayEntry.grid(row=4 , column=1)

class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date        
    def age(self):
        today = datetime.date.today().year        
        age = today - self.birth_date.year
        return age

def get_input():
    name = nameEntry.get()
    try:
        new_date = datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    except ValueError:
        messagebox.showerror('Error!','The date must be a number.')
    today = datetime.date.today()
    year = int(yearEntry.get())
    if year > today.year:
        messagebox.showerror('Error','invalid year, please enter a year less than the current year')
    else:
        p = Person(name, new_date)
        text_area = tk.Text(window, width=25, height=20)
        text_area.grid(column=1, row=6)
        answer = 'hey {name}! your age is {age} years old'.format(name=name, age=p.age())
        # answer = 'hey {}! your age is {} years old'.format(name, p.age()) #in normal situation format we put {} then the variable ouside but if we put {var} then outside must be var=variable
        text_area.insert(tk.END, answer)

button = tk.Button(window, text='Calculate age', command= get_input, bg ='pink')
button.grid(row=5, column=1)

image = Image.open('age.jpg')
image.thumbnail((300,300),Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(row=0, column=1)
window.mainloop()

















