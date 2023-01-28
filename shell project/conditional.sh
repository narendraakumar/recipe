#!/bin/sh


seconds=1

seconds=2
echo $seconds
echo $( ls )

c=0
for file in $( ls )
do
    echo $c $file
    echo "$c=$file"
    eval "var$c=$file"
    echo eval "var$c=$file"
    c=$((c+1))
    echo $c

    
done

echo $c


echo "Enter a value bet 1 to 10"

read choice
case $choice in
1)echo "you entered 1"
;;
2)echo "you entered 2"
;;
*)echo "you are in def case"
;;
esac



echo "enter something"

read input
case $input in
[a-z]) echo "you entered small case letter"
;;
[A-Z]) 
name="narendra"
echo $name
;;
?) echo "entered special char"
;;
"nn") echo "nn"
;;
*) echo "entered default"
;;

esac

