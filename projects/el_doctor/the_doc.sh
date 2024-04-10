#!/bin/bash

# Date and Time
echo "		#######################################################
		# Server Monitoring Report - $(date +%c) #
		#######################################################"

echo "## Weather"
curl -s wttr.in/?format=3
temp=$(curl -s wttr.in/?format=3 | awk '{print $4}' | grep -o '[0-9]*')
if [ "$temp" -gt 15 ]; then
    echo "Don't forget to touch grass after your computer work, it's a good day to be alive :D"
else
    echo "Maybe the weather will be better tomorrow :("
fi

# OS Information
echo ""
echo "## OS Information"
echo "  Hostname: $(hostname | cut -f 1 -d.)"
echo "  Architecture: $(uname -m)"
echo "  Kernel: $(uname -r)"

# Services
echo ""
echo "## State of your services"
systemctl --type=service | grep -E -i 'lidarr|sonarr|radarr|transmission|jackett|samba|wg|monitorix|mediacenter|cron|description'

# Internet Connectivity
echo ""
echo "## This Month's Bandwidth Usage
USED		LEFT
4.20 Tb		1.80 Tb
"

# Internet Connectivity
echo ""
echo "## Internet Connectivity"
ping -c 1 google.com &> /dev/null && echo "  Status: Connected" || echo "  Status: Disconnected"

# IP Addresses
echo ""
echo "## IP Addresses"
echo "  Public IP: $(curl -s ipecho.net/plain;echo)"
echo "  Private IP: $(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1)"

# DNS Server
echo ""
echo "## DNS Server"
cat /etc/resolv.conf | grep nameserver | awk '{print $2}'

# Network Services
echo ""
echo "## Network Services"
sudo ss -tlnp | tail -n+2 | tr -s ' ' | cut -d ' ' -f 1,4,7 | column -ts ' '

# Memory Usage
echo ""
echo "## Memory Usage"
egrep --color 'Mem|Cache|Swap' /proc/meminfo

# CPU Usage
echo ""
echo "## CPU Usage"
sar -P ALL -h 0 | tail -n +3 | tr -s ' ' | tr '[:lower:]' '[:upper:]' | cut -d ' ' -f 2,3,5,8 | sed -e '1 a \ ' -e 's/ALL/\*/g' | column -tes ' '

# Storage Usage
echo ""
echo "## Storage Usage"
percentage=$(df -h /dev/sda1 | awk 'NR>1 {print $5}')
left=$(df -h /dev/sda1 | awk 'NR>1 {print $4}')
echo "Used: $percentage"
echo "Left: $left"

# Uptime
echo ""
echo "## Uptime"
uptime | awk '{print $3,$4}' | cut -f1 -d,

# Torrent List
echo ""
echo "## Torrent List"
transmission-remote -l | awk '{print $10, $9}'