import starkbank
from starkintro.infra.Config import Config


class BaseApp:

    @property
    def _stark_user(self):
        return starkbank.Project(
            environment=Config.STARK_ENVIRONMENT,
            id=Config.STARK_ID,
            private_key=Config.STARK_PRIVATE_KEY
        )
