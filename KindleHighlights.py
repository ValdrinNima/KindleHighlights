import os
import re

# ((?<=={10}\n).+\n)(- Ihre Markierung .+ \d{4}|- Ihre Notiz auf Seite \d+)(.+\n+)(\n.+)

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


with open(DESKTOP_PATH_CLIPPINGS , encoding="utf-8") as clippings:
    content = clippings.read()

    wholeRegex = re.compile('((?<=={10}\n).+\n)(- Ihre Markierung .+ \d{4}|- Ihre Notiz auf Seite .+ \d{4})(.+\n+)(\n.+)')
    whole_match = re.findall(wholeRegex, content)

'''Filtering the title_quote_list into a dict with the titles as the key and a list of corresponding
   quotes as the value'''

main_dict = {}
for item in whole_match:
    if item[0] not in main_dict:
        main_dict[item[0]] = []

for item in whole_match:
    main_dict[item[0]].append(item[1:4])


for key in main_dict:

    i = 0
    while i < len(main_dict[key]):
        j = i + 1
        if j > len(main_dict[key]) - 1:
            break
        if main_dict[key][i][2] in main_dict[key][j][2] or main_dict[key][j][2] in main_dict[key][i][2]:
            if len(main_dict[key][i][2]) < len(main_dict[key][j][2]):
                del main_dict[key][i]
            else:
                del main_dict[key][j]
        else:
            i += 1

# for quotes in main_dict.values():
#     i = 0
#     while i < len(quotes)-1:
#         # i is index a quote and j of the following quote
#         j = i + 1
#         if j > len(quotes)-1:
#             break
#         if quotes[i] in quotes[j] or quotes[j] in quotes[i]:
#             # compares quotes and if one contains the other delete the shorter one
#             if len(quotes[i]) < len(quotes[j]):
#                 del quotes[i]
#             else:
#                 del quotes[j]
#         else:
#             i += 1


for key, value in main_dict.items():
    print(key, value)


# HTML Document
def create_html():
    try:
        with open(DESKTOP_PATH_HTML, encoding='utf-8',mode="x") as html_doc:
            html_doc.write('''<style>body {
        font-family: Arial, Helvetica, sans-serif;
        font-size: 1.2rem;
        font-weight: 500;
      }
      .head {
        margin: 4em auto 1em;
        width: 70%;
        text-align: center;
        font-size: 1rem;
      }
        .table_of_content {
        margin: 0 auto;
        width: 70%;
        font-size: 1.2rem;
        }
        a {
            text-decoration: none;
        }
        a:link, a:visited {
            color: black;
        }
        a:hover {
            color: blue;
        }
        li {
        padding: 0.2em 0;
        }
      .head h3 {
        font-size: 1.2rem;
        margin-bottom: 1.6em;
        border-bottom: 1px solid rgb(177, 174, 174);
        padding-bottom: 0.5em;
      }
      .quote {
        margin: 0.5em auto;
        width: 70%;
        border-left: 5px solid rgb(255, 230, 2);
        padding: 0.5em;
      }
      .info {
        margin: 2.2em auto 0em;
        width: 70%;
        font-size: 1rem;
        font-weight: 400;
        color: gray;
      }</style>\n<h1>Kindle Highlights</h1>\n
                            ''')
            html_doc.write('<div class="table_of_content"><ol>\n')
            i = 0
            for key1 in main_dict:
                html_doc.write('<li><a href=#' + str(i) + '>' + key1 + '</a></li>\n')
                i += 1
            html_doc.write('</ol></div>\n')

            j = 0
            for key2 in main_dict:
                html_doc.write('<div class="head"><h1 id="' + str(j) + '">' + key2 + '</h1>\n<h3>' + str(len(main_dict[key2])) + ' Entries' + '</h3></div>\n')
                j += 1
                for index in range(len(main_dict[key2])):
                    html_doc.write('<p class="info">' + main_dict[key2][index][0] + '</p>')
                    html_doc.write('<div class="quote">' + main_dict[key2][index][2] + '</div>\n')
    except FileExistsError:
        print("File already exist's")


create_html()
