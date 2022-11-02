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
        self.__tax_id = args.get("amount", None)
        self.__name = args.get("amount", None)
        self.__bank_code = args.get("amount", None)
        self.__branch_code = args.get("amount", None)
        self.__account_number = args.get("amount", None)
        self.__external_id = args.get("amount", None)
        self.__scheduled = args.get("amount", None)
        self.__tags = args.get("amount", [])

    def notification_validate(self):
        ...
