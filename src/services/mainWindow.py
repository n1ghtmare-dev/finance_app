from PySide6.QtWidgets import QLabel
from src.database.database import Database as Database


class MainWindowController:

    db = Database('database/database.db')

    def __init__(self):
        self.total_income: float = 0
        self.total_outcome: float = 0
        self.savings: float = 0
        self.balance: float = 0
        self.update_info()

    def update_info(self) -> None:
        self.total_income = self.get_total_income()
        self.total_outcome = self.get_total_outcome()
        self.savings = self.get_savings()
        self.balance = self.get_balance()

    def set_total_income(self, value: float) -> None:
        self.db.set_total_income(value)

    def set_total_outcome(self, value: float) -> None:
        self.db.set_total_outcome(value)

    def set_savings(self, value: float) -> None:
        self.db.set_savings(value)

    def set_balance(self, value: float) -> None:
        self.db.set_balance(value)

    def get_total_income(self) -> float:
        self.db.get_total_income()
        result = self.db.get_result()[0]
        return result

    def get_total_outcome(self) -> float:
        self.db.get_total_outcome()
        result = self.db.get_result()[0]
        return result

    def get_savings(self) -> float:
        self.db.get_savings()
        result = self.db.get_result()[0]
        return result

    def get_balance(self) -> float:
        self.db.get_balance()
        result = self.db.get_result()[0]
        return result





