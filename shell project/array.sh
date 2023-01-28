#!/bin/sh

NAME1="narendra"
NAME2="narendra2"

NAME[0]="narendra"
NAME[1]="narendra2"

echo $NAME $NAME1

echo ${NAME[1]}
ARRAY=(1,2,3)
echo $ARRAY

for NME in ${NAME[*]}
do
    echo $NME
done

for NME in ${ARRAY}
do
    echo $NME
done