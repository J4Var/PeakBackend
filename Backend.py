import os
from flask import Flask, jsonify, request
from flask_cors import CORS 
from groq import Groq

app = Flask(__name__)
CORS(app) 

# --- KONFIGURÁCIA GROQ ---
# Na Renderi pridaj premennú GROQ_API_KEY
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Databáza priamo v kóde
databaza = {
    "students": [
        {"id": 1, "name": "Janka", "surname": "Vargová", "nickname": "Dzejna", "bio": "si milá, tichá, miluješ knihy a používaš veľa srdiečok.", "image": "https://pbs.twimg.com/media/EytkdiuWEAYmK_V.jpg"},
        {"id": 2, "name": "Samuel", "surname": "Haring", "nickname": "Samuelito", "bio": "si vtipálek, hokejista a píšeš mega nespisovne.", "image": "https://i.ytimg.com/vi/IVX6pUeKCqc/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCGJqUg99UZPyq1v6LtUoHe3DaxtQ"},
        {"id": 3, "name": "Matej", "surname": "Randziak", "nickname": "Moarari", "bio": "si herný maniak a vyznáš sa v technológiách.", "image": "https://sw6.elbenwald.de/media/03/9a/d6/1629846657/E1050579_2.jpg"},
        {"id": 4, "name": "Matúš", "surname": "Bucko", "nickname": "Kutik", "bio": "si flegmatik, píšeš mega krátko (jj, nwm).", "image": "https://preview.redd.it/mori-is-attractive-and-heres-why-v0-bvnzwyca9kqd1.jpg?width=640&crop=smart&auto=webp&s=4cd1fa8872be343b59bf92f74281b2097bf73241"},
        {"id": 5, "name": "Tomáš", "surname": "Jurčák", "nickname": "Jurcacik", "bio": "si slušný žiak a rád sa učíš.", "image": "https://pbs.twimg.com/media/G7WAlLvX0AAemKg.jpg"},
        {"id": 6, "name": "Adrián", "surname": "Červenka", "nickname": "BigRed", "bio": "si športovec a prirodzený vodca.", "image": "https://images.thedirect.com/media/article_full/oliver-invs.jpg"},
        {"id": 7, "name": "Marcus", "surname": "Martiš", "nickname": "Jew", "bio": "máš rád sarkazmus a čierny humor.", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXbhXxoPTWTWEf6rapVsCXNTkkrICigSNfVg&s"},
        {"id": 8, "name": "Martin", "surname": "Jelinek", "nickname": "Jeliman", "bio": "miluješ futbal a pohyb.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/68c9112594d10f7e9dd591c4/formal-photo/94387b0f-c431-49e2-b562-6a357f415c2d"},
        {"id": 9, "name": "Milan", "surname": "Kokina", "nickname": "Nalimovec", "bio": "si pohoďák a máš rád hudbu.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5efee63f1b04f230d150c5ce/formal-photo/e18f5e4d-9a8d-4196-9e18-30ebf1b60dc4"},
        {"id": 10, "name": "Marko", "surname": "Mihalicka", "nickname": "Markenzie", "bio": "si hokejista a veľmi súťaživý.", "image": "https://img.hockeyslovakia.sk/Player/231280/MarkoMIHALI%C4%8CKA.jpg"},
        {"id": 11, "name": "Samuel", "surname": "Uhrík", "nickname": "Samis", "bio": "si kamoš s každým a rád kecáš.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5d6592fd86dc8b723834ae04/formal-photo/7ab0b847-749f-42e5-af17-ca7f8a12f32d"},
        {"id": 12, "name": "Matus", "surname": "Holecka", "nickname": "Holenka", "bio": "si totálny flegmatik.", "image": "https://eshop.banchem.sk/userdata/cache/images/storecards/000193/600/000193_mop%20strapcovy%20bavlneny%20140%20180%20220%20250%20IT-600x800.jpg"},
        {"id": 13, "name": "Lukas", "surname": "Vindis", "nickname": "Vindik", "bio": "si futbalista a píšeš stručne.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5d6596c286dc8b72383529e0/formal-photo/6ac3297a-522f-460c-9c0f-6ce714ef6c39"},
        {"id": 14, "name": "Pato", "surname": "Korba", "nickname": "Patotvorba", "bio": "miluješ bagre, stroje a prácu.", "image": "https://www.zeriavplus.sk/wp-content/uploads/2022/11/bager-vykopove-prace-liptovsky-mikulas.jpg"},
        {"id": 15, "name": "Daniel", "surname": "Barta", "nickname": "Litwil", "bio": "si kreatívny a tajomný umelec.", "image": "https://img.freepik.com/free-psd/close-up-delicious-apple_23-2151868338.jpg?semt=ais_incoming&w=740&q=80"},
        {"id": 16, "name": "David", "surname": "Skula", "nickname": "Dejvid", "bio": "si umelecká duša.", "image": "https://news.artnet.com/app/news-upload/2024/03/michelangelo-david-close-getty.jpg"},
        {"id": 17, "name": "Rasto", "surname": "Patak", "nickname": "Chessmaster", "bio": "si šachový majster a píšeš inteligentne.", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN35oUPDlZ340sJvvDBVUtGpcyVKU_qzLj2g&s"},
        {"id": 18, "name": "Karolina", "surname": "Kmetova", "nickname": "Kaja", "bio": "miluješ knihy a estetiku.", "image": "https://images.unsplash.com/photo-1697029749544-ffa7f15f9dd0?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Ym9vayUyMGFlc3RoZXRpY3xlbnwwfHwwfHx8MA%3D%3D"},
        {"id": 19, "name": "Samuel", "surname": "Martis", "nickname": "Zib_zib", "bio": "si akčný a máš rád zábavu.", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE28Io_jYYBhrQKXEK0DSwbJxHWbnqbWITeg&s"},
        {"id": 20, "name": "Martin", "surname": "Deglovic", "nickname": "Boywithgunsb", "bio": "si fanúšik airsoftu a zbraní.", "image":"https://airsoftpro.sk/images/stories/virtuemart/product/we-airsoft-pistol-colt-25-ct25-fullmetal-blowback-pink-08.jpg"}
    ]
}

@app.route('/api')
def get_all_students():
    return jsonify(databaza)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    meno = data.get('name', 'Spolužiak')
    sprava = data.get('message', '')

    student = next((s for s in databaza["students"] if s["name"] == meno), None)
    osobnost = student["bio"] if student else "si stredoškolák."

    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": f"Si {meno}. OSOBNOSŤ: {osobnost}. Píš uvoľnene, bez diakritiky, malé písmená, používaj slang. Max 2 vety."},
                {"role": "user", "content": sprava}
            ],
            temperature=0.8
        )
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply": "momentálne mi to nemyslí... 🔧"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
