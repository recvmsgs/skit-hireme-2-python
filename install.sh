#!/bin/bash -x

WORKDIR="$PWD"

chmod u+x ./install.sh ./status.py

{ crontab -l | sed -e '/\/status.sh/d' -e '/mon wkday /d'; \
echo \
'# m  h   day mon wkday   command
   0 */1  *    *     *    '"$WORKDIR"'/status.py' ; } \
 | crontab - ;
 crontab -l
 