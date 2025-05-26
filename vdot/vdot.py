#!/usr/bin/env python3

import sys, os, argparse

def calculate_dot_product(output, vectors: str, filename: str, frmt):
    split_vector = vectors.strip().split()
    if len(split_vector) % 2 != 0:
        print(f"Issue: vector component count is not even!\n")
        return None
    else:
        mid = len(split_vector) // 2
        first_part, second_part, mul_results = [], [], []

        for i, val in enumerate(split_vector):
            try:
                val = float(val)
            except ValueError:
                print(f"Value '{val}' does not match numeric syntax in"
                      f"{filename}!\n")
                return None

            if i < mid:
                first_part.append(val)
            else:
                second_part.append(val)

        for a, b in zip(first_part, second_part):
            mul_results.append(a * b)

        dot_product = sum(mul_results)
        print(f"Result (dot product): {format(dot_product, frmt)}\n")
        return dot_product

def handle_input(output, files, frmt):
    if isinstance(files, str):
        files = [files]

    for file in files:
        results = []
        print(f"\nProcessing {file}...")

        if not os.path.exists(file):
            print(f"Cannot open '{file}': No such file!")
            continue

        with open(file, 'r') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()

            if not line or line.startswith('#'):
                continue
            try:
                print(f"Working with vectors: {line}")
                results.append(calculate_dot_product(output, line, file, frmt))
            except ValueError as e:
                sys.stderr.write(str(e) + '\n')

        try:
            print(str(f"# {len([sum for sum in results if sum is not None])} "
                        f"vector pair(-s) was(were) multiplied in total."))
        except (IOError, OSError) as e:
            print(f"Error writing to file '{output}': {e}...")

    return ""

def main():
    parser = argparse.ArgumentParser(
        description = "Process one or more input files.")
    parser.add_argument(
        "files",
        nargs = '+',  # '+' means one or more arguments
        help = "Path(s) to input file(s)")
    parser.add_argument("-f", "--format", choices=["5.6g", "3.3e",
                                                   "4.4f"], default="5.6g")

    args = parser.parse_args()
    output_file = (
        str(os.path.splitext(os.path.basename(args.files[0]))[0] + ".rez"))
    handle_input(output_file, args.files, args.format)

if __name__ == "__main__":
    main()