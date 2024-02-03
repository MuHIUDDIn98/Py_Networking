import scapy.all as scapy
import optparse



def scan(ip):
    #arp request 
    arp_request = scapy.ARP(pdst=ip)     #seding arp packets request to all ip
    # arp_request.show()
    
    
    #broadcast frame
    broadcastFrame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #layer 2 operation broadcast to all layer 2 devices 
    # broadcastFrame.show()
    
    
    #arp+broadcast packet
    arp_request_broadcast = broadcastFrame/arp_request
    # arp_request_broadcast.show()
    #answered_list,unanswered_list = scapy.srp(arp_request_broadcast,timeout=1)
    answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    # print(answered_list.summary())
    
    clients_list =[]
    for element in answered_list:
        #print(element)
        clients_dict={"ip":element[1].psrc,"MAC":element[1].hwsrc}
        clients_list.append(clients_dict)
    
    return clients_list
    
 
#printing ip and MAC 
def print_Scan_result(result_list):
    print("|------------------------------------------|")
    print("| IP\t\t\tMAC Addresses      |")
    print("|------------------------------------------|")
    for client in result_list:
        print("{:16}        {}".format(client['ip'],client['MAC']))
        

#terminal argument collector
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t","--target",help="Target IP/IP range.")
    (options,arguments) = parser.parse_args()
    return options





options = get_arguments()
clinet_list = scan(options.target)
print_Scan_result(clinet_list)


