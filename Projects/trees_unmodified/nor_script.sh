#!/bin/bash
#measuee runtime with TIMEFORMAT
TIMEFORMAT='Took %R seconds to run 1000 programs'
#run modified binary tree search program 1000 times
for i in {1..100}
do
    time {
        /mnt/c/users/darkt/projects/trees_unmodified/target/release/trees_unmodified.exe
    }
done