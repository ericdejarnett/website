import sqlite3

# initialize the database
def init_db():
    conn = sqlite3.connect('database.db')
    with open('app/schema.sql', 'r') as f:
        conn.executescript(f.read())
    #cur = conn.cursor()
    conn.commit()
    conn.close()

# return a connection object for the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# create a new contact entry
def new_contact_entry(email, content):
    conn = get_db_connection()
    conn.execute('INSERT INTO contacts (email, content, responded) VALUES (?, ?, ?)',(email, content, 0))
    conn.commit()
    conn.close()

# update a contact entry
def update_contact_entry(email):
    pass

# delete a completed contact entry
def delete_contact_entry(email):
    pass
    