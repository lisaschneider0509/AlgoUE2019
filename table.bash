#!/bin/bash

for ((i=1;i <=100;i++))
do
    echo $i
    time -p ./fibo_efficient.py -n $i
done
