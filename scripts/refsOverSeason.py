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
dAFoulsPerRef = {};
dHFoulsPerRef = {};
dYellowsPerRef = {};
dAYellowsPerRef = {};
dHYellowsPerRef = {};
dRedsPerRef = {};
dARedsPerRef = {};
dHRedsPerRef = {};

f.close()

for ref in set(lRefs):
    f = open(sys.argv[1], 'rb')
    cy = csv.reader(f)
    cy.next()
    games = 0
    fouls = 0
    hFouls = 0
    aFouls = 0
    yellows = 0
    hYellows = 0
    aYellows = 0
    reds = 0
    hReds = 0
    aReds = 0
    for row in cy:
        if ref in row[4]:
            games += 1
            fouls += int(row[5])
            hFouls += int(row[5])
            fouls += int(row[6])
            aFouls += int(row[6])
            yellows += int(row[7])
            hYellows += int(row[7])
            yellows += int(row[8])
            aYellows += int(row[8])
            reds += int(row[9])
            hReds += int(row[9])
            reds += int(row[10])
            aReds += int(row[10])
    dGamesPerRef[ref] = games
    dFoulsPerRef[ref] = fouls
    dHFoulsPerRef[ref] = hFouls
    dAFoulsPerRef[ref] = aFouls
    dYellowsPerRef[ref] = yellows
    dHYellowsPerRef[ref] = hYellows
    dAYellowsPerRef[ref] = aYellows
    dRedsPerRef[ref] = reds
    dHRedsPerRef[ref] = hReds
    dARedsPerRef[ref] = aReds
    f.close()

w = csv.writer(open("refs.csv", "wb"))

w.writerow(["Name","Games","Fouls", "HFouls", "AFouls", "Yellows", "HYellows", "AYellows", "Reds", "HReds", "AReds", "F/G", "Y/G", "R/G"])

for ref in set(lRefs):
    w.writerow([ref, dGamesPerRef[ref], dFoulsPerRef[ref], dHFoulsPerRef[ref], dAFoulsPerRef[ref], dYellowsPerRef[ref], dHYellowsPerRef[ref], dAYellowsPerRef[ref], dRedsPerRef[ref], dHRedsPerRef[ref], dARedsPerRef[ref], dFoulsPerRef[ref]/float(dGamesPerRef[ref]), dYellowsPerRef[ref]/float(dGamesPerRef[ref]), dRedsPerRef[ref]/float(dGamesPerRef[ref])])

print "Finished!"
