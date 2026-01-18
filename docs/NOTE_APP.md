# Notes App 

## Todos

those are the main todos and goals in the app:

- [ ] Notes must be encrypted! v1.0
- [ ] Create SQLite database first then migrate to PostgreSQL
- [ ] CLI Version
	- [ ] new_note():
		- [X] opens nano/vim or any other editor to write the .md note
		- [X] save it temporary in a file
		- [X] get the .md content from that file and delete the file
		- [ ] save note content in the database as a new note 
	- [ ] view_notes(): 
		- [ ] gets & prints all notes from the database
		- [ ] each note has an *id* so we can easily: 
			- [ ] print note properties
			- [ ] open the note and edit it via the editor
			- [ ] remove the note
- [ ] GUI Version v2.0
	- [ ] coming soon...
- [ ] Web Version v3.0
	- [ ] coming soon...

## Database

### Notes Table

id | title | content | created_at | last_edit_at
1  | Learn Python | lorem ipsum | 11/1/2026 %H:%M:%S .. 

## Globals:

1. All notes are written in `.md` and saved in the database.
2. All of them are connected to the same `.env` and the same database either it's sqlite or any other
 
