from starkintro.domain.value_objects import Notification


class TransferNotification(Notification):
    __amount: int
    __tax_id: str
    __name: str
    __bank_code: str
    __branch_code: str
    __account_number: str
    __external_id: str
    __scheduled: str
    __tags: tuple

    def __init__(self, args: dict):
        self.__amount = args.get("amount", 0)
        self.__tax_id = args.get("tax_id", None)
        self.__name = args.get("name", None)
        self.__bank_code = args.get("bank_code", None)
        self.__branch_code = args.get("branch_code", None)
        self.__account_number = args.get("account_number", None)
        self.__external_id = args.get("external_id", None)
        self.__scheduled = args.get("scheduled", None)
        self.__tags = args.get("tag", [])

    def notification_validate(self):
        # Validacao dos campos
        return True

    def amount(self):
        return self.__amount
    def tax_id(self):
        return self.__tax_id

    def name(self):
        return self.__name

    def bank_code(self):
        return self.__bank_code

    def branch_code(self):
        return self.__branch_code

    def account_number(self):
        return self.__account_number

    def external_id(self):
        return self.__external_id

    def scheduled(self):
        return self.__scheduled

    def tags(self):
        return self.__tags

