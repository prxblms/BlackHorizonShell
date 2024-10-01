import os, sys
import geoip2.database
import geoip2.errors
from colorama import Fore as fg

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASN_DB = os.path.join(BASE_DIR, 'dbs', 'GeoLite2-ASN.mmdb')
COUNTRY_DB = os.path.join(BASE_DIR, 'dbs', 'GeoLite2-Country.mmdb')
CITY_DB = os.path.join(BASE_DIR, 'dbs', 'GeoLite2-City.mmdb')

def banner():
    print(f'''{fg.RED}
            ┌─┐┬─┐─┐ ┬┌┐ ┬  ┌┬┐┌─┐       ┬┌─┐  ┬  ┌─┐┌─┐┬┌─┬ ┬┌─┐
            ├─┘├┬┘┌┴┬┘├┴┐│  │││└─┐  ───  │├─┘  │  │ ││ │├┴┐│ │├─┘
            ┴  ┴└─┴ └─└─┘┴─┘┴ ┴└─┘       ┴┴    ┴─┘└─┘└─┘┴ ┴└─┘┴  
                     Developed by 27prxblms - ver. 2.05''')

class IPLookup:
    def __init__(self):
        self.asn_db = geoip2.database.Reader(ASN_DB)
        self.country_db = geoip2.database.Reader(COUNTRY_DB)
        self.city_db = geoip2.database.Reader(CITY_DB)

    def lookup(self):
        while True:
            os.system('cls')
            os.system('title @27prxblms - IP Lookup')
            banner()
            self.get_input()

    def get_input(self):
        print(f"\n {fg.RED}┌───ͼ 27prxblms ͽ")
        ip = input(F" {fg.RED}└─ͼ {fg.LIGHTWHITE_EX}enter a {fg.LIGHTRED_EX}IP {fg.LIGHTWHITE_EX}or {fg.LIGHTRED_EX}Host: {fg.LIGHTGREEN_EX}")
        if not ip:
            print("\n {fg.LIGHTWHITE_EX}please enter a valid IP or Host!")

        elif ip == 'exit':
            print("\n {fg.LIGHTWHITE_EX}Finishing...")
            sys.exit(0)

        else:
            self.database_search(ip)
            self.wait_action()

    def database_search(self, ip):
        try:
            get_asn = self.asn_db.asn(ip)
            get_country = self.country_db.country(ip)
            get_city = self.city_db.city(ip)

            print(f'''
            {fg.RED}IP: {fg.LIGHTWHITE_EX}{ip}
            {fg.RED}Cidade: {fg.LIGHTWHITE_EX}{get_city.city.name}
            {fg.RED}Estado: {fg.LIGHTWHITE_EX}{get_city.subdivisions.most_specific.name}
            {fg.RED}País: {fg.LIGHTWHITE_EX}{get_country.country.name}
            {fg.RED}Organização: {fg.LIGHTWHITE_EX}{get_asn.autonomous_system_organization}
            {fg.RED}Latitude: {fg.LIGHTWHITE_EX}{get_city.location.latitude}
            {fg.RED}Longitude: {fg.LIGHTWHITE_EX}{get_city.location.longitude}
            ''')

        except geoip2.errors.AddressNotFoundError:
            print(f"\n {fg.LIGHTRED_EX}IP/Host {fg.LIGHTWHITE_EX}not found in our database.")

        except Exception as e:
            print(f"\n {fg.LIGHTWHITE_EX}Error: {fg.LIGHTRED_EX}[ {ip} ] {fg.LIGHTWHITE_EX}does not appear to be an IPv4 or IPv6 address.")
            self.get_input()

    def wait_action(self):
        cmd = input(f"\n {fg.LIGHTWHITE_EX}Press {fg.LIGHTRED_EX}[ enter ] {fg.LIGHTWHITE_EX}for a new search or type {fg.LIGHTRED_EX}[ exit ] {fg.LIGHTWHITE_EX}to close the tool: {fg.LIGHTGREEN_EX}")
        if cmd == 'exit':
            print(f"\n {fg.LIGHTWHITE_EX}Finishing...")
            sys.exit(0)
        else:
            self.lookup()

    def close(self):
        self.asn_db.close()
        self.country_db.close()
        self.city_db.close()

if __name__ == '__main__':
    ip_lookup = IPLookup()
    try:
        ip_lookup.lookup()
    except KeyboardInterrupt:
        print(f"\n {fg.LIGHTWHITE_EX}Finishing...")
        sys.exit(0)
    finally:
        ip_lookup.close()