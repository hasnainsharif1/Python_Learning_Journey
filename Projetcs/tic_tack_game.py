import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8], [0,3,6], [1,4,7],[2,5,8], [0,4,8], 2,4,6]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]["text"]].config(bg="green")
            buttons[combo[1]["text"]].config(bg="green")
            buttons[combo[2]["text"]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {combo[0]["text"]} Win!")
            root.quit()

def button_click(index):