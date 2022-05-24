from . import tags as tg

def genDoc():
    f = open('doc.html','w')
    f.write('<!DOCTYPE html>\n')

def buildHTML(html, head, body):
    f = open('doc.html', 'a')
    fr = open('doc.html', 'r')

    body_str = html.__str__()
    f.write(body_str)

    