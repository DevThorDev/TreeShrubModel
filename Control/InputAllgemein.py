# ### INPUT - ALLGEMEIN ########################################################
import os, sys

# --- Header -------------------------------------------------------------------
ND_TYPES = 'Wald'
ND_PROGFILES = 'ProgramFiles'
ND_TOOLS = 'Tools'
lDSub = [ND_TYPES, ND_PROGFILES, ND_TOOLS]
for cDSub in lDSub:
    sys.path.append(os.path.join(sys.path[0], '..', cDSub))

from Konstanten import (M_DETER, M_STOCH, P0, UV_X_3D, UV_Y_3D, UV_Z_3D,
                        BASIS_R3, EPS)

# --- Input: Debug Info --------------------------------------------------------
levelDebugOut = 0   # level of debug output (0: no debug output)

# --- Input: Allgemeine Daten --------------------------------------------------
# dBaumGruppe = {4: [((0., 0., 0.), 0),       # key: index of "Baum" type
#                    ((30., 10., 0.), 2)],    # value: list of tuples:
#                1: [((-10., -20., 0.), 1)]}  # [(starting pos., start year)]
# dBaumGruppe = {4: [((0., 0., 0.), 0),
#                    ((40., 25., 0.), 1),
#                    ((-40., 25., 0.), 2),
#                    ((60., 35., 0.), 1),
#                    ((-60., -40., 0.), 0),
#                    ((30., 10., 0.), 1),
#                    ((40., -50., 0.), 2),
#                    ((-20., -60., 0.), 1),
#                    ((70., -40., 0.), 0)],
#                7: [((-80., 60., 0.), 0)]}
# dBaumGruppe = {6: [((0., 0., 0.), 0),
#                    ((-80., 0., 0.), 2),
#                    ((80., 0., 0.), 2),
#                    ((-160., 0., 0.), 1),
#                    ((160., 0., 0.), 1)]}
# dBaumGruppe = {7: [((50., -13., 0.), 0),
#                    ((180., -60., 0.), 1),
#                    ((27., -178., 0.), 1),
#                    ((-106., -63., 0.), 0),
#                    ((-146., 59., 0.), 0),
#                    ((154., -175., 0.), 2),
#                    ((170., 193., 0.), 1)],
#                4: [((-50., 80., 0.), 2),
#                    ((-180., 180., 0.), 1)]}
# dBaumGruppe = {4: [((-20., -80., 0.), 0),
#                    ((20., -80., 0.), 0),
#                    ((60., -80., 0.), 0),
#                    ((120., -80., 0.), 1),
#                    ((0., 0., 0.), 1)]}
# dBaumGruppe = {4: [((0., 0., 0.), 1)],
#                7: [((-70., 0., 0.), 0),
#                    ((100., 100., 0.), 1)]}
# dBaumGruppe = {7: [((-100., 0., 0.), 0),
#                    ((0., 0., 0.), 0),
#                    ((100., 0., 0.), 0)]}
dBaumGruppe = {7: [((0., 0., 0.), 0)], 4: [((0., 100., 0.), 3)]}
nYears = 6                              # number of time steps modelled
lViewPlt = [(5., -70),                  # (elevation, azim. angle)
            (10., 55)]
lYPltBaumGruppe = range(nYears + 1)     # years in which to plot "BaumGruppe"

dPlot = {'Knoten': (True, 'All'),       # 'All', 'Active', 'Inactive'
         'Zweig': True,
         'Blatt': (False, 'Current')}   # 'All', 'Current', 'Previous'

dPrint = {'Knoten': (False, 'All'),     # 'All', 'Active', 'Inactive'
          'Zweig': False,
          'Blatt': False}

cMode = M_STOCH         # M_DETER / M_STOCH
modelBlatt = True       # True / False

# lists of strings of the "explanatory" and "response" variables (DON'T CHANGE)
lSExplV = ['VertZ', 'RelPZw', 'RelPKt', 'LenZw', 'AgeZw', 'AgeBm']
lSRespV_Disc = ['NKZw', 'NKKt']
lSRespV_Cont = ['LenZw', 'AngPol', 'AngAzm', 'PrPKs', 'PrPZw']

# --- Input: Daten fuer Baum / Knoten / Knospe / Zweig / Blatt -----------------
nKtZwMax = 80           # max. number of new "Knoten" on "Zweig"
nKKtMax = 6             # max. number of "Knospen" on "Knoten"
fWdthZw = 0.2           # factor for "Zweig" width (1 / 0.2)
offsWdthZw = 0          # offset for "Zweig" width (-0.5 / 0)
tolAngV = 5             # tolerance of angle (deg) to vertical dir.
dMinMax = {'STD': (0, 1, False),        # (min., max., doMod)
           'NKZw': (1, nKtZwMax, False),
           'NKKt': (1, nKKtMax, False),
           'FctPKZw': (0, 1, False),
           'FctPEZw': (EPS, 1 - EPS, False),
           'LenZw': (EPS, -1, False),   # negative numbers imply no min./max.
           'AngPol': (0, 180, True),
           'AngAzm': (0, 360, True)}

# --- Input: Daten fuer Lichtaufnahme ------------------------------------------
# tNumBk = (20, 20, 50)               # number of "Bloecke" (x, y, z)
tNumBk = (60, 60, 60)               # number of "Bloecke" (x, y, z)
tDimBkG = (20., 20., 15.)        # dimensions of "Block" [cm]
tDirRay = (0, 2, -1)                # direction of sun rays (x, y, z)
# tLtDilF = (0.5, 0.75, 0.25)         # light dilution factors (x, y, z)
tLtDilF = (1., 1., 1.)         # light dilution factors (x, y, z)
intRay = 1.                         # intensity of sun rays
# prpDLC = 0.5                        # prop. of direct light coll. in block
# prpSLC = 0.25                       # prop. of scattered light coll. in block

# --- Input: Daten fuer plot ---------------------------------------------------
eqDstScl = True                     # equidistant scaling of the plots?
colModeZw = 'Age'                # 'Random' / 'Age'
colModeBl = 'Random'                # 'Random' / 'Age'
colSetBl = 'Autumn'                 # 'Spring' / 'Autumn' (only for 'Random')

# --- Input: Farbdefinitionen --------------------------------------------------
lClrZweig = [(0.0, 0.9, 0.0), (0.1, 0.7, 0.0), (0.2, 0.6, 0.0),
             (0.3, 0.5, 0.0), (0.4, 0.3, 0.0), (0.4, 0.2, 0.0),
             (0.4, 0.1, 0.0), (0.4, 0.0, 0.0), (0.3, 0.0, 0.0),
             (0.2, 0.0, 0.0), (0.1, 0.0, 0.0), (1.0, 0.0, 0.0),
             (0.8, 0.5, 0.0), (0.9, 0.9, 0.0), (0.0, 0.9, 0.0),
             (0.0, 0.2, 0.3), (0.0, 0.0, 0.9), (0.3, 0.0, 0.7),
             (0.6, 0.0, 0.4)]
lClrKntnS1 = [(0.75, 0.75, 0.75), (0.6, 0.6, 0.6), (0.45, 0.45, 0.45),
              (0.3, 0.3, 0.3), (0.15, 0.15, 0.15)]
lClrKntnS2 = [(0.9, 1.0, 0.0), (1.0, 0.75, 0.0), (1.0, 0.5, 0.0),
              (1.0, 0.25, 0.0), (1.0, 0.0, 0.0)]
# lClrBltS1 = [(0.0, 1.0, 0.0), (0.15, 0.85, 0.0), (0.3, 0.7, 0.0),
#              (0.45, 0.55, 0.0), (0.6, 0.4, 0.0), (0.75, 0.25, 0.0)]
lClrBltS1 = [(0.0, 1.0, 0.0), (0.0, 0.85, 0.05), (0.0, 0.7, 0.1),
             (0.0, 0.55, 0.15), (0.0, 0.4, 0.2), (0.0, 0.25, 0.25)]
lClrBltS2 = [(0.4, 0.0, 0.0), (0.7, 0.0, 0.0), (1.0, 0.0, 0.0),
             (0.9, 0.3, 0.0), (0.9, 0.6, 0.0), (0.9, 0.9, 0.0)]

# --- Input: Namen und Verzeichnisnamen ----------------------------------------
nFEndPY = '.py'                     # py file
nFEndPDF = '.pdf'                   # pdf file
nFEndTXT = '.txt'                   # txt file

nDPlots = 'PlotsAnalysis'           # name of directory for plots
nDOutTXT = 'OutputInfo'             # name of directory for output info

# --- Ueberpruefen der Annahmen ------------------------------------------------
assert len(tNumBk) == 3
assert len(tDimBkG) == 3
assert len(tDirRay) == 3
assert len(tLtDilF) == 3
assert intRay >= 0

# --- Berechnete Werte ---------------------------------------------------------
dictInpA = {# --- Input: Debug Info
            'lvlDbg': levelDebugOut,
            # --- Input: Allgemeine Daten
            'dBaumGruppe': dBaumGruppe,
            'nYears': nYears,
            'lViewPlt': lViewPlt,
            'lYPltBaumGruppe': lYPltBaumGruppe,
#             'dBaeume': dBaeume,
            'dPlot': dPlot,
            'dPrint': dPrint,
            'Mode': cMode,
            'modelBlatt': modelBlatt,
            'dVDep': {'lSEV': lSExplV,          # dictionary of variables
                      'lSRV_D': lSRespV_Disc,   # describing dependencies
                      'lSRV_C': lSRespV_Cont},
            # --- Input: Daten fuer Baum / Knoten / Knospe / Zweig / Blatt
            'nKtZwMax': nKtZwMax,
            'nKKtMax': nKKtMax,
            'fWdthZw': fWdthZw,
            'offsWdthZw': offsWdthZw,
            'tolAngV': tolAngV,
            'dMinMax': dMinMax,
            # --- Input: Daten fuer Lichtaufnahme
            'tNumBk': tNumBk,
            'tDimBkG': tDimBkG,
            'tDirRay': tDirRay,
            'tDirRayInv': tuple([-tDirRay[k] for k in range(len(tDirRay))]),
            'tLtDilF': tLtDilF,
            'intRay': intRay,
#             'prpDLC': prpDLC,
#             'prpSLC': prpSLC,
            # --- Input: Daten fuer plot
            'eqDstScl': eqDstScl,
            'colModeZw': colModeZw,
            'colModeBl': colModeBl,
            'colSetBl': colSetBl,
            # --- Input: Farbdefinitionen
            'lClrZweig': lClrZweig,
            'lClrKntnS1': lClrKntnS1,
            'lClrKntnS2': lClrKntnS2,
            'lClrBltS1': lClrBltS1,
            'lClrBltS2': lClrBltS2,
            # --- Input: Namen und Verzeichnisnamen
            'nFEndPY': nFEndPY,
            'nFEndPDF': nFEndPDF,
            'nFEndTXT': nFEndTXT,
            'nDPlots': nDPlots,
            'nDOutTXT': nDOutTXT,
            # --- Konstanten
            'P0': P0,
            'vUx': UV_X_3D,
            'vUy': UV_Y_3D,
            'vUz': UV_Z_3D,
            'basisR3': BASIS_R3}

################################################################################
