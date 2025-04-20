import argparse
from Epoch import Generator

def main():
    parser = argparse.ArgumentParser(
        prog = "Epoch Reference Implementation",
        description = "A part/drawing number generator based on the Epoch reference implementation",
    )

    parser.add_argument("num_ID", action = "store", type = int, nargs = '?', default = 1)
    parser.add_argument("--version", action = "version", version = '%(prog)s 0.1')

    args = parser.parse_args()
    
    generator = Generator()

    if args.num_ID > 19:
        print(f"Large number of ID's requested. Estimated repsonse time: {args.num_ID/10} seconds.")
    for i in generator.generate(args.num_ID):
        print(i) 

if __name__ == "__main__":
    main()