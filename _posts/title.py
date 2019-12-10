import subprocess
import sys
import getopt
import ipdb

def usage():
    print "python title.py -t $title -i $image(stored in ../assets/images) --tag $tag"


opts, args = getopt.getopt(sys.argv[1:], "ht:i:c:", ["help", "title=", "image=", "tag=", "category="])
print opts, args
title=""
image=""
tag=""
category="Blog"
displayImage = 'false'

for op, value in opts:
    if op in ("-t", "--title"):
        title = value
    if op in ("-i", "--image"):
        image = value
        displayImage = 'true'
    if op in ("--tag"):
        tag = "- "+value+"\n"
        for t in args:
            tag = tag + "- " +t+"\n"
    if op in ("-c", "--category"):
        category = value
    if op in ("-h", "--help"):
        usage()
        sys.exit()

datetime = subprocess.check_output('date \"+%Y-%m-%d %H:%M\"', shell=True)
date = subprocess.check_output('date \"+%Y-%m-%d\"', shell=True)
date = date.replace('\n', '-')

if title == "":
    print "You must input title at least"
    usage()
    sys.exit(1)

titlecontent=["---",
"\ntitle: "+ title,
"\nlayout: post",
"\ndate: "+ datetime,
"image: /assets/images/"+ image,
"\nheaderImage: "+ displayImage,
"\ncategory: "+ category,
"\ntag:\n"+ tag,
"author: Sun",
"\n---"]

f = open(date+title+".md", 'w')
for content in titlecontent:
    f.writelines(content)
    print content

f.close()
