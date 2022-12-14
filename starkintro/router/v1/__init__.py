from flask import Blueprint
from starkintro.handlers.v1.balance import BalanceHandler
from starkintro.handlers.v1.transfer import TransferHandler
from starkintro.handlers.v1.deposit import DepositHandler

v1_blueprint = Blueprint('v1_blueprint', __name__, url_prefix='/v1')
v1_blueprint.add_url_rule("/balance", view_func=BalanceHandler().get_account_balance, methods=["GET"])

v1_blueprint.add_url_rule("/transfers", view_func=TransferHandler().get_transfers, methods=["GET"])
v1_blueprint.add_url_rule("/transfers/log", view_func=TransferHandler().get_transfers_log, methods=["GET"])
v1_blueprint.add_url_rule("/transfer", view_func=TransferHandler().post_create_transfer, methods=["POST"])
v1_blueprint.add_url_rule("/transfer/<id>", view_func=TransferHandler().get_transfer_info, methods=["GET"])
v1_blueprint.add_url_rule("/transfer/<id>/pdf", view_func=TransferHandler().get_transfer_pdf, methods=["GET"])
v1_blueprint.add_url_rule("/transfer/<id>/log", view_func=TransferHandler().get_transfer_log_byid, methods=["GET"])

v1_blueprint.add_url_rule("/deposits", view_func=DepositHandler().get_deposits, methods=["GET"])
v1_blueprint.add_url_rule("/deposits/<id>", view_func=DepositHandler().get_deposit_by_id, methods=["GET"])
v1_blueprint.add_url_rule("/deposits/logs", view_func=DepositHandler().get_deposits_logs, methods=["GET"])
v1_blueprint.add_url_rule("/deposits/<id>/logs", view_func=DepositHandler().get_deposits_logs_byid, methods=["GET"])
