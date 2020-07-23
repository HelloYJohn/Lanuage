#!/bin/bash
echo 'argc : ' $#
echo '$1: ' $1
echo '$2: ' $2
echo '$3: ' $3
echo '$4: ' $4
echo '$5: ' $5
./testargc.sh $1 $2 $3 $4 $5 $6 $7 $8 $9
echo `basename $0`
lv_str="abc"
echo ${#lv_str}
