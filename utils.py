from decimal import Decimal
import os
from logger import log


def getNetworkStrength(signal: str) -> int:
    return int(signal.replace("%", ""))

def hasBetterBand(current:str = '', new: str = ''):
    currentBand = Decimal(current.replace(" GHz",""))
    newBand = Decimal(new.replace(" GHz",""))
    return newBand > currentBand

def getBestNetwork(currentNetwork: dict, allNetworks: list[dict], knownNetworks: list):
    currentSSID = currentNetwork.get("Signal")
    currentStrength = getNetworkStrength(currentSSID)
    currentBand = currentNetwork.get("Band")
    bestNetwork = None
    for network in allNetworks:
        SSID = network.get("SSID")
        isKnownNetwork = knownNetworks.count(SSID) > 0
        networkStrength = getNetworkStrength(network.get("Signal"))
        networkBand = network.get("Band")
        if isKnownNetwork:
            if SSID != currentSSID:
                if networkStrength > currentStrength or hasBetterBand(currentBand, networkBand): # or better band 
                    if bestNetwork:
                        if networkStrength > getNetworkStrength(bestNetwork.get("Signal")):
                            bestNetwork = network
                    else:
                        bestNetwork = network
    return bestNetwork


def connectToNetwork(ssid: str):
    log(f'Connecting to network : {ssid}')
    return os.system(f'''cmd /c "netsh wlan connect name = {ssid}"''')
