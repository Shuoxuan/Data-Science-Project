import csv
import re

def splitGenres(dirty):
    #insert spaces
    dirty = re.sub(r"(\w)([A-Z])", r"\1 \2", dirty)
    dirty = dirty.replace("(", "")
    dirty = dirty.replace("U SA)", "")

    m = re.search("\d", dirty)

    if m:
        pos = m.start()
        return dirty[:pos], dirty[pos:].rstrip().replace(" ", "-")

    return dirty, ""

def splitLevel(dirty):
    m = re.search(",", dirty)
    if m:
        pos = m.start()
        return dirty[:pos]
    return dirty



with open('./imdb.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    with open('cleanIMDB.csv', 'w', newline='') as csvfile:
        #spamwriter = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in csv_reader:
            if line_count == 0:
                row.append("release_date")
                spamwriter.writerow(row)
                line_count += 1
            else:
                genres, release_date = splitGenres(row[0].strip())
                row.append(release_date)
                row[0] = genres
                row[1] = splitLevel(row[1].strip()).rstrip()
                row[2] = row[2].strip()
                row[3] = row[3].strip()
                row[4] = row[4].strip()
                row[5] = row[5].strip()

                if "TV" not in row[1] and "TV" not in row[0]:
                    spamwriter.writerow(row)
                    line_count += 1
        print(f'Processed {line_count} lines.')
