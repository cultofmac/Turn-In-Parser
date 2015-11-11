#!/usr/bin/python
#Uses OS, Sys, and shutil modules
import os, sys, shutil, tarfile, datetime, getopt

#CurrentDir will be the path to the root directory for script
#ContentsDir will be the initial contents of the directory in a list
currentDir  = os.getcwd()
contentsDir = os.listdir(currentDir)
PROJECT		= raw_input("What asssignemnt is this (TA NAME): ")

#====================================================================
# PART 1 || Sorting all student files into student folders
#====================================================================
os.makedirs(currentDir+"/badfiles")

for stuFile in contentsDir:
	if stuFile.endswith('.txt') or stuFile.endswith('.java') or stuFile.endswith('.java~'):
		os.rename(stuFile, stuFile[stuFile.find("_")+1:])

for stuFile in os.listdir(currentDir):
	if stuFile.endswith('.txt') or stuFile.endswith('.java') or stuFile.endswith('.java~'):
		if not os.path.exists(currentDir+"/"+stuFile[:stuFile.find("_")]):
			os.makedirs(currentDir+"/"+stuFile[:stuFile.find("_")])
		shutil.move(stuFile, currentDir+"/"+stuFile[:stuFile.find("_")]+"/"+stuFile)
	elif stuFile.endswith('.class'):
		shutil.move(stuFile, currentDir+"/badfiles/"+stuFile)

# #====================================================================
# # PART 2 || Parse submitted files for each student into folders
# #====================================================================
for d in os.listdir(currentDir):
	if d != "badfiles":
		if os.path.isdir(d) == True:
			for s in os.listdir(currentDir+"/"+d):
				if s.endswith('.txt'):
					os.remove(currentDir+"/"+d+"/"+s)
				else:
					if not os.path.exists(os.getcwd()+"/"+d+"/"+s[s.rfind("_")+1:s.rfind(".java")]):
						os.makedirs(os.getcwd()+"/"+d+"/"+s[s.rfind("_")+1:s.rfind(".java")])
					shutil.move(os.getcwd()+"/"+d+"/"+s, os.getcwd()+"/"+d+"/"+s[s.rfind("_")+1:s.rfind(".java")]+"/"+s)

# #====================================================================
# # PART 3 || Pull out most recently submitted file
# #====================================================================
for d in os.listdir(currentDir):
	if d != "badfiles" and os.path.isdir(d) == True:
		for ds in os.listdir(currentDir+"/"+d):
			if os.path.isdir(currentDir+"/"+d+"/"+ds) == True:
				lastTime = None
				print(s[s.find("_attempt_")+9:s.find("_attempt_")+28])
				for s in os.listdir(currentDir+"/"+d+"/"+ds):
					dts = datetime.datetime.strptime(s[s.find("_attempt_")+9:s.find("_attempt_")+28], '%Y-%m-%d-%H-%M-%S')
					if lastTime == None or lastTime < dts:
						lastTime = dts
				for s in os.listdir(currentDir+"/"+d+"/"+ds):
					dts = datetime.datetime.strptime(s[s.find("_attempt_")+9:s.find("_attempt_")+28], '%Y-%m-%d-%H-%M-%S')
					if lastTime == dts:
						shutil.move(os.getcwd()+"/"+d+"/"+ds+"/"+s, os.getcwd()+"/"+d+"/"+ds+".java")
		os.makedirs(os.getcwd()+"/"+d+"/previous_submissions")
		for ds in os.listdir(currentDir+"/"+d):
			if os.path.isdir(currentDir+"/"+d+"/"+ds) == True:
				shutil.move(os.getcwd()+"/"+d+"/"+ds, os.getcwd()+"/"+d+"/previous_submissions")

# #====================================================================
# # PART 4 || Pull in command line file paths
# #====================================================================
for num in range(2, len(sys.argv)):
	path = sys.argv[num]
	for d in os.listdir(currentDir):
		if d != "badfiles" and os.path.isdir(d) == True:
			shutil.copyfile(path, os.getcwd()+"/"+d+"/"+path[path.rfind("/")+1:])

# #====================================================================
# # PART 5 || Sort students by assigned TA
# #====================================================================
taList 				= []
taInstructorList 	= []
with open(sys.argv[1], "rw+") as handle:
	for line in handle:
		if line.startswith("@"):
			taList.append(line.strip('@').rstrip('\n').split(','))
for ta in taList:
	taInstructorList.append(ta[0]+"_"+PROJECT)
	ta.remove(ta[0])
for ta in taInstructorList:
	os.mkdir(ta)
iTA = 0
for ta in taList:
	for student in ta:
		for s in os.listdir("."):
			if s.find(student) != -1:
				shutil.move(s, currentDir+"/"+taInstructorList[iTA])
	iTA = iTA + 1
for ta in taInstructorList:
	shutil.make_archive(ta, 'zip', ta)
					


