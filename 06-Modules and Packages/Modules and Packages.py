#PyPi is a repository for open-source third party Python packages

#we can use pip install at the command line to install the packages

# pip install <pkg name>
from colorama import init
init()#just like initialization
from colorama import Fore
print(Fore.RED + "text in Red color")
print(Fore.GREEN + "test in green color")

