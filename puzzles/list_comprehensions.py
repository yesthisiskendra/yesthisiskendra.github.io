cats = ["Michael", "Kevin", "Stanley", "Angela", "Dwight", "Phyllis"]
excited_cats = [cat.upper() for cat in cats]
print(excited_cats)

girl_cats = [cat for cat in cats if cat[-1] is 'a' or cat[-1] is 's']

print(girl_cats)
