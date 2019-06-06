################################################################################
# BaumwachstumMain.py #
################################################################################
#
# Johannistriebe (zugleich Austrieb mit Blatt)
# Alter des Baumes bestimmt:
#    * Laengenwachstum der neuen Zweige
#    * Zweigverlust von aelteren Aesten
#    * Blattdimensionen
#    * Austriebswahrscheinlichkeit fuer Blattachselknospe
# Alter des Zweiges bestimmt:
#    * Laengenwachstum des neuen Zweiges
#    * Zweigverlust von aelteren Aesten
#    * Blattdimensionen
#    * Blattwachstum
#    * Abstaende der Knoten des aktuellen Zweiges (Internodienlaengen)
#    * Wuchsrichtung des Blattes
# Relative Position des Knotens auf dem tragenden Zweig (Distanz) bestimmt:
#    * Austriebswahrscheinlichkeit fuer Blattachselknospe
#    * Zweigverlust von aelteren Aesten
#    * Blattdimensionen
#    * Wuchsrichtung des Blattes
# Richtung (Wuchswinkel zur Vertikalen) des Zweiges bestimmt:
#    * Austriebswahrscheinlichkeit fuer Blattachselknospe
#    * Zweigverlust von aelteren Aesten
#    * Blattdimensionen
#    * Abstaende der Knoten des aktuellen Zweiges (Internodienlaengen)
# Richtung (Wuchswinkel zum tragenden Zweig) des Zweiges bestimmt:
#    * Austriebswahrscheinlichkeit fuer Blattachselknospe
#    * Zweigverlust von aelteren Aesten
#    * Blattdimensionen
#    * Abstaende der Knoten des aktuellen Zweiges (Internodienlaengen)
# Richtung (Wuchswinkel zur Vertikalen) des Blattes bestimmt:
#    * Laengenwachstum des neuen Zweiges
#    * Abstaende der Knoten des aktuellen Zweiges (Internodienlaengen)
# Richtung (Wuchswinkel zum tragenden Zweig) des Blattes bestimmt:
#    * Laengenwachstum des neuen Zweiges
#    * Abstaende der Knoten des aktuellen Zweiges (Internodienlaengen)
# Wuchsrichtungen der benachbarten Blaetter eines Blattes bestimmt:
#    * Wuchsrichtung des Blattes
# Zusaetzlich Liste von aktiven (und ev. inaktiven) Knoten

# Blaetter inkl. Wuchsrichtung und Laenge/Breite
# Relative Position des Knotens auf dem tragenden Zweig (Distanz) bestimmt:
#    * Laengenwachstum des neuen Zweiges
#    * Wuchsrichtung des neuen Zweiges (polar, azimuth)
#    * Anzahl der Knoten eines neuen Zweiges
#    * Anzahl der Knospen auf jedem Knoten eines neuen Zweiges
# Richtung (Wuchswinkel zur Vertikalen) des Zweiges bestimmt:
#    * Laengenwachstum des aktuellen Zweiges
#    * Wuchsrichtung des neuen Zweiges (polar, azimuth)
#    * Anzahl der Knoten eines neuen Zweiges
#    * Anzahl der Knospen auf jedem Knoten eines neuen Zweiges
# Richtung (Wuchswinkel zum tragenden Zweig) des Zweiges bestimmt:
#    * Laengenwachstum des aktuellen Zweiges
#    * Wuchsrichtung des neuen Zweiges (polar, azimuth)
#    * Anzahl der Knoten eines neuen Zweiges
#    * Anzahl der Knospen auf jedem Knoten eines neuen Zweiges
# Anzahl an Knoten des tragenden Zweiges bestimmt:
#    * Laengenwachstum des aktuellen Zweiges
# Variabilitaet in der Anzahl an Knoten pro Zweig
# Variabilitaet in der Anzahl an Knospen pro Knoten
# Variabilitaet in der Anzahl an Blaettern pro Knoten
# Letzter Knoten muss immer an der Spitze des Zweiges sein
# Equidistant scaling (min-, max-values der Knoten fuer x, y, z)
# "Gebogene" Zweige
# Richtige Anzeige der Anzahl an Knoten und Zweigen in jedem Jahr
# Ausduennen der Zweige und Knospen

################################################################################

import os, time, random
# import math

import InputAllgemein as InpA
# from Funktionen import drawDst, printElapsedTimeSim
from Funktionen import printElapsedTimeSim
# from Funktionen import rotatePt2D, rotatePt3D
from KlassenM import InputData, Baum, BaumGruppe
# from KlassenM import InputData, Knoten, ZweigMod, Baum, BaumPlots
from KlassenS import Mosaik
################################################################################

print('Baumwachstum')
print('Modelliert das Wachstum von Baeumen und Straeuchern in Konkurrenz.')

# ### MAIN #####################################################################
startTimeSim = time.time()
print('+'*30 + ' START', time.ctime(startTimeSim), '+'*30)
cWD = os.getcwd()
print('Current working directory:', cWD)
inpDataA = InputData(InpA.dictInpA)
inpDataA.addBaumTps(InpA.ND_TYPES)
# print('Current mode:', inpDataA.dI['Mode'])

cBaumGr = BaumGruppe(inpDataA)
print('\n', '+'*80, '\n')
print(cBaumGr)
cBaumGr.printBaeume()
cBaumGr.growBaeume(inpDataA)
if cBaumGr.dIA['lvlDbg'] > 0:
    print('+'*20, 'dBlocks (FINAL)', '+'*20)
    cBaumGr.cMk.printDBlocks()

# cBaumGr.collectLight()

# for cNum, (iTp, numTS, cView) in inpDataA.dI['dBaeume'].items():
#     print('\n', '+'*80, '\n', '#'*24, 'Baum', cNum, '#'*24)
#     cBaum = Baum(inpDataA, iTp)
#     print(cBaum)
#     for cTS in range(1, numTS + 1):
#         print('-'*24, 'Current time step:', cTS, '-'*24)
#         cBaum.wachse1Y()
#         print(cBaum)
#         cBaum.printLCKnoten()
#         print('# "Knoten":', cBaum.lNumK[2], '/', len(cBaum.lK), '-- active:',
#               cBaum.lNumK[1], '-- inactive:', cBaum.lNumK[0])
#         cBaum.plotBaum3D(cView[0], cView[1])
#         print('-'*40)
#     if inpDataA.dI['dPrint']['Knoten'][0]:
#         cBaum.printAllKnoten(inpDataA.dI['dPrint']['Knoten'][1])
#     if inpDataA.dI['dPrint']['Zweig']:
#         cBaum.printAllZweige()
#     if inpDataA.dI['dPrint']['Blatt']:
#         cBaum.printAllBlaetter()

printElapsedTimeSim(startTimeSim, time.time(), 'Total time')
print('*'*20 + ' DONE', time.ctime(time.time()), '*'*20)

################################################################################
