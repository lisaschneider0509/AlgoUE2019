#!/bin/bash
# Basic while loop

counter=1
while [ $counter -le 25 ]
do
    (time python3 lisaschneider0509-TowersOfHanoi.py -n $counter > TowersOfHanoi.out 2>> DiskMoves.out) 2>> runntime.out
    ((counter++))
done

