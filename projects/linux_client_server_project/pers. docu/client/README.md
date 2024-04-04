# Client Config

Not much to say here honestly, lots of GUI so pretty intuitive.\
The only thing I had to go in the terminal for was to install Mullvad Browser

## Introduction:
This readme file outlines the configuration steps undertaken to set up a workstation. The process primarily involved graphical user interface (GUI) operations, making it intuitive for users to follow. Additionally, some tasks required terminal commands, which are detailed below.

## Software Installation:

### Mullvad Browser Installation:

Mullvad Browser was installed via the terminal using the following commands:\
`wget --content-disposition https://mullvad.net/en/download/browser/linux-x86_64/latest -P ~/Downloads`\
```
cd ~/Downloads

tar -xvf mullvad-browser-linux-x86_64-X.X.tar.xz
```
Now we add it to the applications:\
`cp ~/Downloads/mullvad-browser/start-mullvad-browser.desktop ~/.local/share/applications/`

### Additional Software:

**LibreOffice:** Preinstalled with Ubuntu.\
**GIMP:** Installed from the Ubuntu App Center.

### Partition Configuration:

Manual partitioning was performed during the installation process:\
Partition 1: /\
Partition 2: /boot\
Partition 3: /home\

### Networking Configuration:

The workstation utilizes automatic addressing for networking. However, there are issues with obtaining IP addresses from the DHCP server, resulting in manual intervention. Further troubleshooting is planned to resolve this issue.

### Conclusion:

This readme provides an overview of the workstation configuration, detailing software installations, partition configurations, and networking settings.\
For any additional assistance or troubleshooting, please refer to the relevant sections.