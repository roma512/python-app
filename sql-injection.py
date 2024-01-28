import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)

def vulnerable_login(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    success_login = cursor.fetchone()
    if success_login:
        query_token = f"SELECT flag FROM token"
        cursor.execute(query_token)
        result = cursor.fetchone()
        conn.close()
        return result

    
@app.route('/', methods=['GET', 'POST'])
def vulnerable_login_form():
    if request.method == 'POST':
        login = request.form.get('name')
        password = request.form.get('password')
        result = vulnerable_login(login, password)
        return render_template('profile.html', result=result)
    return render_template('vulnerable.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")