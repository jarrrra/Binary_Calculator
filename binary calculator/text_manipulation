import re

def text_split(text, separator):
    for sep in separator:
        text = text.replace(sep, '|')
        
    return [txt.strip() for txt in text.split('|') if txt != '']
          
def text_filter(text, separator):
    text = re.sub('0|1|NOT|~', ' ', text)
    text = text.split(' ')

    return [t for t in text if t in separator]