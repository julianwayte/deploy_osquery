import platform
import subprocess 

# determine platform (Linux/Windows)
platform = str(platform.platform())
print('Platform: ', platform)

# On Linux run 'uname -a' to get more details of the OS
process = subprocess.Popen("uname -a", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
unameOutput = str(process.communicate()[0])
process.wait()
exitCode = process.returncode
print('uname output: ',str(unameOutput))

