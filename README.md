==>  Security Log Keyword Scanner

A simple Python script that scans a log file for security-related keywords, saves matching lines to an output file, and generates a summary report.

==> What it does
- Reads a text log file
- Searches for multiple security-related keywords
- Writes matching lines to `output/matches.txt` (or a path you choose)
- Optionally writes a CSV summary report


==> Run the scanner on the included sample log.

3) Check outputs:
output/matches.txt
output/report.csv

==> Use your own log file
 python scanner.py --input sample_logs\sample.log --use-default-keywords --ignore-case --csv output\report.csv

