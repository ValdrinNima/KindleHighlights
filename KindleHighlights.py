import os
import re

#E:\documents\My Clippings.txt
# for the title(?<=={10}\n-\s)

#get the "My Clippings" text document
with open(r"C:\Users\Valdrin\Desktop\My Clippings.txt", encoding="utf8") as clippings:
    clippings_text = clippings.read()

    #match the title (maybe author)
    titleRegex = re.compile(r"(?<=={10}\n\ufeff).+(?=\n)")
    title_match = re.findall(titleRegex, clippings_text)
    print(title_match)

    #match the quote
    quoteRegex = re.compile((r"(?<=\n\n).+(?=\n={10})"))
    quote_match = re.findall(quoteRegex, clippings_text)

