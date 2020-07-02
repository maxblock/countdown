# Countdown Solver
Inspired by the television show Countdown.

## Problem Description
Each instance has a target and a set of numbers. The numbers may combined in any way using addition, subtraction, and multiplication. Players may also calculate in any order, i.e., using brackets.

## Usage
```
> py countdown.py target [numbers]
```

For example
```
> py countdown.py 843 100 75 10 2 8 5
Trying to reach 843 using 100, 75, 10, 2, 8, 5
    New best: 100+75=175, distance: 668
    New best: 100*10=1000, distance: 157
    New best: 100*8=800,  distance: 43
    New best: 100+75*10=850, distance: 7
    New best: (100+5)*8=840, distance: 3
    New best: 100-(8-75*10)=842, distance: 1
    New best: 100-2-(5-75*10)=843, distance: 0
```