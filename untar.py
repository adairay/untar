#!/usr/bin/env python
# encoding: utf-8

import npyscreen
import os

def myFunction(*args):
    liste_ext = [u".tar.gz", u".tar.bz2", u".bz2", u".rar", u".gz", u".tar", u".tbz2", u".tgz", u".zip", u".Z"]
    F = npyscreen.Form(name=u"EasyTar")
    path = F.add(npyscreen.TitleFilenameCombo, name=u"Path to archive")
    extensions = F.add(npyscreen.TitleSelectOne,name=u"Archive extension", values = liste_ext, scroll_exit=True)
    F.edit()
    return {'path': path.value, 'extensions': extensions.value}

if __name__ == '__main__':
    i = 1
    direction = u"/"
    liste_ext = [u"tar -xzf", u"tar -xjf", u"bunzip2", u"rar x", u"gunzip", u"tar -xf", u"tar -xjf", u"tar -xzf", u"unzip", u"uncompress"]

    selected = npyscreen.wrapper_basic(myFunction)
    cutPath = selected['path']
    if cutPath:
        cutPath.split('/')
        while i < len(cutPath) - 1:
            direction = u"{0}{1}{2}".format(direction, cutPath[i], u"/" if direction else u"")
            i = i + 1
        if selected['extensions']:
            try:
                os.system(u"{0} {1}".format(liste_ext[selected['extensions'][0]], selected['path']))
            except OSError:
                print "Wrong extension or wrong file"
        else:
            print "No extension selected"
    else:
        print "No file selected"
