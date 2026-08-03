class DexmaEngineException(DexmaException):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class DexmaAgentException(DexmaException):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class DexmaServiceException(DexmaException):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
