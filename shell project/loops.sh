#!/bin/sh

a=0

while [ $a -lt 10 ]
do 
    b=$a
    while [ $b -gt 0 ]
    do
        echo "$b \t"
        b=$(($b-1))
    done
    echo
    a=`expr $a + 1`
done


b=1
c=$(($b+1))
echo $c