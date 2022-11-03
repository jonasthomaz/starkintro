from enum import Enum


class TransferListFilter(Enum):
    CURSOR = 'cursor'
    LIMIT = 'limit'
    FIELDS = 'fields'
    AFTER = 'after'
    BEFORE = 'before'
    TRANSACTIONIds = 'transactionIds'
    STATUS = 'status'
    TAX_ID = 'taxId'
    IDS = 'ids'
    SORT = 'sort'
    TAGS = 'tags'
