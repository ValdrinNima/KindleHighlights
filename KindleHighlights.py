import os
import re

# E:\documents\My Clippings.txt (?<=={10}\n
# for the title(?<=={10}\n).+\n
# for the quotes (?<=\n\n).*(?=\n={10})

homedrive = os.getenv('HOMEDRIVE')
user = os.getenv('USERNAME')
homepath = os.getenv('HOMEPATH')
desktop = "Desktop\\"
myclippings = "My Clippings.txt"
html_file = "Kindle_Zitate.html"

DESKTOP_PATH_CLIPPINGS = os.path.join(homedrive, user, homepath, desktop, myclippings)
DESKTOP_PATH_HTML = os.path.join(homedrive, user, homepath, desktop, html_file)

# edit the clippings file so that the regex works - not optimal :(
edit_needed = False

with open(DESKTOP_PATH_CLIPPINGS, encoding="utf-8", mode="r") as clippings:
    content = clippings.readlines()
    if content[0] != "==========\n":
        edit_needed = True

if edit_needed:
    with open(DESKTOP_PATH_CLIPPINGS ,encoding="utf-8", mode='r') as contents:
        save = contents.read()
    with open(DESKTOP_PATH_CLIPPINGS ,encoding="utf-8", mode='w') as contents:
        contents.write("==========\n")
    with open(DESKTOP_PATH_CLIPPINGS ,encoding="utf-8", mode='a') as contents:
        contents.write(save)


# get the "My Clippings" text document
with open(DESKTOP_PATH_CLIPPINGS , encoding="utf-8") as clippings:
    content = clippings.read()
    # match the title (maybe author)
    titleRegex = re.compile(r'(?<=={10}\n).+\n')
    title_match = re.findall(titleRegex, content)

    # match the quote
    quoteRegex = re.compile(r"(?<=\n\n).*(?=\n={10})")
    quote_match = re.findall(quoteRegex, content)

    # match the note
    quoteRegex =

    title_quote_list = (list(zip(title_match, quote_match)))
    # title_quote_list is a list of tuples with two values: title and quote

'''Filtering the title_quote_list into a dict with the titles as the key and a list of corresponding
   quotes as the value'''

title_quote_list = [comb for comb in title_quote_list if comb[1] != ""]


main_dict = {}
for item in title_quote_list:
    if item[0] not in main_dict:
        main_dict[item[0]] = []

for item in title_quote_list:
    main_dict[item[0]].append(item[1])

for quotes in main_dict.values():
    i = 0
    while i < len(quotes)-1:
        # i is index a quote and j of the following quote
        j = i + 1
        if j > len(quotes)-1:
            break
        if quotes[i] in quotes[j] or quotes[j] in quotes[i]:
            # compares quotes and if one contains the other delete the shorter one
            if len(quotes[i]) < len(quotes[j]):
                del quotes[i]
            else:
                del quotes[j]
        else:
            i += 1

for key, value in main_dict.items():
    print(key, value)

'''HTML Document'''


def create_html():
    with open(DESKTOP_PATH_HTML, encoding='utf-8',mode="x") as html_doc:
        html_doc.write('''<style>html {font-family: Arial; font-size: 16px; margin: 0 auto; width: 75%}
                        h1 {font-size: 3rem} h2 {font-size: 1.7rem}</style>\n<h1 align="center">Kindle Highlights</h1>\n
                        ''')
        html_doc.write('<ul>\n')
        i = 0
        for key in main_dict:
            html_doc.write('<li><a href=#' + str(i) + '>' + key + '</a></li>\n')
            i += 1
        html_doc.write('</ul>\n')

        j = 0
        for key in main_dict:
            html_doc.write('<br><h2 id="' + str(j) + '">' + key + '</h2><hr>\n')
            j += 1
            html_doc.write('<ul>')
            for quote in main_dict[key]:
                html_doc.write('<li><p>' + quote + '</p></li>\n')
            html_doc.write('</ul>')


create_html()