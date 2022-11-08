from starkintro.domain.value_objects import Notification


class IdentityNotification(Notification):
    __name: str
    __tax_id: str
    __tags: dict

    def __init__(self, args: dict):
        self.__name = args.get("name", "")
        self.__tax_id = args.get("tax_id", "")
        self.__tags = args.get("tags", {})

    def name(self):
        return self.__name

    def tax_id(self):
        return self.__tax_id

    def tags(self):
        return self.__tags
