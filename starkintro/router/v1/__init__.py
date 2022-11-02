from flask import Blueprint
from starkintro.handlers.v1.balance import BalanceHandler

v1_blueprint = Blueprint('v1_blueprint', __name__, url_prefix='/v1')
v1_blueprint.add_url_rule("/balance", view_func=BalanceHandler.get_balance, methods=["GET"])
