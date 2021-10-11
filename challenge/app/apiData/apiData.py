from app.apiTools.formatJsonOutput import formatJsonOutput
from app.models import Data


class AliveAPI():
    """Class for validate if API be UP"""

    def aliveAPIObject(self):
        return {"Alive": 1, "HTTPStatus": 200, "Error": {"errorTitle": None, "errorMessage": None}}

    def getAllData(self):
        listValues = []
        for i in Data.objects.values().all():
            listValues.append(i)
        return {"valuesList": listValues}
