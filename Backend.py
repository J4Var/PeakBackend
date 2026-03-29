from flask import Flask, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


databaza = {
    "students": [
        {"id": 1, "name": "Janka", "surname": "Vargová", "nickname": "Dzejna", "image": "https://pbs.twimg.com/media/EytkdiuWEAYmK_V.jpg"},
        {"id": 2, "name": "Samuel", "surname": "Haring", "nickname": "Samuelito", "image": "https://cdn.discordapp.com/attachments/1415008017010786394/1487837336246030518/hq720.jpg?ex=69ca97ff&is=69c9467f&hm=237148fa707fe0952aba50a33c044be51914feb2e1914573a263ec2babc70686&"},
        {"id": 3, "name": "Matej", "surname": "Randziak", "nickname": "Moarari", "image": "https://sw6.elbenwald.de/media/03/9a/d6/1629846657/E1050579_2.jpg"},
        {"id": 4, "name": "Matúš", "surname": "Bucko", "nickname": "Kutik", "image": "https://preview.redd.it/mori-is-attractive-and-heres-why-v0-bvnzwyca9kqd1.jpg?width=640&crop=smart&auto=webp&s=4cd1fa8872be343b59bf92f74281b2097bf73241"},
        {"id": 5, "name": "Tomáš", "surname": "Jurčák", "nickname": "Jurcacik", "image": "https://pbs.twimg.com/media/G7WAlLvX0AAemKg.jpg"},
        {"id": 6, "name": "Adrián", "surname": "Červenka", "nickname": "BigRed", "image": "https://cdn.discordapp.com/attachments/1465277883777024082/1469426348115099721/Screenshot_20260206_211508_Gallery.jpg?ex=69ca312e&is=69c8dfae&hm=3158bf91b369476112530358e31bf59d55d4fbbeae0799e264a9443f8efcf3a1&"},
        {"id": 7, "name": "Marcus", "surname": "Martiš", "nickname": "Jew", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXbhXxoPTWTWEf6rapVsCXNTkkrICigSNfVg&s"},
        {"id": 8, "name": "Martin", "surname": "Jelinek", "nickname": "Jeliman", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/68c9112594d10f7e9dd591c4/formal-photo/94387b0f-c431-49e2-b562-6a357f415c2d"},
        {"id": 9, "name": "Milan", "surname": "Kokina", "nickname": "Nalimovec", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5efee63f1b04f230d150c5ce/formal-photo/e18f5e4d-9a8d-4196-9e18-30ebf1b60dc4"},
        {"id": 10, "name": "Marko", "surname": "Mihalicka", "nickname": "Markenzie", "image": "https://img.hockeyslovakia.sk/Player/231280/MarkoMIHALI%C4%8CKA.jpg"},
        {"id": 11, "name": "Samuel", "surname": "Uhrík", "nickname": "Samis", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5d6592fd86dc8b723834ae04/formal-photo/7ab0b847-749f-42e5-af17-ca7f8a12f32d"},
        {"id": 12, "name": "Matus", "surname": "Holecka", "nickname": "Holenka", "image": "https://eshop.banchem.sk/userdata/cache/images/storecards/000193/600/000193_mop%20strapcovy%20bavlneny%20140%20180%20220%20250%20IT-600x800.jpg"},
        {"id": 13, "name": "Lukas", "surname": "Vindis", "nickname": "Vindik", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5d6596c286dc8b72383529e0/formal-photo/6ac3297a-522f-460c-9c0f-6ce714ef6c39"},
        {"id": 14, "name": "Pato", "surname": "Korba", "nickname": "Patotvorba", "image": "https://www.zeriavplus.sk/wp-content/uploads/2022/11/bager-vykopove-prace-liptovsky-mikulas.jpg"},
        {"id": 15, "name": "Daniel", "surname": "Barta", "nickname": "Litwil", "image": "https://img.freepik.com/free-psd/close-up-delicious-apple_23-2151868338.jpg?semt=ais_incoming&w=740&q=80"},
        {"id": 16, "name": "David", "surname": "Skula", "nickname": "Dejvid", "image": "https://news.artnet.com/app/news-upload/2024/03/michelangelo-david-close-getty.jpg"},
        {"id": 17, "name": "Rasto", "surname": "Patak", "nickname": "Chessmaster", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN35oUPDlZ340sJvvDBVUtGpcyVKU_qzLj2g&s"},
        {"id": 18, "name": "Karolina", "surname": "Kmetova", "nickname": "Kaja", "image": "https://images.unsplash.com/photo-1697029749544-ffa7f15f9dd0?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Ym9vayUyMGFlc3RoZXRpY3xlbnwwfHwwfHx8MA%3D%3D"},
        {"id": 19, "name": "Samuel", "surname": "Martis", "nickname": "Zib_zib", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE28Io_jYYBhrQKXEK0DSwbJxHWbnqbWITeg&s"},
        {"id": 20, "name": "Martin", "surname": "Deglovic", "nickname": "Boywithgunsb", "image":"https://airsoftpro.sk/images/stories/virtuemart/product/we-airsoft-pistol-colt-25-ct25-fullmetal-blowback-pink-08.jpg"}
    ]
}

@app.route('/')
def home():
    return jsonify({"message": "Vitajte v studentskom API s fotkami!"})

@app.route('/api')
def get_all_students():
    return jsonify(databaza)

@app.route("/api/student/<int:student_id>")
def get_one_student(student_id):
    # Vyhľadávanie podľa ID
    student = next((s for s in databaza["students"] if s["id"] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student nenajdeny"}), 404

if __name__ == '__main__':
    CORS(app)
    app.run(port=5000, debug=True)