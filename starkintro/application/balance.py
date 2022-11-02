import starkbank
from starkintro.infra.Config import Config


class Balance:

    @property
    def _stark_user(self):
        return starkbank.Project(
            environment=Config.STARK_ENVIRONMENT,
            id=Config.STARK_ID,
            private_key=Config.STARK_PRIVATE_KEY
        )

    def get_balance(self):
        cutomer_balance = starkbank.balance.get(self._stark_user)

        return cutomer_balance.__dict__
