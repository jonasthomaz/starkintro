from starkintro.handlers.v1 import HandlerABC
from starkintro.application.balance import Balance

class BalanceHandler(HandlerABC):

    @staticmethod
    def get_balance():
        balance = Balance()
        return balance.get_balance()
