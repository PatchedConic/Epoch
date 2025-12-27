import argparse
from Epoch import Generator
import sys
from Epoch.GUI import Epoch
from PyQt6.QtWidgets import QApplication
import csv

def main():
    parser = argparse.ArgumentParser(
        prog = "Epoch Reference Implementation",
        description = "A part/drawing number generator based on the Epoch reference implementation",
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument("num_ID",
                       action = "store",
                       type = int,
                       nargs = '?',
                       default = 1,
                       help= "Number of ID's to generate. Default is 1.")
    parser.add_argument("-f", "--file",
                       action = "store",
                       type = str,
                       metavar = "<filepath>",
                       help = "File to save ID's to. Default is stdout.")

    group.add_argument("-c", "--check",
                       action = "store",
                       type = str,
                       metavar = "<part_number>",
                       help = "Check part number for validity")
    parser.add_argument("--version",
                        action = "version",
                        version = '%(prog)s 0.1.0')

    args = parser.parse_args()
    
    generator = Generator()

    if args.check:
        check = generator.check(args.check)
        print("Pass" if check else "Failed")
        sys.exit(0 if check else 1)
    
    if args.num_ID > 19:
        print(f"Large number of ID's requested. Estimated repsonse time: {args.num_ID/10} seconds.")

    if args.file:
        writer = csv.writer(open(args.file, "w", newline=''))
    for i in generator.generate(args.num_ID):
        if args.file:
            writer.writerow([i])
        print(i)
if __name__ == "__main__":
    main()