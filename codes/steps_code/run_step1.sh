#!/bin/bash
module load gcc
module load python3
python3 step1.py 0 &
python3 step1.py 10 &
python3 step1.py 20 &
python3 step1.py 30 &
python3 step1.py 40 &
python3 step1.py 50
wait
