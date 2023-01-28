#!/bin/sh


#Auther Narendra
echo "what is your name"
read PERSON
echo "Hello, $PERSON"

NAME="nar"
readonly NAME
# you cant define the readonly variable again
#NAME="mah"

#file name of current script
echo $0 "\n \t file name of current script, \$0"
#argument with the script is invoked
echo $1 "\n \t argument with the script is invoked \$1"
echo $2 "\n \t argument with the script is invoked \$2"
#The number of arguments supplied to a script.
echo $# "\n \t The number of arguments supplied to a script. \$#"
#All the arguments are double quoted. If a script receives two arguments, $* is equivalent to $1 $2.
echo $* "\n \t All the arguments are double quoted. If a script receives two arguments, \$* is equivalent to \$1 \$2."
#All the arguments are individually double quoted. If a script receives two arguments, $@ is equivalent to $1 $2.
echo $@ "\n \t #All the arguments are individually double quoted. If a script receives two arguments, \$@ is equivalent to \$1 \$2."
#The exit status of the last command executed.
echo $?  "\n \t The exit status of the last command executed."


echo "\n \n \v"
echo "File Name: $0"
echo "First Parameter : $1"
echo "Second Parameter : $2"
echo "Quoted Values: $@"
echo "Quoted Values: $*"
echo "Total Number of Parameters : $#"