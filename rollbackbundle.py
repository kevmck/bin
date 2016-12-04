#!/usr/bin/python3

import os
import sys

#Deploys a given bundle to a given branch

#1st param: name of bundle
#2nd param: branch to deploy to

bundleName = "API_" + sys.argv[1] + "_v"

#send deployment request 
os.system("php /home/vm164/bin/bundle/rabbitMQClient.php rollbackBundle " + bundleName + " " + sys.argv[2])
