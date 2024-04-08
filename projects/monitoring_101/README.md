# Monitoring 101

### The first part

The goal for this one is to research how & what to monitor in a Linux system. We want to make sure that all the services on our machines remain available, reliable and secure.

#### Here are examples of a few questions we should answer during this part (we are not limited to this):
- What are the main areas of concern when monitoring a system? (EX: CPU load, disk usage, ...)
    - System load, CPU temperature
- How can you check what are the most memory intensive running processes ?
    - s
- What are log files? Where can you find them on a typical Linux system ?
    - They're the history of your machine in a file. You can find them in `/var/log`.
- How can you check who where the last connected users, what they did, when they left ?
    - a
- What are the different metrics of health and performance of a system ?
    - 1
- How can you check the uptime of a machine ?
    - With the `uptime` command
- How can you assess the network traffic ?
    - 1

### The second part

This is the practical part, where we write reports on the state of the machine with as much relevant data as possible.

### End goal 

Be able to keep track of the state of machines, troubleshoot them to understand errors and in the best cases prevent issues before they even happen!

### The machine

I'm gonna be monitoring a remote osmc machine.\
Which has the following services running:

- wireguard vpn
- radarr
- sonarr
- lidarr
- transmission (torrenting client)
- kodi

