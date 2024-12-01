import sqlite3



#creates the database
def create_db():
    #create table users in users database
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE users
                    (
                    username text,
                    password text,
                    access_level text
                    )''')
        conn.commit()
        return True
    except BaseException:
        print("exception")
        return False
    finally:
        if c is not None:
            c.close()
        if conn is not None:
            conn.close()

create_db()  
