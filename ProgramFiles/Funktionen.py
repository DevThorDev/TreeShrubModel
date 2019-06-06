################################################################################
# --- FUNKTIONEN ---------------------------------------------------------------
################################################################################
import os, math, random
import numpy as np

from Konstanten import (M_DETER, M_STOCH, V0_2D, V0_3D, BASIS_R3, L_TP_NUM,
                        R04, R06, R12, R14, EPS)
################################################################################

def createDir(pF):
    if not os.path.isdir(pF):
        os.mkdir(pF)

def joinToPath(nF = 'Dummy.txt', lD = []):
    if len(lD) > 0:
        pFull = lD[0]
        for cD in lD[1:]:
            pFull = os.path.join(pFull, cD)
        createDir(pFull)
        return os.path.join(pFull, nF)
    else:
        return nF

def seedRNG(cMode):
    if cMode == M_STOCH:
        random.seed()

def addLElToList(lMain, lToAdd, avoidDup = True):
    if avoidDup:
        for cEl in lToAdd:
            if cEl not in lMain:
                lMain.append(cEl)
    else:
        lMain += lToAdd

def adToDictCount(cD, cK, ctInc = 1):
    if cK in cD:
        cD[cK] += ctInc
    else:
        cD[cK] = ctInc

def addToDictL(cD, cK, cE):
    if cK in cD:
        cD[cK].append(cE)
    else:
        cD[cK] = [cE]

def fillDictMinMax(cD, lCoord):
    for cC, cV in cD.items():
        cI, cMin, cMax = cV
        if cMin != None:
            cD[cC][1] = min(cMin, lCoord[cI])
        else:
            cD[cC][1] = lCoord[cI]
        if cMax != None:
            cD[cC][2] = max(cMax, lCoord[cI])
        else:
            cD[cC][2] = lCoord[cI]

def geo_mean_overflow(iterable):
    a = np.log(iterable)
    return np.exp(a.sum()/len(a))

def weightedGeoMean(arrVals, arrWts):
    arrVals, arrWts = np.array(arrVals), np.array(arrWts)
    a = np.log(arrVals)
    a *= arrWts
    return np.exp(a.sum()/arrWts.sum())

def normaliseV(vC):
    normV, vN = np.linalg.norm(vC), np.array([vC[k] for k in range(len(vC))])
    if abs(normV) >= EPS:
        vN = np.array([vC[k]/normV for k in range(len(vC))])
    return vN

def normaliseLV(lVO):
    lVN = [V0_3D]*len(lVO)
    for cI, cV in enumerate(lVO):
        lVN[cI] = normaliseV(cV)
    return lVN

def valuesTooSmallError(z, cLen, vD = V0_3D, minZ = EPS/2, minLen = 0):
    isErr = False
    if (z < minZ and vD[2] < 0) or cLen <= minLen:
        if z < minZ and vD[2] < 0:
            print('ERROR: z-coordinate of start point is too small!')
        if cLen <= minLen:
            print('ERROR: length is not positive!')
        print('z-coordinate:', z, '- length:', cLen, '- vDir:', vD)
        isErr = True
    return isErr

def avoidNegZVal(posS, vD, lenPrev):
    assert len(posS) == 3 and len(vD) == 3
    if valuesTooSmallError(posS[2], lenPrev, vD):
        print('...occurred in "avoidNegZVal" (BEGIN).')
    assert (posS[2] >= EPS/2 or vD[2] > 0) and lenPrev > 0
    posE, lenCur = posS + vD*lenPrev, lenPrev
    if posE[2] < EPS:
        posE[2] = EPS
        vSE = posE - posS
        vD, lenCur = normaliseV(vSE), np.linalg.norm(vSE)
    return posE, vD, lenCur

def constructSeg(lDrS, lPSE, lLnS, n, lInpV, lFDsE, lAnEP, lAnEA):
    [pRC, pSC, vDC, lenZ, cSPsZw, cAnChDr, cTol] = lInpV
    if valuesTooSmallError(pSC[2], lenZ, vDC):
        print('...occurred in "constructSeg" (BEGIN).')
    vDRotA = np.array([cC for cC in vDC])
    vDRotA = rotatePt3D(vDRotA, findRotAxis(vDRotA, cSPsZw, cTol), cAnChDr)
    for iSeg in range(n + 1):
        if iSeg < n:
            lenC = lenZ*(lFDsE[iSeg] - pRC)
            if lFDsE[iSeg] <= pRC or lenC <= 0:
                print('ERROR: Rel. length of segment', iSeg, 'too small!')
                print('Rel. length of segment', iSeg, ':', lFDsE[iSeg])
                print('cur. len.:', lenC, '- lenZ =', lenZ, '- pRC =', pRC)
            assert lFDsE[iSeg] > pRC
            pRC = lFDsE[iSeg]
            pSC, vDC, lLnS[iSeg] = avoidNegZVal(pSC, vDC, lenC)
            lPSE[iSeg], lDrS[iSeg] = np.array([cSC for cSC in pSC]), vDC
            # calculate the "next" vDC
            vDC = rotatePt3D(vDC, findRotAxis(vDC, cSPsZw, cTol), lAnEP[iSeg])
            vDC = rotatePt3D(vDC, vDRotA, lAnEA[iSeg])
        else:
            lenC = lenZ*(1. - pRC)
            assert lenC > 0
            lPSE[iSeg], lDrS[iSeg], lLnS[iSeg] = avoidNegZVal(pSC, vDC, lenC)

def getRPsSK(cFDsK):
    if isSpecNum(cFDsK, 1, EPS):
        cRPsSK = 'End'
    elif isSpecNum(cFDsK, 0, EPS):
        cRPsSK = 'Start'
    else:
        cRPsSK = 'Mid'
    return cRPsSK

def getInfoKt(lVDKn, lCKn, k, vDsK, lInpV, lDrS, lLnS):
    [pSt, iSSt, cTDs, cTLn, incTLn] = lInpV
    for iS in range(iSSt, len(lDrS)):
        if incTLn:
            cTLn += lLnS[iS]
        if vDsK[k] <= cTLn:
            lCKn[k], lDrS[iS], _ = avoidNegZVal(pSt, lDrS[iS], vDsK[k] - cTDs)
            if valuesTooSmallError(lCKn[k][2], vDsK[k] - cTDs, vDsK[k]):
                print('...occurred in "getInfoKt".')
            lVDKn[k] = lDrS[iS]
            incTLn = False
            break
        else:
            pSt += lLnS[iS]*lDrS[iS]
            cTDs += lLnS[iS]
            incTLn = True
    iSSt = iS
    return [pSt, iSSt, cTDs, cTLn, incTLn]

def getAvDist(lLDist):
    if len(lLDist) > 0:
        for cL in lLDist[1:]:
            assert len(cL) == len(lLDist[0])
        lAvDist = [0. for _ in range(len(lLDist[0]))]
        for k in range(len(lLDist[0])):
            lAvDist[k] = np.mean([cL[k] for cL in lLDist])
        if np.abs(1. - sum(lAvDist)) < EPS:
            return lAvDist
        else:
            print('ERROR: Distribution probabilities do not sum to one.')
            print('Distribution:', lAvDist, '- sum:', sum(lAvDist))
            return [cPr/sum(lAvDist) for cPr in lAvDist]
    else:
        return []

def getIMaxList(cL):
    maxL = max(cL)
    return min([i for i, cE in enumerate(cL) if cE == maxL])

def cutMinMax(cL, tMnMx = (0, -1, False)):
    assert len(tMnMx) == 3
    if not tMnMx[2]:
        if type(cL) in L_TP_NUM:
            if tMnMx[0]>= 0:    # a valid cutoff value --> do lower cutoff
                cL = max(cL, tMnMx[0])
            if tMnMx[1]>= 0:    # a valid cutoff value --> do upper cutoff
                cL = min(cL, tMnMx[1])
        else:
            if tMnMx[0]>= 0:    # a valid cutoff value --> do lower cutoff
                for k in range(len(cL)):
                    cL[k] = max(cL[k], tMnMx[0])
            if tMnMx[1]>= 0:    # a valid cutoff value --> do upper cutoff
                for k in range(len(cL)):
                    cL[k] = min(cL[k], tMnMx[1])
    return cL

def drawLPr(tVals, cMode = M_DETER, tMnMx = (0, -1, False), fAd = 1,
            convInt = True):
    assert len(tVals) == 2      # ((list of) means, (list of) SDs)
    if cMode == M_DETER:
        if type(tVals[0]) == list:
            assert type(tVals[1]) == list and len(tVals[1]) == len(tVals[0])
            iMaxPr = getIMaxList(tVals[1])
            if convInt:
                return int(round(cutMinMax(tVals[0][iMaxPr]*fAd, tMnMx)))
            else:
                return float(cutMinMax(tVals[0][iMaxPr]*fAd, tMnMx))
        else:
            assert type(tVals[0]) in L_TP_NUM
            if convInt:
                return int(round(cutMinMax(tVals[0]*fAd, tMnMx)))
            else:
                return float(cutMinMax(tVals[0]*fAd, tMnMx))
    elif cMode == M_STOCH:
        if type(tVals[0]) == list and type(tVals[1]) == list:
            assert len(tVals[0]) == len(tVals[1])
            assert min(tVals[1]) >= 0.
            lProb = [tVals[1][k]/sum(tVals[1]) for k in range(len(tVals[1]))]
            cV = np.random.choice(tVals[0], p = lProb)*fAd
            if convInt:
                return int(round(cutMinMax(cV, tMnMx)))
            else:
                return float(cutMinMax(cV, tMnMx))
        else:
            assert (type(tVals[0]) in L_TP_NUM and type(tVals[1]) in L_TP_NUM)
            if convInt:
                return int(round(cutMinMax(tVals[0]*fAd, tMnMx)))
            else:
                return float(cutMinMax(tVals[0]*fAd, tMnMx))

def drawDst(tVals, cMode = M_DETER, tMnMx = (0, -1, False), fAd = 1,
            convInt = False, dType = 'Norm'):
    assert len(tVals) == 2 and len(tMnMx) == 3  # (mean(s), SD(s))
    if dType == 'Norm':
        if cMode == M_DETER:
            if type(tVals[0]) == list:
                cL = cutMinMax([x*fAd for x in tVals[0]], tMnMx)
                if convInt:
                    return sorted([int(round(cE)) for cE in cL])
                else:
                    return sorted([float(cE) for cE in cL])
            else:
                assert type(tVals[0]) in L_TP_NUM
                if convInt:
                    return int(round(cutMinMax(tVals[0]*fAd, tMnMx)))
                else:
                    return float(cutMinMax(tVals[0]*fAd, tMnMx))
        elif cMode == M_STOCH:
            if type(tVals[0]) == list and type(tVals[1]) == list:
                assert len(tVals[0]) == len(tVals[1])
                lDrVal = [0.]*len(tVals[0])
                for k in range(len(tVals[0])):
                    lDrVal[k] = random.normalvariate(tVals[0][k]*fAd,
                                                     tVals[1][k]*fAd)
                cL = cutMinMax(lDrVal, tMnMx)
                if convInt:
                    return sorted([int(round(cE)) for cE in cL])
                else:
                    return sorted([float(cE) for cE in cL])
            else:
                assert (type(tVals[0]) in L_TP_NUM and
                        type(tVals[1]) in L_TP_NUM)
                cDrVal = random.normalvariate(tVals[0]*fAd, tVals[1]*fAd)
                if convInt:
                    return int(round(cutMinMax(cDrVal, tMnMx)))
                else:
                    return float(cutMinMax(cDrVal, tMnMx))
    else:
        print('ERROR: distribution type', dType, 'not yet implemented.')
        return -1

def adjustAngPA(cAnP, cAnA, tMnMxP = (0, 180, True), tMnMxA = (0, 360, True)):
    if (tMnMxA[2] and (cAnA < tMnMxA[0] or cAnA > tMnMxA[1])):
        cAnA = cAnA%(tMnMxA[1] - tMnMxA[0]) + tMnMxA[0]
    if (tMnMxP[2] and (cAnP < tMnMxP[0] or cAnP > tMnMxP[1])):
        while cAnP < tMnMxP[0]:
            if cAnP >= tMnMxP[0] - tMnMxP[1]:
                cAnP = tMnMxP[0] - cAnP
                cAnA += (tMnMxA[1] - tMnMxA[0])/2.
                break
            cAnP += (tMnMxP[1] - tMnMxP[0])
            cAnA += (tMnMxA[1] - tMnMxA[0])/2.
        while cAnP > tMnMxP[1]:
            if cAnP <= 2*tMnMxP[1] - tMnMxP[0]:
                cAnP = 2*tMnMxP[1] - cAnP
                cAnA += (tMnMxA[1] - tMnMxA[0])/2.
                break
            cAnP -= (tMnMxP[1] - tMnMxP[0])
            cAnA += (tMnMxA[1] - tMnMxA[0])/2.
        cAnA = cAnA%(tMnMxA[1] - tMnMxA[0]) + tMnMxA[0]
    return cAnP, cAnA

def adjustAngles(lAnP, lAnA, tMnMxP = (0, 180, True), tMnMxA = (0, 360, True)):
    assert len(lAnP) == len(lAnA)
    assert tMnMxP[1] > tMnMxP[0] and tMnMxA[1] > tMnMxA[0]
    if tMnMxP[2]:
        tMnMxA = (tMnMxA[0], tMnMxA[1], True)
    for k in range(len(lAnP)):
        lAnP[k], lAnA[k] = adjustAngPA(lAnP[k], lAnA[k], tMnMxP, tMnMxA)

def drawD(dDat, dBnd, dCtWt, dInfC, sDr, cMd, tMnMx = (0, -1, False),
          drDstTp = 0):
    assert len(dBnd) == len(dInfC)
    lCtWt, lDr = [0 for _ in range(len(dBnd))], [-1 for _ in range(len(dBnd))]
    if drDstTp not in [0, 1]:
        print('ERROR: Distribution type', drDstTp, 'not yet implemented.')
        return -1
    for cI, (cK, cV) in enumerate(dInfC.items()):
        cAr = len(dBnd[cK])
        for i, cBnd in enumerate(dBnd[cK]):
            if cV < cBnd:
                cAr = i
                break
        lCtWt[cI] = dCtWt[cK]
        if drDstTp == 0:
            lDr[cI] = drawDst(dDat[cK][cAr][sDr], cMd, tMnMx, 1, True)
        elif drDstTp == 1:
            lDr[cI] = drawLPr(dDat[cK][cAr][sDr], cMd, tMnMx)
    return drawLPr((lDr, lCtWt), cMd, tMnMx)

def drawDict(dTp, dInf, dMnMx, sDDst, sVar, sDVar, sDBnd, sDCtWt, sDir, cMd):
    return drawD(dTp[sDVar], dTp[sDBnd][sVar], dTp[sDCtWt][sVar], dInf, sDir,
                 cMd, dMnMx[sVar], dTp[sDDst][sVar])

def drawVRel(dVR, cK1, cK2, cMd, tMnMx = (0, -1, False), tMnMx2 = (0, -1),
             fAd = 1, drDstTp = 0, nonNeg = True):
    if drDstTp not in [0, 1]:
        print('ERROR: Distribution type', drDstTp, 'not yet implemented.')
        return -1
    if drDstTp == 0:
        ([cMax, cMin], cSD) = dVR[drDstTp][cK2]
        if cK1 <= tMnMx2[0]:
            cVR = drawDst((cMax, cSD), cMd, tMnMx, fAd)
        else:
            cDelta = (cMax - cMin)/(tMnMx2[1] - 1)
            cVRMn = cMax - (cK1 - tMnMx2[0])*cDelta
            cVR = drawDst((cVRMn, cSD*cVRMn), cMd, tMnMx, fAd)
    elif drDstTp == 1:
        cVR = drawDst(dVR[cK1][cK2], cMd, tMnMx, fAd)
    if nonNeg and cVR < 0:
        print('ERROR: Length of new "Zweig is', cVR, '- drDstTp =', drDstTp) 
    return cVR

def drawLVRel(dVR, cK1, cK2, cMd, tMnMx = (0, -1, False), drDstTp = 0):
    if drDstTp not in [0, 1]:
        print('ERROR: Distribution type', drDstTp, 'not yet implemented.')
        return [-1]
    if drDstTp == 0:
        if cK1 <= 0:
            lVR = [1]
        else:
            lVRMn = [dVR[drDstTp][cK2][0] - k/cK1 for k in range(cK1)]
            lVRSD = [0.] + [dVR[drDstTp][cK2][1]]*(len(lVRMn) - 1)
            lVRSD = [0.] + [lVRSD[k]*lVRMn[k] for k in range(1, len(lVRMn))]
            lVR = drawDst((lVRMn, lVRSD), cMd, tMnMx)
    elif drDstTp == 1:
        lVR = drawDst(dVR[cK1][cK2], cMd, tMnMx)
    return sorted(lVR)

def convRadToDeg(angRad):
    return(angRad*180/math.pi)

def convDegToRad(angDeg):
    return(angDeg/180*math.pi)

def convPolarToCart(cLen = 1, angP = 0, angA = 0, vS = V0_3D):
    vE = np.array([vS[k] for k in range(len(vS))])
    angP, angA = convDegToRad(angP), convDegToRad(angA)
    vE[0] += cLen*math.sin(angP)*math.cos(angA)
    vE[1] += cLen*math.sin(angP)*math.sin(angA)
    vE[2] += cLen*math.cos(angP)
    return np.around(vE, R14)

def convCartToPolar(vE = V0_3D, vS = V0_3D):
    assert len(vE) == len(vS)
    vC = np.array([vE[k] - vS[k] for k in range(len(vE))])
    lEP = [math.sqrt(sum([vC[k]*vC[k] for k in range(len(vC))])), 0, 0]
    if lEP[0] > 0:                                      # lEP[0]: length
        lEP[1] = convRadToDeg(math.acos(vC[2]/lEP[0]))  # lEP[1]: ang. polar
    lEP[2] = convRadToDeg(math.atan2(vC[1], vC[0]))     # lEP[2]: ang. azimuth
    return np.around(np.array(lEP))

def convLCartToLPolar(lTE, lTS = []):
    if len(lTS) == 0:
        lTS = [V0_3D]*len(lTE)
    elif len(lTS) == 1:
        lTS = [np.array(lTS[0])]*len(lTE)
    assert len(lTE) == len(lTS)
    lTP = [V0_3D]*len(lTE)
    for iEC, vEC in enumerate(lTE):
        assert len(vEC) == 3     # x-, y- and z-coordinate
        lTP[iEC] = convCartToPolar(vEC, lTS[iEC])
    return lTP

def isSpecNum(numC, numSpec = 1, accDev = EPS):
    isNumSpec = False
    if abs(numC - numSpec) < accDev:
        isNumSpec = True
    return isNumSpec

def calcAngle2Vect3D(v1, v2, degOut = True):
    cAng = math.atan2(np.linalg.norm(np.cross(v1, v2)), np.dot(v1, v2))
    if degOut:
        cAng = convRadToDeg(cAng)
    return round(cAng, R12)

def calcAngle2Plains3D_NV(vN1, vN2, degOut = True):
    assert np.linalg.norm(vN1)*np.linalg.norm(vN2) > 0
    dP12 = np.dot(vN1, vN2)
    den = np.linalg.norm(vN1)*np.linalg.norm(vN2)
    cAng = math.acos(round(np.linalg.norm(dP12)/den, R14))
    if dP12 > 0:
        cAng = math.pi - cAng
    if degOut:
        cAng = convRadToDeg(cAng)
    return round(cAng, R12)

def calcAngle2Plains3D(lVP1, lVP2, degOut = True):
    assert len(lVP1) >= 2 and len(lVP2) >= 2
    vN1 = np.cross(lVP1[0], lVP1[1])
    vN2 = np.cross(lVP2[0], lVP2[1])
    if np.linalg.norm(vN1)*np.linalg.norm(vN2) == 0:
        if np.linalg.norm(vN1) == 0:    # "Zweig" growth in z-direction
            if np.linalg.norm(vN2) == 0:# "Knospe" growth in same direction
                return -3               # special 'angle' for this case
            else:                       # "Knospe" growth in other direction
                return -2               # special 'angle' for this case
        else:           # "Zweig" and "Knospe" growth in same (not z) direction
            return -1   # special 'angle' for this case
    else:
        return calcAngle2Plains3D_NV(vN1, vN2, degOut)

def isVertZ(vD, vZ, angTol = 0):
    assert len(vD) == len(vZ)
    isVert = True
    if calcAngle2Vect3D(vD, vZ) > angTol:
        isVert = False
    return isVert

def getSDir(sDirPrv, vDirCur, vZ, angTol = 0):
    if sDirPrv == 'k':          # "Keim"
        sDirCur = 's'           # "Schoessling"
    else:
        sDirCur = 'x'           # general "Zweig"
        if sDirPrv in ['s', 'v']:
            if isVertZ(vDirCur, vZ, angTol):
                sDirCur = 'v'   # vertical "Zweig" on main axis
            else:
                sDirCur = 'w'   # "Zweig" on main axis, not vertical
    return sDirCur

def getOneVUnit(vT, angTol = 0, lVD = BASIS_R3):
    # Here, lVD contains generally the standard basis of R^3
    assert len(lVD) == 3    # 3D (vectors of lVD form basis)
    [vX, vY, vZ] = lVD
    vD = vZ
    if isVertZ(vT, vZ, angTol):
        vD = vY
        if isVertZ(vT, vY, angTol):
            vD = vX
    return vD

def findRotAxis(cDir, cTp = 'vSTD', angTol = 0, lVDir = BASIS_R3):
    if cTp in ['Sl', 'vSTD', 'wSTD', 'xSTD', 'T00']:
        vD = getOneVUnit(cDir, angTol, lVDir)
        return normaliseV(np.cross(cDir, vD))
    elif cTp in ['Keim']:
        return normaliseV(cDir)
    else:
        print('ERROR: "Zweig" type "', cTp, '" not implemented.')
        return normaliseV(cDir)

def rotatePt2D(vRPtS, vRCtr = V0_2D, phi = 0., isDeg = True):
    assert len(vRPtS) == 2 and len(vRCtr) == 2       # 2D
    if isDeg:
        phi = convDegToRad(phi)
    matR2D = np.mat([[math.cos(phi), -math.sin(phi)],
                     [math.sin(phi), math.cos(phi)]])
    # matrix multiplication resulting in a rotation of vRPtS
    matRPt = matR2D*(np.mat(vRPtS).T)
    vRPtE = np.array([matRPt[0, 0] + vRCtr[0], matRPt[1, 0] + vRCtr[1]])
    return np.around(vRPtE, R14)

def rotatePt3D(vRPtS, vRAx = V0_3D, phi = 0., isDeg = True):
    assert len(vRPtS) == 3 and len(vRAx) == 3        # 3D
    if isDeg:
        phi = convDegToRad(phi)
    # normalise the rotation axis vRAx
    vRAx = normaliseV(vRAx)
    # define the 9 components of the rotation matrix
    r11 = (1 - math.cos(phi))*vRAx[0]*vRAx[0] + math.cos(phi)
    r12 = (1 - math.cos(phi))*vRAx[0]*vRAx[1] - math.sin(phi)*vRAx[2]
    r13 = (1 - math.cos(phi))*vRAx[0]*vRAx[2] + math.sin(phi)*vRAx[1]
    r21 = (1 - math.cos(phi))*vRAx[1]*vRAx[0] + math.sin(phi)*vRAx[2]
    r22 = (1 - math.cos(phi))*vRAx[1]*vRAx[1] + math.cos(phi)
    r23 = (1 - math.cos(phi))*vRAx[1]*vRAx[2] - math.sin(phi)*vRAx[0]
    r31 = (1 - math.cos(phi))*vRAx[2]*vRAx[0] - math.sin(phi)*vRAx[1]
    r32 = (1 - math.cos(phi))*vRAx[2]*vRAx[1] + math.sin(phi)*vRAx[0]
    r33 = (1 - math.cos(phi))*vRAx[2]*vRAx[2] + math.cos(phi)
    matR3D = np.mat([[r11, r12, r13], [r21, r22, r23], [r31, r32, r33]])
    # matrix multiplication resulting in a rotation of vRPtS
    vRPtE = matR3D*(np.mat(vRPtS).T)
    # return normalised vector of new direction
    return normaliseV(np.around(np.squeeze((vRPtE.T).A), R14))

def getFAdjVertZ(vD, vZ, adInf, mn = 0., mx = 1.):
    if adInf[0] == 'std1':
        return 1
    elif adInf[0] in ['linA']:  # linear with angle
        x = calcAngle2Vect3D(vD, vZ, False)
        if adInf[2] == 'dec':
            x = math.pi - x
        return mn + x/math.pi*(mx - mn)
    elif adInf[0] == 'cosA':    # cosine of angle
        x = (np.dot(vD, vZ) + np.linalg.norm(vD))/(np.linalg.norm(vD)**2)
        return mn + x*(mx - mn)
    else:                       # default - adjustment factor = 1
        return 1

def getFAdjRelPosZw(cRAn, adInf, mn = 0., mx = 1.):
    if adInf[0] == 'std1':
        return 1
    if round(cRAn, R14) >= 0:   # only positive angles (others: special cases)
        if adInf[0] in ['linA', 'linB']:    # linear with angle
            x = cRAn
            if adInf[2] == 'dec':
                x = 180 - x     # 180 degrees angle relatively to "Zweig"
            return mn + x/180*(mx - mn)
        elif adInf[0] == 'sinA':   # sine of angle
            x = math.sin(convDegToRad(cRAn/2))
            if adInf[2] == 'dec':
                x = math.sin(convDegToRad(90 + cRAn/2))
            return mn + x*(mx - mn)
        else:                   # default - adjustment factor = 1
            return 1
    else:
        dParLinB = adInf[1]['linB']
        if cRAn == -1:
            if adInf[0] == 'linB':
                return dParLinB['m1V']
            else:
                return 1
        elif cRAn == -2:
            if adInf[0] == 'linB':
                return dParLinB['m2V']
            else:
                return 1
        elif cRAn == -3:
            if adInf[0] == 'linB':
                return dParLinB['m3V']
            else:
                return 1
        else:
            return 1

def getFAdjRelPosKt(pR, adInf, mn = 0., mx = 1.):
    if adInf[0] == 'std1':
        return 1
    elif adInf[0] == 'linA':    # linear
        x = pR
        if adInf[2] == 'dec':
            x = 1. - x
        return mn + x*(mx - mn)
    else:                       # default - adjustment factor = 1
        return 1

def getFAdjLenZw(lnZ, adInf, mn = 0., mx = 1.):
    if adInf[0] == 'std1':
        return 1
    elif adInf[0] == 'logF':    # logistic function
        dPar = adInf[1]['logF']
        x = 1./(1. + math.exp(-dPar['k']*(lnZ - dPar['ln0'])))
        if adInf[2] == 'dec':
            x = 1. - x
        return mn + x*(mx - mn)
    else:                       # default - adjustment factor = 1
        return 1

def getFAdjAgeZw(ageZ, adInf, mn = 0., mx = 1.):
    if adInf[0] == 'std1':
        return 1
    elif adInf[0] == 'logF':    # logistic function
        dPar = adInf[1]['logF']
        x = 1./(1. + math.exp(-dPar['k']*(ageZ - dPar['age0'])))
        if adInf[2] == 'dec':
            x = 1. - x
        return mn + x*(mx - mn)
    else:                       # default - adjustment factor = 1
        return 1

def getFAdjAgeBm(ageB, adInf, mn = 0., mx = 1.):
    if adInf[0] == 'std1':
        return 1
    elif adInf[0] == 'logF':    # logistic function
        dPar = adInf[1]['logF']
        x = 1./(1. + math.exp(-dPar['k']*(ageB - dPar['age0'])))
        if adInf[2] == 'dec':
            x = 1. - x
        return mn + x*(mx - mn)
    else:                       # default - adjustment factor = 1
        return 1

def getLFAdj(lDID, cVt, dTpA, dFA, vD, vUz, cAR, pKR, lZw, ageZw, ageBm, sDN, cM):
    lFAdj = [1 for _ in range(len(lDID))]
    for i, cDID in enumerate(lDID):
        tpAdj = dTpA[cVt][cDID]
        tVAdj = dFA[cVt][cDID][sDN]
        mnV, mxV = drawDst(tVAdj, cM)
        mnV, mxV = max(0, min(mnV, mxV)), max(0, mnV, mxV)
        if cDID == 'VertZ':
            lFAdj[i] = getFAdjVertZ(vD, vUz, tpAdj, mnV, mxV)
        elif cDID == 'RelPZw':
            lFAdj[i] = getFAdjRelPosZw(cAR, tpAdj, mnV, mxV)
        elif cDID == 'RelPKt':
            lFAdj[i] = getFAdjRelPosKt(pKR, tpAdj, mnV, mxV)
        elif cDID == 'LenZw':
            lFAdj[i] = getFAdjLenZw(lZw, tpAdj, mnV, mxV)
        elif cDID == 'AgeZw':
            lFAdj[i] = getFAdjAgeZw(ageZw, tpAdj, mnV, mxV)
        elif cDID == 'AgeBm':
            lFAdj[i] = getFAdjAgeBm(ageBm, tpAdj, mnV, mxV)
    return lFAdj

def roundLTups(lT, rPr = R14):
    lTRd = [None]*len(lT)
    for iL, cT in enumerate(lT):
        lRd = [None]*len(cT)
        for iT, cE in enumerate(cT):
            lRd[iT] = round(cE, rPr)
        lTRd[iL] = tuple(lRd)
    return lTRd

def getCCMidP(pCS, vD, cLen = 1):
    pCM = pCS + cLen/2.*vD
    return [pCM[0]], [pCM[1]], [pCM[2]]

def getLenNewCS(tP, aDr):
    assert len(tP) == len(aDr)
    return sum([tP[l]*aDr[l] for l in range(len(tP))])

def getKeyDBk(tK, tDrR):
    assert len(tK) == len(tDrR)
    lK = list(tK)
    for k in range(len(lK)):
        if tDrR[k]< 0:
            lK[k] *= -1
    return tuple(lK)

def isInRange(lAEXtr, tSgR, pToTest, lDbgOut = 0):
    inRange = True
    for i, cSig in enumerate([-1, 1]):
        for k in range(3):
            if -cSig*tSgR[k]*pToTest[k] + cSig*tSgR[k]*lAEXtr[i][k] < 0:
                inRange = False
                if lDbgOut > 0:
                    print('cSig =', cSig, '/ tSgR[', k, '] =', tSgR[k],
                          '/ pToTest[', k, '] =', pToTest[k], '/ lAEXtr[', i, 
                          '][', k, '] =',lAEXtr[i][k])
                break
    return inRange

def isInBlock(aMdBk, aDimBk, pToTest):
    inBlock = True
    for k in range(3):
        if (pToTest[k] < (aMdBk[k] - aDimBk[k]/2.) or
            pToTest[k] >= (aMdBk[k] + aDimBk[k]/2.)):
            inBlock = False
            break
    return inBlock

def addObjToBlock(cMk, pCtr, lDbgOut = 0):
    assert isInRange(cMk.lAEdgeXtr, cMk.tSigRays, pCtr, lDbgOut)
    pMidBk0 = np.array(cMk.dBk[(0, 0, 0)].pM)
    aSteps = (pCtr - pMidBk0)/cMk.aDim
    (aMin, aMax) = (np.floor(aSteps), np.ceil(aSteps))
    for i in range(int(round(aMin[0])), int(round(aMax[0])) + 1):
        for j in range(int(round(aMin[1])), int(round(aMax[1])) + 1):
            for k in range(int(round(aMin[2])), int(round(aMax[2]) + 1)):
                pMdBkC = np.array([pMidBk0[0] + i*cMk.aDim[0],
                                   pMidBk0[1] + j*cMk.aDim[1],
                                   pMidBk0[2] + k*cMk.aDim[2]])
                if isInBlock(pMdBkC, cMk.aDim, pCtr):
                    return cMk.goDirRay((i, j, k), retTup = True)
    print('WARNING: No Block found. Returning (0, 0, 0)...')
    return (0, 0, 0)

def getCol(lCol, colMode = 'Random', cVal = 1):
    cCol = (0.0, 0.0, 0.0)
    if colMode == 'Random':
        cCol = lCol[random.randrange(0, len(lCol))]
    elif colMode == 'Age':
        cCol = lCol[(cVal - 1)%len(lCol)]
    else:
        print('ERROR: Color mode', colMode, 'not implemented.')
    return cCol

def printElapsedTimeSim(stT, cT, sPre = 'Time'):
    # calculate and display elapsed time 
    elT = round(cT - stT, R04)
    print(sPre, 'elapsed:', elT, 'seconds, this is', round(elT/60, R04),
          'minutes or', round(elT/3600, R04), 'hours or',
          round(elT/(3600*24), R04), 'days.')
    
################################################################################
