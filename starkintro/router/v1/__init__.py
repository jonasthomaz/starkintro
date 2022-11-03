from flask import Blueprint
from starkintro.handlers.v1.balance import BalanceHandler
from starkintro.handlers.v1.transfer import TransferHandler

v1_blueprint = Blueprint('v1_blueprint', __name__, url_prefix='/v1')
v1_blueprint.add_url_rule("/balance", view_func=BalanceHandler().get_account_balance, methods=["GET"])

v1_blueprint.add_url_rule("/transfer", view_func=TransferHandler().post_create_transfer, methods=["POST"])
