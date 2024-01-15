# deploy_osquery
Deploys the osquery agent with an osquery.conf specifying queries to collect event and differential data for most important tables.
Output is to a Kafka topic.

The following combinations of OS/architecture have been tested: 
Amzn Linux x86 64bit (no event data)
Amzn Linux ARM 64bit (no event data)
Debian     x86 64bit
Debian     ARM 64bit
Ubuntu     x86 64bit
Ubuntu     ARM 64bit
RHEL       x86 64bit (no event data)
RHEL       ARM 64bit (no event data)
CentOS     x86 64bit (no event data)
CentOS     ARM 64bit (no event data)

To be tested (should work): 
Windows        64bit
MAC            64bit

Will never work:
All 32bit operating systems

Note that due to the presence of auditd running on RHEL, CentOS, & Amzn Linux I was not able to get event data working (differential data does work). 

