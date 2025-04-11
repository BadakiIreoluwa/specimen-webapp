from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Ensure DB and table exist
def init_db():
    conn = sqlite3.connect('specimens.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS specimens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            microSize REAL,
            actualSize REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        username = request.form.get("username")
        micro_size = float(request.form.get("microSize"))
        input_mode = request.form.get("inputMode")

        if input_mode == "total":
            total_mag = float(request.form.get("totalMagnification"))
        else:
            eyepiece = float(request.form.get("eyepieceMagnification"))
            objective = float(request.form.get("objectiveMagnification"))
            total_mag = eyepiece * objective

        if total_mag == 0:
            result = "Magnification cannot be zero."
        else:
            actual_size = (micro_size / total_mag) * 1000
            result = f"The actual size of the specimen is {actual_size:.2f} µm"

            # Save to DB
            conn = sqlite3.connect('specimens.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO specimens (username, microSize, actualSize) VALUES (?, ?, ?)",
                           (username, micro_size, actual_size))
            conn.commit()
            conn.close()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
