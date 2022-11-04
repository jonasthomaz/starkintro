from starkintro.handlers.v1 import HandlerABC
from starkintro.application.deposit import Deposit


class DepositHandler(HandlerABC):
    __application = Deposit()

    def get_deposits(self):
        return self.response(self.__application.get_deposits())

    def get_deposit_by_id(self, id: int):
        return self.response(self.__application.get_deposit(id))

    def get_deposits_logs(self):
        return self.response(self.__application.get_deposits_logs())

    def get_deposits_logs_byid(self, id: int):
        return self.response(self.__application.get_deposit_log(id))
