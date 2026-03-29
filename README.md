# 🎓 Študentský Portál | PeakBackend API

[![GitHub Pages](https://img.shields.io/badge/Live_Demo-Online-blueviolet?style=for-the-badge&logo=github)]([https://j4var.github.io/PeakBackend/](https://j4var.github.io/PeakBackend/))


Vitajte v modernom rozhraní pre správu študentskej databázy. Tento projekt demonštruje prepojenie vlastného Python backendu s responzívnym frontendom v elegantnom "Midnight" vizuále.

---

## 🛰️ O Projekte
Tento projekt je finálnym zadaním na tému **Fullstack Vývoj**. Cieľom bolo vytvoriť kompletný ekosystém: od vlastného API servera v Pythone až po dynamické klientske rozhranie, ktoré tieto dáta spracováva.

### Hlavné funkcie:
* **Vlastné Flask API:** Server bežiaci na porte 5000, ktorý poskytuje dáta vo formáte JSON.
* **Midnight Soft Design:** Tmavé rozhranie šetriace oči s plynulými prechodmi a modernou typografiou.
* **Full CRUD Ready:** Architektúra pripravená na prezeranie celého zoznamu aj konkrétnych detailov študentov.
* **Live Filtering:** Okamžité vyhľadávanie v databáze bez nutnosti obnovovať stránku.

---

## 🛠️ Použité technológie
* **Python (Flask)** – Srdce backendu a správa routovania.
* **Flask-CORS** – Zabezpečenie komunikácie medzi rôznymi doménami.
* **JavaScript (ES6)** – Asynchrónny `fetch` a dynamická manipulácia s DOM.
* **CSS3** – Moderný Dark Mode vizuál s využitím Flexboxu a CSS Grid.
* **GitHub Pages** – Hosting pre klientsku časť aplikácie.

---

## 🧠 Ako to funguje? (Technické okienko)

Na rozdiel od predošlých zadaní, kde sme dáta čerpali z externého `boozeapi`, tento projekt využíva **môj vlastný lokálny backend**. Frontend posiela požiadavky na lokálnu adresu, prijme JSON objekt so študentmi a pomocou cyklu `forEach` vygeneruje interaktívne karty.

```python
# Ukážka backend logiky (Flask)
@app.route('/api')
def get_students():
    return jsonify(databaza)
