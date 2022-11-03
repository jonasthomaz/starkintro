from flask import request
from starkintro.handlers.v1 import HandlerABC
from starkintro.application.transfer import Transfer
from starkintro.domain.value_objects.transfer_notification import TransferNotification


class TransferHandler(HandlerABC):
    __application = Transfer()

    def post_create_transfer(self):
        # Cria o obejto de notificação

        notification = TransferNotification(request.json)
        self.__application.create_transfer(notification)

        # Chama a aplicação com a noitificação
        return self.response({"response": "teste"})
