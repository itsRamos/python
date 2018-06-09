#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regular expressions form their own complex mini-language
"""

import re

regex  = r"""(?P<quote>['"]).*?(?P=quote)"""

# try with single or double quites inside....
target = """The man said he was "an alien from Mars" hah hah"""

m = re.search(regex, target)
if m:
    print("Found match:", m.string[m.start():m.end()])
    
newstring = re.sub(r":", " ", "remove:colons:replace:with:space")
print("Substitution: ", newstring)

newlist = re.split(r":", "use:regex:as:the:split:string")
print("List from split:", newlist)
