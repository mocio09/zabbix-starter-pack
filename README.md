# zabbix-starter-pack

curl --request POST \
  --url 'http://18.133.139.129/api_jsonrpc.php' \
  --header 'Content-Type: application/json-rpc' \
  --data '{"jsonrpc":"2.0","method":"user.login","params":{"username":"Admin","password":"zabbix"},"id":1}'


curl -X POST -H 'Content-Type: application/json-rpc' -d '
{
  "jsonrpc": "2.0",
  "method": "host.get",
  "params": {
    "output": ["hostid", "host"],
    "selectInterfaces": ["interfaceid", "ip", "dns", "type", "main", "useip", "port"],
    "selectGroups": ["groupid", "name"]
  },
  "auth": "1d4f859f35d21a9e81237dcfdbc14b2b",
  "id": 1
}' http://18.133.139.129/api_jsonrpc.php
