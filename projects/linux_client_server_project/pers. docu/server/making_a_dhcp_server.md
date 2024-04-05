# How to make a DHCP server

### Setting up the VM...
Alright here we go, first I will make a new VM to have a blank machine.
(Using a bridged adapter on both machines btw)

Probably should've put that in the main readme as well...

Ubuntu server allows you to add openssh pre-installation so I used that, let's do the first ssh into this machine:
`ssh pindjouf@192.168.129.37`
And we're greeted with this beautiful welcome text! \
![alt text](/assets/ssh_greeting.png "Title")
___
### The DHCP (server) part!
I will be following this tutorial: https://www.youtube.com/watch?v=1csFmQeXHlg

First I have to install `isc-dhcp-server` like so: `sudo apt install isc-dhcp-server`.

The next step is to tell my server on which interface it has to listen for the dhcp requests. Here is how I did it: `sudo vim /etc/default/isc-dhcp-server` then I put `enp0s3` for the INTERFACEV4.

Next step is editing the actual global config file for isc-dhcp-server.
so `sudo vim /etc/dhcp/dhcpd.conf` and here is my config:
```
subnet 192.168.129.0 netmask 255.255.255.0 {
  range 192.168.129.100 192.168.129.200;
  option domain-name-servers server.example.org;
  option domain-name "example.org";
  option subnet-mask 255.255.255.0;
  option routers 192.168.129.1;
  option broadcast-address 192.168.129.255;
  default-lease-time 600;
  max-lease-time 7200;
}
```
*Some considerations:*
1. My actual router has a different address that is not on the same subnet, so I'm not sure if I have to put the real one or if this config declares a new virtual default gateway on my server's interface. anyways this wasn't mentioned in the tutorial so I will just follow along for now.
2. My actual subnet mask is 255.255.254.0 OR /23 but I tried that earlier on my old server and it didn't work so I will not reproduce this step!
3. Why this specific address pool? It's in my actual network but I have nothing in that range so I used unallocated hosts to know if it's working or not.
4. I'm not sure if the domain names matter here so I just put what was in the tutorial.

OK so for the last part (on the server-side) `sudo systemctl restart isc-dhcp-server`. \
And after a `sudo systemctl status isc-dhcp-server` we can see that the server is indeed running!
```
● isc-dhcp-server.service - ISC DHCP IPv4 server
     Loaded: loaded (/lib/systemd/system/isc-dhcp-server.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2024-04-04 19:06:15 UTC; 19s ago
       Docs: man:dhcpd(8)
   Main PID: 2221 (dhcpd)
      Tasks: 4 (limit: 3949)
     Memory: 4.5M
        CPU: 17ms
     CGroup: /system.slice/isc-dhcp-server.service
             └─2221 dhcpd -user dhcpd -group dhcpd -f -4 -pf /run/dhcp-server/dhcpd.pid -cf /etc/dhcp/dhcpd.conf enp0s3
```

OK not so fast actually I have to open the port on my server to allow those dhcp requests.
By doing `sudo netstat -anp | grep dhcp` we can see that my dhcp server is running on port 67:
```
udp        0      0 0.0.0.0:67              0.0.0.0:*       2221/dhcpd
raw        0      0 0.0.0.0:1               0.0.0.0:*    7  2221/dhcpd
unix  3      [ ]         STREAM     CONNECTED     28784    2221/dhcpd
unix  2      [ ]         DGRAM      CONNECTED     27906    2221/dhcpd
```

So to make sure the port is open we do:
`sudo ufw allow 67/udp` \
`sudo ufw enable` \
and to check if it's working: \
`sudo ufw status` \
here's what we get:
```
Status: active

To                         Action      From
----------------------------------------------------
67/udp                     ALLOW       Anywhere
67/udp (v6)                ALLOW       Anywhere (v6)
```

So far so good everything's smooth sailing :D
___
### The DHCP (client) part!
Well he didn't do anything in particular for this and it worked perfectly fine in the video, but as I could've guessed it is NOT working for me.

##### There are two reasons I could see for this:
1. I messed up somewhere in the configuration.
2. He has a different network setup for his VMs. (Remember I put mine on a bridged adapter)

# The Day After

Let's explore our options.\
It can't be the VM Network config because out of my only three options:\
1. NAT = Both machines get the exact same IP.
2. Internal Network = My machines don't get IP addresses.
3. Bridged Adapter = hasn't worked in the past but seems like the most viable option.

So it must be something wrong with the DHCP Configuration file.

But it makes sense that the client doesn't start getting his IP from my DHCP server automatically, that would be odd. If that was the case then people could just create the dhcp pools they want, and have you in them. Without any configuration on your device.

So when thinking about this logically the issue must lie in the client, there must be something I can do to tell my WORKSTATION what DHCP server to get his IP from. But what?

This is what I will be researching today.\
I will also have to adapt the DHCP configuration to match my current IP since I am in a different location.\
10.10.0.0 is my network address now.

Also something to take into consideration is the fact that with this bridged adapter, both of these machines are connected to my `wlan0` interface. I'm not sure if that plays a role here but if I remember correctly from my packet tracer days, you can't have more than one connection on an interface. (Might just be on packet tracer though i don't know.)

Ok so let's clarify our potential avenues of exploration to get a clearer view of what we can do now:

1. Find out how to tell WORKSTATION which dhcp server to focus on.
2. Create new interface on my computer to not have both machines on one interface.

After some research option 1 seems like THE solution.
I have to setup the network configuration in virtualbox first!
I have to use a Host-only adapter so that I can put both of my machines on the same network!
![alt text](/assets/vm_net.png)
![alt text](/assets/ubu_net.png)
As we can see our interface has been added but it's down let's bring it up with `sudo ifconfig enp0s8 inet 192.168.56.2 up`
![alt text](/assets/working_net.png)
Perfect!

Now let's adapt the DHCP config to reflect those changes.\
And we can now see our DHCP server is running perfectly.
![alt text](/assets/working_dhcp.png)
I just restarted my machine to see if everything would stay the same but no I have to turn on my interface on every startup so that messes up the dhcp config as well i have to restart that everytime after turning on my interface. I will have to fix that later.

## Now for the client part

I'm assuming all I have to do is to create another VM network config where I say that @ubuserver is my DHCP server and everything will be alright!
![alt text](/assets/dhcp_client.png)
I actually don't know why it is still forcing me to use manual addressing and on the wrong subnet but that's okay because let's look at the actual interface:
![alt text](/assets/dhcp_success.png)
The dhcp server overpowers the glitches of virtualbox!
Here is proof that I am using automatic addressing and that my IP is indeed in the DHCP pool we configured previously.

I now have a functional DHCP server to my name.


### Things that still need to be done:
1. Turn on host-only interface on startup and restart isc-dhcp-server as well.
2. Update the DHCP config to include my DNS server when it's done.


This document serves as a testament to my current understanding of the subject.