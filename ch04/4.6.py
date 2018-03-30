import re

street_pattern = r"^[0-9]*\s[A-Z][a-z]*\s" \
    + r"(Street|St|Rd|Road|Ave|Avenue|Blvd|Way|Wy)"

print(street_pattern)

city_pattern = r"^[A-Z][a-z]*,\s[A-Z]{2},[0-9]{5}$"
address_pattern = street_pattern + r"\n" \
    + city_pattern

address_re = re.compile(address_pattern)
text = open("some_file.txt", "r").read()
print(text)
matches = re.findall(street_pattern, text)
print(matches)

open("addresses_w_space_between.txt", "w").write("\n\n".join(matches))