# Current state = Server cannot ping the internet for some reason

It's 8 PM \
My project has turned into a mess. \
I will restart the server from scratch. \
Here's what needs to be done by Friday 00:00 and the time I'm giving myself to do them:

1. DHCP server (1 hour) [docs](https://github.com/pindjouf/Linuxx/blob/main/projects/linux_client_server_project/pers.%20docu/server/making_a_dhcp_server.md)
2. DNS server (1 hour) [docs](https://github.com/pindjouf/Linuxx/blob/main/projects/linux_client_server_project/pers.%20docu/server/dns/)
3. Http + mariadb + GLPI (1 hour) [docs](https://github.com/pindjouf/Linuxx/blob/main/projects/linux_client_server_project/pers.%20docu/server/making_an_http_server.md)
4. Weekly Config Backups (30 minutes) [docs](https://github.com/pindjouf/Linuxx/blob/main/projects/linux_client_server_project/pers.%20docu/server/weekly_config_backup.md)
5. Documentation (15 minutes)

Those estimates are probably way off but let's see. I will leave this as the main readme for the challenge and update tomorrow to see how far I've gotten.

Post-sprint comments @ 12:45 PM:
*"The estimates were way off indeed"*

## Checklist & Deliverables

1. One server (no GUI) running the following services:
	- [x] DHCP (one scope serving the local internal network)  isc-dhcp-server
    - [ ] DNS (resolve internal resources, a redirector is used for external resources) bind
    - [ ] HTTP + mariadb + GLPI
    - **Required**
        - [ ] Weekly backup the configuration files for each service into one single compressed archive
        - [x]  The server is remotely manageable (SSH)
    - **Optional**
        - [ ] Backups are placed on a partition located on  separate disk, this partition must be mounted for the backup, then unmounted

3. One workstation running a desktop environment and the following apps:
    - [x] LibreOffice
    - [x] Gimp
    - [x] Mullvad browser
    - **Required** 
        - [x] This workstation uses automatic addressing
        - [x] The /home folder is located on a separate partition, same disk 
    - **Optional**
        - [ ] Propose and implement a solution to remotely help a user

## Deliverables
https://docs.google.com/document/d/18iHTN3YBXxK5nIiNiYMgM5f5u1MnjklDDH5HOl2_A60/edit?usp=sharing
