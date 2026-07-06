grade = [  ("Alice", "Math", 85),  ("Bob", "Science", 92),  ("Alice", "Science", 78),  ("Charlie", "Math", 90),  ("Bob", "Math", 88),  ("Alice", "English", 95)]

set_pelajar =set()
set_subjek =set()

for nama, subjek, markah in grade:
    set_pelajar.add(nama)
    set_subjek.add(subjek)

print(set_pelajar)
print(set_subjek)