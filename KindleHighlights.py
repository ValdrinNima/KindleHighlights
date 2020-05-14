import os
import re
import pprint

# E:\documents\My Clippings.txt (?<=={10}\n
# for the title(?<=={10}\n-\s)

# get the "My Clippings" text document
with open(r"C:\Users\Valdrin\Desktop\My Clippings.txt", "rb") as clippings:
    content = clippings.read().decode('utf-8')
    print(content)
    # match the title (maybe author)
    titleRegex = re.compile(r'(?<=={10}\n-\s)')
    title_match = re.findall(titleRegex, content)
    print(title_match)
    # match the quote
    quoteRegex = re.compile(r"(?<=\n\n).+(?=\n={10})")
    quote_match = re.findall(quoteRegex, content)
    print(quote_match)
    title_quote_list = (list(zip(title_match, quote_match)))

'''Filtering the title_quote_list into a dict with the titles as the key and a list of corresponding
   quotes as the value'''

main_dict = {}
for title in title_match:
    main_dict[title] = []

for item in title_quote_list:
    main_dict[item[0]].append(item[1])
# print(main_dict)

someArray = []
for quotes in main_dict.values():
    for quote in quotes:
        pass




    # index = someArray.index(max(someArray))
    # new = quotes[index]
    # quotes.clear()
    # quotes.append(new)




# for title, quotes in main_dict.items():
#     for quote in quotes:
#         print(f"{title}\n{quote}")