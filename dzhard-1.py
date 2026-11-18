student = [("Анна", 16), ("Бронислав", 15), ("Федот", 18)]
old=max(student, key=lambda x:x[1])
print(old[0])