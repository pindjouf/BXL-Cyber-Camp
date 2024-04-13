# Research

### Why monitor? (simple)

To prevent and/or fix issues in a system

### Why monitor? (extended)

Let's identify why we should care about monitoring a system.

There are many reasons to monitor a system, if you plan on having servers that run services as most companies do. You'll want those to run smoothly because you're likely to rely on them.

So having random outages and services not working is not something you can afford, thus the need for monitoring is ever increasing as we rely on those services more and more.

If you have no way of pinpointing/understanding a problem, there's no way you're ever going to fix it.\
So monitoring allows us to have records of what causes problems in order to fix them/prevent them.


We don't have unlimited resources so making sure we use them as efficiently as possible is of the utmost importance.

**Simple example (resource allocation)**:\
If your media streaming company has 100 kbps upload speed, and from previously acquired data you know that 80 of those should be available at all times because that is what your customer base needs from your servers on average, all your other services (combined) should never go over 20 kbps or you're gonna be decreasing the quality of your service and losing customers as a result of that.


**Simple example (system load)**:\
The same streaming company has been growing lately.\
After looking at the graphs on your system monitoring tool you notice that the system load is getting ridiculously high, the hardware you currently have is never gonna be enough if your company keeps growing at this rate. \
Thanks to that data you will be able to prevent your service being down in the future due to your system failing.

### Simplified Version
Gather data to see if somehting's messed up in your machine. 

1. Get Data
2. Send Alerts
3. Make Report(s)

### How to take care of your system
Your services should stay available, reliable and secure.

### Availability
**How to check what services are up and running?**

- With `systemctl --type=service --state=running`.\
You can omit the `--state=running` flag if you want to see all the services.
- Another option for displaying services is `nmap`. This is oriented more towards your network but is worth mentionning if it is a machine other than your own that you want to monitor. (It also works if you scan your machine)

### Reliability 
**How do you make sure that your services are reliable?**

- Setup 'heartbeat checks' so that you can notice trends and prevent your server from getting pushed to its operational limits.
- Ensuring reliability is all about prevention and quick responses to the common pitfalls of a machine.

### Security
**How can monitoring practices keep your system safe?**

- Setup alerts for when there are too many failed authentication attempts.
- Alerts for failed backups/automated reports.
- Automatically kill processes that are not meant to run.


### What to monitor

For a physical server (one you physically have access to) The most important things that will be relevant in all organizations are CPU & Memory utilization, disk I/O and network performance.\
For a virtual server, database & webserver response time, network bandwidth utilization are gonna be more relevant.\
But remember it all depends on the type of organization and server(s) you have.

#### Some general metrics to aim for
- Staying <= 1.0 system load, Anything above that means that there are processes in queue.

- CPU & Memory (RAM) Utilization: Keep below 70-80% so it never gets too high and allows for those special cases where it does go over our limit. If you kept it at >= 100% everything would get messed up if it even goes 1% too high whereas if you keep it at a reasonable capacity you avoid those problems.

- Disk I/O: Measure the rate of data read from and written to disk. High disk I/O can indicate potential bottlenecks. Aim for balanced disk usage and monitor for any spikes or consistently high levels that may indicate performance issues.

- Network Traffic: Monitor inbound and outbound network traffic to ensure the network is not becoming saturated. Aim for consistent network usage within the capacity of your network infrastructure.

- Response Time: Measure the time it takes for the system to respond to requests. This could include application response times, database query times, or website loading times. Aim for low and consistent response times to ensure a good user experience.

- Error Rates: Keep an eye on the number of errors occurring within your system, such as application errors, disk errors, or network errors. Aim to minimize errors and promptly address any that occur to maintain system stability.

- System Uptime: Monitor the amount of time your system has been running without interruption. Aim for high uptime to ensure reliability and availability.

- Temperature and Hardware Health: Monitor the temperature of critical components such as CPU, GPU, and hard drives. Also, keep an eye on the overall health status of hardware components to prevent failures.

- Resource Allocations and Limits: Ensure that resources are appropriately allocated to different applications and services, and set limits where necessary to prevent resource contention.

## The commands

### General
To get a general overview of your machine you can use tools like the classic `top` and all its variations like: `htop`, `btop`, `atop`, etc...

Most of the `top` variations have specific use cases like `PowerTOP` diagnoses issues with the Linux system’s power consumption and power management for example.\
But since they all come **from** `top` I feel comfortable putting them in this section

### Network-specific
- Tools like `btop/bpytop` can give you some insight into your network interfaces' Download and Upload usage.

- `nethogs` Can show you how much bandwidth individual services are using with the advantage of whoing you the PID directly so you can remove anything that seems suspicious or out of place.\
**example of what it looks like:**
```
NetHogs version 0.8.5-2+b1

    PID USER     PROGRAM                                                                     DEV        SENT      RECEIVED
    675 rbfi     /usr/bin/transmission-daemon                                                eth0      210.506       9.652 KB/sec
    818 rbfi     sshd: rbfi@pts/0                                                            nw0        27.259       1.070 KB/sec
      ? root     192.168.29.15:5920-200.82.112.221:48                                                   0.013       0.013 KB/sec
      ? root     10.28.9.12:5920-200.82.112.221:48                                                      0.000       0.010 KB/sec
      ? root     200.82.112.221:48-10.28.9.12:5920                                                      0.000       0.010 KB/sec

  TOTAL                                                                                                237.778      10.754 KB/sec
```

### User-specific
- `w` + example of what it does: 
```
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
rbfi     pts/0    10.28.9.12       14:08    2.00s  0.07s  0.01s w
```
- `lastlog` + example of what it does:
```
Username         Port     From             Latest
rbfi             pts/0    10.28.9.12       Tue Apr  9 14:08:23 +0200 2024
```
- `last` + example of what it does:
```
rbfi     pts/0        10.28.9.12       Tue Apr  9 14:55   still logged in
rbfi     pts/0        10.28.9.12       Tue Apr  9 14:08 - 14:55  (00:47)
rbfi     pts/0        10.28.9.12       Tue Apr  9 14:07 - 14:08  (00:00)
rbfi     pts/0        10.28.9.12       Tue Apr  9 14:05 - 14:06  (00:01)
rbfi     pts/0        10.28.9.12       Tue Apr  9 14:02 - 14:03  (00:00)
rbfi     pts/0        10.28.9.12       Tue Apr  9 14:00 - 14:01  (00:01)
rbfi     pts/0        10.28.9.12       Tue Apr  9 12:21 - 12:21  (00:00)
rbfi     pts/0        10.28.9.12       Tue Apr  9 12:20 - 12:20  (00:00)
rbfi     pts/0        10.28.9.12       Tue Apr  9 12:20 - 12:20  (00:00)
rbfi     pts/0        10.28.9.12       Tue Apr  9 12:19 - 12:19  (00:00)
rbfi     pts/0        10.28.9.12       Tue Apr  9 10:35 - 10:39  (00:03)
reboot   system boot  5.15.92-1-rbfi   Thu Jan  1 01:00   still running
reboot   system boot  5.15.92-1-rbfi   Thu Jan  1 01:00 - 23:12 (19821+21:12)

wtmp begins Thu Jan  1 01:00:03 1970
```

### Worthy Mentions

- `df` to see all the drives that are mounted on your machine. This can be useful if your machine relies on data stored on an external drive for example. If not properly setup it doesn't get mounted automatically on boot. (Although this specific issue can be fixed like [this](https://unix.stackexchange.com/questions/654952/consistent-auto-mount-of-external-hard-drive))


### Last notes

You will get pretty much the same KPIs from most monitoring tools, so knowing what matters most for **your** specific use cases is gonna be key.\
This is the difference between information and intel.\
Raw data means nothing without a goal.

## Report draft on a media server

### Preamble
The goal is to keep this machine as low-cost, low-consumption as possible since it only has 1-2 client(s) and is supposed to be mostly idle.\
We're gonna be investigating to see if there is any over-consumption of its resources and try to determine why they're happening.

### The machine

I'm gonna be monitoring a remote machine quite similar to the one in this repo [mediapiratestack](https://github.com/pindjouf/mediapiratestack).\
Which has the following services running:

- wireguard vpn
- radarr
- sonarr
- lidarr
- transmission (torrenting client)
- kodi (media center)
- monitorix

### Footnotes

- *Some IPs, services & network interfaces have been altered to protect user privacy.*

## Things that still need to be done
- ### Automatic Email Reports
Before we start checking the performance of the server I want to set something up to know who is logging into my server, by getting alerts (e-mails) Everytime there is a login into the server.\
[docs](https://www.monitorix.org/documentation.html#67)

- ### Report document

