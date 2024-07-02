# SSH

## The main idea: make your servers trust a central authority that clients get *approved* by.
## Simple analogy: It's like new acquaintance trusts you because you got introduced by a mutual friend.

### High-level overview

- You make a CA that has a priv and pubkey. (On CA)
- Give 0644 permissions to the pubkey. (On CA)
- You put that pubkey in all your servers.
- Make all servers trust that pubkey. (On Servers)
- On a client's machine `ssh-keygen`. (On Client)
- Send the client's pubkey to CA for signing. (On Client)
- Sign the client's pubkey with the CA's privkey, choose principals and length of validity. (On CA)
- You can now login to any server that trusts the CA.
*Resource for details:* [meta article](https://engineering.fb.com/2016/09/12/security/scalable-and-secure-access-with-ssh/)

## Central authentication is needed to access servers at scale. Why?

### What are signed certificates?

- They're a way to authenticate SSH keys using a Certificate Authority.
So we use the CA to validate the authenticity of the SSH keys.

#### What is a certificate authority?

- The central issuer of certificates for you public keys. It signs them to prove their validity.

#### What is the difference between a certificate authority & signed certificates?

- They're the same thing this is a really dumb question. Signed certificates are issued by the certificate authority it's in the names use your brain.

### So what does this look like in practice?

- Well instead of doing a `ssh-keygen ; ssh-copy-id` you send your public key to the CA with a request to sign it.

- The CA signs it and that creates a certificate with the pubkey, CA signature and metadata.

- When mfs try to connect, the server or client verifies the certificate against the CA's pubkey.

### So the CA is just out here giving certificates to everyone?!

- No you can define rules under which it can operate.
- For instance when users submit CSR's they have to put in their identity and you also get metadata that you can use that you can identify users within a certain network for example if you decide to implement that rule.

#### Examples of policies you can make:
- Define which usernames / hostnames can be included in the certs.
- Specify duration of validity for the cert.
- Require MFA.

#### A quick example:



### What is LDAP?

- A protocol but basically it allows us to have a central place to store user credentials so they don't have to be on the local server themselves you can just connect to the LDAP server to retrieve the credentials and gtfo.

### What is kerberos?

- A protocol but basically it's a way to verify identity between server and client over a non-secure network, by sending tickets.

*The biggest con of using a central point for auth is if the service or server goes down you're fucked since your credentials are stuck in a service or server that is not accessible.*

### Why is "traditional" public key auth fucked?

- Apparently it's not uncommon to get unknown public keys in the authorized_keys files. Also it's a headache to scale that is true.

### ???????
When you have a large set of users, you need a central directory to manage them. To avoid a single point of failure, our production systems only have local accounts in `/etc/passwd.`

### ????????
The most common account used is `root`. The SSH servers only accept `root` logins if the client certificate has some very specific capabilities given by the CA, and the CA itself determines who can use SSH and where.

### ?????????
Using local accounts introduces a problem, though. The standard Unix login accounting (`utmp`, `wtmp`) is of no use here, and the last command can only show local accounts that have logged in. However, OpenSSH can give you detailed information on which certificate was used to authenticate, providing enough information for rich accountability.

## Implementation / How this shit works

- ### Make a CA
Which just means dedicate a server for that job.
**Let's go through it step by step:**
- `ssh-keygen -C CA -f ca` 
    - `-C` is to modify the comment associated to the key-pair and `-f` is to choose the file name.
    - give the `ca.pub` file 0644 permissions.
        - 0644 means you can read and write but others can only read it.
    - You can now distribute `ca.pub` to all your servers.
    - Configure all the servers to have the following line in their sshd_config:
        - `TrustedUserCAKeys /etc/ssh/ca.pub`

- ### 
