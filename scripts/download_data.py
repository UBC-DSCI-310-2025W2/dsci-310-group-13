import pandas as pd
import sys
import os

# command line arguments
red_url = sys.argv[1]
white_url = sys.argv[2]
output_dir = sys.argv[3]

# create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# download datasets
red = pd.read_csv(red_url, sep=";")
white = pd.read_csv(white_url, sep=";")

# define output paths
red_output = os.path.join(output_dir, "winequality-red.csv")
white_output = os.path.join(output_dir, "winequality-white.csv")

# save raw files
red.to_csv(red_output, index=False)
white.to_csv(white_output, index=False)

print("Red wine data saved to:", red_output)
print("White wine data saved to:", white_output)