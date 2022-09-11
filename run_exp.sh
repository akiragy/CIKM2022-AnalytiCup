#!/bin/bash
rm -r exp/group*

for i in {1..3};do
  nohup python group${i}.py > log${i} &
done
wait

python merge_results.py