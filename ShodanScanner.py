import shodan
import sys
import socket
import os
import urllib3
import json

API_KEY = input("Enter api key")
api = shodan.Shodan(API_KEY)

#Search the target by their IP address
def HostIP():
    IP = input("Enter target's IP address: ")
    hostinfo = api.host(IP)

    print("""
IP: {}
Organisation: {}
Operating System: : {}""".format(hostinfo['ip_str'], hostinfo.get('org', 'n/a'), hostinfo.get('os', 'n/a')))
    print("Country: {}".format(hostinfo['country_name']))


    for item in hostinfo ['data']: 
        print(""" 
Hostname: {}
Open ports: {}""".format(item['hostnames'], item['port']))     


#Search the target by their hostname
def ShodanScan():   
    try:
        target = input("Enter the target's hostname: ")
        results = api.search(target)
        print("Results found: {}".format(results['total']))

        for results in results['matches']:
            print('IP: {}'.format(results['ip_str']))
            hostinfo = api.host(results['ip_str'])
            print("Country: {}".format(hostinfo['country_name']))

            for results in hostinfo['data']:
                print("""
Hostname: {} 
Open ports: {}""".format(results['hostnames'], results['port']))
            print('----------------------')


    except shodan.APIError as e:
        print('Error: {}'.format(e))

def MyIP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("your IP address: ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 

choice = 1
while choice != 0:
    choice = int(input("""_________________________________
Enter 1 - To get your IP.
Enter 2 - To scan a specific IP address.
Enter 3 - To Shodan scan using hostname.
Enter 0 - To exit the script.

INPUT: """))

    if choice == 1:
        MyIP()
    elif choice == 2:
        HostIP()
    elif choice == 3:
        ShodanScan()
        
if choice == 0:
    print("-----------------EXITTING PROGRAM---------------")


