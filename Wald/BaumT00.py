# ### INPUT - BAUM #############################################################
strType = 'TestBaum'
strNSpec = 'Regelmaessiger Doppelverzweiger'

dPosZweig = {'s': 'Sl',         # (siehe unten)
             'vE': 'T00',
             'vM': 'T00',
             'vS': 'T00',
             'wE': 'T00',
             'wM': 'T00',
             'wS': 'T00',
             'xE': 'T00',
             'xM': 'T00',
             'xS': 'T00'}
dPosBlatt = {'s': 'Sl',         # 'Sl': Schoessling
             'vE': 'k',         # 'w': dispers, 'k': decussiert
             'vM': 'k',
             'vS': 'k',
             'wE': 'k',
             'wM': 'k',
             'wS': 'k',
             'xE': 'k',
             'xM': 'k',
             'xS': 'k'}

tLenSlSt = (10, 2.0)                # [cm]

tLenTMax_s = (10, 2.0)              # [cm]
tLenTMax_vE = (20, 4.0)             # [cm]
tLenTMax_vM = (20, 4.0)             # [cm]
tLenTMax_vS = (20, 4.0)             # [cm]
tLenTMax_wE = (20, 4.0)             # [cm]
tLenTMax_wM = (20, 4.0)             # [cm]
tLenTMax_wS = (20, 4.0)             # [cm]
tLenTMax_xE = (20, 4.0)             # [cm]
tLenTMax_xM = (20, 4.0)             # [cm]
tLenTMax_xS = (20, 4.0)             # [cm]

tLenTAvg_s = (10, 2.5)              # [cm]
tLenTAvg_vE = (12, 2.6)             # [cm]
tLenTAvg_vM = (12, 2.6)             # [cm]
tLenTAvg_vS = (12, 2.6)             # [cm]
tLenTAvg_wE = (12, 2.6)             # [cm]
tLenTAvg_wM = (12, 2.6)             # [cm]
tLenTAvg_wS = (12, 2.6)             # [cm]
tLenTAvg_xE = (12, 2.6)             # [cm]
tLenTAvg_xM = (12, 2.6)             # [cm]
tLenTAvg_xS = (12, 2.6)             # [cm]

tFctNKZw_s = ([1], [0])             # []
tFctNKZw_vE = ([1], [0])            # []
tFctNKZw_vM = ([1], [0])            # []
tFctNKZw_vS = ([1], [0])            # []
tFctNKZw_wE = ([1], [0])            # []
tFctNKZw_wM = ([1], [0])            # []
tFctNKZw_wS = ([1], [0])            # []
tFctNKZw_xE = ([1], [0])            # []
tFctNKZw_xM = ([1], [0])            # []
tFctNKZw_xS = ([1], [0])            # []

tAngKPlr_s = ([0], [0.0])       # [°]
tAngKPlr_vE = ([20, 20], [4.0, 4.0])    # [°]
tAngKPlr_vM = ([20, 20], [4.0, 4.0])    # [°]
tAngKPlr_vS = ([20, 20], [4.0, 4.0])    # [°]
tAngKPlr_wE = ([20, 20], [4.0, 4.0])    # [°]
tAngKPlr_wM = ([20, 20], [4.0, 4.0])    # [°]
tAngKPlr_wS = ([20, 20], [4.0, 4.0])    # [°]
tAngKPlr_xE = ([20, 20], [4.0, 4.0])    # [°]
tAngKPlr_xM = ([20, 20], [4.0, 4.0])    # [°]
tAngKPlr_xS = ([20, 20], [4.0, 4.0])    # [°]

tAngKAzm_s = ([0], [0.0])       # [°]
tAngKAzm_vE = ([0, 180], [15.0, 15.0])    # [°]
tAngKAzm_vM = ([0, 180], [15.0, 15.0])    # [°]
tAngKAzm_vS = ([0, 180], [15.0, 15.0])    # [°]
tAngKAzm_wE = ([0, 180], [15.0, 15.0])    # [°]
tAngKAzm_wM = ([0, 180], [15.0, 15.0])    # [°]
tAngKAzm_wS = ([0, 180], [15.0, 15.0])    # [°]
tAngKAzm_xE = ([0, 180], [15.0, 15.0])    # [°]
tAngKAzm_xM = ([0, 180], [15.0, 15.0])    # [°]
tAngKAzm_xS = ([0, 180], [15.0, 15.0])    # [°]

dLenTMax = {'s': tLenTMax_s,            # Keim --> Schoessling
            'vE': tLenTMax_vE,          # all vertical branches
            'vM': tLenTMax_vM,
            'vS': tLenTMax_vS,
            'wE': tLenTMax_wE,          # side branches from vertical ones
            'wM': tLenTMax_wM,
            'wS': tLenTMax_wS,
            'xE': tLenTMax_xE,          # all other branches
            'xM': tLenTMax_xM,
            'xS': tLenTMax_xS}
dLenTAvg = {'s': tLenTAvg_s,
            'vE': tLenTAvg_vE,
            'vM': tLenTAvg_vM,
            'vS': tLenTAvg_vS,
            'wE': tLenTAvg_wE,
            'wM': tLenTAvg_wM,
            'wS': tLenTAvg_wS,
            'xE': tLenTAvg_xE,
            'xM': tLenTAvg_xM,
            'xS': tLenTAvg_xS}
dFctNKZw = {'s': tFctNKZw_s,
            'vE': tFctNKZw_vE,
            'vM': tFctNKZw_vM,
            'vS': tFctNKZw_vS,
            'wE': tFctNKZw_wE,
            'wM': tFctNKZw_wM,
            'wS': tFctNKZw_wS,
            'xE': tFctNKZw_xE,
            'xM': tFctNKZw_xM,
            'xS': tFctNKZw_xS}
dAngKPlr = {'s': tAngKPlr_s,            # [°]
            'vE': tAngKPlr_vE,
            'vM': tAngKPlr_vM,
            'vS': tAngKPlr_vS,
            'wE': tAngKPlr_wE,
            'wM': tAngKPlr_wM,
            'wS': tAngKPlr_wS,
            'xE': tAngKPlr_xE,
            'xM': tAngKPlr_xM,
            'xS': tAngKPlr_xS}
dAngKAzm = {'s': tAngKAzm_s,            # [°]
            'vE': tAngKAzm_vE,
            'vM': tAngKAzm_vM,
            'vS': tAngKAzm_vS,
            'wE': tAngKAzm_wE,
            'wM': tAngKAzm_wM,
            'wS': tAngKAzm_wS,
            'xE': tAngKAzm_xE,
            'xM': tAngKAzm_xM,
            'xS': tAngKAzm_xS}

tDmTOffs = (0.2095, 0.02)               # [cm]
tDmTInc = (0.0075, 0.0005)              # []
tNSTOffs = (0.3725, 0.05)               # [cm]
tNSTInc = (0.3505, 0.06)                # []
tPeriodBlatt = (1, 0)                   # [yrs]
tAreaBlatt = (6.0, 1.0)                 # [cm^2]

tLenInternod = (2.74, 0.3)              # [cm]
tFConv_PK = (0.006545, 0.001)           # []
tFConv_vt = (0.6655, 0.1)               # []
tInvestK_ErhZ = (12.0, 1.0)             # [%]
tInvestK_NZAx = (40.0, 4.0)             # [%]
tInvestK_NBlt = (12.0, 1.2)             # [%]

# posZweig:
#    'Sl': Schoessling
#    'T00': T00 type
#    'T01': T01 type
#    'T02': T02 type
#    'T03': T03 type
#    'S': Simple type
#    'L': Leeuwenberg model type
#    'W': Wirtel type 
#    'vSTD': Standard-Baum (vertikaler v-Zweig) type
#    'wSTD': Standard-Baum (w-Zweig) type
#    'xSTD': Standard-Baum (x-Zweig) type

# --- assertions regarding input -----------------------------------------------
assert len(dAngKPlr) == len(dAngKAzm)
for cK in dAngKPlr:
    assert cK in dAngKAzm
    assert len(dAngKPlr[cK]) == len(dAngKAzm[cK])

# --- create input dictionary --------------------------------------------------
dictInpB = {'strType': strType,
            'strNSpec': strNSpec,
            'dPosZweig': dPosZweig,
            'dPosBlatt': dPosBlatt,
            'tLenSlSt': tLenSlSt,
            'dLenTMax': dLenTMax,
            'dLenTAvg': dLenTAvg,
            'dFctNKZw': dFctNKZw,
            'dAngKPlr': dAngKPlr,
            'dAngKAzm': dAngKAzm,
            'tDmTOffs': tDmTOffs,
            'tDmTInc': tDmTInc,
            'tNSTOffs': tNSTOffs,
            'tNSTInc': tNSTInc,
            'tPeriodBlatt': tPeriodBlatt,
            'tAreaBlatt': tAreaBlatt,
            'tLenInternod': tLenInternod,
            'tFConv_PK': tFConv_PK,
            'tFConv_vt': tFConv_vt,
            'tInvestK_ErhZ': tInvestK_ErhZ,
            'tInvestK_NZAx': tInvestK_NZAx,
            'tInvestK_NBlt': tInvestK_NBlt}
################################################################################
