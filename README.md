Miskatonic est une application web permettant de générer et de gérer des QCM (Questionnaires à Choix Multiples). Le backend est développé avec FastAPI pour sa rapidité et sa simplicité,
tandis que le frontend utilise Flask pour une interface utilisateur intuitive.

Le développement incrémentiel a été plannifié avec Jira. Cette application est monorepo, avec un dossier src/backend et src/frontend.
Le dossier `./documentation` Contient le schéma de la bdd Utilisateurs, un template des questions et questionnaire MongoDB (Models du backend), ainsi que les user-stories.

## Fonctionnalités:

Génération automatique de QCM à partir de modèles prédéfinis.
Interface utilisateur pour la gestion des questions et des réponses
API RESTful pour l'intégration avec d'autres systèmes.
Support de Docker pour une installation et un déploiement simplifiés.

## Lancement:

Création d'un environnement virtuel et installation des dépendances :

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Le script SQLite de création de la Base Utilisateurs se trouve dans `./db/script_creation.sql`, la base est créée lors de la connexion si absente.

Pour exécuter le projet Miskatonic, il suffit d’abord de lancer la base de données MongoDB dans un conteneur Docker à l’aide de la commande `docker-compose up -d`. MongoBD sera exposé sur le port `http://localhost:27018`

Une fois la base en place, le fichier `main.py` permet de démarrer séquenciellement le backend FastAPI puis le frontend Flask en multithread.

```bash
python3 src/main.py
```

L’interface utilisateur est disponible sur `http://localhost:5005`

Le serveur FastAPI, qui expose l’API RESTful et la documentation interactive OpenAPI, est accessible à l’adresse `http://localhost:8000/docs`

Cette configuration permet de gérer facilement les QCM via l’interface web tout en offrant une API intégrable à d’autres systèmes.

la documentation des modèles et des classes/méthodes est au format docstring est peut être consulté avec `pdoc` ; ouvrir le seveur pdac dans le navigateur après lancement :

```bash
pdoc ./src
```

Prérequis:
Python 3.12
Docker

## Details

Des fichiers README spécifiques documentent le backend et le frontend.

[> backend](./src/backend/readme.backend.md)  
[> frontend](./src/frontend/readme.frontend.md)
