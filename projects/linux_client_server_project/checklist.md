# Current state = Server cannot access the internet for some reason and is not at all setup

1. One server (no GUI) running the following services:
	- [ ] DHCP (one scope serving the local internal network)  isc-dhcp-server
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
        - [ ] This workstation uses automatic addressing
        - [x] The /home folder is located on a separate partition, same disk 
    - **Optional**
        - [ ] Propose and implement a solution to remotely help a user

## Performance criteria
The teams must give a sense of confidence to the audience when presenting their demo,
the documentation must be clear, structured and must provide all elements of configuration.

## Evaluation methods
- Quality of the documentation and the live demo (5),
- All required items are implemented are working (5),
- Optional items are implemented and working (bonus 5),
- The team demonstrates good organisation and planning (5),
- The team explains and justifies the various choices they made (5),
- Tests were performed to ensure the configuration is working (5),
- The team demonstrate a solid knowledge of the Linux environment when answering questions (5)

## Deliverables
https://docs.google.com/document/d/18iHTN3YBXxK5nIiNiYMgM5f5u1MnjklDDH5HOl2_A60/edit?usp=sharing \
a summary in English (at least one page)
Live demonstration in front of the group