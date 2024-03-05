from pyzabbix import ZabbixAPI
import json
import os

with open('hosts_inventory.json', 'r') as f:
    hosts_config = json.load(f)

zapi = ZabbixAPI("http://18.133.139.129/api_jsonrpc.php")
zapi.login(os.getenv("ZABBIX_LOGIN_USER"), os.getenv("ZABBIX_LOGIN_PASSWORD"))


for host in hosts_config:
    result = zapi.host.create(host)
    print(result)
