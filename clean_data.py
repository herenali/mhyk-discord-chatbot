import csv
import re

with open("mhyk-main-story-script.txt") as text_file:
    with open("mhyk-name-line.csv", "w") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('name', 'line'))

        line = text_file.readline()
        while line != "":
            if line != "\n":
                line = line.strip("\n")
                line = re.sub("\n", " ", line)
                if ":" in line:
                    print(line)
                    line = re.split(": ", line)
                # for i in range(len(line)):
                #     line[i] = re.sub("\n", " ", line[i])
                writer.writerow(line)
            line = text_file.readline()

            # TODO: fix issue of lines cutting off
