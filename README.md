# Calculator of dot products

**Author:**
Danielė Stasiūnaitė, IFM 4/2 gr.

**Subject:**
Component Based System Engineering


---
## About the component

---

## Features

---

## Installation
```

```
---

## Usage
The installed component can be used in multiple ways, where different `vdot` program usages are described below. Input files that are used to explain program usage are available in directory `Inputs`:
**1. One input file**.
The program reads one provided file that contains vector values.

***Program call:***
```
vdot ./Inputs/even_nnum.dat
```

***Expected result:***
```
Processing ./Inputs/even_nnum.dat...
Working with vectors: 5 6a 8 9              2.3 4.05 6.001 1.5
Value '6a' does not match numeric syntax in./Inputs/even_nnum.dat!

Working with vectors: 1.5 6.5 5 1.5         3.6 4.05 6_ -6.3
Value '6_' does not match numeric syntax in./Inputs/even_nnum.dat!

Working with vectors: 4 5 6 4               7 4 9d 9
Value '9d' does not match numeric syntax in./Inputs/even_nnum.dat!

Working with vectors: 6.2 5.8 -7.1 5.02    -0.1 -1.05 -1.25 -0.99
Result (dot product): -2.8048

Working with vectors: 7.39 10.31 6.42 7.4   8.88 1.11 7.4 6.96
Result (dot product): 176.079

Working with vectors: 3.84 7.72 2.52 7.87   2.59 4.65 3.91 3.93
Result (dot product): 86.6259

# 3 vector pair(-s) was(were) multiplied in total.
```

**2. Multiple input files**.
The program reads multiple provided files that contain vector values.

***Program call:***
```
vdot ./Inputs/even_nnum.dat ./Inputs/odd_num.dat [file3 file4 ...]
```

***Expected result:***
```
Processing ./Inputs/even_nnum.dat...
Working with vectors: 5 6a 8 9              2.3 4.05 6.001 1.5
Value '6a' does not match numeric syntax in./Inputs/even_nnum.dat!

Working with vectors: 1.5 6.5 5 1.5         3.6 4.05 6_ -6.3
Value '6_' does not match numeric syntax in./Inputs/even_nnum.dat!

Working with vectors: 4 5 6 4               7 4 9d 9
Value '9d' does not match numeric syntax in./Inputs/even_nnum.dat!

Working with vectors: 6.2 5.8 -7.1 5.02    -0.1 -1.05 -1.25 -0.99
Result (dot product): -2.8048

Working with vectors: 7.39 10.31 6.42 7.4   8.88 1.11 7.4 6.96
Result (dot product): 176.079

Working with vectors: 3.84 7.72 2.52 7.87   2.59 4.65 3.91 3.93
Result (dot product): 86.6259

# 3 vector pair(-s) was(were) multiplied in total.

Processing ./Inputs/odd_num.dat...
Working with vectors: 6 3 4 1     9 2 3 4
Result (dot product):    76

Working with vectors: 5 2 3 4     5 3 6
Issue: vector component count is not even!

Working with vectors: 0.1 5 6     5 8 9 1.3
Issue: vector component count is not even!

Working with vectors: 9 7 3 4     9 9 7 3
Result (dot product):   177

# 2 vector pair(-s) was(were) multiplied in total.
```


**3. One or more input files and '-f'**.
The program reads one or more provided files that contain vector values and displays the formatted scalar product (`-f` is used to specify the format; allowed formats: `5.6g`, `3.3e`, `4.4f`):


***Program calls:***
```
vdot ./Inputs/even_nnum.dat -f 3.3e
```

```
vdot ./Inputs/even_nnum.dat ./Inputs/odd_num.dat -f 3.3e
```

***Expected result (the first example):***
```
Processing ./Inputs/even_nnum.dat...
Working with vectors: 5 6a 8 9              2.3 4.05 6.001 1.5
Value '6a' does not match numeric syntax in./Inputs/even_nnum.dat!

Working with vectors: 1.5 6.5 5 1.5         3.6 4.05 6_ -6.3
Value '6_' does not match numeric syntax in./Inputs/even_nnum.dat!

Working with vectors: 4 5 6 4               7 4 9d 9
Value '9d' does not match numeric syntax in./Inputs/even_nnum.dat!

Working with vectors: 6.2 5.8 -7.1 5.02    -0.1 -1.05 -1.25 -0.99
Result (dot product): -2.805e+00

Working with vectors: 7.39 10.31 6.42 7.4   8.88 1.11 7.4 6.96
Result (dot product): 1.761e+02

Working with vectors: 3.84 7.72 2.52 7.87   2.59 4.65 3.91 3.93
Result (dot product): 8.663e+01

# 3 vector pair(-s) was(were) multiplied in total.

```
---

## CHANGELOG
---


## License
```
MIT License

Copyright (c) 2025 Danielė

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```