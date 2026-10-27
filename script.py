class Device:
    def __init__(self, hostname='unknown', mgmt_ip='0.0.0.0', vendor='unknown', status='unknown'):
        print('Device object created!')
        self.hostname = hostname
        self.mgmt_ip = mgmt_ip
        self.vendor = vendor
        self.status = status

    def show(self):
        print(f'Hostname: {self.hostname}')
        print(f'Ip: {self.mgmt_ip}')
        print(f'Vendor: {self.vendor}')
        print(f'Status: {self.status}')

    def ping(self):
        print(f'Pinging {self.hostname} at {self.mgmt_ip}...')

    def backup_config(self):
        print(f'Backing up {self.hostname}  ({self.vendor})...')


class Router(Device):
    def __init__(self, hostname, mgmt_ip, vendor, status, routing_proto, interfaces, ospf_area):
        super().__init__(hostname, mgmt_ip, vendor, status)
        self.routing_proto = routing_proto
        self.interfaces = interfaces
        self.ospf_area = ospf_area

    def show(self):
        super().show()
        print(f'Routing protocol: {self.routing_proto}')
        print(f'Interfaces: {self.interfaces}')
        print(f'Ospf Area: {self.ospf_area}')

    def health_check(self):
        print(f'Health check: {self.status}')


class Switch(Device):
    def __init__(self, hostname, mgmt_ip, vendor, status, vlan_list, stp_enable):
        super().__init__(hostname, mgmt_ip, vendor, status)
        self.vlan_list = vlan_list
        self.stp_enable = stp_enable

    def show(self):
        super().show()
        print(f'Vlan List: {self.vlan_list}')
        print(f'Stp Enable: {self.stp_enable}')

    def health_check(self):
        print(f'Health check: {self.status}')


class Firewall(Device):
    def __init__(self, hostname, mgmt_ip, vendor, status, access_rule, zone_pairs, nat_rules):
        super().__init__(hostname, mgmt_ip, vendor, status)
        self.access_rule = access_rule
        self.zone_pairs = zone_pairs
        self.nat_rules = nat_rules

    def show(self):
        super().show()
        print(f'Access rule : {self.access_rule}')
        print(f'Zone Pairs: {self.zone_pairs}')
        print(f'Nat Rules: {self.nat_rules}')

    def health_check(self):
        print(f'Health check: {self.status}')



router1 = Router('R1', '192.168.1.1', 'Cisco', 'UP', 'OSPF', ['eth0', 'eth1', 'eth2'], 0)

switch1 = Switch('SW1', '192.168.1.2', 'Cisco', 'UP', [10, 20, 30, 99], True)

firewall1 = Firewall('FW1', '192.168.1.3', 'Fortinet', 'UP', ['permit tcp any any eq 80'], [('inside', 'outside')], ['inside -> outside PAT'])

devices = [router1, switch1, firewall1]

for device in devices:
    print(f'\n-- {type(device).__name__} --')
    device.show()
    device.ping()
    device.backup_config()
    device.health_check()
