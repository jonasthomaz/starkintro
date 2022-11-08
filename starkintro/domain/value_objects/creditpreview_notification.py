from starkintro.domain.value_objects import Notification


class CreditPreviewNotification(Notification):
    __initial_amount: int
    __initial_due: str
    __interval: str
    __nominal_amount: int
    __nominal_interest: float
    __rebate_amount: int
    __scheduled: str
    __tax_id: str
    __type: str

    def __init__(self, args: dict):
        self.__initial_amount = args.get("initial_amount", 0)
        self.__initial_due = args.get("initial_due", "")
        self.__interval = args.get("interval", "")
        self.__nominal_amount = args.get("nominal_amount", 0)
        self.__nominal_interest = args.get("nominal_interest", 0)
        self.__rebate_amount = args.get("rebate_amount", 0)
        self.__scheduled = args.get("scheduled", "")
        self.__tax_id = args.get("tax_id", "")
        self.__type = args.get("type", "")

    def initial_amount(self):
        return self.__initial_amount

    def initial_due(self):
        return self.__initial_due

    def interval(self):
        return self.__interval

    def nominal_amount(self):
        return self.__nominal_amount

    def nominal_interest(self):
        return self.__nominal_interest

    def rebate_amount(self):
        return self.__rebate_amount

    def scheduled(self):
        return self.__scheduled

    def tax_id(self):
        return self.__tax_id

    def type(self):
        return self.__type
