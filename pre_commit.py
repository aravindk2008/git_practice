#!/usr/bin/env python3

import subprocess
import sys

def get_files():
    r = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True,
        text=True
    )
    return r.stdout.split()

def check(f):
    e = []

    if not f.endswith(".sv"):
        return e

    try:
        with open(f, "r") as file:
            l = file.readlines()
    except:
        return [f + ": cannot read file"]

    # Check line length
    for i, x in enumerate(l, 1):
        if len(x.rstrip("\n")) > 120:
            e.append(f"{f}: line {i} exceeds 120 characters")

    # Check for reg
    c = "".join(l)
    if "reg" in c:
        e.append(f"{f}: deprecated keyword 'reg' used")

    # Check header
    h = "".join(l[:5])

    if "Author:" not in h:
        e.append(f"{f}: missing Author: in first 5 lines")

    if "Date:" not in h:
        e.append(f"{f}: missing Date: in first 5 lines")

    return e

def main():
    err = []

    for f in get_files():
        err += check(f)

    if err:
        print("\nPRE-COMMIT CHECK FAILED\n")
        for x in err:
            print(x)
        sys.exit(1)

    print("All SystemVerilog checks passed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
