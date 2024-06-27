from clean_data import clean_data
from merge_files import merge_csv

if __name__ == "__main__":
    # Clean data for the main story (Part 1)
    clean_data("mhyk-main-story-script.txt", "mhyk-name-line.csv")

    # Clean data for the main story (Part 1.5)
    clean_data("mhyk-main-story-1.5-script.txt", "mhyk-1.5-name-line.csv")

    # Clean data for Murr's affection story
    clean_data("murr-affection-story-script.txt", "murr-affection-story-name-line.csv")

    # Clean data for Murr's spot story
    clean_data("murr-spot-story-script.txt", "murr-spot-story-name-line.csv")

    # Clean data for West prelude
    clean_data("west-prelude-script.txt", "west-prelude-name-line.csv")

    # Merge files
    files = ["mhyk-name-line.csv", "mhyk-1.5-name-line.csv", "murr-affection-story-name-line.csv", "murr-spot-story-name-line.csv", "west-prelude-name-line.csv"]
    merge_csv(files, "all-name-line.csv")
