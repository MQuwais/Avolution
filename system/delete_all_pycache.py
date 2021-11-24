###
# Author : Muhammad Quwais Saputra
###

import subprocess

def DAP():
    subprocess.call('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf',
            shell=True)
