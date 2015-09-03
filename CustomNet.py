#!/usr/bin/python

from mininet.topolib import TreeTopo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import sys

x = sys.argv[1]
y = sys.argv[2]
h = []
s = []
def emptyNet():

    "Create an empty network and add nodes to it."
    
    net = Mininet( autoStaticArp=True, link=TCLink )
    
    info( '*** Adding controller\n' )
    net.addController( controller=RemoteController )

    info( '*** Adding hosts\n' )
    for i in range(1,int(x)*int(y)+1):
    	if i%2 != 0:
    	  	ipaddr='10.0.0.'+str(i)
    		print ipaddr
      	  	temp=net.addHost('h'+str(i), ip=ipaddr)
    	  	h.append(temp)
    	else:
    		ipaddr='11.0.0.'+str(i)
    		print ipaddr
    		temp=net.addHost('h'+str(i), ip=ipaddr)
                    h.append(temp)			

    info( '*** Adding switch\n' )
    for i in range(1,int(y)+1):
    	temp = net.addSwitch( 's'+str(i) )
    	s.append(temp)

    info( '***Creating links' )
    
    c = 1
    p = 0
    for i in range(int(x)*int(y)):
    	temp = net.addLink( h[i], s[p] )
    	print "\nadding\n",h[i],s[p]
            if(i%2 == 0):
            	temp.intf1.config(bw=1)	
    	else:
    		temp.intf1.config(bw=2)
    	if c%int(x) == 0:
    		p = p + 1
    	c = c + 1

    for i in range(len(s)-1):
    	net.addLink( s[i], s[i+1])
	
    print "*****",s[i],s[i+1]
    info( '*** Starting network\n')

    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
