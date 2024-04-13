# The doc monitor script

*note this is still very much a work in progress*

What matters in this case is that my data usage doesn't get reach its monthly limit so I want to make sure I get regular reports that tell me how much I've used so far.

At first I wanted to use curl to get that information from my ISP but for some reason it won't work even though I have tried using the -u flag to authenticate and also tried with a curl to python script that included everything in the cookies.

So now I will make my own solution to solve this problem.

A few things I want to keep track of:


Here's what a report can look like:
```
		#######################################################
		# Server Monitoring Report - Sat Apr 13 13:47:25 2024 #
		#######################################################
## Weather
Waterloo, Belgium: ☀️   +19°C
Don't forget to touch grass after your computer work, it's a good day to be alive :D

## OS Information
  Hostname: watermelon
  Architecture: aarch64
  Kernel: 6.8.4-arch1-1

## State of your services
  UNIT                               LOAD      ACTIVE SUB     DESCRIPTION
  cron.service                       loaded    active running Regular background program processing daemon
  jackett.service                    loaded    active running Jackett Daemon
  lidarr.service                     loaded    active running Lidarr Daemon
  mediacenter.service                loaded    active running media center application
  monitorix.service                  loaded    active running Monitorix
  nmbd.service                       loaded    active running Samba NMB Daemon
  radarr.service                     loaded    active running Radarr Daemon
  samba.service                      loaded    active exited  Samba Server
  smbd.service                       loaded    active running Samba SMB Daemon
  sonarr.service                     loaded    active running Sonarr Daemon
  transmission.service               loaded    active running Transmission BitTorrent Daemon
  wg-quick@wg0.service               loaded    active exited  WireGuard via wg-quick(8) for wg0

## This Month's Bandwidth Usage
Bandwidth Usage: 2.94 TB / 6 TB

## Internet Connectivity
  Status: Connected

## IP Addresses
  Local IP: 192.168.12.5
  Public IP: 116.196.141.111

## DNS Server
::1
127.0.0.1

## Memory Usage
Memory: 750MiB / 3793MiB

## CPU Usage
CPU  %USER  %SYSTEM  %IDLE
*    5.3%   0.8%     93.5%
0    2.7%   0.6%     96.5%
1    6.7%   0.9%     91.9%
2    6.3%   0.9%     92.3%
3    5.5%   0.9%     93.2%

## Storage Usage
Used: 48%
Left: 490G

## Uptime
1 day

## Torrent List
 Name
archlinux-2024.04.01-x86_64.iso Idle
```