#!/usr/bin/env python

import urllib.request
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url", help="the URL whose HTML you want to extract telephone numbers from", type=str)
args = parser.parse_args()

with urllib.request.urlopen(args.url) as response:
  html = response.read().decode('utf-8')

# Naive, simple regex; can be further refined (overinclusive in some respects (e.g., any 10-digit numerical string), no detection when non-parentheses phone number first in a parenthetical clause, no real international support, no extension support, no letters-as-numbers support)
regex = re.compile(r'0?0?1?-?\(?[0-9]{3}\)?\s?-?[0-9]{3}-?[0-9]{4}')

print(regex.findall(html))