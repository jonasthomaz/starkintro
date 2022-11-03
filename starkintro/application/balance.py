import starkbank
from starkintro.application import BaseApp


class Balance(BaseApp):

    def get_balance(self):
        cutomer_balance = starkbank.balance.get(self._stark_user)
        return cutomer_balance.__dict__
