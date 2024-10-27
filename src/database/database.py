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
                    query, params, fetch = self.query_queue.get(timeout=1)
                    try:
                        cursor.execute(query, params)
                        connection.commit()
                        if fetch == "one":
                            self.result_queue.put(cursor.fetchone())
                        else:
                            self.result_queue.put(cursor.fetchall())
                    except sqlite3.Error as e:
                        self.result_queue.put(e)
                except Empty:
                    continue


    def execute_query(self, query, params=(), fetch="all"):
        self.query_queue.put((query, params, fetch))

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

    def get_transaction_type(self, transaction_type):
        sql = "SELECT * FROM transaction_types WHERE type = ?"
        self.execute_query(sql, params=(transaction_type,), fetch="one")

    def set_total_income(self, value):
        sql = "UPDATE info SET total_income = ?"
        self.execute_query(sql, params=(value,))

    def set_total_outcome(self, value):
        sql = "UPDATE info SET total_outcome = ?"
        self.execute_query(sql, params=(value,))

    def set_savings(self, value):
        sql = "UPDATE info SET savings = ?"
        self.execute_query(sql, params=(value,))

    def set_balance(self, value):
        sql = "UPDATE info SET balance = ?"
        self.execute_query(sql, params=(value,))

    def get_total_income(self):
        sql = "SELECT total_income FROM info"
        self.execute_query(sql, fetch="one")

    def get_total_outcome(self):
        sql = "SELECT total_outcome FROM info"
        self.execute_query(sql, fetch="one")

    def get_savings(self):
        sql = "SELECT savings FROM info"
        self.execute_query(sql, fetch="one")

    def get_balance(self):
        sql = "SELECT balance FROM info"
        self.execute_query(sql, fetch="one")

    def get_all_outcome(self):
        sql = "SELECT * FROM transactions WHERE amount < 0"
        self.execute_query(sql, fetch="all")

    def get_all_transaction_types(self):
        sql = "SELECT * FROM transaction_types"
        self.execute_query(sql, fetch="all")
