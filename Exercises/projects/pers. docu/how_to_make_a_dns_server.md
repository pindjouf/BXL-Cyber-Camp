# How to make a DNS server
IDK.

I've followed the official documentation from Ubuntu to try and make `google.com` redirect to my server's IP but it doesn't. Instead `google.com` gets some random ipv6 address and a weird domain name assigned to it from I don't know where. Here's what the ping command shows us:
`PING google.com(ams15s44-in-x0e.1e100.net (2a00:1450:400e:80f::200e)) 56 data bytes`
And on WORKSTATION:
`PING google.com (142.251.36.46) 56(84) bytes of data.`
So from the looks of it, i'm guessing it might a google server in Amsterdam. As for WORKSTATION, it doesn't seem affected by the DNS server at all. 

So I will give up the DNS for now and focus on DHCP.

Here are changes I've done so far. (This is for a primary server setup):

I added a DNS zone by editing `/etc/bind/named.conf.local` like so:
```
zone "google.com" {
    type master;
    file "/etc/bind/db.google.com";
};
```

I then used an existing zone file as a template to create the `/etc/bind/db.google.com` file:
```
sudo cp /etc/bind/db.local /etc/bind/db.google.com
```

With that template I created an _A record_ for the base domain, `google.com`. Here's my config for `db.google.com`:
```
;
; BIND data file for google.com
;
$TTL    604800
@       IN      SOA     google.com. esaubukasa.protonmail.com. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL

@       IN      NS      ns.google.com
@       IN      A       192.168.129.34
```
And then a `sudo systemctl restart bind9.service` obviously.
