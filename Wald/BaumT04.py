# ### INPUT - BAUM #############################################################
import numpy as np
from Konstanten import (L_MX_1, L_MX_2, L_MX_3, L_MX_4, L_MX_5, L_MX_6,
                        EPS, E12, E06)
# general ----------------------------------------------------------------------
strType = 'Pappel'
strNSpec = 'Pappelartiger Verzweiger'

# positions of "Zweig" and "Blatt" ---------------------------------------------
dPosZweig = {'k': 'Keim',       # Keim
             's': 'Sl',         # 'Sl': Schoessling
             'v': 'vSTD',       # all vertical branches on main axis
             'w': 'wSTD',       # side branches from vertical ones
             'x': 'xSTD'}       # all other branches
dPosBlatt = {'k': 'Keim',       # Keim
             's': 'Sl',         # 'Sl': Schoessling
             'v': 'k',          # 'w': dispers, 'k': decussiert
             'w': 'k',
             'x': 'k'}

# dictionary specifying the distributions used ---------------------------------
dDist = {'NKZw': 0,     # 0: 'normal' / 1: 'custom'
         'NKKt': 0,     # 0: 'normal' / 1: 'custom'
         'FctPKZw': 0,  # 0: 'normal'
         'LenZw': 0,    # 0: 'normal'
         'AngPol': 0,   # 0: 'normal'
         'AngPol': 0}   # 0: 'normal'

# dictionaries containing boundaries and category weights ----------------------
# dictionary of the boundaries for number of new "Knoten" on a "Zweig"
dBndAr_NKZw = {'VertZ': [10, 45, 80, 100, 135],     # [deg]
               'RelPZw': [-2.5, -1.5, -0.5, 45, 135],   # [deg]
               'RelPKt': [0.1, 0.5, 0.9, 1. - E12], # []
               'LenZw': [],                         # [cm]
               'AgeZw': [],                         # [yr]
               'AgeBm': []}                         # [yr]

# dictionary of the boundaries for number of new "Knospen" on a "Knoten"
dBndAr_NKKt = {'VertZ': [10, 45, 80, 100, 135],     # [deg]
               'RelPZw': [-2.5, -1.5, -0.5, 45, 135],   # [deg]
               'RelPKt': [0.1, 0.5, 0.9, 1. - E12], # []
               'LenZw': [],                         # [cm]
               'AgeZw': [],                         # [yr]
               'AgeBm': []}                         # [yr]

# dictionary of the category weights for number of new "Knoten" on a "Zweig"
dCtWt_NKZw = {'VertZ': 0.25,    # []
              'RelPZw': 0.1,    # []
              'RelPKt': 0.15,   # []
              'LenZw': 0.5,     # []
              'AgeZw': 0.0,     # []
              'AgeBm': 0.0}     # []

# dictionary of the category weights for number of new "Knospen" on a "Knoten"
dCtWt_NKKt = {'VertZ': 0.25,    # []
              'RelPZw': 0.25,   # []
              'RelPKt': 0.25,   # []
              'LenZw': 0.25,    # []
              'AgeZw': 0.0,     # []
              'AgeBm': 0.0}     # []

# dictionary of the category weights for the length of a new "Zweig"
dCtWt_LenZw = {'VertZ': 0.25,   # []
               'RelPZw': 0.2,   # []
               'RelPKt': 0.15,  # []
               'LenZw': 0.4,    # []
               'AgeZw': 0.0,    # []
               'AgeBm': 0.0}    # []

# dictionary of the category weights for the polar angle of a new "Zweig"
dCtWt_AngPol = {'VertZ': 0.3,   # []
                'RelPZw': 0.4,  # []
                'RelPKt': 0.15, # []
                'LenZw': 0.15,  # []
                'AgeZw': 0.0,   # []
                'AgeBm': 0.0}   # []

# dictionary of the category weights for the azim. angle of a new "Zweig"
dCtWt_AngAzm = {'VertZ': 0.2,   # []
                'RelPZw': 0.4,  # []
                'RelPKt': 0.2,  # []
                'LenZw': 0.2,   # []
                'AgeZw': 0.0,   # []
                'AgeBm': 0.0}   # []

# dictionary of the category weights for the pinch-out prob. of a new "Knospe"
dCtWt_PrPKs = {'VertZ': 0.4,    # []
               'RelPZw': 0.2,   # []
               'RelPKt': 0.2,   # []
               'LenZw': 0.2,    # []
               'AgeZw': 0.0,    # []
               'AgeBm': 0.0}    # []

# dictionary of the category weights for the pinch-out prob. of a new "Zweig"
dCtWt_PrPZw = {'VertZ': 0.4,    # []
               'RelPZw': 0.1,   # []
               'RelPKt': 0.2,   # []
               'LenZw': 0.1,    # []
               'AgeZw': 0.2,    # []
               'AgeBm': 0.0}    # []

# MORPHOLOGICAL DATA -----------------------------------------------------------

(numNKZwAv_VertZ_A0, numNKZwSD_VertZ_A0) = (36.0, 5.0)
(numNKZwAv_VertZ_A1, numNKZwSD_VertZ_A1) = (34.0, 4.5)
(numNKZwAv_VertZ_A2, numNKZwSD_VertZ_A2) = (32.0, 4.0)
(numNKZwAv_VertZ_A3, numNKZwSD_VertZ_A3) = (30.0, 3.5)
(numNKZwAv_VertZ_A4, numNKZwSD_VertZ_A4) = (28.0, 3.0)
(numNKZwAv_VertZ_A5, numNKZwSD_VertZ_A5) = (26.0, 2.5)

(numNKZwAv_RelPZw_A0, numNKZwSD_RelPZw_A0) = (35.0, 5.0)
(numNKZwAv_RelPZw_A1, numNKZwSD_RelPZw_A1) = (33.0, 4.5)
(numNKZwAv_RelPZw_A2, numNKZwSD_RelPZw_A2) = (31.0, 4.0)
(numNKZwAv_RelPZw_A3, numNKZwSD_RelPZw_A3) = (29.0, 3.5)
(numNKZwAv_RelPZw_A4, numNKZwSD_RelPZw_A4) = (27.0, 3.0)
(numNKZwAv_RelPZw_A5, numNKZwSD_RelPZw_A5) = (25.0, 2.5)

(numNKZwAv_RelPKt_A0, numNKZwSD_RelPKt_A0) = (22.0, 2.5)
(numNKZwAv_RelPKt_A1, numNKZwSD_RelPKt_A1) = (26.0, 3.0)
(numNKZwAv_RelPKt_A2, numNKZwSD_RelPKt_A2) = (30.0, 3.5)
(numNKZwAv_RelPKt_A3, numNKZwSD_RelPKt_A3) = (29.5, 3.5)
(numNKZwAv_RelPKt_A4, numNKZwSD_RelPKt_A4) = (34.0, 4.0)
(numNKZwAv_RelPKt_A5, numNKZwSD_RelPKt_A5) = (numNKZwAv_RelPKt_A4, numNKZwSD_RelPKt_A4)

(numNKZwAv_LenZw_A0, numNKZwSD_LenZw_A0) = (33.5, 4.0)

(numNKZwAv_AgeZw_A0, numNKZwSD_AgeZw_A0) = (33.5, 4.0)

(numNKZwAv_AgeBm_A0, numNKZwSD_AgeBm_A0) = (33.5, 4.0)

(numNKKtAv_VertZ_A0, numNKKtSD_VertZ_A0) = (1.0, 0.0)
(numNKKtAv_VertZ_A1, numNKKtSD_VertZ_A1) = (1.0, 0.0)
(numNKKtAv_VertZ_A2, numNKKtSD_VertZ_A2) = (1.0, 0.0)
(numNKKtAv_VertZ_A3, numNKKtSD_VertZ_A3) = (1.0, 0.0)
(numNKKtAv_VertZ_A4, numNKKtSD_VertZ_A4) = (1.0, 0.0)
(numNKKtAv_VertZ_A5, numNKKtSD_VertZ_A5) = (1.0, 0.0)

(numNKKtAv_RelPZw_A0, numNKKtSD_RelPZw_A0) = (1.0, 0.0)
(numNKKtAv_RelPZw_A1, numNKKtSD_RelPZw_A1) = (1.0, 0.0)
(numNKKtAv_RelPZw_A2, numNKKtSD_RelPZw_A2) = (1.0, 0.0)
(numNKKtAv_RelPZw_A3, numNKKtSD_RelPZw_A3) = (1.0, 0.0)
(numNKKtAv_RelPZw_A4, numNKKtSD_RelPZw_A4) = (1.0, 0.0)
(numNKKtAv_RelPZw_A5, numNKKtSD_RelPZw_A5) = (1.0, 0.0)

(numNKKtAv_RelPKt_A0, numNKKtSD_RelPKt_A0) = (1.0, 0.0)
(numNKKtAv_RelPKt_A1, numNKKtSD_RelPKt_A1) = (1.0, 0.0)
(numNKKtAv_RelPKt_A2, numNKKtSD_RelPKt_A2) = (1.0, 0.0)
(numNKKtAv_RelPKt_A3, numNKKtSD_RelPKt_A3) = (1.0, 0.0)
(numNKKtAv_RelPKt_A4, numNKKtSD_RelPKt_A4) = (1.0, 0.0)
(numNKKtAv_RelPKt_A5, numNKKtSD_RelPKt_A5) = (numNKKtAv_RelPKt_A4, numNKKtSD_RelPKt_A4)

(numNKKtAv_LenZw_A0, numNKKtSD_LenZw_A0) = (1.0, 0.0)

(numNKKtAv_AgeZw_A0, numNKKtSD_AgeZw_A0) = (1.0, 0.0)

(numNKKtAv_AgeBm_A0, numNKKtSD_AgeBm_A0) = (1.0, 0.0)

# number of new "Knoten" on a "Zweig"
# 1st tuple: (av. of distr., SD of distr.) - in case a distr. is used
# 2nd tuple: ([list of num. of new "Knoten"], [list of probabilities/weights])
# dimension: []
tNumNKZw_s_VertZ_A0 = ((numNKZwAv_VertZ_A0, numNKZwSD_VertZ_A0), (L_MX_4, [0.02, 0.3, 0.5, 0.18]))
tNumNKZw_v_VertZ_A0 = ((numNKZwAv_VertZ_A0, numNKZwSD_VertZ_A0), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_VertZ_A0 = ((numNKZwAv_VertZ_A0, numNKZwSD_VertZ_A0), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_VertZ_A0 = ((numNKZwAv_VertZ_A0, numNKZwSD_VertZ_A0), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_VertZ_A1 = tNumNKZw_s_VertZ_A0
tNumNKZw_v_VertZ_A1 = ((numNKZwAv_VertZ_A1, numNKZwSD_VertZ_A1), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_VertZ_A1 = ((numNKZwAv_VertZ_A1, numNKZwSD_VertZ_A1), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_VertZ_A1 = ((numNKZwAv_VertZ_A1, numNKZwSD_VertZ_A1), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_VertZ_A2 = tNumNKZw_s_VertZ_A0
tNumNKZw_v_VertZ_A2 = ((numNKZwAv_VertZ_A2, numNKZwSD_VertZ_A2), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_VertZ_A2 = ((numNKZwAv_VertZ_A2, numNKZwSD_VertZ_A2), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_VertZ_A2 = ((numNKZwAv_VertZ_A2, numNKZwSD_VertZ_A2), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_VertZ_A3 = tNumNKZw_s_VertZ_A0
tNumNKZw_v_VertZ_A3 = ((numNKZwAv_VertZ_A3, numNKZwSD_VertZ_A3), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_VertZ_A3 = ((numNKZwAv_VertZ_A3, numNKZwSD_VertZ_A3), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_VertZ_A3 = ((numNKZwAv_VertZ_A3, numNKZwSD_VertZ_A3), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_VertZ_A4 = tNumNKZw_s_VertZ_A0
tNumNKZw_v_VertZ_A4 = ((numNKZwAv_VertZ_A4, numNKZwSD_VertZ_A4), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_VertZ_A4 = ((numNKZwAv_VertZ_A4, numNKZwSD_VertZ_A4), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_VertZ_A4 = ((numNKZwAv_VertZ_A4, numNKZwSD_VertZ_A4), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_VertZ_A5 = tNumNKZw_s_VertZ_A0
tNumNKZw_v_VertZ_A5 = ((numNKZwAv_VertZ_A4, numNKZwSD_VertZ_A4), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_VertZ_A5 = ((numNKZwAv_VertZ_A4, numNKZwSD_VertZ_A4), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_VertZ_A5 = ((numNKZwAv_VertZ_A4, numNKZwSD_VertZ_A4), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPZw_A0 = ((numNKZwAv_RelPZw_A0, numNKZwSD_RelPZw_A0), (L_MX_4, [0.02, 0.3, 0.5, 0.18]))
tNumNKZw_v_RelPZw_A0 = ((numNKZwAv_RelPZw_A0, numNKZwSD_RelPZw_A0), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPZw_A0 = ((numNKZwAv_RelPZw_A0, numNKZwSD_RelPZw_A0), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPZw_A0 = ((numNKZwAv_RelPZw_A0, numNKZwSD_RelPZw_A0), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPZw_A1 = tNumNKZw_s_RelPZw_A0
tNumNKZw_v_RelPZw_A1 = ((numNKZwAv_RelPZw_A1, numNKZwSD_RelPZw_A1), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPZw_A1 = ((numNKZwAv_RelPZw_A1, numNKZwSD_RelPZw_A1), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPZw_A1 = ((numNKZwAv_RelPZw_A1, numNKZwSD_RelPZw_A1), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPZw_A2 = tNumNKZw_s_RelPZw_A0
tNumNKZw_v_RelPZw_A2 = ((numNKZwAv_RelPZw_A2, numNKZwSD_RelPZw_A2), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPZw_A2 = ((numNKZwAv_RelPZw_A2, numNKZwSD_RelPZw_A2), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPZw_A2 = ((numNKZwAv_RelPZw_A2, numNKZwSD_RelPZw_A2), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPZw_A3 = tNumNKZw_s_RelPZw_A0
tNumNKZw_v_RelPZw_A3 = ((numNKZwAv_RelPZw_A3, numNKZwSD_RelPZw_A3), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPZw_A3 = ((numNKZwAv_RelPZw_A3, numNKZwSD_RelPZw_A3), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPZw_A3 = ((numNKZwAv_RelPZw_A3, numNKZwSD_RelPZw_A3), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPZw_A4 = tNumNKZw_s_RelPZw_A0
tNumNKZw_v_RelPZw_A4 = ((numNKZwAv_RelPZw_A4, numNKZwSD_RelPZw_A4), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPZw_A4 = ((numNKZwAv_RelPZw_A4, numNKZwSD_RelPZw_A4), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPZw_A4 = ((numNKZwAv_RelPZw_A4, numNKZwSD_RelPZw_A4), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPZw_A5 = tNumNKZw_s_RelPZw_A0
tNumNKZw_v_RelPZw_A5 = ((numNKZwAv_RelPZw_A5, numNKZwSD_RelPZw_A5), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPZw_A5 = ((numNKZwAv_RelPZw_A5, numNKZwSD_RelPZw_A5), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPZw_A5 = ((numNKZwAv_RelPZw_A5, numNKZwSD_RelPZw_A5), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPKt_A0 = ((numNKZwAv_RelPKt_A0, numNKZwSD_RelPKt_A0), (L_MX_4, [0.02, 0.3, 0.5, 0.18]))
tNumNKZw_v_RelPKt_A0 = ((numNKZwAv_RelPKt_A0, numNKZwSD_RelPKt_A0), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPKt_A0 = ((numNKZwAv_RelPKt_A0, numNKZwSD_RelPKt_A0), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPKt_A0 = ((numNKZwAv_RelPKt_A0, numNKZwSD_RelPKt_A0), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPKt_A1 = tNumNKZw_s_RelPKt_A0
tNumNKZw_v_RelPKt_A1 = ((numNKZwAv_RelPKt_A1, numNKZwSD_RelPKt_A1), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPKt_A1 = ((numNKZwAv_RelPKt_A1, numNKZwSD_RelPKt_A1), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPKt_A1 = ((numNKZwAv_RelPKt_A1, numNKZwSD_RelPKt_A1), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPKt_A2 = tNumNKZw_s_RelPKt_A0
tNumNKZw_v_RelPKt_A2 = ((numNKZwAv_RelPKt_A2, numNKZwSD_RelPKt_A2), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPKt_A2 = ((numNKZwAv_RelPKt_A2, numNKZwSD_RelPKt_A2), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPKt_A2 = ((numNKZwAv_RelPKt_A2, numNKZwSD_RelPKt_A2), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPKt_A3 = tNumNKZw_s_RelPKt_A0
tNumNKZw_v_RelPKt_A3 = ((numNKZwAv_RelPKt_A3, numNKZwSD_RelPKt_A3), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPKt_A3 = ((numNKZwAv_RelPKt_A3, numNKZwSD_RelPKt_A3), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPKt_A3 = ((numNKZwAv_RelPKt_A3, numNKZwSD_RelPKt_A3), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPKt_A4 = tNumNKZw_s_RelPKt_A0
tNumNKZw_v_RelPKt_A4 = ((numNKZwAv_RelPKt_A4, numNKZwSD_RelPKt_A4), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPKt_A4 = ((numNKZwAv_RelPKt_A4, numNKZwSD_RelPKt_A4), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPKt_A4 = ((numNKZwAv_RelPKt_A4, numNKZwSD_RelPKt_A4), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_RelPKt_A5 = tNumNKZw_s_RelPKt_A0
tNumNKZw_v_RelPKt_A5 = ((numNKZwAv_RelPKt_A5, numNKZwSD_RelPKt_A5), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_RelPKt_A5 = ((numNKZwAv_RelPKt_A5, numNKZwSD_RelPKt_A5), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_RelPKt_A5 = ((numNKZwAv_RelPKt_A5, numNKZwSD_RelPKt_A5), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_LenZw_A0 = ((numNKZwAv_LenZw_A0, numNKZwSD_LenZw_A0), (L_MX_4, [0.02, 0.3, 0.5, 0.18]))
tNumNKZw_v_LenZw_A0 = ((numNKZwAv_LenZw_A0, numNKZwSD_LenZw_A0), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_LenZw_A0 = ((numNKZwAv_LenZw_A0, numNKZwSD_LenZw_A0), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_LenZw_A0 = ((numNKZwAv_LenZw_A0, numNKZwSD_LenZw_A0), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_AgeZw_A0 = ((numNKZwAv_AgeZw_A0, numNKZwSD_AgeZw_A0), (L_MX_4, [0.02, 0.3, 0.5, 0.18]))
tNumNKZw_v_AgeZw_A0 = ((numNKZwAv_AgeZw_A0, numNKZwSD_AgeZw_A0), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_AgeZw_A0 = ((numNKZwAv_AgeZw_A0, numNKZwSD_AgeZw_A0), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_AgeZw_A0 = ((numNKZwAv_AgeZw_A0, numNKZwSD_AgeZw_A0), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

tNumNKZw_s_AgeBm_A0 = ((numNKZwAv_AgeBm_A0, numNKZwSD_AgeBm_A0), (L_MX_4, [0.02, 0.3, 0.5, 0.18]))
tNumNKZw_v_AgeBm_A0 = ((numNKZwAv_AgeBm_A0, numNKZwSD_AgeBm_A0), (L_MX_4, [0.02, 0.1, 0.7, 0.18]))
tNumNKZw_w_AgeBm_A0 = ((numNKZwAv_AgeBm_A0, numNKZwSD_AgeBm_A0), (L_MX_4, [0.05, 0.8, 0.12, 0.03]))
tNumNKZw_x_AgeBm_A0 = ((numNKZwAv_AgeBm_A0, numNKZwSD_AgeBm_A0), (L_MX_4, [0.8, 0.17, 0.02, 0.01]))

# number of new "Knospen" on a "Knoten"
# 1st tuple: (av. of distr., SD of distr.) - in case a distr. is used
# 2nd tuple: ([list of num. of new "Knospen"], [list of probabilities/weights])
# dimension: []
tNumNKKt_s_VertZ_A0 = ((numNKKtAv_VertZ_A0, numNKKtSD_VertZ_A0), (L_MX_6, [0.02, 0.2, 0.4, 0.26, 0.11, 0.01]))
tNumNKKt_v_VertZ_A0 = ((numNKKtAv_VertZ_A0, numNKKtSD_VertZ_A0), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_VertZ_A0 = ((numNKKtAv_VertZ_A0, numNKKtSD_VertZ_A0), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_VertZ_A0 = ((numNKKtAv_VertZ_A0, numNKKtSD_VertZ_A0), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_VertZ_A1 = tNumNKKt_s_VertZ_A0
tNumNKKt_v_VertZ_A1 = ((numNKKtAv_VertZ_A1, numNKKtSD_VertZ_A1), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_VertZ_A1 = ((numNKKtAv_VertZ_A1, numNKKtSD_VertZ_A1), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_VertZ_A1 = ((numNKKtAv_VertZ_A1, numNKKtSD_VertZ_A1), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_VertZ_A2 = tNumNKKt_s_VertZ_A0
tNumNKKt_v_VertZ_A2 = ((numNKKtAv_VertZ_A2, numNKKtSD_VertZ_A2), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_VertZ_A2 = ((numNKKtAv_VertZ_A2, numNKKtSD_VertZ_A2), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_VertZ_A2 = ((numNKKtAv_VertZ_A2, numNKKtSD_VertZ_A2), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_VertZ_A3 = tNumNKKt_s_VertZ_A0
tNumNKKt_v_VertZ_A3 = ((numNKKtAv_VertZ_A3, numNKKtSD_VertZ_A3), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_VertZ_A3 = ((numNKKtAv_VertZ_A3, numNKKtSD_VertZ_A3), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_VertZ_A3 = ((numNKKtAv_VertZ_A3, numNKKtSD_VertZ_A3), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_VertZ_A4 = tNumNKKt_s_VertZ_A0
tNumNKKt_v_VertZ_A4 = ((numNKKtAv_VertZ_A4, numNKKtSD_VertZ_A4), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_VertZ_A4 = ((numNKKtAv_VertZ_A4, numNKKtSD_VertZ_A4), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_VertZ_A4 = ((numNKKtAv_VertZ_A4, numNKKtSD_VertZ_A4), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_VertZ_A5 = tNumNKKt_s_VertZ_A0
tNumNKKt_v_VertZ_A5 = ((numNKKtAv_VertZ_A5, numNKKtSD_VertZ_A5), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_VertZ_A5 = ((numNKKtAv_VertZ_A5, numNKKtSD_VertZ_A5), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_VertZ_A5 = ((numNKKtAv_VertZ_A5, numNKKtSD_VertZ_A5), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPZw_A0 = ((numNKKtAv_RelPZw_A0, numNKKtSD_RelPZw_A0), (L_MX_6, [0.02, 0.2, 0.4, 0.26, 0.11, 0.01]))
tNumNKKt_v_RelPZw_A0 = ((numNKKtAv_RelPZw_A0, numNKKtSD_RelPZw_A0), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPZw_A0 = ((numNKKtAv_RelPZw_A0, numNKKtSD_RelPZw_A0), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPZw_A0 = ((numNKKtAv_RelPZw_A0, numNKKtSD_RelPZw_A0), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPZw_A1 = tNumNKKt_s_RelPZw_A0
tNumNKKt_v_RelPZw_A1 = ((numNKKtAv_RelPZw_A1, numNKKtSD_RelPZw_A1), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPZw_A1 = ((numNKKtAv_RelPZw_A1, numNKKtSD_RelPZw_A1), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPZw_A1 = ((numNKKtAv_RelPZw_A1, numNKKtSD_RelPZw_A1), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPZw_A2 = tNumNKKt_s_RelPZw_A0
tNumNKKt_v_RelPZw_A2 = ((numNKKtAv_RelPZw_A2, numNKKtSD_RelPZw_A2), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPZw_A2 = ((numNKKtAv_RelPZw_A2, numNKKtSD_RelPZw_A2), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPZw_A2 = ((numNKKtAv_RelPZw_A2, numNKKtSD_RelPZw_A2), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPZw_A3 = tNumNKKt_s_RelPZw_A0
tNumNKKt_v_RelPZw_A3 = ((numNKKtAv_RelPZw_A3, numNKKtSD_RelPZw_A3), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPZw_A3 = ((numNKKtAv_RelPZw_A3, numNKKtSD_RelPZw_A3), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPZw_A3 = ((numNKKtAv_RelPZw_A3, numNKKtSD_RelPZw_A3), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPZw_A4 = tNumNKKt_s_RelPZw_A0
tNumNKKt_v_RelPZw_A4 = ((numNKKtAv_RelPZw_A4, numNKKtSD_RelPZw_A4), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPZw_A4 = ((numNKKtAv_RelPZw_A4, numNKKtSD_RelPZw_A4), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPZw_A4 = ((numNKKtAv_RelPZw_A4, numNKKtSD_RelPZw_A4), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPZw_A5 = tNumNKKt_s_RelPZw_A0
tNumNKKt_v_RelPZw_A5 = ((numNKKtAv_RelPZw_A5, numNKKtSD_RelPZw_A5), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPZw_A5 = ((numNKKtAv_RelPZw_A5, numNKKtSD_RelPZw_A5), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPZw_A5 = ((numNKKtAv_RelPZw_A5, numNKKtSD_RelPZw_A5), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPKt_A0 = ((numNKKtAv_RelPKt_A0, numNKKtSD_RelPKt_A0), (L_MX_6, [0.02, 0.2, 0.4, 0.26, 0.11, 0.01]))
tNumNKKt_v_RelPKt_A0 = ((numNKKtAv_RelPKt_A0, numNKKtSD_RelPKt_A0), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPKt_A0 = ((numNKKtAv_RelPKt_A0, numNKKtSD_RelPKt_A0), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPKt_A0 = ((numNKKtAv_RelPKt_A0, numNKKtSD_RelPKt_A0), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPKt_A1 = tNumNKKt_s_RelPKt_A0
tNumNKKt_v_RelPKt_A1 = ((numNKKtAv_RelPKt_A1, numNKKtSD_RelPKt_A1), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPKt_A1 = ((numNKKtAv_RelPKt_A1, numNKKtSD_RelPKt_A1), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPKt_A1 = ((numNKKtAv_RelPKt_A1, numNKKtSD_RelPKt_A1), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPKt_A2 = tNumNKKt_s_RelPKt_A0
tNumNKKt_v_RelPKt_A2 = ((numNKKtAv_RelPKt_A2, numNKKtSD_RelPKt_A2), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPKt_A2 = ((numNKKtAv_RelPKt_A2, numNKKtSD_RelPKt_A2), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPKt_A2 = ((numNKKtAv_RelPKt_A2, numNKKtSD_RelPKt_A2), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPKt_A3 = tNumNKKt_s_RelPKt_A0
tNumNKKt_v_RelPKt_A3 = ((numNKKtAv_RelPKt_A3, numNKKtSD_RelPKt_A3), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPKt_A3 = ((numNKKtAv_RelPKt_A3, numNKKtSD_RelPKt_A3), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPKt_A3 = ((numNKKtAv_RelPKt_A3, numNKKtSD_RelPKt_A3), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPKt_A4 = tNumNKKt_s_RelPKt_A0
tNumNKKt_v_RelPKt_A4 = ((numNKKtAv_RelPKt_A4, numNKKtSD_RelPKt_A4), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPKt_A4 = ((numNKKtAv_RelPKt_A4, numNKKtSD_RelPKt_A4), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPKt_A4 = ((numNKKtAv_RelPKt_A4, numNKKtSD_RelPKt_A4), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_RelPKt_A5 = tNumNKKt_s_RelPKt_A0
tNumNKKt_v_RelPKt_A5 = ((numNKKtAv_RelPKt_A5, numNKKtSD_RelPKt_A5), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_RelPKt_A5 = ((numNKKtAv_RelPKt_A5, numNKKtSD_RelPKt_A5), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_RelPKt_A5 = ((numNKKtAv_RelPKt_A5, numNKKtSD_RelPKt_A5), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_LenZw_A0 = ((numNKKtAv_LenZw_A0, numNKKtSD_LenZw_A0), (L_MX_6, [0.02, 0.2, 0.4, 0.26, 0.11, 0.01]))
tNumNKKt_v_LenZw_A0 = ((numNKKtAv_LenZw_A0, numNKKtSD_LenZw_A0), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_LenZw_A0 = ((numNKKtAv_LenZw_A0, numNKKtSD_LenZw_A0), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_LenZw_A0 = ((numNKKtAv_LenZw_A0, numNKKtSD_LenZw_A0), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_AgeZw_A0 = ((numNKKtAv_AgeZw_A0, numNKKtSD_AgeZw_A0), (L_MX_6, [0.02, 0.2, 0.4, 0.26, 0.11, 0.01]))
tNumNKKt_v_AgeZw_A0 = ((numNKKtAv_AgeZw_A0, numNKKtSD_AgeZw_A0), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_AgeZw_A0 = ((numNKKtAv_AgeZw_A0, numNKKtSD_AgeZw_A0), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_AgeZw_A0 = ((numNKKtAv_AgeZw_A0, numNKKtSD_AgeZw_A0), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

tNumNKKt_s_AgeBm_A0 = ((numNKKtAv_AgeBm_A0, numNKKtSD_AgeBm_A0), (L_MX_6, [0.02, 0.2, 0.4, 0.26, 0.11, 0.01]))
tNumNKKt_v_AgeBm_A0 = ((numNKKtAv_AgeBm_A0, numNKKtSD_AgeBm_A0), (L_MX_6, [0.02, 0.1, 0.5, 0.26, 0.11, 0.01]))
tNumNKKt_w_AgeBm_A0 = ((numNKKtAv_AgeBm_A0, numNKKtSD_AgeBm_A0), (L_MX_6, [0.05, 0.6, 0.22, 0.11, 0.01, 0.01]))
tNumNKKt_x_AgeBm_A0 = ((numNKKtAv_AgeBm_A0, numNKKtSD_AgeBm_A0), (L_MX_6, [0.6, 0.34, 0.04, 0.015, 0.004, 0.001]))

# offset of azim. angle for next "Knoten" (dep. on # "Knospen" on a "Knoten")
# (mean, SD)
# dimension: [deg]
tOffsAngAzm_k_1 = (0, 0.)
tOffsAngAzm_s_1 = (120, 25.)
tOffsAngAzm_v_1 = (120, 25.)
tOffsAngAzm_w_1 = (120, 25.)
tOffsAngAzm_x_1 = (120, 25.)

tOffsAngAzm_s_2 = (120, 25.)
tOffsAngAzm_v_2 = (120, 25.)
tOffsAngAzm_w_2 = (120, 25.)
tOffsAngAzm_x_2 = (120, 25.)

tOffsAngAzm_s_3 = (120, 25.)
tOffsAngAzm_v_3 = (120, 25.)
tOffsAngAzm_w_3 = (120, 25.)
tOffsAngAzm_x_3 = (120, 25.)

tOffsAngAzm_s_4 = (120, 25.)
tOffsAngAzm_v_4 = (120, 25.)
tOffsAngAzm_w_4 = (120, 25.)
tOffsAngAzm_x_4 = (120, 25.)

tOffsAngAzm_s_5 = (120, 25.)
tOffsAngAzm_v_5 = (120, 25.)
tOffsAngAzm_w_5 = (120, 25.)
tOffsAngAzm_x_5 = (120, 25.)

tOffsAngAzm_s_6 = (120, 25.)
tOffsAngAzm_v_6 = (120, 25.)
tOffsAngAzm_w_6 = (120, 25.)
tOffsAngAzm_x_6 = (120, 25.)

# length factors of positions of new "Knoten" on a "Zweig"
# (mean, SD)
# dimension: []
tFctPKZw_s_0 = (1, 0.03)     # 0 corresponds to the normal distribution
tFctPKZw_v_0 = (1, 0.03)     # SD as a proportion of the resp. mean value
tFctPKZw_w_0 = (1, 0.03)
tFctPKZw_x_0 = (1, 0.03)

# ([list of means], [list of SDs])
tFctPKZw_s_1 = ([1], [0])
tFctPKZw_v_1 = ([1], [0])
tFctPKZw_w_1 = ([1], [0])
tFctPKZw_x_1 = ([1], [0])

tFctPKZw_s_2 = ([1, 0.5], [0, 0.05])
tFctPKZw_v_2 = ([1, 0.45], [0, 0.04])
tFctPKZw_w_2 = ([1, 0.4], [0, 0.03])
tFctPKZw_x_2 = ([1, 0.3], [0, 0.02])

tFctPKZw_s_3 = ([1, 0.7, 0.45], [0, 0.06, 0.03])
tFctPKZw_v_3 = ([1, 0.6, 0.35], [0, 0.05, 0.025])
tFctPKZw_w_3 = ([1, 0.5, 0.25], [0, 0.04, 0.02])
tFctPKZw_x_3 = ([1, 0.4, 0.15], [0, 0.03, 0.015])

tFctPKZw_s_4 = ([1, 0.6, 0.55, 0.25], [0, 0.07, 0.05, 0.025])
tFctPKZw_v_4 = ([1, 0.7, 0.45, 0.2], [0, 0.06, 0.04, 0.02])
tFctPKZw_w_4 = ([1, 0.6, 0.35, 0.15], [0, 0.05, 0.03, 0.015])
tFctPKZw_x_4 = ([1, 0.5, 0.25, 0.1], [0, 0.04, 0.02, 0.01])

# length factors of positions of edges on new "Zweig" (0 and 1 are disregarded)
# ([list of means], [list of SDs])
# dimension: []
tFctPEZw_s = ([], [])
tFctPEZw_v = ([], [])
tFctPEZw_w = (list(np.logspace(-6., 0., 20, endpoint = False, base = 2.)), list(np.logspace(-9., -3., 20, endpoint = False, base = 2.)))
tFctPEZw_x = (list(np.logspace(-6.1, -0.1, 20, endpoint = False, base = 2.)), list(np.logspace(-9.1, -3.1, 20, endpoint = False, base = 2.)))

# "Zweig" lengths, depending on the number of "Knoten" on parent "Zweig"
# ([max, min], SD)
# dimension: [cm]
tLengthZw_s_0 = ([110, 35], 0.1)    # 0 corresponds to the normal distribution
tLengthZw_v_0 = ([130, 90], 0.1)    # SD as a proportion of the resp. value
tLengthZw_w_0 = ([90, 70], 0.1)
tLengthZw_x_0 = ([60, 45], 0.1)

# (mean, SD)
tLengthZw_s_1 = (40, 4.0)
tLengthZw_v_1 = (110, 8.0)
tLengthZw_w_1 = (80, 6.0)
tLengthZw_x_1 = (50, 4.5)

tLengthZw_s_2 = (40, 4.0)
tLengthZw_v_2 = (105, 7.5)
tLengthZw_w_2 = (75, 5.6)
tLengthZw_x_2 = (45, 4.2)

tLengthZw_s_3 = (40, 4.0)
tLengthZw_v_3 = (100, 7.0)
tLengthZw_w_3 = (70, 5.2)
tLengthZw_x_3 = (40, 3.9)

tLengthZw_s_4 = (40, 4.0)
tLengthZw_v_4 = (95, 6.5)
tLengthZw_w_4 = (65, 5.0)
tLengthZw_x_4 = (35, 3.6)

# polar angles of new "Knospen" on a "Knoten"
# ([list of means], [list of SDs])
# dimension: [deg]
# polar angles for "Knoten" not at the end of parent "Zweig"
tAngKPlr_k_1 = ([0], [0.0])
tAngKPlr_s_1 = ([40], [1.0])
tAngKPlr_v_1 = ([42], [1.0])
tAngKPlr_w_1 = ([43], [2.0])
tAngKPlr_x_1 = ([44], [3.0])

tAngKPlr_s_2 = ([40, 40], [3.0, 3.0])
tAngKPlr_v_2 = ([42, 42], [3.0, 3.0])
tAngKPlr_w_2 = ([43, 43], [3.0, 3.0])
tAngKPlr_x_2 = ([45, 45], [3.0, 3.0])

tAngKPlr_s_3 = ([40, 40, 40], [3.0, 3.0, 3.0])
tAngKPlr_v_3 = ([42, 42, 42], [3.0, 3.0, 3.0])
tAngKPlr_w_3 = ([43, 43, 43], [3.0, 3.0, 3.0])
tAngKPlr_x_3 = ([45, 45, 45], [3.0, 3.0, 3.0])

tAngKPlr_s_4 = ([40, 40, 40, 40], [3.0, 3.0, 3.0, 3.0])
tAngKPlr_v_4 = ([42, 42, 42, 42], [3.0, 3.0, 3.0, 3.0])
tAngKPlr_w_4 = ([43, 43, 43, 43], [3.0, 3.0, 3.0, 3.0])
tAngKPlr_x_4 = ([45, 45, 45, 45], [3.0, 3.0, 3.0, 3.0])

tAngKPlr_s_5 = ([40, 40, 40, 40, 40], [3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_v_5 = ([42, 42, 42, 42, 42], [3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_w_5 = ([43, 43, 43, 43, 43], [3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_x_5 = ([45, 45, 45, 45, 45], [3.0, 3.0, 3.0, 3.0, 3.0])

tAngKPlr_s_6 = ([40, 40, 40, 40, 40, 40], [3.0, 3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_v_6 = ([42, 42, 42, 42, 42, 42], [3.0, 3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_w_6 = ([43, 43, 43, 43, 43, 43], [3.0, 3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_x_6 = ([45, 45, 45, 45, 45, 45], [3.0, 3.0, 3.0, 3.0, 3.0, 3.0])

# polar angles for "Knoten" at the end of parent "Zweig"
tAngKPlr_k_1_E = tAngKPlr_k_1
tAngKPlr_s_1_E = ([0], [1.0])
tAngKPlr_v_1_E = ([0], [1.0])
tAngKPlr_w_1_E = ([0], [2.0])
tAngKPlr_x_1_E = ([0], [3.0])

tAngKPlr_s_2_E = ([0, 43], [3.0, 3.0])
tAngKPlr_v_2_E = ([0, 44], [3.0, 3.0])
tAngKPlr_w_2_E = ([0, 45], [3.0, 3.0])
tAngKPlr_x_2_E = ([0, 46], [3.0, 3.0])

tAngKPlr_s_3_E = ([0, 43, 43], [3.0, 3.0, 3.0])
tAngKPlr_v_3_E = ([0, 44, 44], [3.0, 3.0, 3.0])
tAngKPlr_w_3_E = ([0, 45, 45], [3.0, 3.0, 3.0])
tAngKPlr_x_3_E = ([0, 46, 46], [3.0, 3.0, 3.0])

tAngKPlr_s_4_E = ([0, 43, 43, 43], [3.0, 3.0, 3.0, 3.0])
tAngKPlr_v_4_E = ([0, 44, 44, 44], [3.0, 3.0, 3.0, 3.0])
tAngKPlr_w_4_E = ([0, 45, 45, 45], [3.0, 3.0, 3.0, 3.0])
tAngKPlr_x_4_E = ([0, 46, 46, 46], [3.0, 3.0, 3.0, 3.0])

tAngKPlr_s_5_E = ([0, 43, 43, 43, 43], [3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_v_5_E = ([0, 44, 44, 44, 44], [3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_w_5_E = ([0, 45, 45, 45, 45], [3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_x_5_E = ([0, 46, 46, 46, 46], [3.0, 3.0, 3.0, 3.0, 3.0])

tAngKPlr_s_6_E = ([0, 43, 43, 43, 43, 43], [3.0, 3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_v_6_E = ([0, 44, 44, 44, 44, 44], [3.0, 3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_w_6_E = ([0, 45, 45, 45, 45, 45], [3.0, 3.0, 3.0, 3.0, 3.0, 3.0])
tAngKPlr_x_6_E = ([0, 46, 46, 46, 46, 46], [3.0, 3.0, 3.0, 3.0, 3.0, 3.0])

# azimuth angles of new "Knospen" on a "Knoten"
# ([list of means], [list of SDs])
# dimension: [deg]
# azimuth angles for "Knoten" not at the end of parent "Zweig"
tAngKAzm_k_1 = ([0], [0.0])
tAngKAzm_s_1 = ([0], [1.0])
tAngKAzm_v_1 = ([0], [9.0])
tAngKAzm_w_1 = ([180], [9.0])
tAngKAzm_x_1 = ([180], [9.0])

tAngKAzm_s_2 = ([0, 180], [9.0, 9.0])
tAngKAzm_v_2 = ([0, 180], [9.0, 9.0])
tAngKAzm_w_2 = ([80, 280], [9.0, 9.0])
tAngKAzm_x_2 = ([70, 290], [9.0, 9.0])

tAngKAzm_s_3 = ([0, 120, 240], [9.0, 9.0, 9.0])
tAngKAzm_v_3 = ([0, 120, 240], [9.0, 9.0, 9.0])
tAngKAzm_w_3 = ([50, 180, 310], [9.0, 9.0, 9.0])
tAngKAzm_x_3 = ([40, 180, 320], [9.0, 9.0, 9.0])

tAngKAzm_s_4 = ([0, 90, 180, 270], [9.0, 9.0, 9.0, 9.0])
tAngKAzm_v_4 = ([0, 90, 180, 270], [9.0, 9.0, 9.0, 9.0])
tAngKAzm_w_4 = ([35, 125, 235, 325], [9.0, 9.0, 9.0, 9.0])
tAngKAzm_x_4 = ([25, 115, 245, 335], [9.0, 9.0, 9.0, 9.0])

tAngKAzm_s_5 = ([0, 72, 144, 216, 288], [9.0, 9.0, 9.0, 9.0, 9.0])
tAngKAzm_v_5 = ([0, 72, 144, 216, 288], [9.0, 9.0, 9.0, 9.0, 9.0])
tAngKAzm_w_5 = ([26, 98, 180, 262, 334], [9.0, 9.0, 9.0, 9.0, 9.0])
tAngKAzm_x_5 = ([16, 88, 180, 272, 344], [9.0, 9.0, 9.0, 9.0, 9.0])

tAngKAzm_s_6 = ([0, 60, 120, 180, 240, 300], [9.0, 9.0, 9.0, 9.0, 9.0, 9.0])
tAngKAzm_v_6 = ([0, 60, 120, 180, 240, 300], [9.0, 9.0, 9.0, 9.0, 9.0, 9.0])
tAngKAzm_w_6 = ([20, 80, 140, 220, 280, 340], [9.0, 9.0, 9.0, 9.0, 9.0, 9.0])
tAngKAzm_x_6 = ([15, 75, 135, 225, 285, 345], [9.0, 9.0, 9.0, 9.0, 9.0, 9.0])

# azimuth angles for "Knoten" at the end of parent "Zweig"
tAngKAzm_k_1_E = tAngKAzm_k_1
tAngKAzm_s_1_E = ([0], [1.0])
tAngKAzm_v_1_E = ([0], [9.0])
tAngKAzm_w_1_E = ([0], [9.0])
tAngKAzm_x_1_E = ([0], [9.0])

tAngKAzm_s_2_E = ([0, 0], [15.0, 15.0])
tAngKAzm_v_2_E = ([0, 0], [15.0, 15.0])
tAngKAzm_w_2_E = ([0, 180], [15.0, 15.0])
tAngKAzm_x_2_E = ([0, 180], [15.0, 15.0])

tAngKAzm_s_3_E = ([0, 0, 180], [15.0, 15.0, 15.0])
tAngKAzm_v_3_E = ([0, 0, 180], [15.0, 15.0, 15.0])
tAngKAzm_w_3_E = ([0, 80, 280], [15.0, 15.0, 15.0])
tAngKAzm_x_3_E = ([0, 70, 290], [15.0, 15.0, 15.0])

tAngKAzm_s_4_E = ([0, 0, 120, 240], [15.0, 15.0, 15.0, 15.0])
tAngKAzm_v_4_E = ([0, 0, 120, 240], [15.0, 15.0, 15.0, 15.0])
tAngKAzm_w_4_E = ([0, 50, 180, 310], [15.0, 15.0, 15.0, 15.0])
tAngKAzm_x_4_E = ([0, 40, 180, 320], [15.0, 15.0, 15.0, 15.0])

tAngKAzm_s_5_E = ([0, 0, 90, 180, 270], [15.0, 15.0, 15.0, 15.0, 15.0])
tAngKAzm_v_5_E = ([0, 0, 90, 180, 270], [15.0, 15.0, 15.0, 15.0, 15.0])
tAngKAzm_w_5_E = ([0, 35, 125, 235, 325], [15.0, 15.0, 15.0, 15.0, 15.0])
tAngKAzm_x_5_E = ([0, 25, 115, 245, 335], [15.0, 15.0, 15.0, 15.0, 15.0])

tAngKAzm_s_6_E = ([0, 0, 72, 144, 216, 288], [15.0, 15.0, 15.0, 15.0, 15.0, 15.0])
tAngKAzm_v_6_E = ([0, 0, 72, 144, 216, 288], [15.0, 15.0, 15.0, 15.0, 15.0, 15.0])
tAngKAzm_w_6_E = ([0, 26, 98, 180, 262, 334], [15.0, 15.0, 15.0, 15.0, 15.0, 15.0])
tAngKAzm_x_6_E = ([0, 16, 88, 180, 272, 344], [15.0, 15.0, 15.0, 15.0, 15.0, 15.0])

# polar angles of edges on new "Zweig"
# ([list of means], [list of SDs])
# dimension: [deg]
tAngEPlr_s = ([], [])
tAngEPlr_v = ([], [])
tAngEPlr_w = (list(np.logspace(3., 0., 20, endpoint = False, base = 2.)), [1.]*20)
tAngEPlr_x = (list(np.logspace(3.5, 0., 20, endpoint = False, base = 2.)), [1.5]*20)

# azim. angles of edges on new "Zweig"
# ([list of means], [list of SDs])
# dimension: [deg]
tAngEAzm_s = ([], [])
tAngEAzm_v = ([], [])
tAngEAzm_w = ([0.]*len(tAngEPlr_w[0]), [1.]*len(tAngEPlr_w[1]))
tAngEAzm_x = ([0.]*len(tAngEPlr_x[0]), [1.]*len(tAngEPlr_x[1]))

tAngChDr_s = (0., 0.)
tAngChDr_v = (0., 0.)
tAngChDr_w = (0., 0.)
tAngChDr_x = (0., 0.)

# proportion of objects to be "pinched out"
# (mean, SD)
# dimension: [deg]
tPrpPinch_Knospe_k = (E12, E06)
tPrpPinch_Knospe_s = (E12, 0.04)
tPrpPinch_Knospe_v = (0.02, 0.002)
tPrpPinch_Knospe_w = (0.33, 0.06)
tPrpPinch_Knospe_x = (0.48, 0.07)

tPrpPinch_Zweig_k = (E12, E06)
tPrpPinch_Zweig_s = (0.3, 0.045)
tPrpPinch_Zweig_v = (0.33, 0.05)
tPrpPinch_Zweig_w = (0.42, 0.07)
tPrpPinch_Zweig_x = (0.48, 0.09)

# "Blatt" data -----------------------------------------------------------------
fAngBlattPlr = 1.4  # factor (mult.) for polar angle of "Blatt"    []
lenBlatt = 2.0      # [cm]
widBlatt = 1.0      # [cm]
shapeBlatt = 'oval' # 'rectangle' / 'oval'

# direction dependent adjustment factors: [min , max] --------------------------
# ([list of means], [list of SDs])
# dimension: []

# adjustments of "Zweig" length - depending on dir. relative to vUz
tAdjLenZw_VertZ_s = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_VertZ_v = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_VertZ_w = ([0.6, 1.0], [0.002, 0.0])
tAdjLenZw_VertZ_x = ([0.4, 0.8], [0.002, 0.0])

# adjustments of "Zweig" length - depending on dir. relative to parent "Zweig"
tAdjLenZw_RelPZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_RelPZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_RelPZw_w = ([0.4, 1.0], [0.002, 0.0])
tAdjLenZw_RelPZw_x = ([0.2, 0.8], [0.002, 0.0])

# adjustments of "Zweig" length - depending on pos. relative to parent "Zweig"
tAdjLenZw_RelPKt_s = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_RelPKt_v = ([0.6, 1.0], [0.0, 0.0])
tAdjLenZw_RelPKt_w = ([0.5, 1.0], [0.002, 0.0])
tAdjLenZw_RelPKt_x = ([0.4, 1.0], [0.002, 0.0])

# adjustments of "Zweig" length - depending on parent "Zweig" length
tAdjLenZw_LenZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_LenZw_v = ([EPS, 1.0], [0.0, 0.0])
tAdjLenZw_LenZw_w = ([EPS, 1.0], [0.002, 0.0])
tAdjLenZw_LenZw_x = ([EPS, 1.0], [0.002, 0.0])

# adjustments of "Zweig" length - depending on parent "Zweig" age
tAdjLenZw_AgeZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_AgeZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_AgeZw_w = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_AgeZw_x = ([1.0, 1.0], [0.0, 0.0])

# adjustments of "Zweig" length - depending on "Baum" age
tAdjLenZw_AgeBm_s = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_AgeBm_v = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_AgeBm_w = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_AgeBm_x = ([1.0, 1.0], [0.0, 0.0])

# adjustments of polar angle of "Knospe" - depending on dir. relative to vUz
tAdjAngPol_VertZ_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_VertZ_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_VertZ_w = ([0.8, 1.0/0.8], [0.002, 0.002])
tAdjAngPol_VertZ_x = ([0.6, 1.0/0.6], [0.002, 0.002])

# adjustments of polar angle of "Knospe" - depending on dir. relative to parent "Zweig"
tAdjAngPol_RelPZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_RelPZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_RelPZw_w = ([0.7, 1.0/0.7], [0.002, 0.002])
tAdjAngPol_RelPZw_x = ([0.55, 1.0/0.55], [0.002, 0.002])

# adjustments of polar angle of "Knospe" - depending on pos. relative to parent "Zweig"
tAdjAngPol_RelPKt_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_RelPKt_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_RelPKt_w = ([0.45, 1.0/0.64], [0.002, 0.002])
tAdjAngPol_RelPKt_x = ([0.5, 1.0/0.5], [0.002, 0.002])

# adjustments of polar angle of "Knospe" - depending on parent "Zweig" length
tAdjAngPol_LenZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_LenZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_LenZw_w = ([0.65, 1.0/0.65], [0.002, 0.002])
tAdjAngPol_LenZw_x = ([0.5, 1.0/0.5], [0.002, 0.002])

# adjustments of polar angle of "Knospe" - depending on parent "Zweig" age
tAdjAngPol_AgeZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_AgeZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_AgeZw_w = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_AgeZw_x = ([1.0, 1.0], [0.0, 0.0])

# adjustments of polar angle of "Knospe" - depending on "Baum" age
tAdjAngPol_AgeBm_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_AgeBm_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_AgeBm_w = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_AgeBm_x = ([1.0, 1.0], [0.0, 0.0])

# adjustments of azim. angle of "Knospe" - depending on dir. relative to vUz
tAdjAngAzm_VertZ_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_VertZ_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_VertZ_w = ([0.9, 1.0/0.9], [0.002, 0.002])
tAdjAngAzm_VertZ_x = ([0.75, 1.0/0.75], [0.002, 0.002])

# adjustments of azim. angle of "Knospe" - depending on dir. relative to parent "Zweig"
tAdjAngAzm_RelPZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_RelPZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_RelPZw_w = ([0.8, 1.0/0.8], [0.002, 0.002])
tAdjAngAzm_RelPZw_x = ([0.65, 1.0/0.65], [0.002, 0.002])

# adjustments of azim. angle of "Knospe" - depending on pos. relative to parent "Zweig"
tAdjAngAzm_RelPKt_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_RelPKt_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_RelPKt_w = ([0.7, 1.0/0.7], [0.002, 0.002])
tAdjAngAzm_RelPKt_x = ([0.55, 1.0/0.55], [0.002, 0.002])

# adjustments of azim. angle of "Knospe" - depending on parent "Zweig" length
tAdjAngAzm_LenZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_LenZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_LenZw_w = ([0.7, 1.0/0.7], [0.002, 0.002])
tAdjAngAzm_LenZw_x = ([0.45, 1.0/0.45], [0.002, 0.002])

# adjustments of azim. angle of "Knospe" - depending on parent "Zweig" age
tAdjAngAzm_AgeZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_AgeZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_AgeZw_w = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_AgeZw_x = ([1.0, 1.0], [0.0, 0.0])

# adjustments of azim. angle of "Knospe" - depending on "Baum" age
tAdjAngAzm_AgeBm_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_AgeBm_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_AgeBm_w = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_AgeBm_x = ([1.0, 1.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Knospe" - depending on dir. relative to vUz
tAdjPrPKs_VertZ_s = ([E12, E06], [0.0, 0.0])
tAdjPrPKs_VertZ_v = ([0.1, 2.0], [0.0, 0.0])
tAdjPrPKs_VertZ_w = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPKs_VertZ_x = ([0.5, 2.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Knospe" - depending on dir. relative to parent "Zweig"
tAdjPrPKs_RelPZw_s = ([E12, E06], [0.0, 0.0])
tAdjPrPKs_RelPZw_v = ([0.1, 2.0], [0.0, 0.0])
tAdjPrPKs_RelPZw_w = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPKs_RelPZw_x = ([0.5, 2.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Knospe" - depending on pos. relative to parent "Zweig"
tAdjPrPKs_RelPKt_s = ([E12, E06], [0.0, 0.0])
tAdjPrPKs_RelPKt_v = ([0.2, 2.0], [0.0, 0.0])
tAdjPrPKs_RelPKt_w = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPKs_RelPKt_x = ([0.5, 2.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Knospe" - depending on parent "Zweig" length
tAdjPrPKs_LenZw_s = ([E12, E06], [0.0, 0.0])
tAdjPrPKs_LenZw_v = ([0.1, 2.0], [0.0, 0.0])
tAdjPrPKs_LenZw_w = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPKs_LenZw_x = ([0.5, 2.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Knospe" - depending on parent "Zweig" age
tAdjPrPKs_AgeZw_s = ([E12, E06], [0.0, 0.0])
tAdjPrPKs_AgeZw_v = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPKs_AgeZw_w = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPKs_AgeZw_x = ([0.5, 2.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Knospe" - depending on "Baum" age
tAdjPrPKs_AgeBm_s = ([E12, E06], [0.0, 0.0])
tAdjPrPKs_AgeBm_v = ([1.0, 1.0], [0.0, 0.0])
tAdjPrPKs_AgeBm_w = ([1.0, 1.0], [0.0, 0.0])
tAdjPrPKs_AgeBm_x = ([1.0, 1.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Zweig" - depending on dir. relative to vUz
tAdjPrPZw_VertZ_s = ([E12, E06], [0.0, 0.0])
tAdjPrPZw_VertZ_v = ([0.1, 2.0], [0.0, 0.0])
tAdjPrPZw_VertZ_w = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPZw_VertZ_x = ([0.5, 2.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Zweig" - depending on dir. relative to parent "Zweig"
tAdjPrPZw_RelPZw_s = ([E12, E06], [0.0, 0.0])
tAdjPrPZw_RelPZw_v = ([0.1, 2.0], [0.0, 0.0])
tAdjPrPZw_RelPZw_w = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPZw_RelPZw_x = ([0.5, 2.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Zweig" - depending on pos. relative to parent "Zweig"
tAdjPrPZw_RelPKt_s = ([E12, E06], [0.0, 0.0])
tAdjPrPZw_RelPKt_v = ([0.2, 2.0], [0.0, 0.0])
tAdjPrPZw_RelPKt_w = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPZw_RelPKt_x = ([0.5, 2.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Zweig" - depending on parent "Zweig" length
tAdjPrPZw_LenZw_s = ([E12, E06], [0.0, 0.0])
tAdjPrPZw_LenZw_v = ([0.1, 2.0], [0.0, 0.0])
tAdjPrPZw_LenZw_w = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPZw_LenZw_x = ([0.5, 2.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Zweig" - depending on parent "Zweig" age
tAdjPrPZw_AgeZw_s = ([E12, E06], [0.0, 0.0])
tAdjPrPZw_AgeZw_v = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPZw_AgeZw_w = ([0.5, 2.0], [0.0, 0.0])
tAdjPrPZw_AgeZw_x = ([0.5, 2.0], [0.0, 0.0])

# adjustments of pinch-out prob. of "Zweig" - depending on "Baum" age
tAdjPrPZw_AgeBm_s = ([E12, E06], [0.0, 0.0])
tAdjPrPZw_AgeBm_v = ([1.0, 1.0], [0.0, 0.0])
tAdjPrPZw_AgeBm_w = ([1.0, 1.0], [0.0, 0.0])
tAdjPrPZw_AgeBm_x = ([1.0, 1.0], [0.0, 0.0])

# dictionary containing the parameters necessary for calculating adj. factors
dParFAdj_VertZ = {'std1': {},
                  'linA': {'a': 1.}}
dParFAdj_RelPZw = {'std1': {},
                   'linA': {'a': 1.},
                   'linB': {'m1V': 0.2, 'm2V': 0.5, 'm3V': 0.1}}
dParFAdj_RelPKt = {'std1': {},
                   'linA': {'a': 1.}}
dParFAdj_LenZw = {'std1': {},
                  'logF': {'k': 0.1, 'ln0': 50.}}
dParFAdj_AgeZw = {'std1': {},
                  'logF': {'k': 1., 'age0': 3.}}
dParFAdj_AgeBm = {'std1': {},
                  'logF': {'k': 1., 'age0': 3.}}

# direction dependent function types -------------------------------------------
tTypeAdjLenZw_VertZ = ('linA', dParFAdj_VertZ, 'dec')   # std1 / linA / cosA // // inc / dec
tTypeAdjLenZw_RelPZw = ('linA', dParFAdj_RelPZw, 'inc') # std1 / linA / sinA // // inc / dec
tTypeAdjLenZw_RelPKt = ('linA', dParFAdj_RelPKt, 'inc') # std1 / lin         // // inc / dec
tTypeAdjLenZw_LenZw = ('logF', dParFAdj_LenZw, 'inc')   # std1 / logF        // // inc / dec
tTypeAdjLenZw_AgeZw = ('std1', dParFAdj_AgeZw, 'inc')   # std1 / logF        // // inc / dec
tTypeAdjLenZw_AgeBm = ('std1', dParFAdj_AgeBm, 'inc')   # std1 / logF        // // inc / dec
tTypeAdjAngPol_VertZ = ('std1', dParFAdj_VertZ, 'inc')  # std1 / linA / cosA // // inc / dec
tTypeAdjAngPol_RelPZw = ('std1', dParFAdj_RelPZw, 'dec')# std1 / linA / sinA // // inc / dec
tTypeAdjAngPol_RelPKt = ('std1', dParFAdj_RelPKt, 'dec')# std1 / lin         // // inc / dec
tTypeAdjAngPol_LenZw = ('std1', dParFAdj_LenZw, 'inc')  # std1 / logF        // // inc / dec
tTypeAdjAngPol_AgeZw = ('std1', dParFAdj_AgeZw, 'inc')  # std1 / logF        // // inc / dec
tTypeAdjAngPol_AgeBm = ('std1', dParFAdj_AgeBm, 'inc')  # std1 / logF        // // inc / dec
tTypeAdjAngAzm_VertZ = ('std1', dParFAdj_VertZ, 'dec')  # std1 / linA / cosA // // inc / dec
tTypeAdjAngAzm_RelPZw = ('std1', dParFAdj_RelPZw, 'inc')# std1 / linA / sinA // // inc / dec
tTypeAdjAngAzm_RelPKt = ('std1', dParFAdj_RelPKt, 'dec')# std1 / lin         // // inc / dec
tTypeAdjAngAzm_LenZw = ('std1', dParFAdj_LenZw, 'inc')  # std1 / logF        // // inc / dec
tTypeAdjAngAzm_AgeZw = ('std1', dParFAdj_AgeZw, 'inc')  # std1 / logF        // // inc / dec
tTypeAdjAngAzm_AgeBm = ('std1', dParFAdj_AgeBm, 'inc')  # std1 / logF        // // inc / dec
tTypeAdjPrPKs_VertZ = ('linA', dParFAdj_VertZ, 'inc')   # std1 / linA / cosA // // inc / dec
tTypeAdjPrPKs_RelPZw = ('linB', dParFAdj_RelPZw, 'dec') # std1 / linA / sinA // // inc / dec
tTypeAdjPrPKs_RelPKt = ('linA', dParFAdj_RelPKt, 'dec') # std1 / lin         // // inc / dec
tTypeAdjPrPKs_LenZw = ('std1', dParFAdj_LenZw, 'inc')   # std1 / logF        // // inc / dec
tTypeAdjPrPKs_AgeZw = ('logF', dParFAdj_AgeZw, 'inc')   # std1 / logF        // // inc / dec
tTypeAdjPrPKs_AgeBm = ('std1', dParFAdj_AgeBm, 'inc')   # std1 / logF        // // inc / dec
tTypeAdjPrPZw_VertZ = ('linA', dParFAdj_VertZ, 'inc')   # std1 / linA / cosA // // inc / dec
tTypeAdjPrPZw_RelPZw = ('linB', dParFAdj_RelPZw, 'dec') # std1 / linA / sinA // // inc / dec
tTypeAdjPrPZw_RelPKt = ('linA', dParFAdj_RelPKt, 'dec') # std1 / lin         // // inc / dec
tTypeAdjPrPZw_LenZw = ('std1', dParFAdj_LenZw, 'inc')   # std1 / logF        // // inc / dec
tTypeAdjPrPZw_AgeZw = ('logF', dParFAdj_AgeZw, 'inc')   # std1 / logF        // // inc / dec
tTypeAdjPrPZw_AgeBm = ('std1', dParFAdj_AgeBm, 'inc')   # std1 / logF        // // inc / dec

# other variables --------------------------------------------------------------
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

# plot variables ---------------------------------------------------------------
fMarkSzKt = 1.0         # mult. factor for "Knoten" marker size (0.5 / 1.5)
fMarkSzBl = 4.0         # mult. factor for "Blatt" marker size
wdEdgeKt = 0.1          # marker edge width for "Knoten"
wdEdgeBl = 0.1          # marker edge width for "Blatt"

# ------------------------------------------------------------------------------
dBndAr = {'NKZw': dBndAr_NKZw,
          'NKKt': dBndAr_NKKt}

dCtWt = {'NKZw': dCtWt_NKZw,
         'NKKt': dCtWt_NKKt,
         'LenZw': dCtWt_LenZw,
         'AngPol': dCtWt_AngPol,
         'AngAzm': dCtWt_AngAzm,
         'PrPKs': dCtWt_PrPKs,
         'PrPZw': dCtWt_PrPZw}

dNumNKZw_VertZ = {0: {'s': tNumNKZw_s_VertZ_A0[dDist['NKZw']],
                      'v': tNumNKZw_v_VertZ_A0[dDist['NKZw']],
                      'w': tNumNKZw_w_VertZ_A0[dDist['NKZw']],
                      'x': tNumNKZw_x_VertZ_A0[dDist['NKZw']]},
                  1: {'s': tNumNKZw_s_VertZ_A1[dDist['NKZw']],
                      'v': tNumNKZw_v_VertZ_A1[dDist['NKZw']],
                      'w': tNumNKZw_w_VertZ_A1[dDist['NKZw']],
                      'x': tNumNKZw_x_VertZ_A1[dDist['NKZw']]},
                  2: {'s': tNumNKZw_s_VertZ_A2[dDist['NKZw']],
                      'v': tNumNKZw_v_VertZ_A2[dDist['NKZw']],
                      'w': tNumNKZw_w_VertZ_A2[dDist['NKZw']],
                      'x': tNumNKZw_x_VertZ_A2[dDist['NKZw']]},
                  3: {'s': tNumNKZw_s_VertZ_A3[dDist['NKZw']],
                      'v': tNumNKZw_v_VertZ_A3[dDist['NKZw']],
                      'w': tNumNKZw_w_VertZ_A3[dDist['NKZw']],
                      'x': tNumNKZw_x_VertZ_A3[dDist['NKZw']]},
                  4: {'s': tNumNKZw_s_VertZ_A4[dDist['NKZw']],
                      'v': tNumNKZw_v_VertZ_A4[dDist['NKZw']],
                      'w': tNumNKZw_w_VertZ_A4[dDist['NKZw']],
                      'x': tNumNKZw_x_VertZ_A4[dDist['NKZw']]},
                  5: {'s': tNumNKZw_s_VertZ_A5[dDist['NKZw']],
                      'v': tNumNKZw_v_VertZ_A5[dDist['NKZw']],
                      'w': tNumNKZw_w_VertZ_A5[dDist['NKZw']],
                      'x': tNumNKZw_x_VertZ_A5[dDist['NKZw']]}}
dNumNKZw_RelPZw = {0: {'s': tNumNKZw_s_RelPZw_A0[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPZw_A0[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPZw_A0[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPZw_A0[dDist['NKZw']]},
                   1: {'s': tNumNKZw_s_RelPZw_A1[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPZw_A1[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPZw_A1[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPZw_A1[dDist['NKZw']]},
                   2: {'s': tNumNKZw_s_RelPZw_A2[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPZw_A2[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPZw_A2[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPZw_A2[dDist['NKZw']]},
                   3: {'s': tNumNKZw_s_RelPZw_A3[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPZw_A3[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPZw_A3[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPZw_A3[dDist['NKZw']]},
                   4: {'s': tNumNKZw_s_RelPZw_A4[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPZw_A4[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPZw_A4[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPZw_A4[dDist['NKZw']]},
                   5: {'s': tNumNKZw_s_RelPZw_A5[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPZw_A5[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPZw_A5[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPZw_A5[dDist['NKZw']]}}
dNumNKZw_RelPKt = {0: {'s': tNumNKZw_s_RelPKt_A0[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPKt_A0[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPKt_A0[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPKt_A0[dDist['NKZw']]},
                   1: {'s': tNumNKZw_s_RelPKt_A1[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPKt_A1[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPKt_A1[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPKt_A1[dDist['NKZw']]},
                   2: {'s': tNumNKZw_s_RelPKt_A2[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPKt_A2[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPKt_A2[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPKt_A2[dDist['NKZw']]},
                   3: {'s': tNumNKZw_s_RelPKt_A3[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPKt_A3[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPKt_A3[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPKt_A3[dDist['NKZw']]},
                   4: {'s': tNumNKZw_s_RelPKt_A4[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPKt_A4[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPKt_A4[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPKt_A4[dDist['NKZw']]},
                   5: {'s': tNumNKZw_s_RelPKt_A5[dDist['NKZw']],
                       'v': tNumNKZw_v_RelPKt_A5[dDist['NKZw']],
                       'w': tNumNKZw_w_RelPKt_A5[dDist['NKZw']],
                       'x': tNumNKZw_x_RelPKt_A5[dDist['NKZw']]}}
dNumNKZw_LenZw = {0: {'s': tNumNKZw_s_LenZw_A0[dDist['NKZw']],
                      'v': tNumNKZw_v_LenZw_A0[dDist['NKZw']],
                      'w': tNumNKZw_w_LenZw_A0[dDist['NKZw']],
                      'x': tNumNKZw_x_LenZw_A0[dDist['NKZw']]}}
dNumNKZw_AgeZw = {0: {'s': tNumNKZw_s_AgeZw_A0[dDist['NKZw']],
                      'v': tNumNKZw_v_AgeZw_A0[dDist['NKZw']],
                      'w': tNumNKZw_w_AgeZw_A0[dDist['NKZw']],
                      'x': tNumNKZw_x_AgeZw_A0[dDist['NKZw']]}}
dNumNKZw_AgeBm = {0: {'s': tNumNKZw_s_AgeBm_A0[dDist['NKZw']],
                      'v': tNumNKZw_v_AgeBm_A0[dDist['NKZw']],
                      'w': tNumNKZw_w_AgeBm_A0[dDist['NKZw']],
                      'x': tNumNKZw_x_AgeBm_A0[dDist['NKZw']]}}
dNumNKZw = {'VertZ': dNumNKZw_VertZ,
            'RelPZw': dNumNKZw_RelPZw,
            'RelPKt': dNumNKZw_RelPKt,
            'LenZw': dNumNKZw_LenZw,
            'AgeZw': dNumNKZw_AgeZw,
            'AgeBm': dNumNKZw_AgeBm}

dNumNKKt_VertZ = {0: {'s': tNumNKKt_s_VertZ_A0[dDist['NKKt']],
                      'v': tNumNKKt_v_VertZ_A0[dDist['NKKt']],
                      'w': tNumNKKt_w_VertZ_A0[dDist['NKKt']],
                      'x': tNumNKKt_x_VertZ_A0[dDist['NKKt']]},
                  1: {'s': tNumNKKt_s_VertZ_A1[dDist['NKKt']],
                      'v': tNumNKKt_v_VertZ_A1[dDist['NKKt']],
                      'w': tNumNKKt_w_VertZ_A1[dDist['NKKt']],
                      'x': tNumNKKt_x_VertZ_A1[dDist['NKKt']]},
                  2: {'s': tNumNKKt_s_VertZ_A2[dDist['NKKt']],
                      'v': tNumNKKt_v_VertZ_A2[dDist['NKKt']],
                      'w': tNumNKKt_w_VertZ_A2[dDist['NKKt']],
                      'x': tNumNKKt_x_VertZ_A2[dDist['NKKt']]},
                  3: {'s': tNumNKKt_s_VertZ_A3[dDist['NKKt']],
                      'v': tNumNKKt_v_VertZ_A3[dDist['NKKt']],
                      'w': tNumNKKt_w_VertZ_A3[dDist['NKKt']],
                      'x': tNumNKKt_x_VertZ_A3[dDist['NKKt']]},
                  4: {'s': tNumNKKt_s_VertZ_A4[dDist['NKKt']],
                      'v': tNumNKKt_v_VertZ_A4[dDist['NKKt']],
                      'w': tNumNKKt_w_VertZ_A4[dDist['NKKt']],
                      'x': tNumNKKt_x_VertZ_A4[dDist['NKKt']]},
                  5: {'s': tNumNKKt_s_VertZ_A5[dDist['NKKt']],
                      'v': tNumNKKt_v_VertZ_A5[dDist['NKKt']],
                      'w': tNumNKKt_w_VertZ_A5[dDist['NKKt']],
                      'x': tNumNKKt_x_VertZ_A5[dDist['NKKt']]}}
dNumNKKt_RelPZw = {0: {'s': tNumNKKt_s_RelPZw_A0[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPZw_A0[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPZw_A0[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPZw_A0[dDist['NKKt']]},
                   1: {'s': tNumNKKt_s_RelPZw_A1[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPZw_A1[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPZw_A1[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPZw_A1[dDist['NKKt']]},
                   2: {'s': tNumNKKt_s_RelPZw_A2[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPZw_A2[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPZw_A2[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPZw_A2[dDist['NKKt']]},
                   3: {'s': tNumNKKt_s_RelPZw_A3[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPZw_A3[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPZw_A3[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPZw_A3[dDist['NKKt']]},
                   4: {'s': tNumNKKt_s_RelPZw_A4[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPZw_A4[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPZw_A4[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPZw_A4[dDist['NKKt']]},
                   5: {'s': tNumNKKt_s_RelPZw_A5[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPZw_A5[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPZw_A5[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPZw_A5[dDist['NKKt']]}}
dNumNKKt_RelPKt = {0: {'s': tNumNKKt_s_RelPKt_A0[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPKt_A0[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPKt_A0[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPKt_A0[dDist['NKKt']]},
                   1: {'s': tNumNKKt_s_RelPKt_A1[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPKt_A1[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPKt_A1[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPKt_A1[dDist['NKKt']]},
                   2: {'s': tNumNKKt_s_RelPKt_A2[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPKt_A2[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPKt_A2[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPKt_A2[dDist['NKKt']]},
                   3: {'s': tNumNKKt_s_RelPKt_A3[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPKt_A3[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPKt_A3[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPKt_A3[dDist['NKKt']]},
                   4: {'s': tNumNKKt_s_RelPKt_A4[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPKt_A4[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPKt_A4[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPKt_A4[dDist['NKKt']]},
                   5: {'s': tNumNKKt_s_RelPKt_A5[dDist['NKKt']],
                       'v': tNumNKKt_v_RelPKt_A5[dDist['NKKt']],
                       'w': tNumNKKt_w_RelPKt_A5[dDist['NKKt']],
                       'x': tNumNKKt_x_RelPKt_A5[dDist['NKKt']]}}
dNumNKKt_LenZw = {0: {'s': tNumNKKt_s_LenZw_A0[dDist['NKKt']],
                      'v': tNumNKKt_v_LenZw_A0[dDist['NKKt']],
                      'w': tNumNKKt_w_LenZw_A0[dDist['NKKt']],
                      'x': tNumNKKt_x_LenZw_A0[dDist['NKKt']]}}
dNumNKKt_AgeZw = {0: {'s': tNumNKKt_s_AgeZw_A0[dDist['NKKt']],
                      'v': tNumNKKt_v_AgeZw_A0[dDist['NKKt']],
                      'w': tNumNKKt_w_AgeZw_A0[dDist['NKKt']],
                      'x': tNumNKKt_x_AgeZw_A0[dDist['NKKt']]}}
dNumNKKt_AgeBm = {0: {'s': tNumNKKt_s_AgeBm_A0[dDist['NKKt']],
                      'v': tNumNKKt_v_AgeBm_A0[dDist['NKKt']],
                      'w': tNumNKKt_w_AgeBm_A0[dDist['NKKt']],
                      'x': tNumNKKt_x_AgeBm_A0[dDist['NKKt']]}}
dNumNKKt = {'VertZ': dNumNKKt_VertZ,
            'RelPZw': dNumNKKt_RelPZw,
            'RelPKt': dNumNKKt_RelPKt,
            'LenZw': dNumNKKt_LenZw,
            'AgeZw': dNumNKKt_AgeZw,
            'AgeBm': dNumNKKt_AgeBm}

dFctPKZw = {0: {'s': tFctPKZw_s_0,      # 0 corresponds to the normal distr.
                'v': tFctPKZw_v_0,
                'w': tFctPKZw_w_0,
                'x': tFctPKZw_x_0},
            1: {'s': tFctPKZw_s_1,      # dep. on number of "Knoten" on "Zweig"
                'v': tFctPKZw_v_1,
                'w': tFctPKZw_w_1,
                'x': tFctPKZw_x_1},
            2: {'s': tFctPKZw_s_2,
                'v': tFctPKZw_v_2,
                'w': tFctPKZw_w_2,
                'x': tFctPKZw_x_2},
            3: {'s': tFctPKZw_s_3,
                'v': tFctPKZw_v_3,
                'w': tFctPKZw_w_3,
                'x': tFctPKZw_x_3},
            4: {'s': tFctPKZw_s_4,
                'v': tFctPKZw_v_4,
                'w': tFctPKZw_w_4,
                'x': tFctPKZw_x_4}}

dFctPEZw = {'s': tFctPEZw_s,
            'v': tFctPEZw_v,
            'w': tFctPEZw_w,
            'x': tFctPEZw_x}

dLengthZw = {0: {'s': tLengthZw_s_0,    # 0 corresponds to the normal distr.
                 'v': tLengthZw_v_0,
                 'w': tLengthZw_w_0,
                 'x': tLengthZw_x_0},
             1: {'s': tLengthZw_s_1,    # dep. on number of "Knoten" on "Zweig"
                 'v': tLengthZw_v_1,
                 'w': tLengthZw_w_1,
                 'x': tLengthZw_x_1},
             2: {'s': tLengthZw_s_2,
                 'v': tLengthZw_v_2,
                 'w': tLengthZw_w_2,
                 'x': tLengthZw_x_2},
             3: {'s': tLengthZw_s_3,
                 'v': tLengthZw_v_3,
                 'w': tLengthZw_w_3,
                 'x': tLengthZw_x_3},
             4: {'s': tLengthZw_s_4,
                 'v': tLengthZw_v_4,
                 'w': tLengthZw_w_4,
                 'x': tLengthZw_x_4}}

dAngKPlr = {1: {'k': tAngKPlr_k_1,
                's': tAngKPlr_s_1,
                'v': tAngKPlr_v_1,
                'w': tAngKPlr_w_1,
                'x': tAngKPlr_x_1},
            2: {'s': tAngKPlr_s_2,
                'v': tAngKPlr_v_2,
                'w': tAngKPlr_w_2,
                'x': tAngKPlr_x_2},
            3: {'s': tAngKPlr_s_3,
                'v': tAngKPlr_v_3,
                'w': tAngKPlr_w_3,
                'x': tAngKPlr_x_3},
            4: {'s': tAngKPlr_s_4,
                'v': tAngKPlr_v_4,
                'w': tAngKPlr_w_4,
                'x': tAngKPlr_x_4},
            5: {'s': tAngKPlr_s_5,
                'v': tAngKPlr_v_5,
                'w': tAngKPlr_w_5,
                'x': tAngKPlr_x_5},
            6: {'s': tAngKPlr_s_6,
                'v': tAngKPlr_v_6,
                'w': tAngKPlr_w_6,
                'x': tAngKPlr_x_6}}
dAngKPlr_E = {1: {'k': tAngKPlr_k_1_E,
                  's': tAngKPlr_s_1_E,
                  'v': tAngKPlr_v_1_E,
                  'w': tAngKPlr_w_1_E,
                  'x': tAngKPlr_x_1_E},
              2: {'s': tAngKPlr_s_2_E,
                  'v': tAngKPlr_v_2_E,
                  'w': tAngKPlr_w_2_E,
                  'x': tAngKPlr_x_2_E},
              3: {'s': tAngKPlr_s_3_E,
                  'v': tAngKPlr_v_3_E,
                  'w': tAngKPlr_w_3_E,
                  'x': tAngKPlr_x_3_E},
              4: {'s': tAngKPlr_s_4_E,
                  'v': tAngKPlr_v_4_E,
                  'w': tAngKPlr_w_4_E,
                  'x': tAngKPlr_x_4_E},
              5: {'s': tAngKPlr_s_5_E,
                  'v': tAngKPlr_v_5_E,
                  'w': tAngKPlr_w_5_E,
                  'x': tAngKPlr_x_5_E},
              6: {'s': tAngKPlr_s_6_E,
                  'v': tAngKPlr_v_6_E,
                  'w': tAngKPlr_w_6_E,
                  'x': tAngKPlr_x_6_E}}

dAngKAzm = {1: {'k': tAngKAzm_k_1,
                's': tAngKAzm_s_1,
                'v': tAngKAzm_v_1,
                'w': tAngKAzm_w_1,
                'x': tAngKAzm_x_1},
            2: {'s': tAngKAzm_s_2,
                'v': tAngKAzm_v_2,
                'w': tAngKAzm_w_2,
                'x': tAngKAzm_x_2},
            3: {'s': tAngKAzm_s_3,
                'v': tAngKAzm_v_3,
                'w': tAngKAzm_w_3,
                'x': tAngKAzm_x_3},
            4: {'s': tAngKAzm_s_4,
                'v': tAngKAzm_v_4,
                'w': tAngKAzm_w_4,
                'x': tAngKAzm_x_4},
            5: {'s': tAngKAzm_s_5,
                'v': tAngKAzm_v_5,
                'w': tAngKAzm_w_5,
                'x': tAngKAzm_x_5},
            6: {'s': tAngKAzm_s_6,
                'v': tAngKAzm_v_6,
                'w': tAngKAzm_w_6,
                'x': tAngKAzm_x_6}}
dAngKAzm_E = {1: {'k': tAngKAzm_k_1_E,
                  's': tAngKAzm_s_1_E,
                  'v': tAngKAzm_v_1_E,
                  'w': tAngKAzm_w_1_E,
                  'x': tAngKAzm_x_1_E},
              2: {'s': tAngKAzm_s_2_E,
                  'v': tAngKAzm_v_2_E,
                  'w': tAngKAzm_w_2_E,
                  'x': tAngKAzm_x_2_E},
              3: {'s': tAngKAzm_s_3_E,
                  'v': tAngKAzm_v_3_E,
                  'w': tAngKAzm_w_3_E,
                  'x': tAngKAzm_x_3_E},
              4: {'s': tAngKAzm_s_4_E,
                  'v': tAngKAzm_v_4_E,
                  'w': tAngKAzm_w_4_E,
                  'x': tAngKAzm_x_4_E},
              5: {'s': tAngKAzm_s_5_E,
                  'v': tAngKAzm_v_5_E,
                  'w': tAngKAzm_w_5_E,
                  'x': tAngKAzm_x_5_E},
              6: {'s': tAngKAzm_s_6_E,
                  'v': tAngKAzm_v_6_E,
                  'w': tAngKAzm_w_6_E,
                  'x': tAngKAzm_x_6_E}}

dOffsAngAzm = {1: {'k': tOffsAngAzm_k_1,
                   's': tOffsAngAzm_s_1,
                   'v': tOffsAngAzm_v_1,
                   'w': tOffsAngAzm_w_1,
                   'x': tOffsAngAzm_x_1},
               2: {'s': tOffsAngAzm_s_2,
                   'v': tOffsAngAzm_v_2,
                   'w': tOffsAngAzm_w_2,
                   'x': tOffsAngAzm_x_2},
               3: {'s': tOffsAngAzm_s_3,
                   'v': tOffsAngAzm_v_3,
                   'w': tOffsAngAzm_w_3,
                   'x': tOffsAngAzm_x_3},
               4: {'s': tOffsAngAzm_s_4,
                   'v': tOffsAngAzm_v_4,
                   'w': tOffsAngAzm_w_4,
                   'x': tOffsAngAzm_x_4},
               5: {'s': tOffsAngAzm_s_5,
                   'v': tOffsAngAzm_v_5,
                   'w': tOffsAngAzm_w_5,
                   'x': tOffsAngAzm_x_5},
               6: {'s': tOffsAngAzm_s_6,
                   'v': tOffsAngAzm_v_6,
                   'w': tOffsAngAzm_w_6,
                   'x': tOffsAngAzm_x_6}}

dAngEPlr = {'s': tAngEPlr_s,
            'v': tAngEPlr_v,
            'w': tAngEPlr_w,
            'x': tAngEPlr_x}

dAngEAzm = {'s': tAngEAzm_s,
            'v': tAngEAzm_v,
            'w': tAngEAzm_w,
            'x': tAngEAzm_x}

dAngChDr = {'s': tAngChDr_s,
            'v': tAngChDr_v,
            'w': tAngChDr_w,
            'x': tAngChDr_x}

dPrpPinch_Knospe = {'k': tPrpPinch_Knospe_k,
                    's': tPrpPinch_Knospe_s,
                    'v': tPrpPinch_Knospe_v,
                    'w': tPrpPinch_Knospe_w,
                    'x': tPrpPinch_Knospe_x}

dPrpPinch_Zweig = {'k': tPrpPinch_Zweig_k,
                   's': tPrpPinch_Zweig_s,
                   'v': tPrpPinch_Zweig_v,
                   'w': tPrpPinch_Zweig_w,
                   'x': tPrpPinch_Zweig_x}

dAdjLenZw_VertZ = {'s': tAdjLenZw_VertZ_s,
                   'v': tAdjLenZw_VertZ_v,
                   'w': tAdjLenZw_VertZ_w,
                   'x': tAdjLenZw_VertZ_x}

dAdjLenZw_RelPZw = {'s': tAdjLenZw_RelPZw_s,
                    'v': tAdjLenZw_RelPZw_v,
                    'w': tAdjLenZw_RelPZw_w,
                    'x': tAdjLenZw_RelPZw_x}

dAdjLenZw_RelPKt = {'s': tAdjLenZw_RelPKt_s,
                    'v': tAdjLenZw_RelPKt_v,
                    'w': tAdjLenZw_RelPKt_w,
                    'x': tAdjLenZw_RelPKt_x}

dAdjLenZw_LenZw = {'s': tAdjLenZw_LenZw_s,
                   'v': tAdjLenZw_LenZw_v,
                   'w': tAdjLenZw_LenZw_w,
                   'x': tAdjLenZw_LenZw_x}

dAdjLenZw_AgeZw = {'s': tAdjLenZw_AgeZw_s,
                   'v': tAdjLenZw_AgeZw_v,
                   'w': tAdjLenZw_AgeZw_w,
                   'x': tAdjLenZw_AgeZw_x}

dAdjLenZw_AgeBm = {'s': tAdjLenZw_AgeBm_s,
                   'v': tAdjLenZw_AgeBm_v,
                   'w': tAdjLenZw_AgeBm_w,
                   'x': tAdjLenZw_AgeBm_x}

dAdjAngPol_VertZ = {'s': tAdjAngPol_VertZ_s,
                    'v': tAdjAngPol_VertZ_v,
                    'w': tAdjAngPol_VertZ_w,
                    'x': tAdjAngPol_VertZ_x}

dAdjAngPol_RelPZw = {'s': tAdjAngPol_RelPZw_s,
                     'v': tAdjAngPol_RelPZw_v,
                     'w': tAdjAngPol_RelPZw_w,
                     'x': tAdjAngPol_RelPZw_x}

dAdjAngPol_RelPKt = {'s': tAdjAngPol_RelPKt_s,
                     'v': tAdjAngPol_RelPKt_v,
                     'w': tAdjAngPol_RelPKt_w,
                     'x': tAdjAngPol_RelPKt_x}

dAdjAngPol_LenZw = {'s': tAdjAngPol_LenZw_s,
                    'v': tAdjAngPol_LenZw_v,
                    'w': tAdjAngPol_LenZw_w,
                    'x': tAdjAngPol_LenZw_x}

dAdjAngPol_AgeZw = {'s': tAdjAngPol_AgeZw_s,
                    'v': tAdjAngPol_AgeZw_v,
                    'w': tAdjAngPol_AgeZw_w,
                    'x': tAdjAngPol_AgeZw_x}

dAdjAngPol_AgeBm = {'s': tAdjAngPol_AgeBm_s,
                    'v': tAdjAngPol_AgeBm_v,
                    'w': tAdjAngPol_AgeBm_w,
                    'x': tAdjAngPol_AgeBm_x}

dAdjAngAzm_VertZ = {'s': tAdjAngAzm_VertZ_s,
                    'v': tAdjAngAzm_VertZ_v,
                    'w': tAdjAngAzm_VertZ_w,
                    'x': tAdjAngAzm_VertZ_x}

dAdjAngAzm_RelPZw = {'s': tAdjAngAzm_RelPZw_s,
                     'v': tAdjAngAzm_RelPZw_v,
                     'w': tAdjAngAzm_RelPZw_w,
                     'x': tAdjAngAzm_RelPZw_x}

dAdjAngAzm_RelPKt = {'s': tAdjAngAzm_RelPKt_s,
                     'v': tAdjAngAzm_RelPKt_v,
                     'w': tAdjAngAzm_RelPKt_w,
                     'x': tAdjAngAzm_RelPKt_x}

dAdjAngAzm_LenZw = {'s': tAdjAngAzm_LenZw_s,
                    'v': tAdjAngAzm_LenZw_v,
                    'w': tAdjAngAzm_LenZw_w,
                    'x': tAdjAngAzm_LenZw_x}

dAdjAngAzm_AgeZw = {'s': tAdjAngAzm_AgeZw_s,
                    'v': tAdjAngAzm_AgeZw_v,
                    'w': tAdjAngAzm_AgeZw_w,
                    'x': tAdjAngAzm_AgeZw_x}

dAdjAngAzm_AgeBm = {'s': tAdjAngAzm_AgeBm_s,
                    'v': tAdjAngAzm_AgeBm_v,
                    'w': tAdjAngAzm_AgeBm_w,
                    'x': tAdjAngAzm_AgeBm_x}

dAdjPrPKs_VertZ = {'s': tAdjPrPKs_VertZ_s,
                   'v': tAdjPrPKs_VertZ_v,
                   'w': tAdjPrPKs_VertZ_w,
                   'x': tAdjPrPKs_VertZ_x}

dAdjPrPKs_RelPZw = {'s': tAdjPrPKs_RelPZw_s,
                    'v': tAdjPrPKs_RelPZw_v,
                    'w': tAdjPrPKs_RelPZw_w,
                    'x': tAdjPrPKs_RelPZw_x}

dAdjPrPKs_RelPKt = {'s': tAdjPrPKs_RelPKt_s,
                    'v': tAdjPrPKs_RelPKt_v,
                    'w': tAdjPrPKs_RelPKt_w,
                    'x': tAdjPrPKs_RelPKt_x}

dAdjPrPKs_LenZw = {'s': tAdjPrPKs_LenZw_s,
                   'v': tAdjPrPKs_LenZw_v,
                   'w': tAdjPrPKs_LenZw_w,
                   'x': tAdjPrPKs_LenZw_x}

dAdjPrPKs_AgeZw = {'s': tAdjPrPKs_AgeZw_s,
                   'v': tAdjPrPKs_AgeZw_v,
                   'w': tAdjPrPKs_AgeZw_w,
                   'x': tAdjPrPKs_AgeZw_x}

dAdjPrPKs_AgeBm = {'s': tAdjPrPKs_AgeBm_s,
                   'v': tAdjPrPKs_AgeBm_v,
                   'w': tAdjPrPKs_AgeBm_w,
                   'x': tAdjPrPKs_AgeBm_x}

dAdjPrPZw_VertZ = {'s': tAdjPrPZw_VertZ_s,
                   'v': tAdjPrPZw_VertZ_v,
                   'w': tAdjPrPZw_VertZ_w,
                   'x': tAdjPrPZw_VertZ_x}

dAdjPrPZw_RelPZw = {'s': tAdjPrPZw_RelPZw_s,
                    'v': tAdjPrPZw_RelPZw_v,
                    'w': tAdjPrPZw_RelPZw_w,
                    'x': tAdjPrPZw_RelPZw_x}

dAdjPrPZw_RelPKt = {'s': tAdjPrPZw_RelPKt_s,
                    'v': tAdjPrPZw_RelPKt_v,
                    'w': tAdjPrPZw_RelPKt_w,
                    'x': tAdjPrPZw_RelPKt_x}

dAdjPrPZw_LenZw = {'s': tAdjPrPZw_LenZw_s,
                   'v': tAdjPrPZw_LenZw_v,
                   'w': tAdjPrPZw_LenZw_w,
                   'x': tAdjPrPZw_LenZw_x}

dAdjPrPZw_AgeZw = {'s': tAdjPrPZw_AgeZw_s,
                   'v': tAdjPrPZw_AgeZw_v,
                   'w': tAdjPrPZw_AgeZw_w,
                   'x': tAdjPrPZw_AgeZw_x}

dAdjPrPZw_AgeBm = {'s': tAdjPrPZw_AgeBm_s,
                   'v': tAdjPrPZw_AgeBm_v,
                   'w': tAdjPrPZw_AgeBm_w,
                   'x': tAdjPrPZw_AgeBm_x}

dMMFAdj = {'LenZw': {'VertZ': dAdjLenZw_VertZ,
                     'RelPZw': dAdjLenZw_RelPZw,
                     'RelPKt': dAdjLenZw_RelPKt,
                     'LenZw': dAdjLenZw_LenZw,
                     'AgeZw': dAdjLenZw_AgeZw,
                     'AgeBm': dAdjLenZw_AgeBm},
           'AngPol': {'VertZ': dAdjAngPol_VertZ,
                      'RelPZw': dAdjAngPol_RelPZw,
                      'RelPKt': dAdjAngPol_RelPKt,
                      'LenZw': dAdjAngPol_LenZw,
                      'AgeZw': dAdjAngPol_AgeZw,
                      'AgeBm': dAdjAngPol_AgeBm},
           'AngAzm': {'VertZ': dAdjAngAzm_VertZ,
                      'RelPZw': dAdjAngAzm_RelPZw,
                      'RelPKt': dAdjAngAzm_RelPKt,
                      'LenZw': dAdjAngAzm_LenZw,
                      'AgeZw': dAdjAngAzm_AgeZw,
                      'AgeBm': dAdjAngAzm_AgeBm},
           'PrPKs': {'VertZ': dAdjPrPKs_VertZ,
                     'RelPZw': dAdjPrPKs_RelPZw,
                     'RelPKt': dAdjPrPKs_RelPKt,
                     'LenZw': dAdjPrPKs_LenZw,
                     'AgeZw': dAdjPrPKs_AgeZw,
                     'AgeBm': dAdjPrPKs_AgeBm},
           'PrPZw': {'VertZ': dAdjPrPZw_VertZ,
                     'RelPZw': dAdjPrPZw_RelPZw,
                     'RelPKt': dAdjPrPZw_RelPKt,
                     'LenZw': dAdjPrPZw_LenZw,
                     'AgeZw': dAdjPrPZw_AgeZw,
                     'AgeBm': dAdjPrPZw_AgeBm}}

dTypeAdj = {'LenZw': {'VertZ': tTypeAdjLenZw_VertZ,
                      'RelPZw': tTypeAdjLenZw_RelPZw,
                      'RelPKt': tTypeAdjLenZw_RelPKt,
                      'LenZw': tTypeAdjLenZw_LenZw,
                      'AgeZw': tTypeAdjLenZw_AgeZw,
                      'AgeBm': tTypeAdjLenZw_AgeBm},
            'AngPol': {'VertZ': tTypeAdjAngPol_VertZ,
                       'RelPZw': tTypeAdjAngPol_RelPZw,
                       'RelPKt': tTypeAdjAngPol_RelPKt,
                       'LenZw': tTypeAdjAngPol_LenZw,
                       'AgeZw': tTypeAdjAngPol_AgeZw,
                       'AgeBm': tTypeAdjAngPol_AgeBm},
            'AngAzm': {'VertZ': tTypeAdjAngAzm_VertZ,
                       'RelPZw': tTypeAdjAngAzm_RelPZw,
                       'RelPKt': tTypeAdjAngAzm_RelPKt,
                       'LenZw': tTypeAdjAngAzm_LenZw,
                       'AgeZw': tTypeAdjAngAzm_AgeZw,
                       'AgeBm': tTypeAdjAngAzm_AgeBm},
            'PrPKs': {'VertZ': tTypeAdjPrPKs_VertZ,
                      'RelPZw': tTypeAdjPrPKs_RelPZw,
                      'RelPKt': tTypeAdjPrPKs_RelPKt,
                      'LenZw': tTypeAdjPrPKs_LenZw,
                      'AgeZw': tTypeAdjPrPKs_AgeZw,
                      'AgeBm': tTypeAdjPrPKs_AgeBm},
            'PrPZw': {'VertZ': tTypeAdjPrPZw_VertZ,
                      'RelPZw': tTypeAdjPrPZw_RelPZw,
                      'RelPKt': tTypeAdjPrPZw_RelPKt,
                      'LenZw': tTypeAdjPrPZw_LenZw,
                      'AgeZw': tTypeAdjPrPZw_AgeZw,
                      'AgeBm': tTypeAdjPrPZw_AgeBm}}

dPrpPinch = {'Knospe': dPrpPinch_Knospe,
             'Zweig': dPrpPinch_Zweig}
# ------------------------------------------------------------------------------

# posZweig:
#    'Sl': Schoessling
#    'T00': T00 type
#    'T01': T01 type
#    'T02': T02 type
#    'T03': T03 type
#    'S': Simple type
#    'L': Leeuwenberg model type
#    'W': Wirtel type 
#    'vSTD': Standard-Baum (vertical v-Zweig) type
#    'wSTD': Standard-Baum (w-Zweig) type
#    'xSTD': Standard-Baum (x-Zweig) type

# --- assertions regarding input -----------------------------------------------
assert len(dAngKPlr) == len(dAngKAzm)
for k1 in dAngKPlr:
    assert k1 in dAngKAzm
    assert len(dAngKPlr[k1]) == len(dAngKAzm[k1])
    for k2 in dAngKPlr[k1]:
        assert k2 in dAngKAzm[k1]
        assert len(dAngKPlr[k1][k2]) == len(dAngKAzm[k1][k2])
assert len(dAngKPlr_E) == len(dAngKAzm_E)
for k1 in dAngKPlr_E:
    assert k1 in dAngKAzm_E
    assert len(dAngKPlr_E[k1]) == len(dAngKAzm_E[k1])
    for k2 in dAngKPlr_E[k1]:
        assert k2 in dAngKAzm_E[k1]
        assert len(dAngKPlr_E[k1][k2]) == len(dAngKAzm_E[k1][k2])

# --- create input dictionary --------------------------------------------------
dictInpB = {# general
            'strType': strType,
            'strNSpec': strNSpec,
            # positions of "Zweig" and "Blatt"
            'dPosZweig': dPosZweig,
            'dPosBlatt': dPosBlatt,
            # dictionary specifying the distributions used
            'dDist': dDist,
            # dictionaries containing boundaries and category weights
            'dBndAr': dBndAr,
            'dCtWt': dCtWt,
            # MORPHOLOGICAL DATA
            'dNumNKZw': dNumNKZw,
            'dNumNKKt': dNumNKKt,
            'dLengthZw': dLengthZw,
            'dFctPKZw': dFctPKZw,
            'dFctPEZw': dFctPEZw,
            'dAngKPlr': dAngKPlr,
            'dAngKPlr_E': dAngKPlr_E,
            'dAngKAzm': dAngKAzm,
            'dAngKAzm_E': dAngKAzm_E,
            'dOffsAngAzm': dOffsAngAzm,
            'dAngEPlr': dAngEPlr,
            'dAngEAzm': dAngEAzm,
            'dAngChDr': dAngChDr,
            'dPrpPinch': dPrpPinch,
            # "Blatt" data
            'fAngBlattPlr': fAngBlattPlr,
            'lenBlatt': lenBlatt,
            'widBlatt': widBlatt,
            'shapeBlatt': shapeBlatt,
            # direction dependent adjustment factors: [min , max]
            'dMMFAdj': dMMFAdj,
            # direction dependent function types
            'dTypeAdj': dTypeAdj,
            # other variables
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
            'tInvestK_NBlt': tInvestK_NBlt,
            # plot variables
            'fMarkSzKt': fMarkSzKt,
            'fMarkSzBl': fMarkSzBl,
            'wdEdgeKt': wdEdgeKt,
            'wdEdgeBl': wdEdgeBl}
################################################################################
