# Turn-In-Parser
A Python script which can be used to parse and sort student files. This script will take a bulk download of Blackboard files and parse them into folders for each TA in the talist, which is an argument required by the script.
Version: 1.0

#About
Turn In Parser (TIP) allows a course administrator to download a assignment from Blackboard, and will parse the student files out to the grader that has been assigned to them in "talist", a CSV file. The program can place any number of other files into the student folders as they are sorted by adding additional command line arguments with the directory location for said files. It is best not to have anything but student files and this script in the directory which this script runs.

#Running
This script requires python 2.#. To run type the command:
`python script.py talist file.txt file2.txt file3.txt ...`
This will run the script pulling the list of students per TA from talist and will place file.txt file2.txt and file3.txt into each student folders.

Final directory structure if the student files were held in directory 'assignment'
assignment
    |
Ta1 Ta2 Ta3 Ta4 Ta5 Ta6 Ta7 ... TaN
 |
 Stu1 Stu2 Stu3 Stu4 Stu5 ... StuN
  |
previous_attempts file.txt file2.txt file3.txt turnedinassignment.java
  |
  turnedinassignment
  |
  <any previous attempts>
  
#Future Releases
This project will, soon, add the ability to run another script on each students turned in assignment in the near future.
