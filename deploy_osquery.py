import platform
import subprocess

# determine platform (Linux/Windows)
platform = str(platform.platform())
print('Platform: ', platform)

# only support x86 architecture now, could add ARM support in future

if "Linux" in platform:
    # if Linux then determine RHEL/CentOS vs Ubuntu/Debian via the uname command 
    process = subprocess.Popen("uname -a", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    unameOutput = str(process.communicate()[0])
    process.wait()
    exitCode = process.returncode
    if "Ubuntu" in unameOutput:    
        downloadCommand = "curl -O https://pkg.osquerypackages.com/deb/osquery_5.10.2-1.linux_amd64.deb"
        installCommand = "sudo dpkg -i osquery_5.10.2-1.linux_amd64.deb"
        confSourcePath = "osquery.conf.deb"
        confTargetPath = "/etc/osquery/osquery.conf"
        flagTargetPath = "/etc/osquery/osquery.flags"
    elif "RHEL" in unameOutput or "amzn" in unameOutput:
        downloadCommand = "curl -O https://pkg.osquerypackages.com/rpm/osquery-5.10.2-1.linux.x86_64.rpm"
        installCommand = "sudo rpm -i osquery-5.10.2-1.linux.x86_64.rpm"
        confSourcePath = "osquery.conf.rpm"
        flagSourcePath = "/etc/osquery/osquery.flags"
    # add handling for CentOS, AmznLinux, Debian

elif "Windows" in platform:
    downloadCommand = "curl -O https://pkg.osquerypackages.com/windows/osquery-5.10.2.msi"
    installCommand = "msiexec /i .\osquery-5.10.2.msi /quiet /qn /norestart /log .\install.log"
    confPath = "C:\Program Files\osquery\osquery.conf"
    flagPath = "C:\Program Files\osquery\osquery.flags"

else:
    print("Platform not supported") 
    exit(1)

# download the osquery agent
try:
    print("Downloading osquery...")
    process = subprocess.Popen(downloadCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    downloadOutput = process.communicate()[0]
    process.wait()
    downloadExitCode = process.returncode
    print(downloadOutput)
except:
    print("An error occurred while trying to download osquery")
    print("Command: ", downloadCommand)
    exit(1)

# install the osquery agent 
try:
    print("Installing osquery...")
    process = subprocess.Popen(installCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    installOutput = str(process.communicate()[0])
    process.wait()
    installExitCode = process.returncode
    print(installOutput)
except: 
    print("An error occurred while trying to install osquery")
    print("Command: ", installCommand)
    exit(1)

# copy the osquery conf file 
try:
    print("Copying osquery conf file...")
    process = subprocess.Popen("sudo cp ./"+confSourcePath+" "+confTargetPath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()[0]
    process.wait()
    exitCode = process.returncode
except:
    print("An error occurred while copying the osquery.conf file to "+confPath)
    exit(1)

# copy the osquery flags file 
try:
    print("Copying osquery flags file...")
    process = subprocess.Popen("sudo cp ./osquery.flags "+flagPath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()[0]
    process.wait()
    exitCode = process.returncode
except:
    print("An error occurred while copying the osquery.flags file to "+flagPath)
    exit(1)

# start the osquery daemon 
try:
    print("Starting osquery...")
    process = subprocess.Popen("sudo systemctl start osqueryd", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = str(process.communicate()[0])
    process.wait()
    exitCode = process.returncode
    print(output)
except:
    print("An error occurred while trying to start osquery")
    print("Command: sudo systemctl start osqueryd")
    exit(1)

