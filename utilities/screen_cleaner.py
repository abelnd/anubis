#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor samir sanchez garnica @sasaga92

from os import system, name

class clear():
    def __init__(self):
        system('cls' if name == 'nt' else 'clear')
