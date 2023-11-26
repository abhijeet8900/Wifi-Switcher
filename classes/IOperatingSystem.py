from abc import ABC, abstractmethod
class IOperatingSystem(ABC):

    @abstractmethod
    def runCommand(self, command: str) -> list[str]:
        pass

    @abstractmethod
    def getAllNetworks() -> list[dict]:
        pass

    @abstractmethod
    def getNetworkInterfaces() -> list[dict]:
        pass

    @abstractmethod
    def getCurrentNetwork() -> dict:
        pass

    @abstractmethod
    def getKnownNetworks() -> list[dict]:
        pass


