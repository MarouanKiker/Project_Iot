# Cold Chain Monitoring — Projet IoT

Surveillance de la chaîne du froid pour laboratoire d'analyse médicale.

## Stack technique
- **Backend** : Django 6.1.2 + Django REST Framework
- **Base de données** : SQLite
- **Hardware** : ESP8266 NodeMCU + Capteur DHT11
- **Alertes** : Gmail (SMTP) + Telegram Bot
- **Dashboard** : HTML/CSS/JS (ApexCharts)

## Installation

```bash
# 1. Cloner le projet
git clone https://github.com/MarouanKiker/Project_Iot.git
cd Project_Iot

# 2. Créer l'environnement virtuel
python -m venv .venv
.\.venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
cp .env.example .env
# Remplir .env avec vos vraies valeurs

# 5. Appliquer les migrations
python manage.py migrate

# 6. Lancer le serveur
python manage.py runserver 0.0.0.0:8000
```

## Configuration ESP8266
Modifier `esp8266_dht11/esp8266_dht11.ino` :
- `WIFI_SSID` / `WIFI_PASSWORD` : identifiants Wi-Fi
- `SERVER_URL` : adresse IP du PC sur le réseau local

## Endpoints API
| Méthode | URL | Description |
|---------|-----|-------------|
| GET | `/list/` | Récupérer toutes les mesures |
| POST | `/post/` | Enregistrer une nouvelle mesure |
| GET/POST | `/admin/` | Interface d'administration Django |

## Norme médicale
Conservation des réactifs et poches de sang : **2°C – 8°C**  
Alerte déclenchée si la température dépasse le seuil configuré dans `.env`.
