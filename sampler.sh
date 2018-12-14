#!/usr/bin/env bash
for c in {a..z}
do
    for((i=0;i<1;i++))
    do
        python generate.py --prime_str ${c} > sample.txt
    done
done