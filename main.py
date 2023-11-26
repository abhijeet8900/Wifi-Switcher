from utils import *
from classes.windows import Windows
import platform


def main():
    operatingSystem = platform.system()
    wifi = None
    if operatingSystem == 'Windows':
        wifi = Windows()

    if wifi != None:
        currentNetwork = wifi.getCurrentNetwork()
        log(f'Current network : {currentNetwork.get("SSID")} [{currentNetwork.get("Signal")}]')
        log("Searching available networks...")
        allAvailalbeNetworks = wifi.getAllNetworks()
        log("Getting known networks...")
        knownNetworks = wifi.getKnownNetworks()
        log("Finding best known network...")
        bestNetwork = getBestNetwork(
            currentNetwork, allAvailalbeNetworks, knownNetworks)
        if bestNetwork != None:
            currentSSID = currentNetwork.get("SSID")
            newSSID = bestNetwork.get("SSID")
            if currentSSID != newSSID:
                log(f'Better netwok found : {bestNetwork.get("SSID")} [{bestNetwork.get("Signal")}] ')
                status = connectToNetwork(newSSID)
                if status == 0:
                    wifi.notify(f'Switched to {bestNetwork.get("SSID")}')
            else: 
                log(f'Cannot find better network')
        else: 
            log(f'Cannot find better network')
    else:
        log(f"Operating System : {operatingSystem} is not supported !! ")
    log(f'Exiting....')


if __name__ == "__main__":
    main()
