#!/home/arthurzey/deltawerx.com/env/bin/python
print "Content-type: text/html\n\n"

from os.path import expanduser, join

from stormpath.client import Client


# This is the absolute path to the file ~/.stormpath/apiKey.properties
# downloaded in the previous section.  This will work on any OS.
API_KEY_FILE = join(expanduser('~'), '.stormpath', 'apiKey.properties')


client = Client(api_key_file=API_KEY_FILE)

application = client.applications.search({'name': 'My Application'})[0]

account = application.accounts.create({
    'given_name': 'Joe',
    'surname': 'Stormtrooper',
    'email': 'tk421@galacticempire.co',
    'password': 'Changeme123!',
})
print('User ' + account.full_name + ' created.')
