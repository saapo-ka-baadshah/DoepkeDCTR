import numpy as np

class ModbusTcpClient:
    def __init__(self, uri : str):
        self._client_ip = uri

    def read_holding_registers(self, _baseReg : bytes, _regCount: int, unit : int = 1):
        return(list(np.concatenate((np.random.randint(256, size=_regCount-2), np.random.randint(2, size=2)) , axis=None)))
