#!/usr/bin/python3
"""
1-main: Script to test the top_ten function from 1-top_ten.py.
"""
import sys

# Ensure the module is in the path for import
try:
    # Attempt to import the function from the neighboring file
    top_ten = __import__('1-top_ten').top_ten
except ImportError:
    # Fallback or error if the file is not found
    print("Error: Could not find '1-top_ten.py'. Ensure it's in the same directory.")
    sys.exit(1)


if __name__ == '__main__':
    # Check if a subreddit argument was provided
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        # Call the top_ten function with the provided argument
        top_ten(sys.argv[1])