import unittest
import threading
from src.database import Database 

class TestDatabaseSingleton(unittest.TestCase):
    def test_singleton_instance(self):

        def create_instance():
            return Database('my_db', 'postgres', 'new_password')

        instances = []

        def thread_func():
            instance = create_instance()
            instances.append(instance)

        num_threads = 5
        threads = [threading.Thread(target=thread_func) for _ in range(num_threads)]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        for instance in instances[1:]:
            self.assertIs(instance, instances[0], "Instances are not the same")

if __name__ == "__main__":
    unittest.main()
