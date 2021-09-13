import sqlite3
from dataclasses import dataclass


@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    
    def __init__(self,name):
        self.name = f'{name}.db'
        self.conn = sqlite3.connect(self.name)
        self.note = self.conn.execute("CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")

    def add(self, note: 'Note'):
        self.note = self.conn.execute(f"INSERT INTO note (title, content) VALUES ('{note.title}', '{note.content}');")
        self.conn.commit()
    
    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        lista_note = []
        for valor in cursor:
            id = valor[0]
            title = valor[1]
            content = valor[2]
        note = Note(id, title, content)
        lista_note.append(note)
        return lista_note

    def update(self, entry: 'Note'):
        self.note = self.conn.execute(f'UPDATE note SET title = {entry.title}, content = {entry.content} WHERE id = {entry.id};')
        self.conn.commit()

    def delete(self, note_id):
        self.note = self.conn.execute(f'DELETE FROM note WHERE id = {note_id};')
        self.conn.commit()


