"""Main script for project."""

import argparse
import sys

from core import demo, evaluate, train
from utils import logger


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(
        description="PyTorch implementation for roadway.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", type=str, default=None,
                        help="path to image file")
    parser.add_argument("-r", "--restore", type=str, default=None,
                        help="path to model snapshot file")
    parser.add_argument("-v", "--verbose", help="set log level to debug",
                        action="store_true")
    parser.add_argument("-s", "--silent", help="set log level to error",
                        action="store_true")
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

    # set log level
    if args.verbose:
        logger.set_level("debug")
    elif args.silent:
        logger.set_level("error")

    # process
    if args.mode == "train":
        train(logger)
    elif args.mode == "evaluate":
        evaluate(logger)
    elif args.mode == "demo" and args.input is not None:
        demo(args.input, logger)
    else:
        parser.print_help()
        sys.exit(1)
