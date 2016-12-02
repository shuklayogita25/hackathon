__author__ = 'Yogita Shukla'
import json
import os

with open("sample.json") as json_file:
    json_data = json.load(json_file)

  # first
json_data["featureConfigs"]["features"][2]["firewallRules"]["firewallRules"][0]["protocol"] = "udp"


  #second
json_data["vnics"]["vnics"][2]["portgroupName"] = "EXT_VLAN_201b"

  #third
json_data["featureConfigs"]["features"][5]["ospf"]["enabled"] = "true"
# forth
json_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["holdDownTimer"] =  json_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["holdDownTimer"] +  json_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["keepAliveTimer"]

json_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][1]["holdDownTimer"] =  json_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][1]["holdDownTimer"] +  json_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][1]["keepAliveTimer"]

json_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][2]["holdDownTimer"] =  json_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][2]["holdDownTimer"] +  json_data["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][2]["keepAliveTimer"]

print (json_data)

# # os.remove(filename)
with open("sample.json", "w") as json_file:
    json_file.write(json.dumps(json_data))