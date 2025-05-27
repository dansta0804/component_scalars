# Calculator of dot products

**Author:**
Danielė Stasiūnaitė, IFM 4/2 gr.

**Subject:**
Component Based System Engineering

---

## About the component
The `vdot` component is an educational tool for upper secondary school (11-12) students who want to better understand the concept of vector scalar product and improve their Python programming language skills by developing programs that integrate the developed component.

---

## ✨ Features
The Python component processes text files containing vectors, computes scalar products and displays the results in a specified format.

#### Input
The component is able to process input files containing:
- Comment lines (they do not contain vector values). These lines start symbol `#`;
- Empty lines;
- Vector values that are provided in a scientific notation (for example, `-5.125e19`);
- Lines with non-numeric vector values (for example, `6d`);
- Odd number of vector values in a line (in such case scalar product cannot be computed).

#### Result
The result (the scalar product) is represented using the default format `5.6g`, which indicates that small numbers are represented using a low decimal expression, very large or very small values are represented using an exponential format (scientific notation).

---

## ⚙️ Installation
```
pip install git+https://github.com/dansta0804/component_scalars.git
```
---

## 📝 Methods
| Method name   | Description    | Parameters    | Output    |
|---------------|----------------|----------------|----------------|
| ``calculate_dot_product (output, str vectors, str filename, frmt)``  | Calculates the dot product of two vectors in a string. | ``vectors:`` a string with vector elements separated by space; ``filename:`` - name of the file (used for error messages); ``frmt`` - output format string (e.g., '5.6g'). | Dot product as float or None if error.|
| ``handle_input (output, files, frmt)``  | Processes input files and computes dot products from each line. | ``files:`` - a list of input file paths; ``frmt`` - output format string (e.g., '5.6g'). | Nothing. Prints results to stdout.|

---

## ❓ Usage
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

## 🔍 CHANGELOG
---
