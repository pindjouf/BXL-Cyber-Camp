# Monitoring 101

### The first part

The goal for this one is to research how & what to monitor in a Linux system. We want to make sure that all the services on our machines remain available, reliable and secure.

#### Here are examples of a few questions we should answer during this part (we are not limited to this):
- What are the main areas of concern when monitoring a system? (EX: CPU load, disk usage, ...)
    - System load, CPU temperature
- How can you check what are the most memory intensive running processes ?
    - With `htop`.
- What are log files? Where can you find them on a typical Linux system ?
    - They're the history of your machine and you can you can find them in `/var/log`.
- How can you check who where the last connected users, what they did, when they left ?
    - You're mostly gonna find this data in the logs like in /var/log/auth.log for example. There's also commands like `w`, `lastlog`, `last`.
- What are the different metrics of health and performance of a system ?
    - CPU & Memory utilization, CPU temp, disk I/O, network performance, database & webserver response time, network bandwidth utilization...
- How can you check the uptime of a machine ?
    - With the `uptime` command or on your system monitoring tool.
- How can you assess the network traffic ?
    - With you system networking tool, you should have a section that shows your network traffic and usage. It's also possible via a simple tool like `btop`.

### The second part

This is the practical part, where we write reports on the state of the machine with as much relevant data as possible.

### End goal 

Be able to keep track of the state of machines, troubleshoot them to understand errors and in the best cases prevent issues before they even happen!


