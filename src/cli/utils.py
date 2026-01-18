import os
import subprocess

def new_note(editor):
        working_dir = subprocess.run("pwd", capture_output=True, text=True).stdout
        temp_file = f"{working_dir.strip()}/temp/new_note.md"
        
        # edit new_note temp file
        os.system(f"{editor} {temp_file}")
        
        # save it's content
        note_content = ""
        with open(temp_file, "rt") as f:
                 note_content = f.read()
        
        # remove the temp file
        os.system(f"rm {temp_file}")
        
        # return the content
        return note_content.strip()
        
