#!/usr/bin/python3
import sys
"""Log Parsing module"""


def print_stats(total_size, status_counts):
    """Prints statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


def process_line(line, total_size, status_counts):
    """Processes Line"""
    try:
        parts = line.split()
        if len(parts) == 10:
            status_code = int(parts[8])
            file_size = int(parts[9])
            total_size += file_size

            if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

        return total_size, status_counts
    except (ValueError, IndexError):
        return total_size, status_counts


def main():
    """Main method to call functions"""
    total_size = 0
    status_counts = {}
    line_count = 0

    try:
        for line in sys.stdin:
            total_size, status_counts = process_line(line.strip(), total_size, status_counts)
            line_count += 1

            if line_count == 10:
                print_stats(total_size, status_counts)
                line_count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
