#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ["Clément Besnier <clem@clementbesnier.fr>", ]

import argparse
from runesdb import reader


def main(filename):
    return reader.read(filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="give an export file from RuneSDB")
    args = parser.parse_args()
    main(args.filename)
