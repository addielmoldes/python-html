class html:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value
    
    def setTag(self, tag):
        self.tags.append(tag)

    def __str__(self) -> str:
        return '<html>\n' + self.tags[0].__str__() + self.tags[1].__str__() + '</html>'

###---###---###---###---###---###---###---###---###---###

class head:
    tags = []

    def setTag(self, tag):
        self.tags.append(tag)

    def __str__(self):
        head_str = '<head>\n'
        for t in self.tags:
            head_str = head_str + t.__str__() + ' '
        
        head_str = head_str + '</head>\n'
        
        return head_str

###--- HEAD TAGS ---###

class title:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return '<title>' + self.title + '</title>'

class meta:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __str__(self):
        return '\n<meta name=' + self.name + ' content=' + self.content + '>'

class link:
    def __init__(self, type, rel, href):
        self.type = type
        self.rel = rel
        self.href = href
    
    def __str__(self):
        return '\n<link type=' + self.type + ' rel=' + self.rel + ' href=' + self.href + '>'

class style:
    def __init__(self, code):
        self.code = code
    
    def __str__(self):
        return '\n<style>\n' + self.code + '\n</style>'

###---###---###---###---###---###---###---###---###---###

class body:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag)

    def __str__(self):
        attr_str = ''
        for a,v in zip(self.attrs.keys(), self.attrs.values()):
            attr_str = attr_str + a + '=' + v + ' '

        tag_str = ''
        for t in self.tags:
            tag_str = tag_str + t.__str__() + ' '

        return '<body ' + attr_str + '>\n' + tag_str + '\n</body>\n'

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
    attrs = {}

    def setAttr(self, attr, value):
        self.attrs[attr] = value

class option:
    attrs = {}
    tags = []

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def setTag(self, tag):
        self.tags.append(tag) 

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

    attrs = {}

    def setAttr(self, attr, value):
        self.attrs[attr] = value

    def __str__(self):
        attr_str = ''
        for a,v in zip(self.attrs.keys(), self.attrs.values()):
            attr_str = attr_str + a + '=' + v + ' '

        return '<img ' + attr_str + ' src=' + self.src + ' alt=' + self.alt + '>'