import platform
import subprocess

# determine platform (Linux/Windows)
platform = str(platform.platform())
print('Platform: ', platform)

# Only tested with the following OS/architecture combinations:
# Ubuntu     64bit x86
# Amzn Linux 64bit ARM

# Should remove events and retest
# RHEL       64bit x86
# Amzn Linux 64bit x86
# CentOS     64bit x86

# Add 
# Debian     64bit x86 
# Windows    64bit x86
# RHEL       64bit ARM


if "Linux" in platform:
    # if Linux then determine RHEL/CentOS vs Ubuntu/Debian via the uname command 
    process = subprocess.Popen("uname -a", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    unameOutput = str(process.communicate()[0])
    process.wait()
    exitCode = process.returncode

    # define a list of strings for RPM flavor operating system
    rpm_os_list = ['el7', 'el8', 'el9', 'amzn', 'centos']
    rpm_os = [os for os in rpm_os_list if(os in unameOutput)]

    # define common linux paths
    confTargetPath = "/etc/osquery/osquery.conf"
    flagTargetPath = "/etc/osquery/osquery.flags"

    # Ubuntu/Debian
    if "Ubuntu" in unameOutput:    
        downloadCommand = "curl -O https://pkg.osquerypackages.com/deb/osquery_5.10.2-1.linux_amd64.deb"
        installCommand = "sudo dpkg -i osquery_5.10.2-1.linux_amd64.deb"
        confSourcePath = "osquery.conf.deb"

    # RHEL/CentOS/AmznLinux
    elif bool(rpm_os):
        downloadCommand = "curl -O https://pkg.osquerypackages.com/rpm/osquery-5.10.2-1.linux.x86_64.rpm"
        installCommand = "sudo rpm -i osquery-5.10.2-1.linux.x86_64.rpm"
        confSourcePath = "osquery.conf.rpm"

elif "Windows" in platform:
    downloadCommand = "curl -O https://pkg.osquerypackages.com/windows/osquery-5.10.2.msi"
    installCommand = "msiexec /i .\osquery-5.10.2.msi /quiet /qn /norestart /log .\install.log"
    confSourcePath = "osquery.conf.windows"
    confTargetPath = "C:\Program Files\osquery\osquery.conf"
    flagiTargetPath = "C:\Program Files\osquery\osquery.flags"

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
    print("An error occurred while copying the osquery.conf file to "+confTargetPath)
    exit(1)

# copy the osquery flags file 
try:
    print("Copying osquery flags file...")
    process = subprocess.Popen("sudo cp ./osquery.flags "+flagTargetPath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()[0]
    process.wait()
    exitCode = process.returncode
except:
    print("An error occurred while copying the osquery.flags file to "+flagTargetPath)
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
