from model.registro import RegistroMeteorologico

class EstacaoMeteorologica:
    def __init__(self, nome, codigo, regiao, uf, latitude, longitude, altitude):
        self._nome = nome if isinstance(nome, str) else None
        self._codigo = codigo if isinstance(codigo, str) else None
        self._regiao = regiao if isinstance(regiao, str) else None
        self._uf = uf if isinstance(uf, str) else None
        self._latitude = latitude if isinstance(latitude, float) else 0
        self._longitude = longitude if isinstance(longitude, float) else 0
        self._altitude = altitude if isinstance(altitude, float) else 0
        self._registros = []

    def __str__(self):
        return (f"Nome da estação: {self._nome} \nCódigo: {self._codigo} \nRegião: {self._regiao} - UF: {self._uf} \nLatitude: {self._latitude} - Longitude: {self._longitude} - Altitude: {self._altitude} \nRelatórios: {len(self._registros)}\n")
    
    @property
    def nome(self):
        return self._nome
    @property
    def codigo(self):
        return self._codigo
    @property
    def regiao(self):
        return self._regiao
    @property
    def uf(self):
        return self._uf
    @property
    def latitude(self):
        return self._latitude
    @property
    def longitude(self):
        return self._longitude
    @property
    def altitude(self):
        return self._altitude
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._nome = valor
        else:
            raise ValueError("O nome deve ser uma string não vazia.")
    @codigo.setter
    def codigo(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._codigo = valor
        else:
            raise ValueError("O código deve ser uma string não vazia.")
    @uf.setter
    def uf(self, valor):
        if isinstance(valor, str) and valor.strip():
            self._uf = valor
        else:
            raise ValueError("A Unidade Federativa deve ser uma string não vazia.")
    @latitude.setter
    def latitude(self, valor):
        if isinstance(valor, float) and valor > 0:
            self._latitude = valor
        else:
            raise ValueError("Insira um valor válido para latitude.")
    @longitude.setter
    def longitude(self, valor):
        if isinstance(valor, float) and valor > 0:
            self._longitude = valor
        else:
            raise ValueError("Insira um valor válido para longitude.")
    @altitude.setter
    def altitude(self, valor):
        if isinstance(valor, float) and valor > 0:
            self._altitude = valor
        else:
            raise ValueError("Insira um valor válido para altitude.")
    

    def adicionar_registro(self, registro: RegistroMeteorologico):
        if isinstance(registro, RegistroMeteorologico):
            self._registros.append(registro)
        else:
            raise TypeError("Só é possível adicionar valores na lista para Registros Metereológicos.")
        
    def obter_registros(self):
        return self._registros
