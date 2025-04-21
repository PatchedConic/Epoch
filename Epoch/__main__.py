import argparse
from Epoch import Generator
import sys
from Epoch.GUI import Epoch
from PyQt6.QtWidgets import QApplication

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
                       default = 1)
    group.add_argument("-g", "--gui",
                       action = "store_true",
                       help = "Launch GUI application")
    group.add_argument("-c", "--check",
                       action = "store",
                       type = str,
                       help = "Check part number for validity")
    parser.add_argument("--version",
                        action = "version",
                        version = '%(prog)s 0.1')


    args = parser.parse_args()
    
    generator = Generator()

    if args.gui:
        app = QApplication(sys.argv)
        window = Epoch()
        window.show()
        return app.exec()

    if args.check:
        check = generator.check(args.check)
        print(check)
        sys.exit(0 if check else 1)
    
    if args.num_ID > 19:
        print(f"Large number of ID's requested. Estimated repsonse time: {args.num_ID/10} seconds.")
    for i in generator.generate(args.num_ID):
        print(i) 

if __name__ == "__main__":
    main()