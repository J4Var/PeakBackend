# 🚀 Môj Prvý Backend (Študentské API)

Tento projekt je zameraný na vytvorenie jednoduchého **REST API** pomocou frameworku **Flask** a jeho následné prepojenie s frontendovou aplikáciou.

## 🔗 Live Demo & Odkazy
- **Frontend (GitHub Pages):** [KLIKNI SEM PRE ZOBRAZENIE STRÁNKY](https://TVOJE_MENO.github.io/moj_prvy_backend/)
- **Backend API (lokálne):** `http://127.0.0.1:5000/api`

## 📋 Funkcionalita
- **Backend:** Flask server spravujúci databázu 10 študentov.
- **Frontend:** Moderná SPA (Single Page Application) s "Midnight Soft Dark" dizajnom.
- **Vyhľadávanie:** Dynamické filtrovanie v reálnom čase (meno, priezvisko, nickname).
- **Bonus:** Pôvodné `boozeapi` bolo nahradené mojím vlastným lokálnym backendom.

## 🛠️ API Endpoints
| Endpoint | Popis |
| :--- | :--- |
| `/` | Uvítacia správa servera |
| `/api` | JSON zoznam všetkých študentov |
| `/api/student/<id>` | Detail konkrétneho študenta podľa ID |

## 🚀 Inštalácia a spustenie

1. **Inštalácia závislostí:**
   ```bash
   pip install -r requirements.txt
