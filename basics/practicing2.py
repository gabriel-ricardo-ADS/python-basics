## TREINO COM A BIBLIA

dict_old_testament = {"Genesis" : 50, "Exodus" : 40, "Leviticus" : 27, "Numbers" : 36, "Deuteronomy" : 34,
        "Joshua" : 24, "Judges" : 21, "Ruth" : 4, "1 Samuel" : 31, "2 Samuel" : 24,
        "1 Kings" : 22, "2 Kings" : 25, "1 Chronicles" : 29, "2 Chronicles" : 36, "Ezra" : 10,
        "Nehemiah" : 13, "Esther" : 10, "Job" : 42, "Psalms" : 150, "Proverbs" : 31,
        "Ecclesiastes" : 12, "Song of Solomon" : 8,
        "Isaiah" : 66, "Jeremiah" : 52, "Lamentations" : 5, "Ezekiel" : 48, "Daniel" : 12,
        "Hosea" : 14, "Joel" : 3, "Amos" : 9, "Obadiah" : 1, "Jonah" : 4,
        "Micah" : 7, "Nahum" : 3, "Habakkuk" : 3, "Zephaniah" : 3, "Haggai" : 2,
        "Zechariah" : 14, "Malachi" : 4,}

dict_new_testament = {"Matthew" : 28, "Mark" : 16, "Luke" : 24, "John" : 21, "Acts" : 28,
        "Romans" : 16, "1 Corinthians" : 16, "2 Corinthians" : 13, "Galatians" : 6, "Ephesians" : 6,
        "Philippians" : 4, "Colossians" : 4,
        "1 Thessalonians" : 5, "2 Thessalonians" : 3, "1 Timothy" : 6, "2 Timothy" : 4, "Titus" : 3,
        "Philemon" : 1, "Hebrews" : 13, "James" : 5, "1 Peter" : 5, "2 Peter" : 3,
        "1 John" : 5, "2 John" : 1, "3 John" : 1, "Jude" : 1, "Revelation" : 22,}

dict_Bible = {"Old Testament" : dict_old_testament, "New Testament" : dict_new_testament}

def number_of_books(dict_Bible):
    total_books = 0
    for testament in dict_Bible:
        total_books += len(dict_Bible[testament])
    return total_books

def number_of_chapters(dict_Bible):
    total_chapters = 0
    for testament in dict_Bible:
        for book in dict_Bible[testament]:
            total_chapters += dict_Bible[testament][book]
    return total_chapters

print(f"The Bible has {number_of_books(dict_Bible)} books", "now, choose to discover: ")
input_number_of_books = input("Old or New Testament? ").strip().title()
print("-" * 30)
while True:
    if input_number_of_books == "Old" or input_number_of_books == "Old Testament":
        print(f"The Old Testament has {len(dict_Bible['Old Testament'])} books.")
        break
    elif input_number_of_books == "New" or input_number_of_books == "New Testament":
        print(f"The New Testament has {len(dict_Bible['New Testament'])} books.")
        break
    else:
        print("Invalid") 
        input_number_of_books = input("Old or New Testament? ")
print("-" * 30)   
print(f"They together gather {number_of_chapters(dict_Bible)} chapters!")
print("-" * 30)
input_testament = input("Put a book of the Bible: ").strip().title()
print("-" * 30)
while True:
    if input_testament in dict_Bible["Old Testament"]:
        print(f"{input_testament} has {dict_Bible['Old Testament'][input_testament]} chapters.")
        break
    elif input_testament in dict_Bible["New Testament"]:
        print(f"{input_testament} has {dict_Bible['New Testament'][input_testament]} chapters.")
        break
    else:
        print("Book not found in the Bible.")

input("Press ENTER to end")
    
