raw = "  alice SMITH "
print(raw.strip().title())
words = ['BOB', 'jones']
print(" ".join(words).title())
name1 = "  alice SMITH "
name2 = "BOB  jones"
name3 = " carol DAVIS  "
print(name1.strip().title())
print(" ".join(words).title())
print(name3.strip().title())