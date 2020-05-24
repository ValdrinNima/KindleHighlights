import os
import re
import pprint

# E:\documents\My Clippings.txt (?<=={10}\n
# for the title(?<=={10}\n).+\n
# for the quotes (?<=\n\n).*(?=\n={10})


# with open(r"C:\Users\Valdrin\Desktop\My Clippings.txt", encoding="utf-8", mode="r+") as clippings:
#    content = clippings.read
#    if content[0] != "﻿==========\n":
#
#        content.seek(0)
#        content.write("==========\n")
#        print("shit has been added")


# get the "My Clippings" text document
with open(r"C:\Users\Valdrin\Desktop\My Clippings.txt", encoding="utf-8") as clippings:
    content = clippings.read()
    # match the title (maybe author)
    titleRegex = re.compile(r'(?<=={10}\n).+\n')
    title_match = re.findall(titleRegex, content)

    # match the quote
    quoteRegex = re.compile(r"(?<=\n\n).*(?=\n={10})")
    quote_match = re.findall(quoteRegex, content)
    title_quote_list = (list(zip(title_match, quote_match)))

'''Filtering the title_quote_list into a dict with the titles as the key and a list of corresponding
   quotes as the value'''

title_quote_list = [comb for comb in title_quote_list if comb[1] != ""]

# for comb in title_quote_list:
#     print(comb)

main_dict = {}
for title in title_match:
    main_dict[title] = []

for item in title_quote_list:
    main_dict[item[0]].append(item[1])

for key, value in main_dict.items():
    print(key, value)

for quotes in main_dict.values():
    for i in range(len(quotes)-1):
        j = i + 1
        if j > len(quotes)-1:
            break
        if quotes[i] in quotes[j] or quotes[j] in quotes[i]:
            if len(quotes[i]) < len(quotes[j]):
                del quotes[i]
            else:
                del quotes[j]


for key, value in main_dict.items():
    print(key, value)