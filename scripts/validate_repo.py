#!/usr/bin/env python3
import os, sys

ROOT = os.path.dirname(os.path.dirname(__file__))
required = [
    "README.md", "LICENSE", "CONTRIBUTING.md",
    "docs/00-abstract.md", "charts/rarity_square_charts.md"
]

missing = [p for p in required if not os.path.exists(os.path.join(ROOT, p))]
if missing:
    print("Missing files:", ", ".join(missing))
    sys.exit(1)
print("Repository structure OK.")
