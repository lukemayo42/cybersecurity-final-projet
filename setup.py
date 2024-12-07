import sqlite3

DATABASE = 'users.db'

def run_sql(query, params):
    # run parameterized query to protect from sql injection
    rtn_flag = True
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # all other queries
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        conn.commit()
        #is it a select statement?
        if query.strip().upper().startswith("SELECT"):
            result = cursor.fetchall()
            return result

    except sqlite3.Error as e:
        print(f"exception: {e}")
        rtn_flag = False
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
    return rtn_flag

if __name__ == "__main__":
    #create the database
    run_sql(query = '''CREATE TABLE users
                    (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT,
                    access_level TEXT
                    )''', params = ())
