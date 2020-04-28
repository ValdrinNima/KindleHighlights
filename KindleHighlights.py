import os
import re

# E:\documents\My Clippings.txt
# for the title(?<=={10}\n-\s)

# get the "My Clippings" text document
with open(r"C:\Users\Valdrin\Desktop\My Clippings.txt", encoding="utf8") as clippings:
    clippings_text = clippings.read()

    # match the title (maybe author)
    titleRegex = re.compile(r"(?<=={10}\n\ufeff).+(?=\n)")
    title_match = re.findall(titleRegex, clippings_text)

    # match the quote
    quoteRegex = re.compile(r"(?<=\n\n).+(?=\n={10})")
    quote_match = re.findall(quoteRegex, clippings_text)

    title_quote_list =(list(zip(title_match, quote_match)))

'''Filtering the title_quote_list into a dict with the titles as the key and a list of corresponding
   quotes as the value'''

main_dict = {}
for title in title_match:
    main_dict[title] = []


for item in title_quote_list:
    main_dict[item[0]].append(item[1])

print(main_dict)

someArray = []
for value in main_dict.values():
    for quote in value:
        someArray.append(len(quote))

    index = someArray.index(max(someArray))
    new = value[index]
    value.clear()
    value.append(new)

print(main_dict)