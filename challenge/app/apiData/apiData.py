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

    def consumptionCalculate(self, obj = {}):
        """Function for calculated consumption"""
        returnObject = {}
        returnObject['destino'] = (str(obj['destino']))
        returnObject['km40'] = (float(obj['km40']) / 9)
        returnObject['km60'] = (float(obj['km60']) / 12)
        returnObject['km80'] = (float(obj['km80']) / 14)
        returnObject['km100'] = (float(obj['km100']) / 16)
        return returnObject

    def saveData(self):
        """Function for save Data inputs"""