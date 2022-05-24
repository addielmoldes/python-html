from . import tags as tg

def genDoc():
    f = open('doc.html','w')
    f.write('<!DOCTYPE html>')

def buildHTML(html, head, body):
    fw = open('doc.html', 'w')
    fr = open('dec.html', 'r')

    
