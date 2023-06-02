import sqlite3

conn = sqlite3.connect('db.db', check_same_thread = False)
cursor = conn.cursor()

def add_user(user_id, user_name, data):
    cursor.execute('INSERT INTO users (user_id, user_name, data_reg) VALUES (?, ?, ?)', (user_id, user_name, data))
    conn.commit()

def add_income(user_id, income, data):
    cursor.execute(f"SELECT user_id FROM user_fin WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO user_fin (user_id, income, data_inc) VALUES (?, ?, ?)', (user_id, income, data))
        cursor.execute(f'UPDATE user_fin SET balance=(SELECT balance FROM user_fin WHERE user_id="{user_id}")+"{income}" WHERE user_id = "{user_id}"')
        cursor.execute(f'UPDATE user_fin SET data_inc="{data}" WHERE user_id = "{user_id}"')
        conn.commit()
    else:
        cursor.execute(f'UPDATE user_fin SET balance=(SELECT balance FROM user_fin WHERE user_id="{user_id}")+"{income}" WHERE user_id = "{user_id}"')
        cursor.execute(f'UPDATE user_fin SET income="{income}" WHERE user_id = "{user_id}"')
        cursor.execute(f'UPDATE user_fin SET data_inc="{data}" WHERE user_id = "{user_id}"')
        conn.commit()
    conn.commit()

def add_expense(user_id, expense, data):
    cursor.execute(f"SELECT user_id FROM user_fin WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO user_fin (user_id, expense, data_exp) VALUES (?, ?, ?)', (user_id, expense, data))
        cursor.execute(f'UPDATE user_fin SET balance=(SELECT balance FROM user_fin WHERE user_id="{user_id}")-"{expense}" WHERE user_id = "{user_id}"')
        cursor.execute(f'UPDATE user_fin SET data_exp="{data}" WHERE user_id = "{user_id}"')
        conn.commit()
    else:
        cursor.execute(f'UPDATE user_fin SET balance=(SELECT balance FROM user_fin WHERE user_id="{user_id}")-"{expense}" WHERE user_id = "{user_id}"')
        cursor.execute(f'UPDATE user_fin SET expense="{expense}" WHERE user_id = "{user_id}"')
        cursor.execute(f'UPDATE user_fin SET data_exp="{data}" WHERE user_id = "{user_id}"')
        conn.commit()

def balance(user_id):
    try:
        try:
            cursor.execute(f"SELECT balance FROM user_fin WHERE user_id = '{user_id}'")
            return cursor.fetchone()[0]
        except TypeError:
            return '⚠️ Database Error... (99)'
    except sqlite3.ProgrammingError:
        return '⚠️ Database Error... (100)'

def chek_ban(user_id):
    try:
        chek = cursor.execute(f"SELECT user_ban FROM users WHERE user_id = '{user_id}'").fetchone()[0]
        if chek == 0:
            return 'False'
        else:
            return 'True'
    except TypeError:
        return '⚠️ Database Error... (101)'

def chek_admin(user_id):
    try:
        chek = cursor.execute(f"SELECT admin FROM users WHERE user_id = '{user_id}'").fetchone()[0]
        if chek == 0:
            return 'False'
        else:
            return 'True'
    except TypeError:
        return '⚠️ Database Error... (102)'
    
def chek_user(user_id):
    try:
        cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
        if cursor.fetchone() is None:
            return 'False'
        else:
            return 'True'
    except sqlite3.ProgrammingError:
        return '⚠️ Database Error.. (103)'
    
def add_admin(user_id):
    cursor.execute(f"UPDATE users SET admin=1 WHERE user_id = '{user_id}'")
    conn.commit()

def clr_admin(user_id):
    cursor.execute(f"UPDATE users SET admin=0 WHERE user_id = '{user_id}'")
    conn.commit()
    
def ban_admin(user_id):
    cursor.execute(f"UPDATE users SET user_ban=1 WHERE user_id = '{user_id}'")
    conn.commit()

def clr_ban_admin(user_id):
    cursor.execute(f"UPDATE users SET user_ban=0 WHERE user_id = '{user_id}'")
    conn.commit()

def mailings():
    cursor.execute('SELECT user_id FROM users')
    mail = cursor.fetchall()
    for i in mail:
        return i[0]
    conn.commit()
 
def all_users():
    result = cursor.execute('SELECT id FROM users')
    return len(result.fetchall())

def data_reg(user_id):
    res = cursor.execute(f'SELECT data_reg FROM users WHERE user_id="{user_id}"').fetchone()[0]
    return f'{res}'

def data_income(user_id):
    try:
        result = cursor.execute(f'SELECT data_inc FROM user_fin WHERE user_id="{user_id}"').fetchone()[0]
        return f'{result}'
    except TypeError:
        return '⚠️ Database Error... (104)'

def last_income(user_id):
    try:
        result = cursor.execute(f'SELECT income FROM user_fin WHERE user_id="{user_id}"').fetchone()[0]
        return f'{result}'
    except TypeError:
        return '⚠️ Database Error... (105)'

def data_expense(user_id):
    try:
        result = cursor.execute(f'SELECT data_exp FROM user_fin WHERE user_id="{user_id}"').fetchone()[0]
        return f'{result}'
    except TypeError:
        return '⚠️ Database Error... (104)'

def last_expense(user_id):
    try:
        result = cursor.execute(f'SELECT expense FROM user_fin WHERE user_id="{user_id}"').fetchone()[0]
        return f'{result}'
    except TypeError:
        return '⚠️ Database Error... (105)'
    
def delete_fin(user_id):
    cursor.execute(f'DELETE FROM user_fin WHERE user_id="{user_id}"')
    conn.commit()

def set_language(user_id, language):
    cursor.execute(f'UPDATE users SET language="{language}" WHERE user_id="{user_id}"')
    conn.commit()

def chek_language(user_id):
    res = cursor.execute(f'SELECT language FROM users WHERE user_id="{user_id}"').fetchone()[0]
    return f'{res}'

def users():
    res = cursor.execute('SELECT * FROM users').fetchall()
    for row in res:
        file = open('users.txt', 'a')
        file.write(f'{row}\n')
    conn.commit()