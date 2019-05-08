# ### INPUT - BAUM #############################################################
strType = 'Schlehe'
strNSpec = 'Prunus spinosa'

dPosZweig = {'s': 'Sl',         # (siehe unten)
             'vE': 'vSTD',
             'vM': 'vSTD',
             'vS': 'vSTD',
             'wE': 'wSTD',
             'wM': 'wSTD',
             'wS': 'wSTD',
             'xE': 'xSTD',
             'xM': 'xSTD',
             'xS': 'xSTD'}
dPosBlatt = {'s': 'Sl',         # 'Sl': Schoessling
             'vE': 'w',         # 'w': dispers, 'k': decussiert
             'vM': 'w',
             'vS': 'w',
             'wE': 'w',
             'wM': 'w',
             'wS': 'w',
             'xE': 'w',
             'xM': 'w',
             'xS': 'w'}

tLenSlSt = (15, 3.0)                # [cm]

tLenTMax_s = (15, 3.0)              # [cm]
tLenTMax_vE = (5, 1.0)              # [cm]
tLenTMax_vM = (10, 2.0)              # [cm]
tLenTMax_vS = (15, 3.0)              # [cm]
tLenTMax_wE = (6, 1.2)             # [cm]
tLenTMax_wM = (12, 2.4)             # [cm]
tLenTMax_wS = (18, 3.6)             # [cm]
tLenTMax_xE = (6, 1.2)             # [cm]
tLenTMax_xM = (12, 2.4)             # [cm]
tLenTMax_xS = (18, 3.6)             # [cm]

tLenTAvg_s = (15, 3.0)              # [cm]
tLenTAvg_vE = (5, 1.0)             # [cm]
tLenTAvg_vM = (10, 2.0)             # [cm]
tLenTAvg_vS = (15, 3.0)             # [cm]
tLenTAvg_wE = (6, 1.2)             # [cm]
tLenTAvg_wM = (12, 2.4)             # [cm]
tLenTAvg_wS = (18, 3.6)             # [cm]
tLenTAvg_xE = (6, 1.2)             # [cm]
tLenTAvg_xM = (12, 2.4)             # [cm]
tLenTAvg_xS = (18, 3.6)             # [cm]

tFctNKZw_s = ([1], [0])             # []
tFctNKZw_vE = ([1, 0.7, 0.5, 0.25], [0, 0.05, 0.05, 0.05])  # []
tFctNKZw_vM = ([1, 0.7, 0.5, 0.25], [0, 0.05, 0.05, 0.05])  # []
tFctNKZw_vS = ([1, 0.7, 0.5, 0.25], [0, 0.05, 0.05, 0.05])  # []
tFctNKZw_wE = ([1], [0])            # []
tFctNKZw_wM = ([1, 0.7, 0.5, 0.25], [0, 0.05, 0.05, 0.05])  # []
tFctNKZw_wS = ([1, 0.7, 0.5, 0.25], [0, 0.05, 0.05, 0.05])  # []
tFctNKZw_xE = ([1, 0.7, 0.5, 0.25], [0, 0.05, 0.05, 0.05])  # []
tFctNKZw_xM = ([1, 0.7, 0.5, 0.25], [0, 0.05, 0.05, 0.05])  # []
tFctNKZw_xS = ([1, 0.7, 0.5, 0.25], [0, 0.05, 0.05, 0.05])  # []

tAngKPlr_s = ([0], [0.0])       # [°]
tAngKPlr_vE = ([0, 90, 90], [10.0, 15.0, 15.0])   # [°]
tAngKPlr_vM = ([90], [15.0])   # [°]
tAngKPlr_vS = ([90], [15.0])   # [°]
tAngKPlr_wE = ([0, 90], [10.0, 15.0])   # [°]
tAngKPlr_wM = ([90], [15.0])   # [°]
tAngKPlr_wS = ([90], [15.0])   # [°]
tAngKPlr_xE = ([0, 90], [10.0, 15.0])   # [°]
tAngKPlr_xM = ([90], [15.0])   # [°]
tAngKPlr_xS = ([90], [15.0])   # [°]

tAngKAzm_s = ([0], [0.0])       # [°]
tAngKAzm_vE = ([0, 0, 180], [0, 60.0, 60.0])    # [°]
tAngKAzm_vM = ([120], [120.0])    # [°]
tAngKAzm_vS = ([240], [60.0])    # [°]
tAngKAzm_wE = ([0, 90], [0, 5.0])    # [°]
tAngKAzm_wM = ([90], [5.0])    # [°]
tAngKAzm_wS = ([90], [5.0])    # [°]
tAngKAzm_xE = ([0, 90], [0, 5.0])    # [°]
tAngKAzm_xM = ([90], [5.0])    # [°]
tAngKAzm_xS = ([90], [5.0])    # [°]

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

tDmTOffs = (0.193, 0.02)               # [cm]
tDmTInc = (0.00653, 0.0005)              # []
tNSTOffs = (0.683, 0.05)               # [cm]
tNSTInc = (0.486, 0.06)                # []
tPeriodBlatt = (1, 0)                   # [yrs]
tAreaBlatt = (2.0, 1.0)                 # [cm^2]

tLenInternod = (1.3, 0.3)              # [cm]
tFConv_PK = (0.00702, 0.001)           # []
tFConv_vt = (0.748, 0.1)               # []
tInvestK_ErhZ = (12.0, 1.0)             # [%]
tInvestK_NZAx = (45.0, 4.0)             # [%]
tInvestK_NBlt = (10.0, 1.2)             # [%]

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
