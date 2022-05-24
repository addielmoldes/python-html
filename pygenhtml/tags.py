from email.errors import HeaderDefect
from mimetypes import init
from multiprocessing import set_forkserver_preload
from operator import methodcaller
from turtle import ht


class html:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value
    
    def setTag(self, tag):
        self.tags.append(tag)

###---###---###---###---###---###---###---###---###---###

class head:
    tags = []

    def setTag(self, tag):
        self.tags.append(tag)

###--- HEAD TAGS ---###

class title:
    def __init__(self, title):
        self.title = title

class meta:
    def __init__(self, name, content):
        self.name = name
        self.content = content

class link:
    def __init__(self, type, rel, href):
        self.type = type
        self.rel = rel
        self.href = href

class style:
    def __init__(self, code):
        self.code = code

###---###---###---###---###---###---###---###---###---###

class body:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)

###--- BODY TAGS ---###

### --- ### CONTAINERS ### --- ###

class header:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)

class nav:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)

class main:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)

class section:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)

class aside:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)

class footer:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)

class div:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)

### --- ### ELEMENTS ### --- ###

class ul:
    def __init__(self, li = []):
        self.li = li

    def setAttr(self, attr, value):
        self.attrs[attr] = value

class li:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)

class a:
    def __init__(self, href):
        self.href = href

    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)   

class form:
    def __init__(self, method, action):
        self.method = method
        self.action = action

    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag) 

class input:
    def __init__(self, type):
        self.type = type

    attrs = {}

    def setAttr(self, attr, value):
        self.attrs[attr] = value

class select:
    pass

class option:
    pass

class label:
    def __init__(self, for_, label):
        self.for_ = for_
        self.label = label

    attrs = {}

    def setAttr(self, attr, value):
        self.attrs[attr] = value

class button:
    def __init__(self, type):
        self.type = type

    attrs = {}

    def setAttr(self, attr, value):
        self.attrs[attr] = value

class p:
    def __init__(self, text):
        self.text = text

class img:
    def __init__(self, src, alt):
        self.src = src
        self.alt = alt