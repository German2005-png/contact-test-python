import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Contacts (id INTEGER PRIMARY KEY, name TEXT, phone TEXT)''')
con.commit()
con.close()

def get_contacts():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('''SELECT * FROM Contacts''')
    rows = cur.fetchall()
    con.close()
    return rows

def create_contacto(name, phone):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO Contacts (name, phone) VALUES (?, ?)''', (name, phone))
    con.commit()
    con.close()

def edit_contact(id, name, phone):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('''SELECT * FROM  Contacts WHERE id = ?''', (id,))
    findContact = cur.fetchone()
    if(findContact):
        cur.execute('''UPDATE Contacts SET name = ?, phone = ? WHERE id = ?''', (name, phone, findContact[0]))
        print(f"Contacto con el nombre: {name} y ID: {findContact[0]} fue actualizado.")
    else:
        print("Contact not found")
    con.commit()
    con.close()

def delete_contact(id):
    print("Eliminando contacto con ID:", id)
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('''SELECT * FROM  Contacts WHERE id = ?''', (id,))
    findContact = cur.fetchone()
    print("Find Contact:", findContact)
    if(findContact):
        cur.execute('''DELETE FROM Contacts WHERE id = ?''', (findContact[0],))
        print(f"Contacto con el ID: {findContact[0]} fue eliminado.")
    else:
        print("Contact not found")
    con.commit()
    con.close()