from model.registro import RegistroMeteorologico

class Estatisticas:
    def __init__(self, registros: list):
        self._registros = registros if isinstance(registros, list) else []

    @property
    def registros(self):
        return self._registros
    
    @registros.setter
    def registros(self, valor):
        if isinstance(valor, list) and all(isinstance(rm, RegistroMeteorologico) for rm in valor):
            self._registros = valor
        else:
            raise ValueError("Tem que ser uma lista de RegistroMeteorologico.")
        
    def media_temperatura(self):
        if not self._registros:
            return 0.0
        return sum(rm.temperatura for rm in self._registros) / len(self._registros)
    
    def max_umidade(self):
        if not self._registros:
            return 0.0
        return max(rm.umidade for rm in self._registros)
    
    def total_precipitacao(self):
        if not self._registros:
            return 0.0
        return sum(rm.precipitacao for rm in self._registros)
