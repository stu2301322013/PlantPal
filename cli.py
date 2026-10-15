import sys

import plantpal


def main():
    if len(sys.argv) < 2:
        print("usage: python cli.py <command> [args]")
        return
    fn = getattr(plantpal, "cmd_" + sys.argv[1], None)
    if fn is None:
        print("unknown command:", sys.argv[1])
        return
    fn(*sys.argv[2:])


if __name__ == "__main__":
    main()
