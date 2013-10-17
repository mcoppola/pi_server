#!/bin/sh
#
#ZIP DIRECTORY for pi_server
#arguments = account, loc
#dir to zip = data/(account)/(loc)
#put zip : data/(acount)/(loc)/(loc).zip
echo $1
echo $2

zip -r data/$1/$2/$2.zip data/$1/$2/