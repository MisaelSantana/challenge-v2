import json

class formatJsonOutput():
    """Classe para formatar o output do JSON para web"""
    
    def format(self, jsonData):
        return json.dumps(jsonData)