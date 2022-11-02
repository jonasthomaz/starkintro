from flask.views import MethodView
from typing import Union


class HandlerABC(MethodView):
    def response(self, body: Union[dict, str], code: int = 200):
        response = {}
        if body is None:
            code = 404

        if not isinstance(body, str):
            for k, v in body.items():
                response.update({k: self.__prepare(v)})

        return {"data": response, "code": code}, code
