import collections

word_counter = collections.defaultdict(int)

text = """In the centre of the room, clamped to an upright easel, stood the
full-length portrait of a young man of extraordinary personal beauty,
and in front of it, some little distance away, was sitting the artist
himself, Basil Hallward, whose sudden disappearance some years ago
caused, at the time, such public excitement and gave rise to so many
strange conjectures.

As the painter looked at the gracious and comely form he had so
skilfully mirrored in his art, a smile of pleasure passed across his
face, and seemed about to linger there. But he suddenly started up, and
closing his eyes, placed his fingers upon the lids, as though he sought
to imprison within his brain some curious dream from which he feared he
might awake.

“It is your best work, Basil, the best thing you have ever done,” said
Lord Henry languidly. “You must certainly send it next year to the
Grosvenor. The Academy is too large and too vulgar. Whenever I have
gone there, there have been either so many people that I have not been
able to see the pictures, which was dreadful, or so many pictures that
I have not been able to see the people, which was worse. The Grosvenor
is really the only place.”
"""

for line in text.split("\n"):
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
