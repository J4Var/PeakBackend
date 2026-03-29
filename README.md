#  Môj Prvý Backend (Študentské API)

Tento projekt je zameraný na vytvorenie jednoduchého **REST API** pomocou frameworku **Flask** a jeho následné prepojenie s moderným frontendom.

---

## 🔗 Dôležité odkazy
* **Frontend (GitHub Pages):** [👉 Klikni sem pre zobrazenie webu]( https://j4var.github.io/PeakBackend/)
* **Lokálne API:** `http://127.0.0.1:5000/api`

---

## 📋 Funkcionalita projektu
* **Backend (Python/Flask):** Server spravujúci databázu 10 študentov.
* **Frontend (HTML/JS):** Moderná aplikácia s "Midnight Soft Dark" dizajnom, ktorý šetrí oči.
* **Dynamické vyhľadávanie:** Filtrovanie študentov v reálnom čase podľa mena, priezviska alebo prezývky.
* **Bonusové body:** Pôvodné `boozeapi` bolo kompletne nahradené mojím vlastným lokálnym backendom.

---

## 🛠️ API Endpoints
| Metóda | Endpoint | Popis |
| :--- | :--- | :--- |
| `GET` | `/` | Uvítacia správa servera |
| `GET` | `/api` | JSON zoznam všetkých študentov |
| `GET` | `/api/student/<id>` | Detail konkrétneho študenta podľa jeho ID |

---

## 🚀 Ako to spustiť u seba?

1.  **Nainštaluj potrebné knižnice:**
    ```bash
    pip install Flask flask-cors
    ```
2.  **Spusti Python server:**
    ```bash
    python Backend.py
    ```
3.  **Otvor web:**
    Jednoducho otvor súbor `index.html` v prehliadači.

---

## 📂 Štruktúra súborov
* `Backend.py` – Flask kód a databáza študentov.
* `index.html` – Štýlový frontend s vyhľadávaním a tmavým režimom.
* `requirements.txt` – Zoznam knižníc potrebných pre beh aplikácie.
* `README.md` – Táto dokumentácia.

---
*Vytvorené pre školskú úlohu z informatiky - marec 2026.*
