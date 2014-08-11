#!/bin/python

import csv
import sys

f = open(sys.argv[1], 'rb')

cr = csv.reader(f)
cr.next()

lRefs = [];

for row in cr:
    lRefs.append(row[4])

dGamesPerRef = {};
dFoulsPerRef = {};
dYellowsPerRef = {};
dRedsPerRef = {};

f.close()

for ref in set(lRefs):
    f = open(sys.argv[1], 'rb')
    cy = csv.reader(f)
    cy.next()
    games = 0
    fouls = 0
    yellows = 0
    reds = 0
    for row in cy:
        if ref in row[4]:
            games += 1
            fouls += int(row[5])
            fouls += int(row[6])
            yellows += int(row[7])
            yellows += int(row[8])
            reds += int(row[9])
            reds += int(row[10])
    dGamesPerRef[ref] = games
    dFoulsPerRef[ref] = fouls
    dYellowsPerRef[ref] = yellows
    dRedsPerRef[ref] = reds
    f.close()

w = csv.writer(open("refs.csv", "wb"))

w.writerow(["Name","Games","Fouls", "Yellows","Reds","F/G", "Y/G","R/G"])

for ref in set(lRefs):
    w.writerow([ref, dGamesPerRef[ref], dFoulsPerRef[ref], dYellowsPerRef[ref], dRedsPerRef[ref], dFoulsPerRef[ref]/float(dGamesPerRef[ref]), dYellowsPerRef[ref]/float(dGamesPerRef[ref]), dRedsPerRef[ref]/float(dGamesPerRef[ref])])

print "Finished!"
