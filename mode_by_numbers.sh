#!/bin/bash
# script to see what each number called to chmod does to permissions

for mod_num in `seq 0 9`; do
echo $mod_num
chmod $mod_num $1
ls -l | grep $1 | cut -d " " -f 1
done
