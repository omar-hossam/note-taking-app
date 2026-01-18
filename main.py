from datetime import datetime as dt
from getch import getch
from src.utils import greeting, new_note, connect_db, close_db
from src.store import app_options

cursor = connect_db()

user_fname = "Omar"
current_hour = int(dt.now().strftime("%H"))


print(greeting(current_hour, user_fname))
print("What can I help you with?\n")

for x in app_options:
        print(f"{x}. {app_options[x]}")

print("")
key = getch()

if key == "2":
        note_content = new_note()
        print(f"Note Content:\n{note_content}")

close_db()
