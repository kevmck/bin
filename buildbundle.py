#!/usr/bin/python3 

import configparser
import os
import sys

# Handles building bundles given the 
# name of bundle. 
#
# buildbundle.py [bundle name]
#
# Note: bundle name must be inside bundle.ini with path to src folder 

conf = configparser.ConfigParser()
conf.read("/home/vm164/bin/bundle.ini")

#get name of bundle from 1st command argument
bundleName = sys.argv[1]

#check if given bundleName in listed Bundles inside bundle.ini
if(not conf.has_option("bundles", bundleName)):
    print("ERROR: " + bundleName + " not in listed bundles.")
    sys.exit()

print("Building Bundle: "+ bundleName  +"...")

#define location of config file
cfgLoc = conf["settings"]["cfg"]

#name of compressed bundle
bundleTarNameskel = conf["settings"]["machine"] + "_" + bundleName + "_v"

#get next version from db
ver = (os.popen("php /home/vm164/bin/bundle/rabbitMQClient.php bundleRequest " + bundleTarNameskel).read())
ver = ver.strip()
#ver = 1
print("The next bundle version is version:  " + str(ver))

#add version#
bundleTarName = bundleTarNameskel + str(ver)

#location where bundle will be built
bundleDst = conf["settings"]["dst"] + bundleTarName

#debugging
print("Name of bundleTar: " + bundleTarName)
print("Location of bundle " + bundleDst)
##

#create the uncompressed bundle
os.system("mkdir " + bundleDst)
os.system("cp -r " + conf["bundles"][bundleName] + " " + bundleDst)
print(bundleDst)
#os.system("rm -rf " + bundleDst + " /.git")
os.system("cp -r " + cfgLoc + " " + bundleDst)

#compress
bundleTar = bundleDst + ".tgz"
os.system("tar -czf " + bundleTar + " -C " + bundleDst + " .")

#send to target machine(bundle archive)
os.system("scp " + bundleTar + " ses@192.168.2.11:/home/ses/bundles")

#update bundle version in db
os.system("php /home/vm164/bin/bundle/rabbitMQClient.php updateBundleVer " + bundleTarNameskel)

#clean up
os.system("rm -r -f " + bundleDst)
os.system("rm -r -f " + bundleDst + ".tgz")

print ("Build Complete")

