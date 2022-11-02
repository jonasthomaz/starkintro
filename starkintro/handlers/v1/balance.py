from starkintro.handlers.v1 import HandlerABC
from starkintro.application.balance import Balance


class BalanceHandler(HandlerABC):
    __application = Balance()

    def get_account_balance(self):
        return self.response(self.__application.get_balance())
