from . import tags as tg

def genDoc():
    f = open('doc.html','w')
    f.write('<!DOCTYPE html>\n')

def buildHTML(html):
    f = open('doc.html', 'a')
    fr = open('doc.html', 'r')

    html_str = html.__str__()
    f.write(html_str)

    