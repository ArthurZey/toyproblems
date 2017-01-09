#!/home/arthurzey/deltawerx.com/env/bin/python

from os.path import expanduser, join
from os import environ

from stormpath.client import Client


# This is the absolute path to the file ~/.stormpath/apiKey.properties
# downloaded in the previous section.  This will work on any OS.
API_KEY_FILE = join(expanduser('~'), '.stormpath', 'apiKey.properties')


client = Client(api_key_file=API_KEY_FILE)

application = client.applications.search({'name': 'My Application'})[0]

url = environ['SCRIPT_URI'] + "?" + environ['QUERY_STRING']

result = application.handle_stormpath_callback(url)

# print "Location: http://www.deltawerx.com/toyproblems/interviews/stormpath/"
print "Content-type: text/html\n\n"


print dir(result.account)
# print "You are being redirected to http://www.deltawerx.com/toyproblems/interviews/stormpath/"