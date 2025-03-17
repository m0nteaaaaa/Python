# WAP TO GREET ALLL THE PERSONS NAMES STORED IN A LIST "L" AND WHICH STARTS WITH S.
l = ["Monty","Soham","Sachin","Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
    else:
        continue