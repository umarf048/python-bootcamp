#text = "python programming" 

#rint(text[0])
#print(text[-1])
#print(text[0:6])
#print(text[:6])
#print(text[7:])
#print(text[1], text [7])

text = """Python is a powerful programming language. It's easy to learn and versatile! You can use Python for web development, data science, andautomation. The syntax is clean and readable. This makes Python perfect for beginners and experts alike"""

char_count = len(text)
word_count = len(text.split())
letter_count  = len(text.replace(" ",""))
sentence_count = text.count(".")+ text.count(" ?") + text.count("!")

print(f"character count: {char_count}")
print(f"word count:{word_count}")
print(f"letter count:{letter_count}")
print(f"sentence count:{sentence_count}")
