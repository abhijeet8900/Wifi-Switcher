import os
from logger import log


def getNetworkStrength(signal: str) -> int:
    return int(signal.replace("%", ""))


def getBestNetwork(currentNetwork: dict, allNetworks: list[dict], knownNetworks: list):
    currentSSID = currentNetwork.get("Signal")
    currentStrength = getNetworkStrength(currentSSID)
    bestNetwork = None
    for network in allNetworks:
        SSID = network.get("SSID")
        isKnownNetwork = knownNetworks.count(SSID) > 0
        networkStrength = getNetworkStrength(network.get("Signal"))
        if isKnownNetwork:
            if SSID != currentSSID:
                if networkStrength > currentStrength:
                    if bestNetwork:
                        if networkStrength > getNetworkStrength(bestNetwork.get("Signal")):
                            bestNetwork = network
                    else:
                        bestNetwork = network
    return bestNetwork


def connectToNetwork(ssid: str):
    log(f'Connecting to network : {ssid}')
    os.system(f'''cmd /c "netsh wlan connect name = {ssid}"''')
