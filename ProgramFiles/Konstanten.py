# ### KONSTANTEN ###############################################################
import numpy as np
# --- names of directories and files -------------------------------------------
NF_BAUM_PRE = 'BaumT'
# --- other constants ----------------------------------------------------------
M_DETER = 'Deterministic'
M_STOCH = 'Stochastic'

V0_2D = np.zeros(2)
V0_3D = np.zeros(3)
P0 = np.zeros(3)
UV_X_3D = np.array((1., 0., 0.))
UV_Y_3D = np.array((0., 1., 0.))
UV_Z_3D = np.array((0., 0., 1.))
BASIS_R3 = [UV_X_3D, UV_Y_3D, UV_Z_3D]

L_MX_1 = list(range(1, 2))
L_MX_2 = list(range(1, 3))
L_MX_3 = list(range(1, 4))
L_MX_4 = list(range(1, 5))
L_MX_5 = list(range(1, 6))
L_MX_6 = list(range(1, 7))

L_TP_NUM = [float, int, np.float64, np.float32, np.float16, np.int64, np.int32,
            np.int16]

R04 = 4
R06 = 6
R12 = 12
R14 = 14

EPS = 10**-R14
E12 = 10**-R12
E06 = 10**-R06
################################################################################
