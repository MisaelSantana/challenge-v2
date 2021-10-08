from app.apiTools.formatJsonOutput import formatJsonOutput
from app.models import Data

class AliveAPI():
    """Class for validate if API be UP"""

    def aliveAPIObject(self):
        return {"Alive": 1, "HTTPStatus": 200, "Error": {"errorTitle": None, "errorMessage": None}}

#class GetAPIDataBase():
#    """Class for get all data in data base"""

#    def getAPIObject(self):
#        return {"Alive": 1, "HTTPStatus": 200, "Error": {"errorTitle": None, "error Message": None}, "Data": {}}

#class GetAPIDataBase():
#    """Class for get all data in data base"""

#    def getAPIObject(self):
#        return  formatJsonOutput().format({Data})