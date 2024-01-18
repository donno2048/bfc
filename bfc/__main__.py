from sys import argv
try:
    from . import compile
except ImportError:
    from __init__ import compile
def main():
    if len(argv) != 3: return print(f"Usage: {argv[0]} input.bf output")
    compile(argv[1], argv[2])
if __name__ == "__main__":
    main()
