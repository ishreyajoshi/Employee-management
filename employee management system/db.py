import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age TEXT,
            doj TEXT,
            email TEXT,
            gender TEXT,
            contact TEXT,
            address TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, doj, email, gender, contact, address):
        try:
            self.cur.execute("INSERT INTO employees VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                             (name, age, doj, email, gender, contact, address))
            self.con.commit()
        except sqlite3.Error as e:
            print("Error inserting data:", e)

    # Fetch All Data from DB
    def fetch(self):
        try:
            self.cur.execute("SELECT * FROM employees")
            rows = self.cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print("Error fetching data:", e)
            return []

    # Delete a Record in DB
    def remove(self, id):
        try:
            self.cur.execute("DELETE FROM employees WHERE id=?", (id,))
            self.con.commit()
        except sqlite3.Error as e:
            print("Error deleting data:", e)

    # Update a Record in DB
    def update(self, id, name, age, doj, email, gender, contact, address):
        try:
            self.cur.execute(
                "UPDATE employees SET name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? WHERE id=?",
                (name, age, doj, email, gender, contact, address, id))
            self.con.commit()
        except sqlite3.Error as e:
            print("Error updating data:", e)

    # Close the connection on deletion of the object
    def __del__(self):
        if self.con:
            self.con.close()
