#!/usr/bin/env python
# encoding: utf-8

import npyscreen
import os

def myFunction(*args):
    F = npyscreen.Form(name=u"EasyTar")
    path = F.add(npyscreen.TitleFilenameCombo, name=u"Path to archive")
    extensions = F.add(npyscreen.TitleMultiSelect,name=u"Archive extension", values = [u".gz", u".bz2"], scroll_exit=True)
    F.edit()
    return {'path': path.value, 'extensions': extensions.value}

if __name__ == '__main__':
    i = 1
    direction = u"/"

    selected = npyscreen.wrapper_basic(myFunction)
    cutPath = selected['path'].split('/')
    while i < len(cutPath) - 1:
        direction = u"{0}{1}{2}".format(direction, cutPath[i], u"/" if direction else u"")
        i = i + 1
    os.system(u"tar -x{0}{1}f {2} -C {3}".format(u"z" if 0 in selected['extensions'] else u"",
                                                 "j" if 1 in selected['extensions'] else u"",
                                                 selected['path'], direction))
