import os
import subprocess

def greeting(hour, fname):
        if hour > 4 and hour < 12:
                return f"Good Morning {fname} ☀️"
        elif hour >= 12 and hour < 17:
                return f"Good Afternoon {fname} ❤️"
        elif hour >= 17 and hour < 20:
                return f"Good Evening {fname} ☺️"
        else:
                return f"Good Night {fname} 🥰"

def new_note():
        working_dir = subprocess.run("pwd", capture_output=True, text=True).stdout
        temp_file = f"{working_dir.strip()}/temp/new_note.md"
        
        print("TEMP: ", temp_file)
        
        # edit new_note temp file
        os.system(f"micro {temp_file}")
        
        # save it's content
        note_content = ""
        with open(temp_file, "rt") as f:
                 note_content = f.read()
        
        # remove the temp file
        os.system(f"rm {temp_file}")
        
        # return the content
        return note_content.strip()
        
