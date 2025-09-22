class RegistroMeteorologico:
    def __init__(self, data, hora, temperatura, umidade, precipitacao):
        self._data = data if isinstance(data, str) else None
        self._hora = hora if isinstance(hora, str) else None
        self._temperatura = temperatura if isinstance(temperatura, (int, float)) else 0
        self._umidade = umidade if isinstance(umidade, (int, float)) else 0
        self._precipitacao = precipitacao if isinstance(precipitacao, (int, float)) else 0
    
    def __str__(self):
        return (f"Data: {self.data} \n"
            f"Hora: {self.hora} \n"
            f"Temperatura: {self.temperatura}°C \n"
            f"Umidade: {self.umidade}% \n"
            f"Precipitação: {self.precipitacao}mm")
    
    @property
    def data(self):
        return self._data
    @property
    def hora(self):
        return self._hora
    @property
    def temperatura(self):
        return self._temperatura
    @property
    def umidade(self):
        return self._umidade
    @property
    def precipitacao(self):
        return self._precipitacao
    
    @data.setter
    def data(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._data = valor
        else:
            raise ValueError("O data deve ser uma string não vazia.")
    @hora.setter
    def hora(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._hora = valor
        else:
            raise ValueError("O código deve ser uma string não vazia.")
    @temperatura.setter
    def temperatura(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._temperatura = valor
        else:
            raise ValueError("Insira um valor válido para temperatura.")
    @umidade.setter
    def umidade(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._umidade = valor
        else:
            raise ValueError("Insira um valor válido para umidade.")
    @precipitacao.setter
    def precipitacao(self, valor):
        if isinstance(valor, (int, float)) and valor >= 0:
            self._precipitacao = valor
        else:
            raise ValueError("Insira um valor válido para precipitacao.")
