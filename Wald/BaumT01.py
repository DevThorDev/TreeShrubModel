# ### INPUT - BAUM #############################################################
from Konstanten import (L_MX_1, L_MX_2, L_MX_3, L_MX_4, L_MX_5, L_MX_6,
                        EPS, E12, E06)
# general ----------------------------------------------------------------------
strType = 'FantasieBaum'
strNSpec = 'Fantasiebaumartiger Verzweiger'

# positions of "Zweig" and "Blatt" ---------------------------------------------
dPosZweig = {'k': 'Keim',       # Keim
             's': 'Sl',         # 'Sl': Schoessling
             'v': 'vSTD',       # all vertical branches
             'w': 'wSTD',       # side branches from vertical ones
             'x': 'xSTD'}       # all other branches
dPosBlatt = {'k': 'Keim',       # Keim
             's': 'Sl',         # 'Sl': Schoessling
             'v': 'k',          # 'w': dispers, 'k': decussiert
             'w': 'k',
             'x': 'k'}
offsAngAzm = 90                 # offset of azim. angle for next "Knoten" [deg]

# dictionary specifying the distributions used ---------------------------------
dDist = {'NKZw': 0,     # 0: 'normal' / 1: 'custom'
         'NKKt': 1,     # 0: 'normal' / 1: 'custom'
         'FctPKZw': 0,  # 0: 'normal'
         'LenZw': 0,    # 0: 'normal'
         'AngPol': 0,   # 0: 'normal'
         'AngPol': 0}   # 0: 'normal'

# dictionaries containing boundaries and category weights ----------------------
# dictionary of the boundaries for number of new "Knoten" on a "Zweig"
dBndAr_NKZw = {'VertZ': [10, 45, 80, 100, 135],     # [deg]
               'RelPZw': [10, 45, 80, 100, 135],    # [deg]
               'RelPKt': [0.1, 0.5, 0.9, 1. - E12]} # []

# dictionary of the boundaries for number of new "Knospen" on a "Knoten"
dBndAr_NKKt = {'VertZ': [10, 45, 80, 100, 135],     # [deg]
               'RelPZw': [10, 45, 80, 100, 135],    # [deg]
               'RelPKt': [0.1, 0.5, 0.9, 1. - E12]} # []

# dictionary of the category weights for number of new "Knoten" on a "Zweig"
dCtWt_NKZw = {'VertZ': 0.2,     # []
              'RelPZw': 0.3,    # []
              'RelPKt': 0.5}    # []

# dictionary of the category weights for number of new "Knoten" on a "Zweig"
dCtWt_NKKt = {'VertZ': 0.1,     # []
              'RelPZw': 0.6,    # []
              'RelPKt': 0.3}    # []

# dictionary of the category weights for the length of a new "Zweig"
dCtWt_LenZw = {'VertZ': 0.3,    # []
               'RelPZw': 0.3,   # []
               'RelPKt': 0.4}   # []

# dictionary of the category weights for the polar angle of a new "Zweig"
dCtWt_AngPol = {'VertZ': 0.4,   # []
                'RelPZw': 0.1,  # []
                'RelPKt': 0.5}  # []

# dictionary of the category weights for the polar angle of a new "Zweig"
dCtWt_AngAzm = {'VertZ': 0.2,   # []
                'RelPZw': 0.2,  # []
                'RelPKt': 0.6}  # []

# MORPHOLOGICAL DATA -----------------------------------------------------------

(numNKZwAv_VertZ_A0, numNKZwSD_VertZ_A0) = (15.0, 5.0)
(numNKZwAv_VertZ_A1, numNKZwSD_VertZ_A1) = (14.0, 4.5)
(numNKZwAv_VertZ_A2, numNKZwSD_VertZ_A2) = (13.0, 4.0)
(numNKZwAv_VertZ_A3, numNKZwSD_VertZ_A3) = (12.0, 3.5)
(numNKZwAv_VertZ_A4, numNKZwSD_VertZ_A4) = (11.0, 3.0)
(numNKZwAv_VertZ_A5, numNKZwSD_VertZ_A5) = (10.0, 2.5)

(numNKZwAv_RelPZw_A0, numNKZwSD_RelPZw_A0) = (7.5, 2.0)
(numNKZwAv_RelPZw_A1, numNKZwSD_RelPZw_A1) = (9.0, 2.5)
(numNKZwAv_RelPZw_A2, numNKZwSD_RelPZw_A2) = (10.5, 3.0)
(numNKZwAv_RelPZw_A3, numNKZwSD_RelPZw_A3) = (12.0, 3.5)
(numNKZwAv_RelPZw_A4, numNKZwSD_RelPZw_A4) = (13.5, 4.0)
(numNKZwAv_RelPZw_A5, numNKZwSD_RelPZw_A5) = (15.0, 5.0)

(numNKZwAv_RelPKt_A0, numNKZwSD_RelPKt_A0) = (15.0, 4.0)
(numNKZwAv_RelPKt_A1, numNKZwSD_RelPKt_A1) = (14.5, 3.5)
(numNKZwAv_RelPKt_A2, numNKZwSD_RelPKt_A2) = (14.0, 3.0)
(numNKZwAv_RelPKt_A3, numNKZwSD_RelPKt_A3) = (13.5, 2.5)
(numNKZwAv_RelPKt_A4, numNKZwSD_RelPKt_A4) = (numNKZwAv_RelPKt_A3, numNKZwSD_RelPKt_A3)
(numNKZwAv_RelPKt_A5, numNKZwSD_RelPKt_A5) = (numNKZwAv_RelPKt_A3, numNKZwSD_RelPKt_A3)

(numNKKtAv_VertZ_A0, numNKKtSD_VertZ_A0) = (2.2, 0.5)
(numNKKtAv_VertZ_A1, numNKKtSD_VertZ_A1) = (2.2, 0.5)
(numNKKtAv_VertZ_A2, numNKKtSD_VertZ_A2) = (2.2, 0.5)
(numNKKtAv_VertZ_A3, numNKKtSD_VertZ_A3) = (2.2, 0.5)
(numNKKtAv_VertZ_A4, numNKKtSD_VertZ_A4) = (2.2, 0.5)
(numNKKtAv_VertZ_A5, numNKKtSD_VertZ_A5) = (2.2, 0.5)

(numNKKtAv_RelPZw_A0, numNKKtSD_RelPZw_A0) = (2.2, 0.5)
(numNKKtAv_RelPZw_A1, numNKKtSD_RelPZw_A1) = (2.2, 0.5)
(numNKKtAv_RelPZw_A2, numNKKtSD_RelPZw_A2) = (2.2, 0.5)
(numNKKtAv_RelPZw_A3, numNKKtSD_RelPZw_A3) = (2.2, 0.5)
(numNKKtAv_RelPZw_A4, numNKKtSD_RelPZw_A4) = (2.2, 0.5)
(numNKKtAv_RelPZw_A5, numNKKtSD_RelPZw_A5) = (2.2, 0.5)

(numNKKtAv_RelPKt_A0, numNKKtSD_RelPKt_A0) = (2.2, 0.5)
(numNKKtAv_RelPKt_A1, numNKKtSD_RelPKt_A1) = (2.2, 0.5)
(numNKKtAv_RelPKt_A2, numNKKtSD_RelPKt_A2) = (2.2, 0.5)
(numNKKtAv_RelPKt_A3, numNKKtSD_RelPKt_A3) = (2.2, 0.5)
(numNKKtAv_RelPKt_A4, numNKKtSD_RelPKt_A4) = (numNKKtAv_RelPKt_A3, numNKKtSD_RelPKt_A3)
(numNKKtAv_RelPKt_A5, numNKKtSD_RelPKt_A5) = (numNKKtAv_RelPKt_A3, numNKKtSD_RelPKt_A3)

# number of new "Knoten" on a "Zweig"
# ([list of number of new "Knoten"], [list of probabilities or weights])
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

# number of new "Knospen" on a "Knoten"
# ([list of number of new "Knospen"], [list of probabilities or weights])
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

# length factors of positions of new "Knoten" on a "Zweig"
# dimension: []
# (mean, SD)
tFctPKZw_s_0 = (1, 0.1)     # 0 corresponds to the normal distribution
tFctPKZw_v_0 = (1, 0.1)     # SD as a proportion of the resp. mean value
tFctPKZw_w_0 = (1, 0.1)
tFctPKZw_x_0 = (1, 0.1)

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
# dimension: []
# ([list of means], [list of SDs])
tFctPEZw_s = ([], [])
tFctPEZw_v = ([], [])
tFctPEZw_w = ([], [])
tFctPEZw_x = ([], [])

# "Zweig" lengths, depending on the number of "Knoten" on parent "Zweig"
# dimension: [cm]
# ([max, min], SD)
tLengthZw_s_0 = ([12, 3], 0.1)    # 0 corresponds to the normal distribution
tLengthZw_v_0 = ([25, 19], 0.1)   # SD as a proportion of the resp. value
tLengthZw_w_0 = ([20, 15.5], 0.1)
tLengthZw_x_0 = ([15, 12], 0.1)

# (mean, SD)
tLengthZw_s_1 = (12, 2.0)
tLengthZw_v_1 = (25, 4.5)
tLengthZw_w_1 = (20, 3.5)
tLengthZw_x_1 = (15, 2.5)

tLengthZw_s_2 = (6, 0.6)
tLengthZw_v_2 = (23, 4.2)
tLengthZw_w_2 = (18.5, 3.2)
tLengthZw_x_2 = (14, 2.3)

tLengthZw_s_3 = (4, 0.4)
tLengthZw_v_3 = (21, 3.9)
tLengthZw_w_3 = (17, 2.9)
tLengthZw_x_3 = (13, 2.2)

tLengthZw_s_4 = (3, 0.3)
tLengthZw_v_4 = (19, 3.6)
tLengthZw_w_4 = (15.5, 2.7)
tLengthZw_x_4 = (12, 2.1)

# polar angles of new "Knospen" on a "Knoten"
# ([list of means], [list of SDs])
# dimension: [deg]
# polar angles for "Knoten" not at the end of parent "Zweig"
tAngKPlr_k_1 = ([0], [0.0])
tAngKPlr_s_1 = ([55], [1.0])
tAngKPlr_v_1 = ([45], [4.0])
tAngKPlr_w_1 = ([35], [4.0])
tAngKPlr_x_1 = ([25], [3.0])

tAngKPlr_s_2 = ([40, 65], [4.0, 9.0])
tAngKPlr_v_2 = ([31, 55], [4.0, 8.0])
tAngKPlr_w_2 = ([22, 55], [4.0, 7.0])
tAngKPlr_x_2 = ([15, 44], [3.0, 4.5])

tAngKPlr_s_3 = ([35, 52, 68], [4.0, 3.5, 7.0])
tAngKPlr_v_3 = ([30, 45, 60], [4.0, 3.0, 9.0])
tAngKPlr_w_3 = ([26, 39, 48], [3.0, 4.0, 8.0])
tAngKPlr_x_3 = ([19, 37, 43], [3.0, 4.0, 8.0])

tAngKPlr_s_4 = ([29, 45, 64, 79], [2.0, 2.5, 5.0, 7.5])
tAngKPlr_v_4 = ([26, 43, 61, 73], [4.0, 3.0, 5.0, 8.5])
tAngKPlr_w_4 = ([24, 42, 56, 68], [3.0, 4.0, 7.5, 8.5])
tAngKPlr_x_4 = ([17, 28, 49, 67], [3.0, 5.0, 8.0, 9.0])

tAngKPlr_s_5 = ([37, 46, 53, 61, 75], [2.0, 2.5, 4.0, 4.5, 7.5])
tAngKPlr_v_5 = ([31, 45, 54, 60, 78], [4.0, 3.0, 5.0, 5.0, 8.5])
tAngKPlr_w_5 = ([24, 44, 64, 72, 81], [3.0, 4.0, 7.5, 8.0, 8.5])
tAngKPlr_x_5 = ([17, 32, 48, 59, 79], [3.0, 4.0, 5.0, 8.0, 9.0])

tAngKPlr_s_6 = ([21, 37, 46, 53, 61, 75], [2.0, 2.0, 2.5, 4.0, 4.5, 7.5])
tAngKPlr_v_6 = ([19, 31, 45, 54, 60, 78], [4.0, 4.0, 3.0, 5.0, 5.0, 8.5])
tAngKPlr_w_6 = ([16, 24, 44, 64, 72, 81], [3.0, 3.0, 4.0, 7.5, 8.0, 8.5])
tAngKPlr_x_6 = ([13, 17, 32, 48, 59, 79], [3.0, 3.0, 4.0, 5.0, 8.0, 9.0])

# polar angles for "Knoten" at the end of parent "Zweig"
tAngKPlr_k_1_E = tAngKPlr_k_1
tAngKPlr_s_1_E = ([0], [1.0])
tAngKPlr_v_1_E = ([0], [4.0])
tAngKPlr_w_1_E = ([0], [4.0])
tAngKPlr_x_1_E = ([0], [3.0])

tAngKPlr_s_2_E = ([0, 65], [4.0, 9.0])
tAngKPlr_v_2_E = ([0, 55], [4.0, 8.0])
tAngKPlr_w_2_E = ([0, 55], [4.0, 7.0])
tAngKPlr_x_2_E = ([0, 44], [3.0, 4.5])

tAngKPlr_s_3_E = ([0, 25, 68], [4.0, 3.5, 7.0])
tAngKPlr_v_3_E = ([0, 15, 60], [4.0, 3.0, 9.0])
tAngKPlr_w_3_E = ([0, 39, 48], [3.0, 4.0, 8.0])
tAngKPlr_x_3_E = ([0, 37, 43], [3.0, 4.0, 8.0])

tAngKPlr_s_4_E = ([0, 23, 44, 59], [2.0, 2.5, 5.0, 7.5])
tAngKPlr_v_4_E = ([0, 12, 41, 63], [4.0, 3.0, 5.0, 8.5])
tAngKPlr_w_4_E = ([0, 42, 56, 68], [3.0, 4.0, 7.5, 8.5])
tAngKPlr_x_4_E = ([0, 28, 49, 67], [3.0, 5.0, 8.0, 9.0])

tAngKPlr_s_5_E = ([0, 18, 39, 54, 75], [2.0, 2.5, 4.0, 4.5, 7.5])
tAngKPlr_v_5_E = ([0, 12, 41, 59, 78], [4.0, 3.0, 5.0, 5.0, 8.5])
tAngKPlr_w_5_E = ([0, 44, 64, 72, 81], [3.0, 4.0, 7.5, 8.0, 8.5])
tAngKPlr_x_5_E = ([0, 32, 48, 59, 79], [3.0, 4.0, 5.0, 8.0, 9.0])

tAngKPlr_s_6_E = ([0, 18, 29, 39, 54, 75], [2.0, 2.5, 2.5, 4.0, 4.5, 7.5])
tAngKPlr_v_6_E = ([0, 12, 26, 41, 59, 78], [4.0, 3.0, 3.0, 5.0, 5.0, 8.5])
tAngKPlr_w_6_E = ([0, 44, 54, 64, 72, 81], [3.0, 4.0, 4.0, 7.5, 8.0, 8.5])
tAngKPlr_x_6_E = ([0, 32, 37, 48, 59, 79], [3.0, 4.0, 4.0, 5.0, 8.0, 9.0])

# azimuth angles of new "Knospen" on a "Knoten"
# ([list of means], [list of SDs])
# dimension: [deg]
# azimuth angles for "Knoten" not at the end of parent "Zweig"
tAngKAzm_k_1 = ([0], [0.0])
tAngKAzm_s_1 = ([0], [1.0])
tAngKAzm_v_1 = ([0], [4.0])
tAngKAzm_w_1 = ([180], [4.0])
tAngKAzm_x_1 = ([180], [3.0])

tAngKAzm_s_2 = ([0, 180], [2.0, 2.0])
tAngKAzm_v_2 = ([0, 180], [4.0, 4.0])
tAngKAzm_w_2 = ([225, 315], [7.0, 7.0])
tAngKAzm_x_2 = ([225, 315], [7.0, 7.0])

tAngKAzm_s_3 = ([0, 120, 240], [2.0, 2.0, 2.0])
tAngKAzm_v_3 = ([0, 120, 240], [4.0, 4.0, 4.0])
tAngKAzm_w_3 = ([50, 180, 310], [7.0, 7.0, 7.0])
tAngKAzm_x_3 = ([70, 180, 290], [9.0, 9.0, 9.0])

tAngKAzm_s_4 = ([0, 90, 180, 270], [2.0, 2.0, 2.0, 2.0])
tAngKAzm_v_4 = ([0, 90, 180, 270], [4.0, 4.0, 4.0, 4.0])
tAngKAzm_w_4 = ([35, 125, 235, 325], [5.0, 5.0, 5.0, 5.0])
tAngKAzm_x_4 = ([55, 145, 215, 305], [5.0, 5.0, 5.0, 5.0])

tAngKAzm_s_5 = ([0, 72, 144, 216, 288], [2.0, 2.0, 2.0, 2.0, 2.0])
tAngKAzm_v_5 = ([0, 72, 144, 216, 288], [4.0, 4.0, 4.0, 4.0, 4.0])
tAngKAzm_w_5 = ([36, 108, 180, 252, 324], [5.0, 5.0, 5.0, 5.0, 5.0])
tAngKAzm_x_5 = ([36, 108, 180, 252, 324], [5.0, 5.0, 5.0, 5.0, 5.0])

tAngKAzm_s_6 = ([0, 60, 120, 180, 240, 300], [2.0, 2.0, 2.0, 2.0, 2.0, 2.0])
tAngKAzm_v_6 = ([0, 60, 120, 180, 240, 300], [4.0, 4.0, 4.0, 4.0, 4.0, 4.0])
tAngKAzm_w_6 = ([36, 84, 156, 204, 276, 324], [5.0, 5.0, 5.0, 5.0, 5.0, 5.0])
tAngKAzm_x_6 = ([36, 84, 156, 204, 276, 324], [5.0, 5.0, 5.0, 5.0, 5.0, 5.0])

# azimuth angles for "Knoten" at the end of parent "Zweig"
tAngKAzm_k_1_E = tAngKAzm_k_1
tAngKAzm_s_1_E = ([0], [1.0])
tAngKAzm_v_1_E = ([0], [4.0])
tAngKAzm_w_1_E = ([0], [4.0])
tAngKAzm_x_1_E = ([0], [3.0])

tAngKAzm_s_2_E = ([0, 0], [2.0, 2.0])
tAngKAzm_v_2_E = ([0, 0], [4.0, 4.0])
tAngKAzm_w_2_E = ([0, 180], [7.0, 7.0])
tAngKAzm_x_2_E = ([0, 180], [7.0, 7.0])

tAngKAzm_s_3_E = ([0, 120, 240], [2.0, 2.0, 2.0])
tAngKAzm_v_3_E = ([0, 120, 240], [4.0, 4.0, 4.0])
tAngKAzm_w_3_E = ([0, 105, 255], [7.0, 7.0, 7.0])
tAngKAzm_x_3_E = ([0, 110, 250], [9.0, 9.0, 9.0])

tAngKAzm_s_4_E = ([0, 90, 180, 270], [2.0, 2.0, 2.0, 2.0])
tAngKAzm_v_4_E = ([0, 90, 180, 270], [4.0, 4.0, 4.0, 4.0])
tAngKAzm_w_4_E = ([0, 95, 180, 265], [5.0, 5.0, 5.0, 5.0])
tAngKAzm_x_4_E = ([0, 100, 180, 260], [5.0, 5.0, 5.0, 5.0])

tAngKAzm_s_5_E = ([0, 0, 90, 180, 270], [2.0, 2.0, 2.0, 2.0, 2.0])
tAngKAzm_v_5_E = ([0, 0, 90, 180, 270], [4.0, 4.0, 4.0, 4.0, 4.0])
tAngKAzm_w_5_E = ([0, 35, 125, 235, 325], [5.0, 5.0, 5.0, 5.0, 5.0])
tAngKAzm_x_5_E = ([0, 55, 145, 215, 305], [5.0, 5.0, 5.0, 5.0, 5.0])

tAngKAzm_s_6_E = ([0, 0, 72, 144, 216, 288], [2.0, 2.0, 2.0, 2.0, 2.0, 2.0])
tAngKAzm_v_6_E = ([0, 0, 72, 144, 216, 288], [4.0, 4.0, 4.0, 4.0, 4.0, 4.0])
tAngKAzm_w_6_E = ([0, 30, 144, 174, 258, 318], [5.0, 5.0, 5.0, 5.0, 5.0, 5.0])
tAngKAzm_x_6_E = ([0, 30, 144, 174, 258, 318], [5.0, 5.0, 5.0, 5.0, 5.0, 5.0])

# polar angles of edges on new "Zweig"
# ([list of means], [list of SDs])
# dimension: [deg]
tAngEPlr_s = ([], [])
tAngEPlr_v = ([], [])
tAngEPlr_w = ([], [])
tAngEPlr_x = ([], [])

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
tAdjLenZw_VertZ_w = ([0.1, 1.0], [0.002, 0.0])
tAdjLenZw_VertZ_x = ([0.2, 0.8], [0.002, 0.0])

# adjustments of "Zweig" length - depending on dir. relative to parent "Zweig"
tAdjLenZw_RelPZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_RelPZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_RelPZw_w = ([0.1, 1.0], [0.002, 0.0])
tAdjLenZw_RelPZw_x = ([0.2, 0.8], [0.002, 0.0])

# adjustments of "Zweig" length - depending on pos. relative to parent "Zweig"
tAdjLenZw_RelPKt_s = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_RelPKt_v = ([1.0, 1.0], [0.0, 0.0])
tAdjLenZw_RelPKt_w = ([0.1, 1.0], [0.002, 0.0])
tAdjLenZw_RelPKt_x = ([0.3, 1.0], [0.002, 0.0])

# adjustments of polar angle of "Knospe" - depending on dir. relative to vUz
tAdjAngPol_VertZ_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_VertZ_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_VertZ_w = ([0.1, 1.0], [0.002, 0.0])
tAdjAngPol_VertZ_x = ([0.2, 0.8], [0.002, 0.0])

# adjustments of polar angle of "Knospe" - depending on dir. relative to parent "Zweig"
tAdjAngPol_RelPZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_RelPZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_RelPZw_w = ([0.1, 1.0], [0.002, 0.0])
tAdjAngPol_RelPZw_x = ([0.2, 0.8], [0.002, 0.0])

# adjustments of polar angle of "Knospe" - depending on pos. relative to parent "Zweig"
tAdjAngPol_RelPKt_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_RelPKt_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngPol_RelPKt_w = ([0.1, 1.0], [0.002, 0.0])
tAdjAngPol_RelPKt_x = ([0.3, 1.0], [0.002, 0.0])

# adjustments of azimuthal angle of "Knospe" - depending on dir. relative to vUz
tAdjAngAzm_VertZ_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_VertZ_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_VertZ_w = ([0.1, 1.0], [0.002, 0.0])
tAdjAngAzm_VertZ_x = ([0.2, 0.8], [0.002, 0.0])

# adjustments of azimuthal angle of "Knospe" - depending on dir. relative to parent "Zweig"
tAdjAngAzm_RelPZw_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_RelPZw_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_RelPZw_w = ([0.1, 1.0], [0.002, 0.0])
tAdjAngAzm_RelPZw_x = ([0.2, 0.8], [0.002, 0.0])

# adjustments of azimuthal angle of "Knospe" - depending on pos. relative to parent "Zweig"
tAdjAngAzm_RelPKt_s = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_RelPKt_v = ([1.0, 1.0], [0.0, 0.0])
tAdjAngAzm_RelPKt_w = ([0.1, 1.0], [0.002, 0.0])
tAdjAngAzm_RelPKt_x = ([0.3, 1.0], [0.002, 0.0])

# direction dependent function types -------------------------------------------
tTypeAdjLenZw_VertZ = ('linA', '-', 'dec')   # std1 / linA / cosA // '-' // inc / dec
tTypeAdjLenZw_RelPZw = ('sinA', '-', 'inc')  # std1 / linA / sinA // '-' // inc / dec
tTypeAdjLenZw_RelPKt = ('lin', '-', 'inc')   # std1 / lin        // '-' // inc / dec
tTypeAdjAngPol_VertZ = ('linA', '-', 'inc')  # std1 / linA / cosA // '-' // inc / dec
tTypeAdjAngPol_RelPZw = ('sinA', '-', 'dec') # std1 / linA / sinA // '-' // inc / dec
tTypeAdjAngPol_RelPKt = ('lin', '-', 'dec')  # std1 / lin    // '-' // inc / dec
tTypeAdjAngAzm_VertZ = ('linA', '-', 'dec')  # std1 / linA / cosA // '-' // inc / dec
tTypeAdjAngAzm_RelPZw = ('sinA', '-', 'inc') # std1 / linA / sinA // '-' // inc / dec
tTypeAdjAngAzm_RelPKt = ('lin', '-', 'dec')  # std1 / lin        // '-' // inc / dec

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
fMarkSzKt = 1.5         # mult. factor for "Knoten" marker size
fMarkSzBl = 2.0         # mult. factor for "Blatt" marker size
wdthMarkEdgeBl = 0.1    # marker edge width for "Blatt"

# ------------------------------------------------------------------------------
dBndAr = {'NKZw': dBndAr_NKZw,
          'NKKt': dBndAr_NKKt}

dCtWt = {'NKZw': dCtWt_NKZw,
         'NKKt': dCtWt_NKKt,
         'LenZw': dCtWt_LenZw,
         'AngPol': dCtWt_AngPol,
         'AngAzm': dCtWt_AngAzm}

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
dNumNKZw = {'VertZ': dNumNKZw_VertZ,
            'RelPZw': dNumNKZw_RelPZw,
            'RelPKt': dNumNKZw_RelPKt}

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
dNumNKKt = {'VertZ': dNumNKKt_VertZ,
            'RelPZw': dNumNKKt_RelPZw,
            'RelPKt': dNumNKKt_RelPKt}

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

dAngEPlr = {'s': tAngEPlr_s,
            'v': tAngEPlr_v,
            'w': tAngEPlr_w,
            'x': tAngEPlr_x}

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

dMMFAdj = {'LenZw': {'VertZ': dAdjLenZw_VertZ,
                     'RelPZw': dAdjLenZw_RelPZw,
                     'RelPKt': dAdjLenZw_RelPKt},
           'AngPol': {'VertZ': dAdjAngPol_VertZ,
                      'RelPZw': dAdjAngPol_RelPZw,
                      'RelPKt': dAdjAngPol_RelPKt},
           'AngAzm': {'VertZ': dAdjAngAzm_VertZ,
                      'RelPZw': dAdjAngAzm_RelPZw,
                      'RelPKt': dAdjAngAzm_RelPKt}}

dTypeAdj = {'LenZw': {'VertZ': tTypeAdjLenZw_VertZ,
                      'RelPZw': tTypeAdjLenZw_RelPZw,
                      'RelPKt': tTypeAdjLenZw_RelPKt},
            'AngPol': {'VertZ': tTypeAdjAngPol_VertZ, 
                       'RelPZw': tTypeAdjAngPol_RelPZw,
                       'RelPKt': tTypeAdjAngPol_RelPKt},
            'AngAzm': {'VertZ': tTypeAdjAngAzm_VertZ, 
                       'RelPZw': tTypeAdjAngAzm_RelPZw,
                       'RelPKt': tTypeAdjAngAzm_RelPKt}}
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
            'offsAngAzm': offsAngAzm,
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
            'dAngEPlr': dAngEPlr,
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
            'wdthMarkEdgeBl': wdthMarkEdgeBl}
################################################################################
