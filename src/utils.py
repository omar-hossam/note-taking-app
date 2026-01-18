import os
import subprocess
import sqlite3

conn = None

def greeting(hour, fname):
        if hour > 4 and hour < 12:
                return f"Good Morning {fname} ☀️"
        elif hour >= 12 and hour < 17:
                return f"Good Afternoon {fname} ❤️"
        elif hour >= 17 and hour < 20:
                return f"Good Evening {fname} ☺️"
        else:
                return f"Good Night {fname} 🥰"

def connect_db():
        global conn
        conn = sqlite3.connect("data.db")
        return conn.cursor()

def create_table(table_name, cols):
        cols_txt = ""
        for c in cols:
                cols_txt = cols_txt + c + "\n"
        print(cols_txt)

def close_db():
        global conn
        conn.commit() # save changes
        conn.close() # close connection

def new_note():
        working_dir = subprocess.run("pwd", capture_output=True, text=True).stdout
        temp_file = f"{working_dir.strip()}/temp/new_note.md"
        
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
        
