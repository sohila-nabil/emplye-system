import sqlite3

class Database:
    def __init__(self, db):
        self.connect = sqlite3.connect(db)
        self.cursor = self.connect.cursor()

        sql = """
             CREATE TABLE IF NOT EXISTS employee(
              id Integer Primary Key,
              name text,
              age text,
              job text,
              email text,
              gender text,
              phone text,
              address text

             )
        """
        self.cursor.execute(sql)
        self.connect.commit()

    def insert(self, name, age, job, email, gender, phone, address):
        self.cursor.execute("insert into employee values(NULL,?,?,?,?,?,?,?)",
        (name, age, job, email, gender, phone, address))

        self.connect.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM employee")
        rows = self.cursor.fetchall()
        return rows
    
    def remove(self, id):
        self.cursor.execute("delete from employee where id=?",(id,))
        self.connect.commit()

    def update(self, id, name, age, job, email, gender, phone, address):
        self.cursor.execute("update employee set name=?, age=?, job=?, email=?, gender=?, phone=?, address=? where id =?",
                            (name, age, job, email, gender, phone, address,id))
        self.connect.commit()

        