import fileinput
import re
import os

// USAGE: python udemy-jl.py links.txt
// links.txt contains courses like
// https://www.udemy.com/foo/learn/

username = 'your@email.here'
password = 'secret'

content = []

for line in fileinput.input():
    courseUrl = line.strip()
    m = re.search('http.*\/.*\.com\/(.*?)\/learn', courseUrl)
    if m:
        courseName = m.group(1)
        destinationPath = "'videos_downloads/{0}/%(autonumber)s-%(title)s.%(ext)s'".format(courseName)
        command = "youtube-dl {0} -o {1} -u {2} -p {3}".format(courseUrl, destinationPath, username, password)
        print command
        os.system(command)

fileinput.close()
