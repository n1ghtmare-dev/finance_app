from queue import Queue, Empty
from threading import Thread
import sqlite3


class Database:
    def __init__(self, file_name):
        self.running = True
        self.query_queue = Queue()
        self.result_queue = Queue()
        self.file_name = file_name
        self.work_thread = Thread(target=self._process_queries)
        self.work_thread.start()

    def _process_queries(self):
        connection = sqlite3.connect(self.file_name)
        cursor = connection.cursor()
        with connection:
            while self.running:
                try:
                    query, params = self.query_queue.get(timeout=1)
                    try:
                        cursor.execute(query, params)

                        connection.commit()
                        self.result_queue.put(cursor.fetchall())
                    except sqlite3.Error as e:
                        self.result_queue.put(e)
                except Empty:
                    continue


    def execute_query(self, query, params=()):
        self.query_queue.put((query, params))

    def get_result(self, timeout=1):
        try:
            return self.result_queue.get(timeout=timeout)
        except Empty:
            return None

    def close(self):
        self.running = False
        self.work_thread.join()

    def get_all_transactions(self):
        sql = "SELECT * FROM transactions"
        self.execute_query(sql)