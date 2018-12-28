import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str,
                        help="Enter a valid equation using 'x', 'X', '+', '*', '^', '.', '=' and integers.\n"
                             "The equation must be a string.")
    parser.add_argument("-d", "--delta", type=int, default=0,
                        help="write '-d 1' to display delta")

    args = parser.parse_args()
    return args.input, args.delta


if __name__ == "__main__":
    print(get_args())
