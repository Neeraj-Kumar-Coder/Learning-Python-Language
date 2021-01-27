d1 = {"Bittu": "Roti", "Neha": "Pizza"}
# print(type(d1))
# print(d1["Bittu"])

# # Dictionary in Dictionary
# d2 = {"Bittu": {"Day": "roti", "Night": "Rice"}, "Master": "Legend"}
# print(type(d2))
# print(d2["Bittu"])
# print(d2["Bittu"]["Night"])

# # With copy() function
# d3 = d2.copy()
# print(d3)
# del d3["Bittu"]
# print(d3)

# # Without copy() function
# d4 = d2
# print(d4)
# del d4["Bittu"]
# print(d2)

print(d1.keys())
print(d1.items())
print(d1.values())
d1.update({"new": "value", "legend": "shark"})
print(d1)