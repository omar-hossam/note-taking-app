from datetime import datetime as dt
from getch import getch
from src.store import app_options, preferred_editor 
from src.utils import greeting, connect_db, close_db
from src.cli.utils import new_note

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
        note_content = new_note(preferred_editor)
        print(f"Note Content:\n{note_content}")

close_db()
