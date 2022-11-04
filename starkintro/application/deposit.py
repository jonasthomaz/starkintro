import starkbank
from starkintro.application import BaseApp


class Deposit(BaseApp):

    # GET / v2 / deposit
    def get_deposits(self):
        deposits_return = {}
        deposits = starkbank.deposit.query(
            after="2022-11-01",
            before="2022-11-15",
            user=self._stark_user
        )
        for deposit in deposits:
            deposits_return[deposit.id] = deposit.__dict__

        return deposits_return

    # GET / v2 / deposit /: id
    def get_deposit(self, _id: int):
        deposit_return = {}
        deposit = starkbank.deposit.get(_id, user=self._stark_user)
        if deposit:
            deposit_return = deposit.__dict__
        return deposit_return

    # GET / v2 / deposit / log
    def get_deposits_logs(self):
        deposits_return = {}
        deposits = starkbank.deposit.query(
            after="2022-11-01",
            before="2022-11-15",
            user=self._stark_user
        )
        for deposit in deposits:
            deposits_return[deposit.id] = deposit.__dict__

        return deposits_return

    # GET / v2 / deposit / log /: id
    def get_deposit_log(self, _id: int):
        return_log = {}
        log = starkbank.deposit.log.get(id=_id, user=self._stark_user)
        if log:
            return_log = {
                "id": log.id,
                "created": log.created,
                "type": log.type
            }

        return return_log
