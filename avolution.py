###
# Author : Muhammad Quwais Saputra
###

import sys

from system.delete_all_pycache import *
from system.clear import *
from src.dialogues.dialog import *
from src.dialogues.malbate.hacking import *
from exploit.xploit import *
from payload.facebook.phising.inject import *

try:
    Dialog.first()
except KeyboardInterrupt:
    DAP()
    sys.exit()
