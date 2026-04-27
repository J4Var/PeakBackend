import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify, request
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# Inicializácia Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Funkcia na pripojenie k databáze
def get_db_connection():
    conn = psycopg2.connect(
        user="embodiment_of_perfection_user",
        password="Ydj9LxNkAkW54fxegZVRf4DTghwnsdqv",
        host="dpg-d7ng32aqqhas73frtoq0-a.oregon-postgres.render.com",
        port=5432,
        database="embodiment_of_perfection",
        sslmode="require"
    )
    return conn

@app.route('/api')
def get_all_students():
    try:
        conn = get_db_connection()
        # RealDictCursor vráti dáta ako slovník (JSON friendly), nie ako zoznam čísel
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT id, name, surname, nickname, bio, image FROM students ORDER BY id;')
        students = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify({"students": students})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        meno = data.get('name', 'Spolužiak')
        sprava = data.get('message', '')

        # Hľadáme bio študenta v databáze
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT bio FROM students WHERE name = %s LIMIT 1;', (meno,))
        result = cur.fetchone()
        cur.close()
        conn.close()

        osobnost = result["bio"] if result else "si stredoškolák."

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": f"Si {meno}. OSOBNOSŤ: {osobnost}. Píš uvoľnene, bez diakritiky, malé písmená. Max 2 vety."},
                {"role": "user", "content": sprava}
            ],
            temperature=0.8
        )
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        print(f"Chyba pri chate: {e}")
        return jsonify({"reply": "momentálne mi to nemyslí... 🔧"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
