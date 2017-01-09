#!/home/arthurzey/deltawerx.com/env/bin/python
print "Content-type: text/html\n\n"

from os.path import expanduser, join

from stormpath.client import Client


# This is the absolute path to the file ~/.stormpath/apiKey.properties
# downloaded in the previous section.  This will work on any OS.
API_KEY_FILE = join(expanduser('~'), '.stormpath', 'apiKey.properties')


client = Client(api_key_file=API_KEY_FILE)

application = client.applications.search({'name': 'My Application'})[0]

from stormpath.error import Error as StormpathError

try:
    result = application.authenticate_account('tk421@galacticempire.co', 'Changeme123!')
    account = result.account

    print('User ' + result.account.full_name + ' logged in.')
except StormpathError, e:
    print('Could not log in. Error: ' + e.user_message)
