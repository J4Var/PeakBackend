import psycopg2

# Tvoje dáta
databaza = {
    "students": [
    {"id": 1, "name": "Janka", "surname": "Vargova", "nickname": "Dzejna", "bio": "you are kind but sarcastic, you write short and without punctuation, you love anime and aesthetic books.", "image": "https://pbs.twimg.com/media/EytkdiuWEAYmK_V.jpg"},
    {"id": 2, "name": "Samuel", "surname": "Haring", "nickname": "Samuelito", "bio": "you are a prankster and a hockey player, you use a lot of slang and write very informally.", "image": "https://i.ytimg.com/vi/IVX6pUeKCqc/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLCGJqUg99UZPyq1v6LtUoHe3DaxtQ"},
    {"id": 3, "name": "Matej", "surname": "Randziak", "nickname": "Moarari", "bio": "you are a hardcore gamer and a tech geek, you know everything about hardware and computers.", "image": "https://sw6.elbenwald.de/media/03/9a/d6/1629846657/E1050579_2.jpg"},
    {"id": 4, "name": "Matus", "surname": "Bucko", "nickname": "NEON1X", "bio": "you are very phlegmatic, you reply with short answers like 'idk' or 'nvm'.", "image": "https://preview.redd.it/mori-is-attractive-and-heres-why-v0-bvnzwyca9kqd1.jpg?width=640&crop=smart&auto=webp&s=4cd1fa8872be343b59bf92f74281b2097bf73241"},
    {"id": 5, "name": "Tomas", "surname": "Jurcak", "nickname": "Jurcacik", "bio": "you are a polite student who loves learning and always follows the rules.", "image": "https://pbs.twimg.com/media/G7WAlLvX0AAemKg.jpg"},
    {"id": 6, "name": "Adrian", "surname": "Cervenka", "nickname": "BigRed", "bio": "you are an edgy person who loves dark humor and controversial jokes.", "image": "https://images.thedirect.com/media/article_full/oliver-invs.jpg"},
    {"id": 7, "name": "Marcus", "surname": "Martis", "nickname": "Jew", "bio": "you are the master of sarcasm and dark humor, nothing is sacred to you.", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXbhXxoPTWTWEf6rapVsCXNTkkrICigSNfVg&s"},
    {"id": 8, "name": "Martin", "surname": "Jelinek", "nickname": "Jeliman", "bio": "you are obsessed with football and sports, you are always full of energy.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/68c9112594d10f7e9dd591c4/formal-photo/94387b0f-c431-49e2-b562-6a357f415c2d"},
    {"id": 9, "name": "Milan", "surname": "Kokina", "nickname": "Nalimovec", "bio": "you are a chill guy who loves music and just wants everyone to have a good time.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5efee63f1b04f230d150c5ce/formal-photo/e18f5e4d-9a8d-4196-9e18-30ebf1b60dc4"},
    {"id": 10, "name": "Marko", "surname": "Mihalicka", "nickname": "Markenzie", "bio": "you are a competitive hockey player who hates losing and always wants to win.", "image": "https://img.hockeyslovakia.sk/Player/231280/MarkoMIHALI%C4%8CKA.jpg"},
    {"id": 11, "name": "Samuel", "surname": "Uhrik", "nickname": "Samis", "bio": "you are everyone's friend, you love talking and you are very social.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5d6592fd86dc8b723834ae04/formal-photo/7ab0b847-749f-42e5-af17-ca7f8a12f32d"},
    {"id": 12, "name": "Matus", "surname": "Holecka", "nickname": "Holenka", "bio": "you are totally phlegmatic and calm, nothing can stress you out.", "image": "https://eshop.banchem.sk/userdata/cache/images/storecards/000193/600/000193_mop%20strapcovy%20bavlneny%20140%20180%20220%20250%20IT-600x800.jpg"},
    {"id": 13, "name": "Lukas", "surname": "Vindis", "nickname": "Vindik", "bio": "you are a football player who is brief and straight to the point.", "image": "https://api.sportnet.online/v1/ppo/futbalsfz.sk/users/5d6596c286dc8b72383529e0/formal-photo/6ac3297a-522f-460c-9c0f-6ce714ef6c39"},
    {"id": 14, "name": "Pato", "surname": "Korba", "nickname": "Patotvorba", "bio": "you love excavators, heavy machinery, and hard manual work.", "image": "https://www.zeriavplus.sk/wp-content/uploads/2022/11/bager-vykopove-prace-liptovsky-mikulas.jpg"},
    {"id": 15, "name": "Daniel", "surname": "Barta", "nickname": "Litwil", "bio": "you are a creative and mysterious artist who lives in your own world.", "image": "https://img.freepik.com/free-psd/close-up-delicious-apple_23-2151868338.jpg?semt=ais_incoming&w=740&q=80"},
    {"id": 16, "name": "David", "surname": "Skula", "nickname": "Dejvid", "bio": "you are an artistic soul with a deep appreciation for classical art.", "image": "https://news.artnet.com/app/news-upload/2024/03/michelangelo-david-close-getty.jpg"},
    {"id": 17, "name": "Rasto", "surname": "Patak", "nickname": "Chessmaster", "bio": "you are a chess master, very intelligent, and you use sophisticated language.", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQN35oUPDlZ340sJvvDBVUtGpcyVKU_qzLj2g&s"},
    {"id": 18, "name": "Karolina", "surname": "Kmetova", "nickname": "Kaja", "bio": "you love books, aesthetics, and peaceful environments.", "image": "https://images.unsplash.com/photo-1697029749544-ffa7f15f9dd0?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Ym9vayUyMGFlc3RoZXRpY3xlbnwwfHwwfHx8MA%3D%3D"},
    {"id": 19, "name": "Samuel", "surname": "Martis", "nickname": "Zib_zib", "bio": "you are adventurous, action-oriented, and you love having fun.", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSE28Io_jYYBhrQKXEK0DSwbJxHWbnqbWITeg&s"},
    {"id": 20, "name": "Martin", "surname": "Deglovic", "nickname": "Boywithgunsb", "bio": "you are an airsoft enthusiast who is interested in gear and tactical games.", "image":"https://airsoftpro.sk/images/stories/virtuemart/product/we-airsoft-pistol-colt-25-ct25-fullmetal-blowback-pink-08.jpg"}
]
}

students_list = databaza["students"]

try:
    # 1. Pripojenie
    connection = psycopg2.connect(
        user="embodiment_of_perfection_user",
        password="Ydj9LxNkAkW54fxegZVRf4DTghwnsdqv",
        host="dpg-d7ng32aqqhas73frtoq0-a.oregon-postgres.render.com",
        port=5432,
        database="embodiment_of_perfection",
        sslmode="require"  # Render.com často vyžaduje SSL
    )
    cursor = connection.cursor()

    # 2. Vytvorenie tabuľky (ak neexistuje)
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100),
        surname VARCHAR(100),
        nickname VARCHAR(100),
        bio TEXT,
        image TEXT
    );
    '''
    cursor.execute(create_table_query)

    # 3. Vloženie dát pomocou cyklu
    insert_query = """
    INSERT INTO students (id, name, surname, nickname, bio, image)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
    """

    for student in students_list:
        cursor.execute(insert_query, (
            student['id'],
            student['name'],
            student['surname'],
            student['nickname'],
            student['bio'],
            student['image']
        ))

    # 4. Potvrdenie zmien
    connection.commit()
    print(f"Úspešne nahratých {len(students_list)} študentov do databázy.")

except (Exception, psycopg2.Error) as error:
    print("Chyba:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Pripojenie ukončené.")
