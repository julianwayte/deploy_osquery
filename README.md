# deploy_osquery
Deploys the osquery agent on the running machine with an osquery.conf specifying queries to collect event and differential data for most important tables.
Output is in JSON format in a local file.

The following combinations of OS/architecture have been tested: 
Amzn Linux ARM 64bit

To be tested (should work): 
Amzn Linux x86 64bit (no event data)
Debian     x86 64bit
Debian     ARM 64bit
Ubuntu     x86 64bit
Ubuntu     ARM 64bit
RHEL       x86 64bit (no event data)
RHEL       ARM 64bit
CentOS     x86 64bit
CentOS     ARM 64bit
Windows        64bit
MAC            64bit

Will never work:
All 32bit operating systems


