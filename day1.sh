#!/bin/sh

input=$1
a=`sed 's/)//g' $input | wc -m`
b=`sed 's/(//g' $input | wc -m`

echo `expr $a - $b`
