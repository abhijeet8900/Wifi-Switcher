
import subprocess
from .IOperatingSystem import IOperatingSystem


class Windows(IOperatingSystem):

    def runCommand(self, command):
        output = []
        commandList = command.split(" ")
        commandOutput = subprocess.check_output(
            commandList)
        commandOutput = commandOutput.decode("ascii")  # needed in python 3
        commandOutput = commandOutput.replace("\r", "")
        commandOutput = commandOutput.split("\n")
        for line in commandOutput:
            line = line.strip()
            if len(line) > 1:
                output.append(line)
        return output

    def getAllNetworks(self) -> list[dict]:
        commandOutput = self.runCommand("netsh wlan show network mode=Bssid")
        commandOutput = commandOutput[2:]
        networks = []
        network = {}
        for index, line in enumerate(commandOutput):
            commandLine = line.strip()
            tokens = commandLine.split(":")
            if commandLine.startswith("SSID") and index > 0:
                networks.append(network)
                network = {}
            if len(tokens) == 2:
                key = tokens[0].strip()
                if key.startswith("SSID"):
                    key = "SSID"
                value = tokens[1].strip()
                network[key] = value
        networks.append(network)
        return networks

    def getNetworkInterfaces(self):
        commandOutput = self.runCommand("netsh wlan show interfaces")
        commandOutput = commandOutput[1:]
        interfaces = []
        interface = {}
        for index, line in enumerate(commandOutput):
            line = line.strip()
            tokens = line.split(":")
            if line.startswith("Name") and index > 0:
                interfaces.append(interface)
                interface = {}
            if len(tokens) == 2:
                key = tokens[0].strip()
                value = tokens[1].strip()
                interface[key] = value
        interfaces.append(interface)
        return interfaces

    def getCurrentNetwork(self):
        currentNetwork = {}
        interfaces = self.getNetworkInterfaces()
        filteredInterfaces = list(
            filter(lambda interface: interface.get("Name") == "Wi-Fi", interfaces))
        if len(filteredInterfaces) > 0:
            wlanInterface = filteredInterfaces[0]
            currentNetwork["SSID"] = wlanInterface.get("SSID")
            currentNetwork["State"] = wlanInterface.get("State")
            currentNetwork["Signal"] = wlanInterface.get("Signal")
            currentNetwork["Profile"] = wlanInterface.get("Profile")
            currentNetwork["Authentication"] = wlanInterface.get(
                "Authentication")
            currentNetwork["Network type"] = wlanInterface.get("Network type")
            currentNetwork["Authentication"] = wlanInterface.get(
                "Authentication")
            currentNetwork["Signal"] = wlanInterface.get("Signal")
            currentNetwork["Radio type"] = wlanInterface.get("Radio type")
            currentNetwork["Band"] = wlanInterface.get("Band")
            currentNetwork["Channel"] = wlanInterface.get("Channel")
            currentNetwork["Basic rates (Mbps)"] = wlanInterface.get(
                "Basic rates (Mbps)")
            currentNetwork["Other rates (Mbps)"] = wlanInterface.get(
                "Other rates (Mbps)")
            return currentNetwork
        return None

    def getKnownNetworks(self) -> list:
        commandOutput = self.runCommand("netsh wlan show profiles")
        commandOutput = commandOutput[6:]
        networkProfiles = []
        for line in commandOutput:
            line = line.strip()
            profileName = line.replace("All User Profile     :", "")
            profileName = profileName.strip()
            networkProfiles.append(profileName)
        return networkProfiles
