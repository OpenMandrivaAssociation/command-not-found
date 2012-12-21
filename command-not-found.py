#!/usr/bin/python

from __future__ import print_function
import json
import sys

if len(sys.argv) < 2:
    exit(15)
    
try:
    with open('/usr/share/command-not-found/data.json', 'r') as fd:
        binaries = json.load(fd)
except:
    exit(15)
    


param = sys.argv[1]

if param in binaries:
    print(" Command '%s' can be found in:" % param, file=sys.stderr)
    for item in binaries[param]:
        print("    package '%s' (%s)" % (item[1], item[0]), file=sys.stderr)
    exit()

    
def similar_words(word):
    """
    return a set with spelling1 distance alternative spellings

    based on http://norvig.com/spell-correct.html
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz-_0123456789'
    s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in s if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in s for c in alphabet if b]
    inserts = [a + c + b     for a, b in s for c in alphabet]
    return set(deletes + transposes + replaces + inserts)
    
params = similar_words(param)
found = []
for p in params:
    if p in binaries:
        found.append(((p, binaries[p])))
            
if not found:
    print("%s: command not found" % param)
    exit()
print("No command '%s' found, did you mean:" % (param), file=sys.stderr)
for item in found:
    cmd_name, locations = item
    loc_string = ', '.join([("package '%s' (%s)" % (c, r)) for r, c in locations])
    print("  Command '%s' from %s" % (cmd_name, loc_string), file=sys.stderr)