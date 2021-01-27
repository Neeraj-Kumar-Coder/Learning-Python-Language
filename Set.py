s = set()
print(type(s))
s.add(1)  # For adding elements
s.add(2)
s.add(3)
print(s)
s1 = set([4, 5, 6])
print(s.isdisjoint(s1))  # Checking the disjointion of two sets s and s1
print(s.union({2, 3, 4, 5, 6})) # Both methods of union are correct
print(s.union([2, 3, 4, 5, 6, 7])) # Both methods of union are correct