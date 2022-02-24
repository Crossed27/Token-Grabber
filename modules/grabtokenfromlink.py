# .py Module by Vertic

# grabtokenfromlink.py

import time

def ScaryGrabbing(lelink):
	shittyArray = [
		"\nToken is: ",
		":)"
	]

	print("Grabbing User Token From Link: " + lelink)

	time.sleep(10)

	for i in shittyArray:
		print(i)

def CreatePrompt():
	linkidstr = "target-link-goes-here"
	linkid = input("Enter the Targetted Link: ")
	if linkid == linkidstr:
		ScaryGrabbing(linkid)