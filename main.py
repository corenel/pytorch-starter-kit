"""Main script for project."""

import argparse
import sys

import init_path
from core import demo, evaluate, train


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(
        description="PyTorch implementation for roadway.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", type=str, default=None,
                        help="path to image file")
    parser.add_argument("-r", "--restore", type=str, default=None,
                        help="path to model snapshot file")
    parser.add_argument("-m", "--mode",
                        default="train",
                        const="train",
                        nargs="?",
                        choices=["train", "evaluate", "demo"],
                        help="process mode (default: %(default)s)")
    return parser


if __name__ == '__main__':
    # parse arguments
    parser = parse_args()
    args = parser.parse_args()

    # process
    if args.mode == "train":
        train()
    elif args.mode == "evaluate":
        evaluate()
    elif args.mode == "demo" and args.input is not None:
        demo(args.input)
    else:
        parser.print_help()
        sys.exit(1)
