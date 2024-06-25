from clean_data import clean_data
from merge_files import merge_csv

# Clean data for the main story
# clean_data("mhyk-main-story-script.txt", "mhyk-name-line.csv")

# Clean data for Murr's affection story
# clean_data("murr-affection-story-script.txt", "murr-affection-story-name-line.csv")

# Merge files
files = ["mhyk-name-line.csv", "murr-affection-story-name-line.csv"]
merge_csv(files, "all-name-line.csv")
