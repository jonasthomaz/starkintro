import starkbank
from starkintro.infra.Config import Config
from starkintro.domain.value_objects.transfer_notification import TransferNotification
from starkintro.domain.enumatetor import TransferListFilter
from starkintro.application import BaseApp


class Transfer(BaseApp):

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

    def get_transfers(self):
        return_transfers = {}
        transfers = starkbank.transfer.query(after="2022-11-01", before="2022-11-15", user=self._stark_user)
        for transfer in transfers:
            return_transfers[transfer.id] = transfer.__dict__

        return return_transfers

    def get_transfer_pdf(self, _id: int):
        transfer_info = {}
        transfer = starkbank.transfer.pdf(_id, user=self._stark_user)
        if transfer:
            transfer_info = {"pdf": "pdf gerado com sucesso"}
        return transfer_info

    def get_transfers_log(self):
        return_logs = {}
        logs = starkbank.transfer.log.query(after="2022-11-01", before="2022-11-15", user=self._stark_user)
        for log in logs:
            return_logs[log.id] = log.__dict__

        return return_logs

    def get_transfer_log(self, _id: int):
        return_log = {}
        log = starkbank.transfer.log.get(id=_id, user=self._stark_user)
        if log:
            return_log = {
                "id": log.id,
                "created": log.created,
                "type": log.type
            }

        return return_log
