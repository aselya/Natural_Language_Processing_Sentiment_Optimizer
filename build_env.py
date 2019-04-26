'''
This file sets up a virtual environment for
the rest of the porgram to run
Installs the needed packages and
sets the environmental variable GOOGLE_APPLICATION_CREDENTIALS
'''
import os
import subprocess
import sys
#sets the string valuse for the os.system commands
install_virtual_env = 'pip install virtualenv'
setup_virtual_env = 'virtualenv shakespheare'
start_virtual_env = 'source shakespheare/bin/activate'
export_google_credentials = 'export GOOGLE_APPLICATION_CREDENTIALS="../shakespheare/shakespeareanInsultGenerator-b00ff00d9faa.json"'

#calls to establish virtualenv
os.system(install_virtual_env)
os.system(setup_virtual_env)
os.system(start_virtual_env)

#function to install needed python packages
def install_package(pack):
    subprocess.call([sys.executable, "-m", "pip", "install", pack])

#calls to install packages
install_package('google-cloud-language')
install_package('pandas')

#sets a enviornmental variable needed for google NLP
def export_cred():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']="../shakespheare/shakespeareanInsultGenerator-b00ff00d9faa.json"

export_cred()

#imports and runs main file
import gen_algo
run_program = gen_algo
