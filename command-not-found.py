#!/usr/bin/python

# Anton Kirilenko, 2012,
# Licensed under GPL, see http://www.gnu.org/licenses/gpl-2.0.html
# for the whole text

from __future__ import print_function
import json
import sys
import argparse


def parse_command_line():
    global command_line
    arg_parser = argparse.ArgumentParser(description='Search for commands in repository.')
    arg_parser.add_argument('command', action='store', nargs='?', help='Command to search for')
    args = sys.argv[1:]
    if not args:
        exit()
    command_line  = arg_parser.parse_args(args)
    

parse_command_line()

if not command_line.command:
    exit(15)
    
try:
    with open('/usr/share/command-not-found/data.json', 'r') as fd:
        binaries = json.load(fd)
except:
    exit(15)
    


param = command_line.command

if param in binaries:
    print(" Command '%s' can be found in:" % param, file=sys.stderr)
    for item in binaries[param]:
        print("    package '%s' (%s)" % (item[1], item[0]), file=sys.stderr)
    exit(127)

    
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
    exit(127)
print(" No command '%s' found, did you mean:" % (param), file=sys.stderr)
for item in found:
    cmd_name, locations = item
    loc_string = ', '.join([("package '%s' (%s)" % (c, r)) for r, c in locations])
    print("  Command '%s' from %s" % (cmd_name, loc_string), file=sys.stderr)
    
exit(127)