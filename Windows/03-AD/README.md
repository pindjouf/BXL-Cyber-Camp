# Windows Server AD 

#### **Must have** : 

**2. Active Directory Setup:**

- [ ] Promote the Domain Controller VM to a domain controller.
- [ ] Create a new Active Directory forest and domain structure.
- [ ] Configure DNS service on the Domain Controller VM.
- [ ] Create organizational units (OUs) for user and group management.
- [ ] Join the Server VM and Client VMs to the domain.

**3. User Management with Alice and Bob:**

- [ ] Create user accounts within Active Directory:
  - Alice (Administrator, assigned to dedicated OU)
  - Bob (Standard User with access to `/Users/Bob` folder, assigned to specific OU)
- [ ] Leverage Group Policy Objects (GPOs) to configure user settings based on OUs.
- [ ] Implement granular permissions based on security principles for both Alice and Bob.

**4. Server Roles:**

**4.1 IIS for Alice:**

- [ ] Install and configure [IIS](https://www.iis.net/overview) on the Server VM for Alice's specific web application/service.
- [ ] Apply robust security best practices (permissions, WAFs, considering Alice's admin role).
- [ ] Test the web application and ensure accessibility for authorized users in the domain.

**4.2 DNS:**

- [ ] Verify DNS functionality within the Active Directory domain environment.
- [ ] Configure conditional forwarders or external DNS integration if needed.

**4.3 DHCP:**

- [ ] Install and configure DHCP on the Server VM for automatic IP assignment within the domain.
- [ ] Integrate DHCP with Active Directory for dynamic DNS updates (optional).

#### **Cool to have** :

**5. Sysmon Monitoring:**

- [ ] Install and configure your chosen [Sysmon monitoring](https://syedhasan010.medium.com/sysmon-how-to-setup-configure-and-analyze-the-system-monitors-events-930e9add78d) solution on the Server VM.
- [ ] Configure Sysmon to capture relevant events and filter noise specific to your domain environment and user activities (e.g., Alice's admin actions, Bob's file access).
- [ ] Demonstrate Sysmon functionality by simulating suspicious activities and capturing events related to both Alice and Bob.

**6. Client-Side Access and Reporting:**

- [ ] Connect to the Server VM from the Client VMs using domain credentials (Alice and Bob).
- [ ] Verify access based on assigned user permissions and GPOs, demonstrating differences between Alice and Bob's access levels.
- [ ] Access and analyze Sysmon logs using your chosen solution.
- [ ] Prepare a client-facing report highlighting captured events, potential security concerns related to both Alice and Bob, and Sysmon's value within the Active Directory domain.

