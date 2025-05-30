#!/bin/bash
#measuee runtime with TIMEFORMAT
TIMEFORMAT='Took %R seconds to run the programs'
#run modified binary tree search program 100 times - run 100 times instead of 1000 to allow for the results to be scrutinised without powershell deleting the results
for i in {1..100}
do
    time {
        /mnt/c/users/darkt/PythonProject/unmodified/output/binary_trees_python.exe
    }
done
