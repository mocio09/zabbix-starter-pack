# zabbix-starter-pack

Repository Structure:

`zabbix_bootrstrap` - Docker compose files used to deploy the Zabbix Server (compose-zabbix-server.yml) and Zabbix Proxy (compose-zabbix-proxy.yml)

`zabbix_hosts` - add_hosts.py - the script used to deploy/remove the hosts via the REST API based on the `hosts_inventory.json` . This way we ensure that the devices stored in the config file are the ones monitored by the server. If someone wants to add/delete a new device it can do it via a GitHub pull request to ensure changes are transparent, verified by a reviewer and that you have a history for them so you can rollback if needed or any other action. 

`secure_zone` - terraform configuration for deploying the 1 VPC, 2 subnets(Public and Private), 1 Internet gateway, 1 security group, In addition, will create Custom Route Tables and associate them with subnets with NAT gateway support. EC2 instances are configured with a startup script in order to enable SNMP service. 