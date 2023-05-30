import requests
import tkinter as tk


def get_history(event):
    year = year_entry.get()

    response = requests.get(f'http://numbersapi.com/{year}/year')

    if response.status_code == 200:
        fact = response.text
    else:
        fact = "Неправильно введен год"

    fact_text.config(state=tk.NORMAL)
    fact_text.delete('1.0', tk.END)
    fact_text.insert(tk.END, fact)
    fact_text.config(state=tk.DISABLED)


window = tk.Tk()
window['bg']='white'
window.title("Этот год в истории")

date_label = tk.Label(window, text="Введите год (ГГГГ):")
date_label.pack()
year_entry = tk.Entry(window)
year_entry.pack()

fetch_button = tk.Button(window, text="Факт из истории")
fetch_button.pack()
fetch_button.bind('<Button-1>', get_history)

fact_text = tk.Text(window, width=50, height=10)
fact_text['bg']='grey'
fact_text.pack()
fact_text.config(state=tk.DISABLED)

window.mainloop()