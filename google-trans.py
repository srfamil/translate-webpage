# English:  https://neculaifantanaru.com/en/python-code-text-google-translate-website-translation-beautifulsoup-library.html
# Romanian:  https://neculaifantanaru.com/python-code-text-google-translate-website-translation-beautifulsoup.html


from bs4 import BeautifulSoup
from bs4.formatter import HTMLFormatter
from googletrans import Translator
import requests

translator = Translator()

class UnsortedAttributes(HTMLFormatter):
    def attributes(self, tag):
        for k, v in tag.attrs.items():
            yield k, v

files_from_folder = r"e:\Carte\BB\17 - Site Leadership\Principal"

use_translate_folder = False

destination_language = 'ceb'

extension_file = ".html"

import os

directory = os.fsencode(files_from_folder)

def recursively_translate(node):
    for x in range(len(node.contents)):
        if isinstance(node.contents[x], str):
            if node.contents[x].strip() != '':
                try:
                    node.contents[x].replaceWith(translator.translate(node.contents[x], dest=destination_language).text)
                except:
                    pass
        elif node.contents[x] != None:
            recursively_translate(node.contents[x])

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    if filename == 'y_key_e479323ce281e459.html' or filename == 'TS_4fg4_tr78.html': #ignore this 2 files
        continue
    if filename.endswith(extension_file):
        with open(os.path.join(files_from_folder, filename), encoding='utf-8') as html:
            soup = BeautifulSoup('<pre>' + html.read() + '</pre>', 'html.parser')
            for title in soup.findAll('title'):
                recursively_translate(title)

            for meta in soup.findAll('meta', {'name':'description'}):
                try:
                    meta['content'] = translator.translate(meta['content'], dest=destination_language).text
                except:
                    pass

            for h1 in soup.findAll('h1', {'itemprop':'name'}, class_='den_articol'):
                begin_comment = str(soup).index('<!-- ARTICOL START -->')
                end_comment = str(soup).index('<!-- ARTICOL FINAL -->')
                if begin_comment < str(soup).index(str(h1)) < end_comment:
                    recursively_translate(h1)

            for p in soup.findAll('p', class_='text_obisnuit'):
                begin_comment = str(soup).index('<!-- ARTICOL START -->')
                end_comment = str(soup).index('<!-- ARTICOL FINAL -->')
                if begin_comment < str(soup).index(str(p)) < end_comment:
                    recursively_translate(p)

            for p in soup.findAll('p', class_='text_obisnuit2'):
                begin_comment = str(soup).index('<!-- ARTICOL START -->')
                end_comment = str(soup).index('<!-- ARTICOL FINAL -->')
                if begin_comment < str(soup).index(str(p)) < end_comment:
                    recursively_translate(p)

            for span in soup.findAll('span', class_='text_obisnuit2'):
                begin_comment = str(soup).index('<!-- ARTICOL START -->')
                end_comment = str(soup).index('<!-- ARTICOL FINAL -->')
                if begin_comment < str(soup).index(str(span)) < end_comment:
                    recursively_translate(span)

            for li in soup.findAll('li', class_='text_obisnuit'):
                begin_comment = str(soup).index('<!-- ARTICOL START -->')
                end_comment = str(soup).index('<!-- ARTICOL FINAL -->')
                if begin_comment < str(soup).index(str(li)) < end_comment:
                    recursively_translate(li)

            for a in soup.findAll('a', class_='linkMare'):
                begin_comment = str(soup).index('<!-- ARTICOL START -->')
                end_comment = str(soup).index('<!-- ARTICOL FINAL -->')
                if begin_comment < str(soup).index(str(a)) < end_comment:
                    recursively_translate(a)

            for h4 in soup.findAll('h4', class_='text_obisnuit2'):
                begin_comment = str(soup).index('<!-- ARTICOL START -->')
                end_comment = str(soup).index('<!-- ARTICOL FINAL -->')
                if begin_comment < str(soup).index(str(h4)) < end_comment:
                    recursively_translate(h4)

            for h5 in soup.findAll('h5', class_='text_obisnuit2'):
                begin_comment = str(soup).index('<!-- ARTICOL START -->')
                end_comment = str(soup).index('<!-- ARTICOL FINAL -->')
                if begin_comment < str(soup).index(str(h5)) < end_comment:
                    recursively_translate(h5)

        print(f'{filename} translated')
        soup = soup.encode(formatter=UnsortedAttributes()).decode('utf-8')
        new_filename = f'{filename.split(".")[0]}.html'
        if use_translate_folder:
            try:
                with open(os.path.join(files_from_folder+r'\translated', new_filename), 'w', encoding='utf-8') as new_html:
                    new_html.write(soup[5:-6])
            except:
                os.mkdir(files_from_folder+r'\translated')
                with open(os.path.join(files_from_folder+r'\translated', new_filename), 'w', encoding='utf-8') as new_html:
                    new_html.write(soup[5:-6])
        else:
            with open(os.path.join(files_from_folder, new_filename), 'w', encoding='utf-8') as html:
                html.write(soup[5:-6])