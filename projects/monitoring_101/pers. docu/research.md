# Research

### Why monitor?

First let's identify why we should care about monitoring a system.

There are many reasons to monitor a system, if you plan on having servers that run services as most companies do. You'll want those to run smoothly because you're likely to rely on them.

So having random outages and services not working is not something you can afford, thus the need for monitoring is ever increasing as we rely on those services more and more.

If you have no way of pinpointing/understanding a problem, there's no way you're ever going to fix it.\
So monitoring allows us to have records of what causes problems in order to fix them/prevent them.

It could be something wrong with the machine (faulty process) or with what a user did/didn't do.

We don't have unlimited resources so making sure we use them as efficiently as possible is of the utmost importance.

**Simple example (resource allocation)**:\
If your media streaming company has 100 kbps upload speed, and from previously acquired data you know that 80 of those should be available at all times because that is what your customer base needs from your servers on average.\
So all your other services (combined) should never go over 20 kbps or you're gonna be decreasing the quality of your service and losing customers as a result of that.


**Simple example (system load)**\
The same streaming company has been growing lately.\
After looking at the graphs on your system monitoring tool you notice that the the system load is getting ridiculously high, the hardware you currently have is never gonna be enough if your company keeps growing at this rate. \
Thanks to that data you will be able to prevent your service being down in the future due to your system failing.

### How to take care of your system
Your services should stay available, reliable and secure.

### Availability
**How to check what services are up and running?**

- With `systemctl --type=service --state=running`.\
You can omit the `--state=running` flag if you want to see all the services.


### Reliability 
**How do you make sure that your services are reliable?**

- Setup 'heartbeat checks' so that you can notice trends and prevent your server from getting pushed to its operational limits.

### Security
**How can monitoring practices keep your system safe?**

- Setup alerts for when there are too many failed authentication attempts.
- Alerts for failed backups/automated reports.


### Report draft on osmc-Edmund (Media server)





