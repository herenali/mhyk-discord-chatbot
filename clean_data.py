import csv
import re

with open("mhyk-main-story-script.txt") as text_file:
    with open("mhyk-name-line.csv", "w") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(("name", "line"))

        line = text_file.readline()
        while line != "":
            last_line = []
            line_lst = []
            if line != "\n":
                line = line.strip("\n")

                if ":" in line and re.search("[0-9]", line) is None:
                    line_lst = re.split(":\xa0", line)
                    line = text_file.readline()
                elif re.search("[0-9]", line) is None and re.search("[a-zA-Z]", line) is not None:
                    line_lst.append("Narrator")
                    line_lst.append(line)
                    line = text_file.readline()
                else:
                    line = text_file.readline()
                    continue

                while line != "\n" and line != "":
                    line = line.strip("\n")
                    line_lst[-1] += " " + line
                    line = text_file.readline()

                # Fix encoding issues
                for i in range(len(line_lst)):
                    line_lst[i] = re.sub("’", "'", line_lst[i])
                    line_lst[i] = re.sub(" ", " ", line_lst[i])
                    line_lst[i] = re.sub("—", "-", line_lst[i])

                # Check for repeated lines
                # if line_lst == last_line:
                #     print(line_lst)
                # last_line = line_lst
                
                writer.writerow(line_lst)

            line = text_file.readline()
