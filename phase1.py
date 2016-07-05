from HTMLParser import HTMLParser
import sys

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
	if tag!='html' :
            global wfile
	    wfile.write("%s="%(tag))
            print tag
	    
    def handle_data(self, data):
        global wfile
	wfile.write("%s\n" %(data))
        print data
	
infilename=sys.argv[1]
ifile=open(infilename, 'r')
wfilename=sys.argv[2]
wfile=open(wfilename, 'a')

lines=""
parser = MyHTMLParser()
for line in ifile:
    # instantiate the parser and fed it some HTML
    lines=lines+line.rstrip()
lines.replace("\n","")    
parser.feed(lines)

wfile.close()
