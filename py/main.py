#!/usr/bin/env python


import sys;
import re;


# db

def db_load(path):
    f = open(path, 'r')
    if f == None: return None
    db = []
    while True:
        l = f.readline()
        if len(l) == 0: break
        elif (l[0] == '#'): continue
        l = l.strip()
        if len(l) == 0: continue
        toks = l.split(' ', 2)
        if len(toks) == 1: toks = (toks[0], '0', '')
        elif len(toks) == 2: toks = (toks[0], toks[1], '')
        db.append(toks)
    return db

def db_find_pattern(db, s, col):
    e = re.compile(s, re.I)
    l = []
    n = 0
    for i in db:
        if e.search(i[col]): l.append(n)
        n = n + 1
    if len(l) == 0: l = None
    return l

def db_find_ref(db, s):
    return db_find_pattern(db, s, 0)

def db_find_comments(db, s):
    return db_find_pattern(db, s, 2)

def db_print(db):
    for i in db:
        print(i[0] + '::' + i[1] + '::' + i[2])
    return


# main

db = db_load('../db/store')
if db != None:
    db_print(db)
    l = db_find_comments(db, 'ampli')
    if l != None:
        for i in l: print(db[i])
