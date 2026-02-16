"""Starter pipeline for tgisNutri-AI

This module provides a minimal entrypoint that will coordinate
future detection, classification, depth, and nutrition steps.
"""

import argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent


def run_detection():
    print("Run detection (TODO)")


def run_classification():
    print("Run classification (TODO)")


def run_depth():
    print("Run depth estimation (TODO)")


def run_nutrition():
    print("Run nutrition estimation (TODO)")


def main():
    parser = argparse.ArgumentParser(description="tgisNutri-AI main pipeline")
    parser.add_argument("--stage", choices=["all","detect","classify","depth","nutrition"], default="all")
    args = parser.parse_args()

    if args.stage in ("all","detect"):
        run_detection()
    if args.stage in ("all","classify"):
        run_classification()
    if args.stage in ("all","depth"):
        run_depth()
    if args.stage in ("all","nutrition"):
        run_nutrition()


if __name__ == "__main__":
    main()
