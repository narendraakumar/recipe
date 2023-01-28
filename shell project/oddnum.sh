#!/bin/sh

NUMS="1 2 3 4 5 6 7"
for NUM in $NUMS
do
    remainder=`expr $NUM % 2`
    if [ $remainder -eq 0 ]
    then
        echo "$NUM is even"
    else
        echo "$NUM is odd"
    fi
done 
DATE=`date`
echo "Date is $DATE"