import starkbank
from infra.Config import Config

user = starkbank.Project(
    environment=Config.STARK_ENVIRONMENT,
    id=Config.STARK_ID,
    private_key=Config.STARK_PRIVATE_KEY
)

balance = starkbank.balance.get(user=user)
print(balance)





