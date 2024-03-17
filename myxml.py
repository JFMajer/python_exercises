def myxml(tagname, content='', **kwargs):
    attributes = ''
    if kwargs:
        attributes = ' '.join(f'{key}="{value}"' for key, value in kwargs.items())
        attributes = ' ' + attributes
    print(f"<{tagname}{attributes}>{content}</{tagname}>")


myxml("test")
myxml("test", "foo")
myxml("test", "foo", a=1, b=2, c=3)
myxml("test", a=1, b=2, c=3)
