import json
import unittest
from src.database import Database
from tests.test_database import TestDatabaseSingleton

def load_config(config_path):
    try:
        with open(config_path) as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print("Config file not found.")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON format in config file.")
        return None

def run_tests():
    unittest.main()

def main():
    config_path = 'config/config.json'
    config = load_config(config_path)
    if config:
        db_name = config.get('db_name')
        user = config.get('user')
        password = config.get('password')

        if db_name and user and password:
            db = Database(db_name, user, password)

            # db.execute_query("CREATE TABLE IF NOT EXISTS test(id serial, name text, age integer)")

            # Run tests
            run_tests()

            db.close_connection()
        else:
            print("Incomplete configuration. Please provide db_name, user, and password in the config file.")
    else:
        print("Failed to load configuration.")

if __name__ == "__main__":
    main()
