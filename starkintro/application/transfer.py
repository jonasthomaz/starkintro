import starkbank
from starkintro.infra.Config import Config
from starkintro.domain.value_objects.transfer_notification import TransferNotification
from starkintro.domain.enumatetor import TransferListFilter


class Transfer:

    @property
    def _stark_user(self):
        return starkbank.Project(
            environment=Config.STARK_ENVIRONMENT,
            id=Config.STARK_ID,
            private_key=Config.STARK_PRIVATE_KEY
        )

    def create_transfer(self, notification: TransferNotification):
        transfers = starkbank.transfer.create([
            starkbank.Transfer(
                amount=notification.amount(),
                tax_id=notification.tax_id(),
                name=notification.name(),
                bank_code=notification.bank_code(),
                branch_code=notification.branch_code(),
                account_number=notification.account_number(),
                external_id=notification.external_id()
            )
        ], user=self._stark_user)

        for transfer in transfers:
            print(transfer)

    def get_transfer_info(self, id: int, pdf: bool = False):
        ...
