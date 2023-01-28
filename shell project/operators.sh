#!/bin/sh


val=`expr 2 + 2`
echo "$val"

a=10
b=20
val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $a / $b`
echo "a / b : $val"

val=`expr $a % $b`
echo "a % b : $val"

if [ $a == $b ]
then
    echo "a is equal to b"
fi

if [ $a != $b ]
then
    echo "a is not equal to b"
fi


if [ $a -eq $b ]
then
    echo "$a -eq $b : a is equal to b"
else
    echo "$a -eq $b : a is not equal to b"
fi

if [ $a -ne $b ]
then
    echo "$a -ne $b : a is not equal to b"
else
    echo "$a -ne $b : a is equal to b"
fi

if [ $a -gt $b ]
then
    echo "$a -gt $b : a is greater to b"
else
    echo "$a -gt $b : a is not greater to b"
fi


if [ $a -lt $b ]
then
    echo "$a -lt $b : a is less than to b"
else
    echo "$a -lt $b : a is not less than to b"
fi

if [ $a -ge $b ]
then
    echo "$a -ge $b : a is greater than or equal to b"
else
    echo "$a -ge $b : a is not greater than or equal to b"
fi


if [ $a -le $b ]
then
    echo "$a -le $b : a is less than or equal to b"
else
    echo "$a -le $b : a is not less than or equal to b"
fi


NEG="not"
file=$0
echo $file
if [ -r $file ]
then
    echo "file has read access"
else
    echo "file has not read access"
fi

if [ -w $file ] 
then
    echo "file has write access"
else
    echo "file dont have write access"
fi

var1="file has execute permission" 
if [ -x $file ]
then
    echo $var1 
else
    echo $var1 $NEG
fi

if [ -f $file ]
then
    echo "file is ordinary file"
else
    echo "file is special"
fi

if [ -d $file ]
then
    echo "file is directory"
else
    echo "file is not directory"
fi

if [ -s $file ]
then
    echo "file size is not zero"
else
    echo "file size is zero"
fi

if [ -e $file ]
then
    echo "file exists"
else
    echo "file not exists"
fi
