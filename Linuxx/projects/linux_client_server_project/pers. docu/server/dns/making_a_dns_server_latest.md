# How to make a DNS server (caching nameserver)

As it's been mentionned in the title I'm gonna be doing a caching nameserver this time due to all the trouble I had when dealing with a primary server.

The primary server has more to teach I believe but I am running out of time and I have to deliver this ASAP.

So here we go first I have to install dnsutils & bind9
`sudo apt install dnsutils bind9`

Now I'll be editing the bind config file by adding the Google and Clouflare DNS IPs:
`sudo vim /etc/bind/named.conf.local`
```
forwarders {
   8.8.8.8;
   8.8.4.4.;
};

listen-on {any;};
```
Then restart the service like so:
`sudo systemctl restart bind9`

Actually that gives us an error:
`Job for named.service failed because the control process exited with error code.`

So let's check the status of the service.
It says failed with result 'exit-code' I have no idea what that means so let's check something else:
`journalctl -xeu named.service`

I get pretty much the same result. Let's check with the syslog:
`sudo cat /var/log/syslog`

I get the same thing I must have messed up the config file. Let me check again.

My bad it was the wrong file let me put the config in /etc/bind/named.conf.options
Here's what it looks like:
```
options {
        directory "/var/cache/bind";

        // If there is a firewall between you and nameservers you want
        // to talk to, you may need to fix the firewall to allow multiple
        // ports to talk.  See http://www.kb.cert.org/vuls/id/800113

        // If your ISP provided one or more IP addresses for stable
        // nameservers, you probably want to use them as forwarders.
        // Uncomment the following block, and insert the addresses replacing
        // the all-0's placeholder.

        forwarders {
                8.8.8.8;
                8.8.4.4.;
        };

        //========================================================================
        // If BIND logs error messages about the root key being expired,
        // you will need to update your keys.  See https://www.isc.org/bind-keys
        //========================================================================
        dnssec-validation auto;

        listen-on {any;};
        listen-on-v6 { any; };
};
```

Let's restart the service again and see how it goes!\
I get the same error.

Maybe let's remove the fluff and only add the forwarders like they say on the official ubuntu docs.

```
options {
        directory "/var/cache/bind";

        // If there is a firewall between you and nameservers you want
        // to talk to, you may need to fix the firewall to allow multiple
        // ports to talk.  See http://www.kb.cert.org/vuls/id/800113

        // If your ISP provided one or more IP addresses for stable
        // nameservers, you probably want to use them as forwarders.
        // Uncomment the following block, and insert the addresses replacing
        // the all-0's placeholder.

        forwarders {
                8.8.8.8;
                8.8.4.4.;
        };

        //========================================================================
        // If BIND logs error messages about the root key being expired,
        // you will need to update your keys.  See https://www.isc.org/bind-keys
        //========================================================================
        dnssec-validation auto;

        listen-on-v6 { any; };
};
```

Same error.

Perhaps it's an issue with the firewall although I don't see how that would stop me from just restarting the service, let's try that.
bin9 runs on port 53 so:
`sudo netstat -anp | grep dhcp`
doesn't show me the service because it's not running of course but from outside sources, I know it's running on port 53 so let's open that.\
`sudo ufw allow 53/udp`
`sudo ufw status`

We can see now that it has been allowed on our firewall, this is a big reach but we never know let's try to restart the service now...

Same error.\
Gonna have to find solution tomorrow with some external input because I'm at a loss for words.\
This document serves as a testament to my current understanding of the subject.