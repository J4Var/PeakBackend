from flask import Flask, jsonify

app = Flask(__name__)

# Toto pridá to pekné formátovanie (odriadkovanie)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

databaza = {
    "students" : [
        {
            "id":1,
          "name":"Janka",
            "surname":"Vargova",
              "nickname":"Dzejna"
              },
        {
            "id":2,
              "name":"Samo",
                "surname":"Haring",
                  "nickname":"BDYJTB"
                  },
        {
            "id":3,
              "name":"Matej",
                "surname":"Randziak",
                  "nickname":"Moarari"
                  },
        {
            "id":4,
              "name":"Matus",
                "surname":"Bucko",
                  "nickname":"Kutik"
                  },
        {
            "id":5,
              "name":"Tomas",
                "surname":"Jurcak", 
                "nickname":"Jurcacik"
                },
        {
            "id":6,
              "name":"Adrian",
                "surname":"Cervenka",
                  "nickname":"BigRed"
                  },
        {
            "id":7,
              "name":"Marcus",
                "surname":"Martis",
                  "nickname":"Jew"
                  },
        {"id":8, "name":"Martin",
         
          "surname":"Jelinek",
            "nickname":"Jeliman"
            },
        {
            "id":9,
              "name":"Milan",
                "surname":"Kokina",
                  "nickname":"Nalimovc"
                  },
    ]
} 

@app.route('/')
def home():
    return jsonify({"message":"Sunshine lollipops"})

@app.route('/api')
def api():
    return jsonify(databaza)

# OPRAVA: <int:student_id> namiesto :id
@app.route("/api/student/<int:student_id>")
def kidy_finder(student_id):
    # OPRAVA: databaza["students"] namiesto "student"
    # Indexujeme od 0, takze id 1 je na indexe 0
    try:
        student = databaza["students"][student_id - 1]
        return jsonify(student)
    except IndexError:
        return jsonify({"error": "Student nenajdeny"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)