#!/bin/python

import csv
import sys

f = open(sys.argv[1], 'rb')

ct = csv.reader(f)
ct.next()

lTeams = [];

for row in ct:
    lTeams.append(row[0])
    
dFoulsForTeamHome = {};
dFoulsForTeamAway = {};
dYellowForTeamHome = {};
dYellowForTeamAway = {};
dRedForTeamHome = {};
dRedForTeamAway = {};

f.close()

for team in set(lTeams):
    f = open(sys.argv[1], 'rb')
    cy = csv.reader(f)
    cy.next()
    foulsH = 0
    foulsA = 0
    yellowH = 0
    yellowA = 0
    redH = 0
    redA = 0
    for row in cy:
        if team in row[0]:
            foulsH += int(row[5])
            yellowH += int(row[7])
            redH += int(row[9])
        if team in row[1]:
            foulsA += int(row[6])
            yellowA += int(row[8])
            redA += int(row[10])
    dFoulsForTeamHome[team] = foulsH
    dFoulsForTeamAway[team] = foulsA
    dYellowForTeamHome[team] = yellowH
    dYellowForTeamAway[team] = yellowA
    dRedForTeamHome[team] = redH
    dRedForTeamAway[team] = redA
    f.close()
    
w = csv.writer(open("teamsOverSeason.csv", "wb"))

w.writerow(["Team","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in set(lTeams):
    w.writerow([team, dFoulsForTeamHome[team], dFoulsForTeamAway[team], dYellowForTeamHome[team], dYellowForTeamAway[team], dRedForTeamHome[team], dRedForTeamAway[team]])


print "Finished!"
