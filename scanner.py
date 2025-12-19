#!/usr/bin/env python3
"""
Basic Security Log Keyword Scanner
"""

import argparse
import os
import csv
from collections import Counter
from datetime import datetime

DEFAULT_KEYWORDS = [
    "failed", "denied", "unauthorized", "invalid",
    "login", "error", "forbidden", "blocked"
]

def scan_log(file_path, keywords):
    matches = []
    counts = Counter()

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            for word in keywords:
                if word.lower() in line.lower():
                    matches.append(line.strip())
                    counts[word] += 1
                    break
    return matches, counts

def write_text(lines, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def write_csv(counts, path, log_file):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Log File", log_file])
        writer.writerow(["Scan Time", datetime.now()])
        writer.writerow([])
        writer.writerow(["Keyword", "Count"])
        for k, v in counts.items():
            writer.writerow([k, v])

def main():
    parser = argparse.ArgumentParser(description="Scan logs for security keywords")
    parser.add_argument("-i", "--input", required=True, help="Log file to scan")
    parser.add_argument("-o", "--output", default="output/matches.txt", help="Text output file")
    parser.add_argument("--csv", help="Optional CSV report")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print("Log file not found.")
        return

    matches, counts = scan_log(args.input, DEFAULT_KEYWORDS)
    write_text(matches, args.output)

    if args.csv:
        write_csv(counts, args.csv, args.input)

    print("Scan complete.")
    print(f"Matched lines: {len(matches)}")

if __name__ == "__main__":
    main()
