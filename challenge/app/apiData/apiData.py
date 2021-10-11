from app.apiTools.formatJsonOutput import formatJsonOutput
from app.models import data



class AliveAPI():
    """Class for validate if API be UP"""

    def aliveAPIObject(self):
        return {"Alive": 1, "HTTPStatus": 200, "Error": {"errorTitle": None, "errorMessage": None}}

