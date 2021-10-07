from app.apiTools.formatJsonOutput import formatJsonOutput

class Alive():
    """Classe de Alive da API"""

    def makeAliveObject(self):
        return {"Alive": 1, "HTTPStatus": 200, "error": {"errorTitle": None, "errorMessage": None}}

class State():
    """Classe de Status da API"""
    
    def makeAliveObject(self, ApplicationStatus = 1, HTTPStatus = 200, errorTitle = None, errorMessage = None, requestGetData = {}):
        return formatJsonOutput().format({"ApplicationStatus": ApplicationStatus, "HTTPStatus": HTTPStatus, "error": {"errorTitle": errorTitle, "errorMessage": errorMessage}, "requestGetData": requestGetData})

class AliveResponse():
    """Classe de Status da API"""
    def AliveResponseObject(self, TesteAlive = True):
        return formatJsonOutput().format({"TesteAlive": TesteAlive})