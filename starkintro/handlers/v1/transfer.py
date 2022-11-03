from flask import request
from starkintro.handlers.v1 import HandlerABC
from starkintro.application.transfer import Transfer
from starkintro.domain.value_objects.transfer_notification import TransferNotification


class TransferHandler(HandlerABC):
    __application = Transfer()

    def post_create_transfer(self):
        notification = TransferNotification(request.json)
        self.__application.create_transfer(notification)
        return self.response({"response": "teste"})

    def get_transfers(self):
        return self.response(self.__application.get_transfers())

    def get_transfer_info(self, id: int):
        return self.response(self.__application.get_transfer_info(id))

    def get_transfer_pdf(self, id: int):
        return self.response(self.__application.get_transfer_pdf(id))

    def get_transfer_log(self: int):
        ...

    def get_transfer_log_byid(self, id: int):
        ...
