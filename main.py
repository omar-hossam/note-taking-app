from datetime import datetime as dt
from getch import getch
import os

def greeting(hour, fname):
        if hour > 4 and hour < 12:
                return f"Good Morning {fname} ☀️"
        elif hour >= 12 and hour < 17:
                return f"Good Afternoon {fname} ❤️"
        elif hour >= 17 and hour < 20:
                return f"Good Evening {fname} ☺️"
        else:
                return f"Good Night {fname} 🥰"
        

user_fname = "Omar"
current_hour = int(dt.now().strftime("%H"))
options = {
        "1": "View all notes 📙",
        "2": "New note 📝",
        "3": "Remove a note 🗑️"
}

print(greeting(current_hour, user_fname))
print("What can I help you with?\n")

for x in options:
        print(f"{x}. {options[x]}")

print("")
key = getch()
if key == "1":
        
