from auth import AOSSAuth
import requests
import json

class get_macs(AOSSAuth):
    def __init__(self, switchip, username, password):
        super().__init__(switchip, username, password)
        url_mactable = "http://" + self.ipaddr + "/rest/" + self.version + "/mac-table"
        try:
            r = requests.get(url_mactable, headers=self.cookie)
            self.mactable = json.loads(r.text)['mac_table_entry_element']
        except requests.exceptions.RequestException as error:
            print("Error:\n" + str(error) + " get_mactable: An Error has occurred")


    def print_mactable(self):
        """
        Function to print mac-address, port id and vlan id in a table
        :param auth: AOSSAuth class object returned by pyarubaoss.auth
        :return prints mac-address table.
        :rtype string
        """
        print('-' * 10)
        print('{:>10}{:>15}{:>15}'.format('MAC-address:', 'Port ID:', 'VLAN ID:'))
        for x in self.mactable:
            print('{:>10}{:>15}{:>15}'.format(x['mac_address'], x['port_id'], str(x['vlan_id'])))