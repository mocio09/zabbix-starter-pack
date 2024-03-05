from pyzabbix import ZabbixAPI
import json
import os

# Get configuration for hosts
with open('hosts_inventory.json', 'r') as f:
    local_hosts_config = json.load(f)

zapi = ZabbixAPI("http://18.133.139.129/api_jsonrpc.php")
zapi.login(os.getenv("ZABBIX_LOGIN_USER"), os.getenv("ZABBIX_LOGIN_PASSWORD"))

# Get all Hosts from remote server
remote_hosts_config = zapi.host.get({
    "output": ["hostid", "host"],
    "selectInterfaces": ["interfaceid", "ip", "dns", "type", "main", "useip", "port"],
    "selectGroups": ["groupid", "name"]
})

# Convert lists of dictionaries to sets of tuples
local_set = set((host["hostid"]) for host in local_hosts_config)
remote_set = set((host) for host in remote_hosts_config)

local_only = [d for d in local_set if not any(d == d2 for d2 in remote_hosts_config)]
remote_only = [d for d in remote_hosts_config if not any(d == d1 for d1 in local_set)]

# Find elements in local, but not in remote, these should be added to keep in sync local config in git with remote
local_only = local_set - remote_set

# Find elements in remote but not in local, , these should be deleted to keep in sync local config in git with remote
remote_only = remote_set - local_set

for host in local_only:
    result = zapi.host.create(host)
    print(f"Added host {host}")

for host in remote_only:
    result = zapi.host.delete(host["hostid"])
    print(f"Added host {host}")
