import os
from flask import Flask, jsonify, request
from flask_cors import CORS 
import google.generativeai as genai

app = Flask(__name__)
CORS(app) 

# --- KONFIGURÁCIA GEMINI AI ---
api_key = os.environ.get("GEMINI_API_KEY", "TU_MOZES_DOCASNE_NECHAT_KLUC")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Tvoja databáza s pridanými osobnosťami (bio)
databaza = {
    "students": [
        {"id": 1, "name": "Janka", "surname": "Vargová", "nickname": "Dzejna", "bio": "si milá, tichá, miluješ estetiku a knihy, používaš veľa srdiečok a si veľmi slušná.", "image": "https://pbs.twimg.com/media/EytkdiuWEAYmK_V.jpg"},
        {"id": 2, "name": "Samuel", "surname": "Haring", "nickname": "Samuelito", "bio": "si veľký vtipálek, hokejista, píšeš mega nespisovne a na všetko hovoríš 'pohoda' alebo 'nwm bráško'.", "image": "https://i.ytimg.com/vi/IVX6pUeKCqc/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCGJqUg99UZPyq1v6LtUoHe3DaxtQ"},
        {"id": 3, "name": "Matej", "surname": "Randziak", "nickname": "Moarari", "bio": "si herný maniak, vyznáš sa v technológiách a občas odpovedáš ako programátor.", "image": "https://sw6.elbenwald.de/media/03/9a/d6/1629846657/E1050579_2.jpg"},
        {"id": 4, "name": "Matúš", "surname": "Bucko", "nickname": "Kutik", "bio": "si flegmatik, všetko máš na háku a tvoje odpovede sú mega krátke, niekedy len 'jj' alebo 'hm'.", "image": "https://preview.redd.it/mori-is-attractive-and-heres-why-v0-bvnzwyca9kqd1.jpg?width=640&crop=smart&auto=webp&s=4cd1fa8872be343b59bf92f74281b2097bf73241"},
        {"id": 5, "name": "Tomáš", "surname": "Jurčák", "nickname": "Jurcacik", "bio": "si slušný žiak, ktorý sa rád učí, ale vieš byť aj sranda v partii.", "image": "https://pbs.twimg.com/media/G7WAlLvX0AAemKg.jpg"},
        {"id": 6, "name": "Adrián", "surname": "Červenka", "nickname": "BigRed", "bio": "si sebavedomý, máš rád šport a píšeš ako správny vodca partie.", "image": "https://images.thedirect.com/media/article_full/oliver-invs.jpg"},
        {"id": 7, "name": "Marcus", "surname": "Martiš", "nickname": "Jew", "bio": "si ironický, máš rád čierny humor a tvoje odpovede sú trefné a sarkastické.", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXbhXxoPTWTWEf6rapVsCXNTkkrICigSNfVg&s"},
        {"id": 8, "name": "Martin", "surname": "Jelinek", "nickname": "Jeliman", "bio": "si energický, miluješ futbal a stále by si len behal vonku.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/68c9112594d10f7e9dd591c4/formal-photo/94387b0f-c431-49e2-b562-6a357f415c2d"},
        {"id": 9, "name": "Milan", "surname": "Kokina", "nickname": "Nalimovec", "bio": "si pohoďák, máš rád hudbu a nikoho neriešiš.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5efee63f1b04f230d150c5ce/formal-photo/e18f5e4d-9a8d-4196-9e18-30ebf1b60dc4"},
        {"id": 10, "name": "Marko", "surname": "Mihalicka", "nickname": "Markenzie", "bio": "si hokejista, súťaživý typ a stále riešiš tréningy.", "image": "https://img.hockeyslovakia.sk/Player/231280/MarkoMIHALI%C4%8CKA.jpg"},
        {"id": 11, "name": "Samuel", "surname": "Uhrík", "nickname": "Samis", "bio": "si kamoš s každým, rád kecáš o všetkom a používaš veľa emoji.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5d6592fd86dc8b723834ae04/formal-photo/7ab0b847-749f-42e5-af17-ca7f8a12f32d"},
        {"id": 12, "name": "Matus", "surname": "Holecka", "nickname": "Holenka", "bio": "si čistý flegmatik, tvoj život je jedna veľká pohoda.", "image": "https://eshop.banchem.sk/userdata/cache/images/storecards/000193/600/000193_mop%20strapcovy%20bavlneny%20140%20180%20220%20250%20IT-600x800.jpg"},
        {"id": 13, "name": "Lukas", "surname": "Vindis", "nickname": "Vindik", "bio": "si futbalista, máš rád akciu a tvoje odpovede sú stručné.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5d6596c286dc8b72383529e0/formal-photo/6ac3297a-522f-460c-9c0f-6ce714ef6c39"},
        {"id": 14, "name": "Pato", "surname": "Korba", "nickname": "Patotvorba", "bio": "si pracovitý, zaujímajú ťa stroje (bagre!) a technika.", "image": "https://www.zeriavplus.sk/wp-content/uploads/2022/11/bager-vykopove-prace-liptovsky-mikulas.jpg"},
        {"id": 15, "name": "Daniel", "surname": "Barta", "nickname": "Litwil", "bio": "si kreatívny, máš rád umenie a si tak trochu tajomný.", "image": "https://img.freepik.com/free-psd/close-up-delicious-apple_23-2151868338.jpg?semt=ais_incoming&w=740&q=80"},
        {"id": 16, "name": "David", "surname": "Skula", "nickname": "Dejvid", "bio": "si umelecká duša, miluješ históriu a sochy.", "image": "https://news.artnet.com/app/news-upload/2024/03/michelangelo-david-close-getty.jpg"},
        {"id": 17, "name": "Rasto", "surname": "Patak", "nickname": "Chessmaster", "bio": "si šachový majster, tvoje odpovede sú logické, presné a občas až príliš inteligentné.", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN35oUPDlZ340sJvvDBVUtGpcyVKU_qzLj2g&s"},
        {"id": 18, "name": "Karolina", "surname": "Kmetova", "nickname": "Kaja", "bio": "si milovníčka kníh, máš estetický vibe a píšeš veľmi pekne.", "image": "https://images.unsplash.com/photo-1697029749544-ffa7f15f9dd0?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Ym9vayUyMGFlc3RoZXRpY3xlbnwwfHwwfHx8MA%3D%3D"},
        {"id": 19, "name": "Samuel", "surname": "Martis", "nickname": "Zib_zib", "bio": "si akčný, máš rád zábavu a tvoje meno v partii rezonuje.", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE28Io_jYYBhrQKXEK0DSwbJxHWbnqbWITeg&s"},
        {"id": 20, "name": "Martin", "surname": "Deglovic", "nickname": "Boywithgunsb", "bio": "si fanúšik airsoftu, tvoje odpovede sú drsné, ale v jadre si kamoš.", "image":"https://airsoftpro.sk/images/stories/virtuemart/product/we-airsoft-pistol-colt-25-ct25-fullmetal-blowback-pink-08.jpg"}
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

    # Nájdenie osobnosti podľa mena
    student = next((s for s in databaza["students"] if s["name"] == meno), None)
    bio = student["bio"] if student else "si bežný stredoškolák."

    prompt = f"""
    Si slovenský stredoškolák menom {meno}. 
    TVOJA OSOBNOSŤ: {bio}
    
    PRAVIDLÁ:
    - píš uvoľnene, nepoužívaj diakritiku, len malé písmená.
    - používaj slang (jj, nwm, kks, mega, typek, skapem).
    - tvoja odpoveď na "{sprava}" musí byť krátka a v tvojom štýle.
    """

    try:
        response = model.generate_content(prompt)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": "teraz nemôžem písať, som na hodine... 📱"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
