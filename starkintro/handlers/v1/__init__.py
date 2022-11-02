from flask.views import MethodView


class HandlerABC(MethodView):

    def response(self, body: dict, code: int = 200):
        return {"data": body, "code": code}, code
