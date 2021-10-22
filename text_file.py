import collections

word_counter = collections.defaultdict(int)

with open("sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        line = line.replace(',', '')
        line = line.replace('.', '')
        line = line.replace('”', '')
        line = line.replace('“', '')
        line = line.lower()
        print(line)
        words = line.split()

        for word in words:
            word_counter[word] += 1

print(word_counter)
