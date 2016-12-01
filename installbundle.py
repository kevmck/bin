#!/usr/bin/python3

import configparser
import os

print ("Installing bundle...")

conf = configparser.ConfigParser()
conf.read("/home/ses/bin/bundle.ini")

bundleTar = conf["settings"]["dst"] + "/backendBundle.tar.gz"

os.system("tar -xzvf " + bundleTar)

#clean up
os.system("rm " + bundleTar)

print("Bundle installed")

