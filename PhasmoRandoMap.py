import random
import tkinter as tk


window = tk.Tk()

window.geometry("550x550")

window.title("Phasmophobia Map randomizer")

def randomize():
    maps = ['Tanglewood', 'Willow Street', 'Ridgeview', 'Edgyfield', 'Bleadsale', 'Grafton', 'Highschool',
            'Sunny Meadows', 'Prison', 'Camp Woodsomething', 'Campsite']
    l['text'] = random.choice(maps)


button = tk.Button(window, text='Randomize', font=(
    'Helvetica', 20), bg='#D3D3D3', command=randomize)
button.config(width=10, height=3)
button.pack(padx=100, pady=50)
l = tk.Label(window, font=('October Crow', 50), bg='#818589')
l.pack()

window.configure(bg='#818589')

window.mainloop()



