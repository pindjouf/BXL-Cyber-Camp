# Step By Step Documentation

I've decided to document nearly everything I'm doing and the reasoning behind it so that I can clearly see the mistakes I make, because a lot of things that are supposed to work smoothly, aren't.

### **The base config**:

- The Domain Controller (DaMain aka DaMain)
  - DNS
- The Server (DaServ aka Alice)
  - IIS
  - DHCP
- The Client (DaClient aka Bob)

All the machines are in an internal network called 'yo'.

I have to add a record for DaServ in the DNS records.
Because it's preventing me from adding DaServ in the Active Directory. Which I need to do in order to let DaServ Manage the DHCP server.

This is why I can't add DaServ to the Active Directory:
https://community.spiceworks.com/t/target-name-resolution-error/726036

This is what I need to do once the DNS is setup properly:
https://community.spiceworks.com/t/dhcp-server-not-authorized/745512

Well after leaving the VMs off for a few hours and coming back to them, everything started working for some reason.

What's left to do:
- Configure DHCP now that DaServ has been added
- Configure Permissions for Bob
- Configure IIS like in the brief


