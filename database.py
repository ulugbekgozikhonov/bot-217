import sqlite3


def create_tables():
    con = sqlite3.connect("mars.db")
    cur = con.cursor()

    cur.execute("""                
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            first_name VARCHAR(45),
            age INTEGER CHECK(age>0),
            address VARCHAR(55),
            phone VARCHAR(13)
        )
""")
    con.commit()
    con.close()


def insert_user(user_id, first_name, age, address, phone):
    try:
        con = sqlite3.connect("mars.db")
        cur = con.cursor()

        cur.execute(
            "INSERT INTO users(user_id, first_name, age, address, phone) VALUES(?,?,?,?,?)",
            (user_id, first_name, age, address, phone),
        )
        con.commit()
        return True
    except Exception as e:
        print(f"ERROR INSERT <<<{e}>>>")
        return False
    finally:
        con.close()


def select_user(user_id):
    con = sqlite3.connect("mars.db")
    cur = con.cursor()
    
    user = cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
    return user
    