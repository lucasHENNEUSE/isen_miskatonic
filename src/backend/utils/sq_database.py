import sqlite3
import os


class Connection:
    connexion = None
    cursor = None

    @classmethod
    def _get_db_path(cls):
        """Détermine le chemin de la base de données."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if "src" in current_dir:
            src_index = current_dir.find("src")
            src_dir = current_dir[: src_index + 3]
            db_dir = os.path.join(src_dir, "db")
        else:
            parent_dir = os.path.dirname(current_dir)
            db_dir = os.path.join(parent_dir, "db")

        return db_dir, os.path.join(db_dir, "utilisateurs.db")

    @classmethod
    def _create_database(cls, db_path, db_dir):
        """Crée la base de données et exécute le script de création."""
        # Créer le répertoire db s'il n'existe pas
        os.makedirs(db_dir, exist_ok=True)

        # Chercher le script de création
        script_path = os.path.join(db_dir, "script_creation.sql")

        if not os.path.exists(script_path):
            print(f"Attention: Script de création non trouvé à {script_path}")
            print("Création d'une base de données vide...")

        # Créer la connexion (cela crée le fichier .db)
        conn = sqlite3.connect(db_path)

        # Exécuter le script de création s'il existe
        if os.path.exists(script_path):
            try:
                with open(script_path, "r", encoding="utf-8") as f:
                    script = f.read()
                conn.executescript(script)
                conn.commit()
                print(
                    f"Base de données créée avec succès à partir du script: {script_path}"
                )
            except Exception as e:
                print(f"Erreur lors de l'exécution du script de création: {e}")
                conn.close()
                raise

        conn.close()

    @classmethod
    def connect(cls):
        if cls.connexion is None:
            try:
                db_dir, db_path = cls._get_db_path()

                # Vérifier si la base de données existe, sinon la créer
                if not os.path.exists(db_path):
                    print(f"Base de données non trouvée à {db_path}")
                    print("Création de la base de données...")
                    cls._create_database(db_path, db_dir)

                # Connexion à la base de données
                cls.connexion = sqlite3.connect(db_path)
                cls.connexion.row_factory = sqlite3.Row

                # Test de la connexion
                cls.connexion.execute("SELECT 1").fetchone()
                print(f"Base de données SQLite connectée: {db_path}")

            except sqlite3.Error as e:
                print(f"Erreur BDD SQLite: {e}")
                cls.connexion = None
                raise
            except Exception as e:
                print(f"Erreur de connexion BDD SQLite: {e}")
                cls.connexion = None
                raise

        if cls.cursor is None and cls.connexion is not None:
            cls.cursor = cls.connexion.cursor()

    @classmethod
    def close(cls):
        if cls.cursor is not None:
            cls.cursor.close()
            cls.cursor = None
        if cls.connexion is not None:
            cls.connexion.close()
            cls.connexion = None
            print("Connexion SQLite fermée")
