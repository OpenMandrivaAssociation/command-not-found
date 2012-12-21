# (c) Zygmunt Krynicki 2005,
# Licensed under GPL, see COPYING for the whole text
#
# This script will look-up command in the database and suggest
# installation of packages available from the repository

command_not_found_handle() {
  if  [ -x /usr/bin/cnf ]; then
     /usr/bin/cnf "$1" 
     return $?
  else
     return 127
  fi        
} 
