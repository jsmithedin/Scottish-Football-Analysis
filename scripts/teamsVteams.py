#!/bin/python

import csv
import sys

lTeams = ["Inverness C", "Celtic", "Dundee United", "Kilmarnock", "Hibernian", "Ross County", "Motherwell", "St Mirren", "Hearts", "Partick", "St Johnstone", "Aberdeen"]
    
inv = {};
cel = {};
du = {};
kil = {};
hib = {};
rc = {};
mot = {};
stm = {};
hea = {};
par = {};
stj = {};
ab = {};

f = open(sys.argv[1], 'rb')
cy = csv.reader(f)
cy.next()
aTeam = ""
hFouls = 0
aFouls = 0
hYel = 0
aYel = 0
hRed = 0
aRed = 0
for row in cy:
    aTeam = row[1]
    hFouls = int(row[5])
    aFouls = int(row[6])
    hYel = int(row[7])
    aYel = int(row[8])
    hRed = int(row[9])
    aRed = int(row[10])
    if "Inverness" in row[0]:
        if aTeam in inv:
            aTeam += "2"
            inv[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            inv[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
    if "Celtic" in row[0]:
        if aTeam in cel:
            aTeam += "2"
            cel[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            cel[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
    if "Dundee" in row[0]:
        if aTeam in du:
            aTeam += "2"
            du[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            du[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
    if "Kilmarnock" in row[0]:
        if aTeam in kil:
            aTeam += "2"
            kil[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            kil[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
    if "Hibernian" in row[0]:
        if aTeam in hib:
            aTeam += "2"
            hib[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            hib[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
    if "Ross" in row[0]:
        if aTeam in rc:
            aTeam += "2"
            rc[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            rc[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
    if "Motherwell" in row[0]:
        if aTeam in mot:
            aTeam += "2"
            mot[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            mot[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
    if "Mirren" in row[0]:
        if aTeam in stm:
            aTeam += "2"
            stm[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            stm[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed] 
    if "Hearts" in row[0]:
        if aTeam in hea:
            aTeam += "2"
            hea[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            hea[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
    if "Partick" in row[0]:
        if aTeam in par:
            aTeam += "2"
            par[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            par[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
    if "Johnstone" in row[0]:
        if aTeam in stj:
            aTeam += "2"
            stj[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            stj[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
    if "Aberdeen" in row[0]:
        if aTeam in ab:
            aTeam += "2"
            ab[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        else:
            ab[aTeam] = [hFouls, aFouls, hYel, aYel, hRed, aRed]
        
f.close()
    
w = csv.writer(open("teamsVteams.csv", "wb"))

w.writerow(["Aberdeen"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in ab:
    thisTeam = ab[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]]) 

w.writerow([""])
w.writerow(["Celtic"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in cel:
    thisTeam = cel[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]])    

w.writerow([""])
w.writerow(["Dundee United"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in du:
    thisTeam = du[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]])     

w.writerow([""])
w.writerow(["Hearts"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in hea:
    thisTeam = hea[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]]) 

w.writerow([""])
w.writerow(["Hibs"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in hib:
    thisTeam = hib[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]])
    
w.writerow([""])
w.writerow(["Inverness"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in inv:
    thisTeam = inv[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]])      

w.writerow([""])
w.writerow(["Kilmarnock"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in kil:
    thisTeam = kil[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]]) 

w.writerow([""])
w.writerow(["Motherwell"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in mot:
    thisTeam = mot[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]]) 

w.writerow([""])
w.writerow(["Partick"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in par:
    thisTeam = par[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]]) 
    
w.writerow([""])
w.writerow(["Ross C"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in rc:
    thisTeam = rc[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]]) 

w.writerow([""])
w.writerow(["St Johnstone"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in stj:
    thisTeam = stj[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]]) 

w.writerow([""])
w.writerow(["St Mirren"])
w.writerow(["ATeam","FoulsH","FoulsA", "YellowsH", "YellowsA", "RedsH", "RedsA"])

for team in stm:
    thisTeam = stm[team]
    w.writerow([team, thisTeam[0], thisTeam[1], thisTeam[2], thisTeam[3], thisTeam[4], thisTeam[5]]) 


print "Finished!"
