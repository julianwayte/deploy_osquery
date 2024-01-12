import platform

# determine platform (Linux/Windows)
platform = str(platform.platform())
print('Platform: ', platform)

# only support x86 architecture now, could add ARM support in future

if "Linux" in platform:
    # if Linux then determine RHEL/CentOS vs Ubuntu/Debian via the uname command 
    process = subprocess.Popen("uname -a", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    unameOutput = str(process.communicate()[0])
    # print(unameOutput)
    exitCode = process.returncode
    if "Ubuntu" in unameOutput:    
        downloadCommand = "curl -O https://pkg.osquerypackages.com/deb/osquery_5.10.2-1.linux_amd64.deb"
        installCommand = "sudo dpkg -i osquery_5.10.2-1.linux_amd64.deb"
    elif "RHEL" in unameOutput:
        downloadCommand = "curl -O https://pkg.osquerypackages.com/rpm/osquery_5.10.2-1.linux_amd64.rpm"
        installCommand = "sudo rpm -i osquery_5.10.2-1.linux_amd64.rpm"
    # add handling for CentOS, AmznLinux, Debian

elif "Windows" in platform:
    foo = bar 
    # do Windows things

else:
    print("Platform not supported") 
    exit(1)

# download the osquery agent
try: 
    process = subprocess.Popen(downloadCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    downloadOutput = process.communicate()[0]
    downloadExitCode = process.returncode
except:
    print("An error occurred while trying to download osquery")
    print("Command: ", downloadCommand)
    exit(1)

# install the osquery agent 
try:
    print("Installing osquery...")
    process = subprocess.Popen(installCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    installOutput = process.communicate()[0]
    installExitCode = process.returncode
except: 
    print("An error occurred while trying to install osquery")
    print("Command: ", downloadCommand)
    exit(1)

# copy the osquery conf file over

# start the osquery daemon 

