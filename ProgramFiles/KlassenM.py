################################################################################
# ### KLASSENM (BAUMWACHSTUM) ##################################################
# ### KlassenM.py             ##################################################
################################################################################
import os, pprint
import math
from importlib import import_module
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D     # necessary for 3d-plots

from Konstanten import NF_BAUM_PRE, V0_3D, EPS
import InputAllgemein as InpA
import Funktionen as Fkt
from KlassenS import Mosaik, Sonne
################################################################################
P0 = InpA.dictInpA['P0']
vUx = InpA.dictInpA['vUx']
vUy = InpA.dictInpA['vUy']
vUz = InpA.dictInpA['vUz']
basR3 = InpA.dictInpA['basisR3']

################################################################################
class InputData:
    def __init__(self, inpDat, lVals = []):
        dInp = {}
        if type(inpDat) is dict:
            for cKey in inpDat:
                dInp[cKey] = inpDat[cKey]
        elif type(inpDat) is list:
            lKeys = inpDat
            nKeys, nVals = len(lKeys), len(lVals)
            if nKeys == nVals:
                for cIdx in range(nKeys):
                    dInp[lKeys[cIdx]] = lVals[cIdx]
            else:
                print('ERROR: Cannot add to input dictionary.')
                print('Length of keys and values lists:', nKeys, '!=', nVals)
        self.dI = dInp
    
    def __str__(self):
        sIn = ('*'*24 + ' "InputData" type ' + '*'*24 +
               '\nInput dictionary:\n' + str(self.dI))
        return sIn

    def addBaumTps(self, nDWald):
        pyX, lenNM, = self.dI['nFEndPY'], len(NF_BAUM_PRE)
        for nF in os.listdir(nDWald):
            if len(nF) >= lenNM + len(pyX):
                if nF[:lenNM] == NF_BAUM_PRE and nF.endswith(pyX):
                    nMod, sBID, iTp = nF[:-len(pyX)], nF[lenNM:-len(pyX)], 0
                    try:
                        iTp = int(sBID)
                    except:
                        print('ERROR: Cannot convert', sBID, 'to an integer.')
                    cMod = import_module(nMod)
                    self.dI[iTp] = getattr(cMod, 'dictInpB')
                    self.dI[iTp]['iTp'] = iTp

    def yieldBaumTraitID(self, iTp = 1, sTrait = 'strType'):
        cTrait = ''
        if iTp in self.dI:
            if sTrait in self.dI[iTp]:
                cTrait = self.dI[iTp][sTrait]
            else:
                print('ERROR: Trait', sTrait, 'not in', self.dI[iTp])
        else:
            print('ERROR: "Baum" ID', iTp, 'not in input dictionary.')
        return cTrait
    
    def yieldBaumTraitTp(self, sType = 'EinfacherBaum', sTrait = 'strNSpec'):
        cTrait = ''
        for cKey in self.dI:
            if type(cKey) is int:       # value corresponds to "Baum" traits
                if sType in self.dI[cKey].values():
                    if sTrait in self.dI[cKey]:
                        cTrait = self.dI[cKey][sTrait]
                    else:
                        print('ERROR: Trait', sTrait, 'not in', self.dI[cKey])
        return cTrait
    
    def yieldOneVal(self, cKey):
        retVal = None
        if cKey in self.dI:
            retVal = self.dI[cKey]
        else:
            print('ERROR: Key', cKey, 'not in input dictionary.')
        return retVal
    
    def yieldValList(self, lKeys):
        retList = [None]*len(lKeys)
        for cIdx, cKey in enumerate(lKeys):
            retList[cIdx] = self.yieldOneVal(cKey)
        return retList
    
    def yieldDict(self, lKeys):
        retDict = {}
        for cKey in lKeys:
            retDict[cKey] = self.yieldOneVal(cKey)
        return retDict
    
    def printInputData(self):
        pprint.pprint(self.dI) 

################################################################################
class Blatt:
    # create a "Blatt" base object
    def __init__(self, dInA, dInTp, cMk, IDBlt, vS = P0, vDB = vUz, vDZ = vUz,
                 lenBl = 1., widBl = 1., shpBl = 'circle', ageBl = 1):
        self.dIA = dInA
        self.dITp = dInTp
        self.cMk = cMk
        self.cM = self.dIA['Mode']
        self.IDBt = IDBlt
        self.pS = vS
        self.vDirBt = vDB
        self.vDirZw = vDZ
        self.shpBt = shpBl
        self.lenBt = lenBl
        self.widBt = widBl
        self.getArea()
        self.pMid = self.pS + (self.lenBt/2.)*self.vDirBt
        self.pRBt = Fkt.getLenNewCS(self.pMid, self.vDirBt)
        self.ageBt = ageBl
        self.addToBlock()
    
    def __str__(self):
        sIn = ('*'*24 + ' "Blatt" type ' + '*'*24 +
               '\nID of this "Blatt": ' + str(self.IDBt) +
               '\nStart position: ' + str(self.pS) +
               '\nDirection of growth of "Blatt": ' + str(self.vDirBt) +
               '\nDirection of growth of "Zweig": ' + str(self.vDirZw) +
               '\nShape: ' + str(self.shpBt) +
               '\nLength: ' + str(self.lenBt) +
               '\nWidth: ' + str(self.widBt) +
               '\nArea: ' + str(self.areaB) +
               '\nMid point: ' + str(self.pMid) +
               '\nRelative position to sunlight: ' + str(self.pRBt) +
               '\nAge: ' + str(self.ageBt) +
               '\nIn Block: ' + str(self.keyBk) +
               '\n' + '-'*80 + '\n')
        return sIn
    
    def getArea(self):
        self.areaB = 0.
        if self.shpBt == 'rectangle':
            self.areaB = self.lenBt*self.widBt
        elif self.shpBt == 'oval':
            self.areaB = self.lenBt/2.*self.widBt/2.*math.pi
        else:
            print('ERROR: Shape', self.shpBt, 'not yet implemented.')
    
#     def isInRange(self):
#         inRange, lAEXtr = True, self.cMk.lAEdgeXtr
#         tSgR = self.cMk.tSigRays
#         for i, cSig in enumerate([-1, 1]):
#             for k in range(3):
#                 if -cSig*tSgR[k]*self.pMid[k] + cSig*tSgR[k]*lAEXtr[i][k] < 0:
#                     inRange = False
#                     break
#         return inRange
#     def isInBlock(self, aMdBk, aDimBk):
#         inBlock = True
#         for k in range(3):
#             if (self.pMid[k] < (aMdBk[k] - aDimBk[k]/2.) or
#                 self.pMid[k] >= (aMdBk[k] + aDimBk[k]/2.)):
#                 inBlock = False
#                 break
#         return inBlock
    
    def addToBlock(self):
        self.keyBk = Fkt.addObjToBlock(self.cMk, self.pMid, self.dIA['lvlDbg'])
        self.cMk.addBlattToBlock(self.keyBk, self.dITp, self.IDBt, self.areaB)

################################################################################
class Zweig:
    # create a "Zweig" base object
    def __init__(self, dInA, dInTp, cMk, dFAdj, dFPE, dAnEP, dAnEA, IDZw,
                 lPathID, yrGrm = 0, ageBm = 0, vS = P0, sD = 's', vDPrv = vUz,
                 vDCur = vUz, cAnV = 0., cAnR = 0., lenZw = 1., lFDstK = [1],
                 ageZw = 1):
        self.dIA = dInA
        self.dITp = dInTp
        self.cMk = cMk
        self.cM = self.dIA['Mode']
        self.IDZ = IDZw
        self.pathID = lPathID
        self.yrG = yrGrm
        self.ageB = ageBm
        self.pS = vS
        self.sDir = sD
        self.vDirP = vDPrv
        self.vDirC = vDCur
        self.lFDsE = Fkt.drawDst(dFPE[self.sDir], self.cM,
                                 self.dIA['dMinMax']['FctPEZw'])
        self.lAnEP = Fkt.drawDst(dAnEP[self.sDir], self.cM,
                                 self.dIA['dMinMax']['AngPol'])
        self.lAnEA = Fkt.drawDst(dAnEA[self.sDir], self.cM,
                                 self.dIA['dMinMax']['AngAzm'])
#         Fkt.adjustAngles(self.lAnEP, self.lAnEA)
        self.cAnVZ = cAnV
        self.cAnRZ = cAnR
        self.getSegments(lenZw)
        self.lFDsK = lFDstK
        self.vDsK = np.array([cFctK*self.lenZ for cFctK in self.lFDsK], float)
        self.getCoordKt()
        self.arrX = np.array([self.pS[0]] + [cP[0] for cP in self.lPSegE])
        self.arrY = np.array([self.pS[1]] + [cP[1] for cP in self.lPSegE])
        self.arrZ = np.array([self.pS[2]] + [cP[2] for cP in self.lPSegE])
        self.dFAd = dFAdj
        self.ageZ = ageZw
    
    def __str__(self):
        sIn = ('*'*24 + ' "Zweig" type ' + '*'*24 +
               '\nID of this "Zweig": ' + str(self.IDZ) +
               '\nPath of previous "Zweig" IDs: ' + str(self.pathID) +
               '\nYear of germination: ' + str(self.yrG) +
               '\nAge of supporting "Baum": ' + str(self.ageB) +
               '\nStart position: ' + str(self.pS) +
               '\nEnd position: ' + str(self.pE) +
               '\nArray of x-coordinates: ' + str(self.arrX) +
               '\nArray of y-coordinates: ' + str(self.arrY) +
               '\nArray of z-coordinates: ' + str(self.arrZ) +
               '\nID string of growth direction: ' + str(self.sDir) +
               '\nDirection of growth (previous "Zweig"): ' + str(self.vDirP) +
               '\nDirection of growth (this "Zweig"): ' + str(self.vDirC) +
               '\nAngle to z-direction (vertical): ' + str(self.cAnVZ) +
               '\nAngle relative to parent "Zweig": ' + str(self.cAnRZ) +
               '\nLength: ' + str(self.lenZ) +
               '\nNumber of "Knoten": ' + str(len(self.vDsK)) +
               '\nDistance factors of "Knoten": ' + str(self.lFDsK) +
               '\nDistances of "Knoten": ' + str(self.vDsK) +
               '\nDistance factors of edges: ' + str(self.lFDsE) +
               '\nPolar angles of edges: ' + str(self.lAnEP) +
               '\nAzimuthal angles of edges: ' + str(self.lAnEA) +
               '\nList of directions of segments: ' + str(self.lDirSeg) +
               '\nList of positions of segment edges: ' + str(self.lPSegE) +
               '\nList of segment lengths: ' + str(self.lLenSeg) +
               '\nList of "Knoten" directions: ' + str(self.lKVD) +
               '\nList of "Knoten" points: ' + str(self.lKC) +
               '\nList of "Knoten" position strings: ' + str(self.lKPS) +
               '\nDictionary of adjustment factors: ' + str(self.dFAd) +
               '\nAge: ' + str(self.ageZ) + 
               '\n' + '-'*80 + '\n')
        return sIn

    def getSegments(self, lenZw):
        assert len(self.pS) == 3 and len(self.vDirC) == 3
        if self.dIA['lvlDbg'] > 0 and (self.pS[2] < 0 or lenZw <= 0):
            print('self.pS[2] =', self.pS[2], '/', 'lenZw =', lenZw)
        assert self.pS[2] >= 0 and lenZw > 0
        assert (len(self.lFDsE) == len(self.lAnEP) and
                len(self.lAnEP) == len(self.lAnEA))
        nE = len(self.lFDsE)
        lDirSg, lPSgE = [V0_3D]*(nE + 1), [V0_3D]*(nE + 1)
        lLenSg = [0.]*(nE + 1)
        cAngChDr = Fkt.drawDst(self.dITp['dAngChDr'][self.sDir], self.cM,
                               self.dIA['dMinMax']['AngPol'])
        lInpV = [0, np.array([cKS for cKS in self.pS]), self.vDirC, lenZw,
                 self.dITp['dPosZweig'][self.sDir], cAngChDr,
                 self.dIA['tolAngV']]
        # lInpV: [pRC, pSC, vDC, lenC, cSPosZweig, cAngChDr, angTol]
        Fkt.constructSeg(lDirSg, lPSgE, lLenSg, nE, lInpV, self.lFDsE,
                         self.lAnEP, self.lAnEA)
        assert len(lDirSg) == len(lPSgE) and len(lDirSg) == len(lLenSg)
        self.lDirSeg, self.lPSegE, self.lLenSeg = lDirSg, lPSgE, lLenSg
        self.pE, self.lenZ = self.lPSegE[-1], sum(self.lLenSeg)
    
    def getCoordKt(self):
        lVDKt, lCKt = [V0_3D]*len(self.vDsK), [V0_3D]*len(self.vDsK)
        lPSKt = ['End']*len(self.vDsK)
        lInpV = [np.array([cK for cK in self.pS]), 0, 0., 0., True]
        # lInpV: [pSC, iSegS, cTDsK, cTLen, incTLen]
        for k in range(len(self.vDsK)):
            lPSKt[k] = Fkt.getRPsSK(self.lFDsK[k])
            lInpV = Fkt.getInfoKt(lVDKt, lCKt, k, self.vDsK, lInpV,
                                  self.lDirSeg, self.lLenSeg)
        self.lKVD, self.lKC, self.lKPS = lVDKt, lCKt, lPSKt

    def growKnoten(self, lKN, mxIDKt, iKN, cY):
        for k in range(len(self.lKC)):
            iKN += 1
            dInfo = {'VertZ': self.cAnVZ, 'RelPZw': self.cAnRZ,
                     'RelPKt': self.lFDsK[k], 'LenZw': self.lenZ,
                     'AgeZw': self.ageZ, 'AgeBm': self.ageB}
            nKKt = Fkt.drawDict(self.dITp, dInfo, self.dIA['dMinMax'], 'dDist',
                                'NKKt', 'dNumNKKt', 'dBndAr', 'dCtWt',
                                self.sDir, self.cM)
#             print('Growing Knoten with ID', mxIDKt + iKN, '.')
            lKN.append(Knoten(self.dIA, self.dITp, self.cMk, self.dFAd,
                              mxIDKt + iKN, self.pathID + [self.IDZ], k, cY,
                              self.ageB, self.ageZ, self.lenZ, self.lKC[k],
                              self.lFDsK[k], self.lKPS[k], self.sDir,
                              self.vDirP, self.lKVD[k], len(self.vDsK), nKKt))
        self.lKZw = [cKt for cKt in lKN[-len(self.lKC):]]
        return iKN

################################################################################
class Knospe:
    # create a "Knospe" object
    def __init__(self, dInA, dInTp, cMk, nKntnZw, IDKnosp, lPathID, iKnosp,
                 yrGrm = 0, ageBm = 0, ageZw = -1, lenZw = 0., pCA = P0,
                 pR = 0., sDPrv = 's', sDNxt = 'v', vDZw = vUz, vDK = vUz,
                 isGerm = True):
        self.dIA = dInA
        self.dITp = dInTp
        self.cMk = cMk
        self.cM = self.dIA['Mode']
        self.dLenZw = self.dITp['dLengthZw']
        self.dNNKZw = self.dITp['dNumNKZw']
        self.dFPKZw = self.dITp['dFctPKZw']
        self.dFPEZw = self.dITp['dFctPEZw']
        self.dAnEPlr = self.dITp['dAngEPlr']
        self.dAnEAzm = self.dITp['dAngEAzm']
        self.dTpAdj = self.dITp['dTypeAdj']
        self.dMMAdj = self.dITp['dMMFAdj']
        self.nKZw = nKntnZw
        self.IDKs = IDKnosp
        self.pathID = lPathID
        self.iKKt = iKnosp
        self.yrG = yrGrm
        self.ageB = ageBm
        self.ageZ = ageZw
        self.lenZ = lenZw
        self.pKC = pCA
        self.pKR = pR
        self.sDirP = sDPrv
        self.sDirN = sDNxt
        self.vDirZw = vDZw
        self.vDir = vDK
        self.cAnVZ = Fkt.calcAngle2Vect3D(self.vDir, vUz)
        self.cAnRZ = Fkt.calcAngle2Plains3D([self.vDirZw, vUz],
                                            [self.vDir, self.vDirZw])
        self.dFAd = self.getFAdj()
        self.fGerm = isGerm
        
    def __str__(self):
        sCTp, sGerm = 'Knospe', '(not germinable)'
        if self.fGerm:
            sGerm = '(GERMINABLE)'
        sIn = ('*'*24 +' "' + sCTp + '" type ' + sGerm + ' ' + '*'*24 +
               '\nDictionary of "Zweig" lengths: ' + str(self.dLenZw) +
               '\nDictionary of number of new "Knoten": ' + str(self.dNNKZw) +
               '\nDictionary of "Knoten" pos. factors: ' + str(self.dFPKZw) +
               '\nDictionary of edge pos. factors: ' + str(self.dFPEZw) +
               '\nDictionary of edge polar angles: ' + str(self.dAnEPlr) +
               '\nDictionary of edge azim. angles: ' + str(self.dAnEAzm) +
               '\nDictionary of adjustment factors: ' + str(self.dFAd) +
               '\nNumber of "Knoten" on supp. "Zweig": ' + str(self.nKZw) +
               '\nID of "' + sCTp + '": ' + str(self.IDKs) +
               '\nPath of previous "Zweig" IDs: ' + str(self.pathID) +
               '\nIndex of "' + sCTp + '": ' + str(self.iKKt) +
               '\nYear of germination: ' + str(self.yrG) +
               '\nAge of supporting "Baum": ' + str(self.ageB) +
               '\nAge of supporting "Zweig": ' + str(self.ageZ) +
               '\nLength of supporting "Zweig": ' + str(self.lenZ) +
               '\nPosition (cartesian): ' + str(self.pKC) +
               '\nPosition (dist. relative to "Zweig"): ' + str(self.pKR) +
               '\nString of original growth direction: ' + str(self.sDirP) +
               '\nString of "' + sCTp + '"growth direction: ' +
               str(self.sDirN) +
               '\nDirection of growth of parent "Zweig": ' + str(self.vDirZw) +
               '\nDirection of growth of "' + sCTp + '": ' + str(self.vDir) +
               '\nAngle to z-direction (vertical): ' + str(self.cAnVZ) +
               '\nAngle relative to parent "Zweig": ' + str(self.cAnRZ) + 
               '\n' + '-'*80 + '\n')
        return sIn
    
    def becomeInact(self):
        self.fGerm = False
    
    # create the dictionary of adjustment factors
    # "explanatory" v. (in lSEV) determine factors for "response" v. (in lSRV_)
    def getFAdj(self):
        lSRV_C, lSEV = self.dIA['dVDep']['lSRV_C'], self.dIA['dVDep']['lSEV']
        dFAdj = {}
        for cVar in lSRV_C:
            # list of adjustment factors (lFA) for cur. response v.
            # contains elements for all explanatory v.
            lFA = Fkt.getLFAdj(lSEV, cVar, self.dTpAdj, self.dMMAdj, self.vDir,
                               vUz, self.cAnRZ, self.pKR, self.lenZ, self.ageZ,
                               self.ageB, self.sDirN, self.cM)
            # list of according weights, as defined in dITp
            lWts = [self.dITp['dCtWt'][cVar][cSEV] for cSEV in lSEV]
            dFAdj[cVar] = Fkt.weightedGeoMean(lFA, lWts)
        return dFAdj
    
    def growZweig(self, cLtPBk):
        assert cLtPBk <= 1
        if self.fGerm:
            self.becomeInact()
            dMnMx = self.dIA['dMinMax']
            # draw a value for the length of this "Zweig"
            lenZw = Fkt.drawVRel(self.dLenZw, self.nKZw, self.sDirN, self.cM,
                                 dMnMx['LenZw'], dMnMx['NKZw'],
                                 self.dFAd['LenZw'], self.dITp['dDist']['NKZw'])
            # adjust the "Zweig" length according to the available light
            if self.dIA['lvlDbg'] > 0 and cLtPBk < 1:
                print('lenZw (before):', lenZw, '- current light propagated in block:', cLtPBk)
            lenZw *= cLtPBk
            if self.dIA['lvlDbg'] > 0:
                print('lenZw (after):', lenZw)
            # TODO - change
            if lenZw < 10:
                return 0
            dInfo = {'VertZ': self.cAnVZ, 'RelPZw': self.cAnRZ,
                     'RelPKt': self.pKR, 'LenZw': self.lenZ, 'AgeZw': 1,
                     'AgeBm': self.ageB}
            # draw a value for the number of "Knoten" on this "Zweig"
            nKZw = Fkt.drawDict(self.dITp, dInfo, dMnMx, 'dDist', 'NKZw',
                                'dNumNKZw', 'dBndAr', 'dCtWt', self.sDirN,
                                self.cM)
#             # adjust the number of "Knoten" according to the available light
#             nKZw = max(1, round(nKZw*cLtPBk))
            lFDstK = Fkt.drawLVRel(self.dFPKZw, nKZw, self.sDirN, self.cM,
                                   dMnMx['FctPKZw'], self.dITp['dDist']['NKZw'])
            return Zweig(self.dIA, self.dITp, self.cMk, self.dFAd, self.dFPEZw,
                         self.dAnEPlr, self.dAnEAzm, self.IDKs, self.pathID,
                         self.yrG, self.ageB, self.pKC, self.sDirN,
                         self.vDirZw, self.vDir, self.cAnVZ, self.cAnRZ, lenZw,
                         lFDstK)

################################################################################
class Knoten:
    # create a "Knoten" base object
    def __init__(self, dInA, dInTp, cMk, dFAdj, IDKntn = 0, lPathID = [],
                 iKntnZw = 0, yrGrm = 0, ageBm = 0, ageZw = -1, lenZw = 0.,
                 pCA = P0, pR = 0., sPKntn = 'End', sD = 's', vDPrv = vUz,
                 vDCur = vUz, nKntnZw = 1, nKKntn = 1, isAct = True):
        assert len(pCA) == 3 and len(vDPrv) == 3 and len(vDCur) == 3
        self.dIA = dInA
        self.dITp = dInTp
        self.cMk = cMk
        self.cM = self.dIA['Mode']
        self.IDKt = IDKntn
        self.pathID = lPathID
        self.iKtZw = iKntnZw
        self.yrG = yrGrm
        self.ageB = ageBm
        self.ageZ = ageZw
        self.lenZ = lenZw
        self.pKC = pCA
        self.pKR = pR
        self.sPKt = sPKntn
        self.fAct = isAct
        self.sDir = sD
        self.vDirP = vDPrv
        self.vDirC = vDCur
        self.sZwTp = self.dITp['dPosZweig'][self.sDir]
        self.nKZw = nKntnZw
        self.nKKt = nKKntn
        self.dFAd = dFAdj
        dAnKPlr = self.dITp['dAngKPlr'][self.nKKt]
        dAnKAzm = self.dITp['dAngKAzm'][self.nKKt]
        if self.sPKt == 'End':
            dAnKPlr = self.dITp['dAngKPlr_E'][self.nKKt]
            dAnKAzm = self.dITp['dAngKAzm_E'][self.nKKt]
        self.lAnKPlr = Fkt.drawDst(dAnKPlr[self.sDir], self.cM,
                                   self.dIA['dMinMax']['AngPol'],
                                   self.dFAd['AngPol'])
        self.lAnKAzm = Fkt.drawDst(dAnKAzm[self.sDir], self.cM,
                                   self.dIA['dMinMax']['AngAzm'],
                                   self.dFAd['AngAzm'])
        Fkt.adjustAngles(self.lAnKPlr, self.lAnKAzm)
        self.lNumKs = [0, 0]
        self.lKKt = []
        self.lZw = []
        self.lIDPinch = []
        self.pinchIt = False
        self.addToBlock()
        self.growBlaetter()
        
    def __str__(self):
        sCTp, sAct = 'Knoten', '(not active)'
        if self.fAct:
            sAct = '(ACTIVE)'
        sIn = ('*'*24 +' "' + sCTp + '" type ' + sAct + ' ' + '*'*24 +
               '\nID of Knoten: ' + str(self.IDKt) +
               '\nPath of previous "Zweig" IDs: ' + str(self.pathID) +
               '\nIndex of Knoten on "Zweig": ' + str(self.iKtZw) +
               '\nYear of germination: ' + str(self.yrG) +
               '\nAge of supporting "Baum": ' + str(self.ageB) +
               '\nAge of supporting "Zweig": ' + str(self.ageZ) +
               '\nLength of supporting "Zweig": ' + str(self.lenZ) +
               '\nPosition (cartesian): ' + str(self.pKC) +
               '\nPosition (dist. relative to "Zweig"): ' + str(self.pKR) +
               '\nString of Knoten position: ' + str(self.sPKt) +
               '\nString of growth direction: ' + str(self.sDir) +
               '\nDirection of growth (parent "Zweig"): ' + str(self.vDirP) +
               '\nDirection of growth (supp. "Zweig"): ' + str(self.vDirC) +
               '\n"Zweig" (direction) type: ' + str(self.sZwTp) +
               '\nNumber of "Knoten" on supp. "Zweig": ' + str(self.nKZw) +
               '\nNumber of "Knospen" on this "Knoten": ' + str(self.nKKt) +
               '\nNumber of "Knospen" (germ., non-germ.): ' + str(self.lNumKs) +
               '\nPolar angles of "Knospen" (adj.): ' + str(self.lAnKPlr) +
               '\nAzimut angles of "Knospen" (adj.): ' + str(self.lAnKAzm) +
               '\nAzimut angles offset: ' + str(self.offsAngAzm) +
               '\nRel. pos. of "Knospen": ' + str([K.pKR for K in self.lKKt]) +
               '\nAbs. pos. of "Blaetter": ' + str([B.pS for B in self.lBt]) +
               '\nList of "Zweige" IDs: ' + str([Zw.IDZ for Zw in self.lZw]) +
               '\nList of "Zweige" IDs to pinch out: ' + str(self.lIDPinch) + 
               '\nDictionary of adjustment factors: ' + str(self.dFAd) +
               '\nIn Block: ' + str(self.keyBk) +
               '\n' + '-'*80 + '\n')
        return sIn

    def printIDListOfZweige(self):
        lZwIDs = [Zw.IDZ for Zw in self.lZw]
        if len(lZwIDs) == 0:
            print('List of "Zweige" IDs for Knoten', self.IDKt, 'is empty!')
        else:
            print('List of "Zweige" IDs for Knoten', self.IDKt, 'is:')
            print('\t', lZwIDs)

    def growBlatt(self, vDirB, iKKt):
        if self.fAct:
            return Blatt(self.dIA, self.dITp, self.cMk, (self.IDKt, iKKt),
                         self.pKC, vDirB, vUz, self.dITp['lenBlatt'],
                         self.dITp['widBlatt'], self.dITp['shapeBlatt'])
    
    def growBlaetter(self):
        self.lBt = []
        tOffsAngAzm = self.dITp['dOffsAngAzm'][self.nKKt][self.sDir]
        self.offsAngAzm = Fkt.drawDst(tOffsAngAzm, self.cM,
                                      self.dIA['dMinMax']['AngAzm'])
        if self.dIA['modelBlatt']:
            vN = Fkt.findRotAxis(self.vDirC, self.sZwTp, self.dIA['tolAngV'])
            for iKKt in range(self.nKKt):
                cAnBtPlr = self.lAnKPlr[iKKt]*self.dITp['fAngBlattPlr']
                cAnKsAzm = self.lAnKAzm[iKKt] + self.offsAngAzm*self.iKtZw
                cAnBtPlr, cAnKsAzm = Fkt.adjustAngPA(cAnBtPlr, cAnKsAzm)
                vR = Fkt.rotatePt3D(self.vDirC, vN, cAnBtPlr)
                vDB = Fkt.rotatePt3D(vR, self.vDirC, cAnKsAzm)
                self.lBt.append(self.growBlatt(vDB, iKKt))

    def pinchSubZw(self, cZw, lZwRm, lIDZPinch):
        cZwToElm = False
        for oneID in cZw.pathID:
            if oneID in lIDZPinch:
                lZwRm.append(cZw)       # remove this one
                cZwToElm = True
                break
        return cZwToElm
    
    def pinchZweig(self, cZw, lZwRm, cPrPZw, tMnMx):
        prPinch = Fkt.drawDst(cPrPZw, self.cM, tMnMx)
        if np.random.uniform() < prPinch:
            lZwRm.append(cZw)           # remove this one

    def removeZwPinchKt(self, lZwRm, lIDZPinch):
        Fkt.addLElToList(lIDZPinch, [Z.IDZ for Z in lZwRm])
        for cZw in lZwRm:
            for cKt in cZw.lKZw:
                cKt.pinchIt = True
        lZwKeep = []
        for cZw in self.lZw:
            if cZw not in lZwRm:
                lZwKeep.append(cZw)
        self.lZw = [cZw for cZw in lZwKeep]
        if len(self.lZw) == 0:
            self.pinchIt = True             # remove this one

    def pinchZweige(self, tMnMx, lNumKt, lIDZPinch, doPinch = False):
        if len(self.lZw) > 0:
            dPrPZw, lZwRm = self.dITp['dPrpPinch']['Zweig'], []
            for cZw in self.lZw:
                cZwToElim = self.pinchSubZw(cZw, lZwRm, lIDZPinch)
                if doPinch and not cZwToElim:
                    self.pinchZweig(cZw, lZwRm, dPrPZw[self.sDir], tMnMx)
            self.removeZwPinchKt(lZwRm, lIDZPinch)
        lNumKt[3] = max(lNumKt[3], self.IDKt)

    def ageBlaetter(self):
        for cBt in self.lBt:
            cBt.ageBt += 1

    def ageZweige(self):
        if self.ageZ >= 0:
            self.ageZ += 1
        for cZw in self.lZw:
            cZw.ageZ += 1
        for cKKt in self.lKKt:
            cKKt.ageZ += 1

    def pinchKnospen(self, dPrPKKt, tMnMx):
        if self.ageZ <= 1:      # pinch out Knospen
            for cKKt in self.lKKt:
                prPinch = Fkt.drawDst(dPrPKKt[self.sDir], self.cM, tMnMx)
                if np.random.uniform() < prPinch:
                    cKKt.becomeInact()
                    self.lNumKs[0] += 1
                    self.lNumKs[1] -= 1

    def formPinchKnospen(self, dPrPKKt, tMnMx):
        if self.fAct:       # form Knospen
            vN = Fkt.findRotAxis(self.vDirC, self.sZwTp, self.dIA['tolAngV'])
            for iKKt in range(self.nKKt):
                cAnKsAzm = self.lAnKAzm[iKKt] + self.offsAngAzm*self.iKtZw
                tAn = Fkt.adjustAngPA(self.lAnKPlr[iKKt], cAnKsAzm)
                self.lAnKPlr[iKKt], cAnKsAzm = tAn
                vR = Fkt.rotatePt3D(self.vDirC, vN, self.lAnKPlr[iKKt])
                vDKKt = Fkt.rotatePt3D(vR, self.vDirC, cAnKsAzm)
                sDirN = Fkt.getSDir(self.sDir, vDKKt, vUz, self.dIA['tolAngV'])
                self.lKKt.append(Knospe(self.dIA, self.dITp, self.cMk,
                                        self.nKZw, (self.IDKt, iKKt),
                                        self.pathID, iKKt, self.yrG, self.ageB,
                                        self.ageZ, self.lenZ, self.pKC,
                                        self.pKR, self.sDir, sDirN, self.vDirC,
                                        vDKKt))
                self.lNumKs[1] += 1
        self.pinchKnospen(dPrPKKt, tMnMx)

    def growZweige(self):
        if self.fAct:
            for cKKt in self.lKKt:
                if cKKt.fGerm:
                    # light propagated in cur. block determines "Zweig" growth
                    cLtPrgtBk = sum(self.cMk.dBk[self.keyBk].aLtP)
                    # only grow a "Zweig" if there is light in cur. block 
                    if cLtPrgtBk > 0:
                        # TODO - improve
                        newZw = cKKt.growZweig(cLtPrgtBk)
                        if newZw != 0:
                            self.lZw.append(newZw)
                            cKKt.fGerm = False
                
    def growKnoten(self, lNmK, lKN, iKN, cY):
        if self.fAct:
            for cZw in self.lZw:
                iKN = cZw.growKnoten(lKN, lNmK[3], iKN, cY)
            self.deactivateK()
            lNmK[0] += 1
            lNmK[1] -= 1
        return iKN

    def deactivateK(self):
        self.fAct = False
        for cKKt in self.lKKt:
            cKKt.becomeInact()

    def addToBlock(self):
        self.keyBk = Fkt.addObjToBlock(self.cMk, self.pKC, self.dIA['lvlDbg'])
        self.cMk.addKnotenToBlock(self.keyBk, self.dITp, self.IDKt)
#         print('Added Knoten with ID', self.IDKt, 'to Block', self.keyBk,
#               '. Dict of Knoten in this Block:', self.cMk.dBk[self.keyBk].dIDKt)

################################################################################
class Baum:
    # create a "Baum" base object
    def __init__(self, inpDat, cMk, iTp = 1, vS = P0, yrGerm = 0, angPKm = 0,
                 angAKm = 0, ageB = 0, lenKm = 0):
        descrB, cSPKtS, cSDrKtS = 'Keim', 'End', 'k'
        IDK, iKZw, cPRKtS, lPathID = 0, 0, 0., []
        self.dIA = inpDat.dI
        self.dITp = inpDat.dI[iTp]
        self.cMk = cMk
        self.cM = self.dIA['Mode']
        self.iT = iTp
        self.tpB = self.dITp['strType']
        self.specB = self.dITp['strNSpec']
        self.descB = descrB
        self.ageB = ageB
        self.lenK = lenKm
        self.pS = vS
        self.yGerm = yrGerm
        self.dPosZw = self.dITp['dPosZweig']
        self.dPosBl = self.dITp['dPosBlatt']
        self.lNumK = [0, 1, 1, IDK] # num. inact., num. act., num. all, max. ID
        self.dFAd = {cVar: 1. for cVar in self.dIA['dVDep']['lSRV_C']}
        angPKm, angAKm = Fkt.adjustAngPA(angPKm, angAKm)
        vDirP, vDirSl, ageZw = vUz, Fkt.convPolarToCart(1., angPKm, angAKm), -1
        self.lK = [Knoten(self.dIA, self.dITp, self.cMk, self.dFAd, IDK,
                          lPathID, iKZw, self.yGerm, self.ageB, ageZw,
                          self.lenK, self.pS, cPRKtS, cSPKtS, cSDrKtS, vDirP,
                          vDirSl)]
        self.lIDZwPinch = []

    def __str__(self):
        sIn = ('*'*24 + ' "Baum" type ' + '*'*24 +
               '\nIndex of type: ' + str(self.iT) +
               '\nType: ' + str(self.tpB) +
               '\nSpecification: ' + str(self.specB) +
               '\nDescription: ' + str(self.descB) +
               '\nAge: ' + str(self.ageB) +
               '\nMode: ' + str(self.cM) +
               '\nStart position (cart.): ' + str(self.pS) +
               '\nGermination year: ' + str(self.yGerm) +
               '\n"Zweig" positions: ' + str(self.dPosZw) +
               '\n"Blatt" positions: ' + str(self.dPosBl) +
               '\nList of number of "Knoten": ' + str(self.lNumK) +
               '\nAdjustment factor dictionary: ' + str(self.dFAd) +
#                '\nList of "Knoten" IDs.: ' + str([K.IDKt for K in self.lK]) +
#                '\nList of "Knoten" IDs to pinch out: ' +
#                str(sorted(self.lIDKtPinch)) +
               '\nList of "Zweige" IDs to pinch out: ' +
               str(sorted(self.lIDZwPinch)) +
               '\n' + '-'*80 + '\n')
#                '\nList of "Knoten" coord.: ' + str([K.pKC for K in self.lK]))
        return sIn
    
    def getLKtPinch(self):
        lKtPinch = []
        for cK in self.lK:
            if cK.pinchIt:
                lKtPinch.append(cK)
        return lKtPinch, len(lKtPinch)
    
    def getLKs(self, minAgeZw = -1, maxAgeZw = -1, tpKs = 'All'):
        lKs = []
        for cK in self.lK:
            if ((max([minAgeZw, maxAgeZw]) < 0) or
                (minAgeZw < 0 and cK.ageZ <= maxAgeZw) or
                (maxAgeZw < 0 and cK.ageZ >= minAgeZw) or
                (min([minAgeZw, maxAgeZw]) >= 0 and
                 cK.ageZ >= minAgeZw and cK.ageZ <= maxAgeZw)):
                for cKs in cK.lKKt:
                    if ((tpKs == 'All') or (tpKs == 'Active' and cKs.fGerm) or
                        (tpKs == 'Inactive' and not cKs.fGerm)):
                        lKs.append(cKs)
        return lKs, len(lKs)
    
    def getLZw(self, minAgeZw = -1, maxAgeZw = -1):
        lZw = []
        for cK in self.lK:
            if ((max([minAgeZw, maxAgeZw]) < 0) or
                (minAgeZw < 0 and cK.ageZ <= maxAgeZw) or
                (maxAgeZw < 0 and cK.ageZ >= minAgeZw) or
                (min([minAgeZw, maxAgeZw]) >= 0 and
                 cK.ageZ >= minAgeZw and cK.ageZ <= maxAgeZw)):
                lZw += [cZw for cZw in cK.lZw]
        return lZw, len(lZw)
    
    def getDInfoDeactKs(self, minAgeZw = -1, maxAgeZw = -1):
        dNumKs = {'All': 0, 'Germinable': 0, 'Deactivated': 0}
        for cK in self.lK:
            if ((max([minAgeZw, maxAgeZw]) < 0) or
                (minAgeZw < 0 and cK.ageZ <= maxAgeZw) or
                (maxAgeZw < 0 and cK.ageZ >= minAgeZw) or
                (min([minAgeZw, maxAgeZw]) >= 0 and
                 cK.ageZ >= minAgeZw and cK.ageZ <= maxAgeZw)):
                dNumKs['Deactivated'] += cK.lNumKs[0]
                dNumKs['Germinable'] += cK.lNumKs[1]
                dNumKs['All'] += sum(cK.lNumKs)
        return dNumKs
    
    def getDZwCat(self, sCat = 'ageZ'):
        dZwCat = {}
        for cK in self.lK:
            if len(cK.lZw) > 0:
                for cZw in cK.lZw:
                    if sCat == 'ageZ':
                        Fkt.adToDictCount(dZwCat, cZw.ageZ)
                    elif sCat == 'ageB':
                        Fkt.adToDictCount(dZwCat, cZw.ageB)
                    elif sCat == 'yrG':
                        Fkt.adToDictCount(dZwCat, cZw.yrG)
        return dZwCat
    
    def printSelInfo(self):
        print('-'*24, self.tpB, 'on position', self.pS, '-'*24)
        print('Number of "Knoten":', self.lNumK[2], '(', self.lNumK, ')')
#         print('List of "Knoten" to pinch out:',
#               sorted([cKt.IDKt for cKt in LKtPinch]))
        for cAge in range(2, self.dIA['nYears'] + 1):
            print('Number of "Knospen" of age', cAge, ':')
            pprint.pprint(self.getDInfoDeactKs(cAge, cAge))
        numZwPinch, dZwAge = len(self.lIDZwPinch), self.getDZwCat('ageZ')
        print('Dictionary of "Zweige" of specific age:')
        pprint.pprint(dZwAge)
        print('Number of "Zweige" that were pinched out:', numZwPinch)
        _, numZw = self.getLZw(3)
        if numZw > 0:
            print('(', numZwPinch/(numZw + numZwPinch)*100.0, '% of "Zweige")')
#         print('List of "Zweige" to pinch out:', sorted(self.lIDZwPinch))
    
    def printSelInfoExt(self):
        self.printSelInfo()
        print('List of "Knoten" IDs (All):', [K.IDKt for K in self.lK])
        print('Dictionary of "Zweig" IDs:', {K.IDKt: [cZw.IDZ for cZw in K.lZw]
                                             for K in self.lK})
    
    def printLCKnoten(self, maxAgeIncLK = 1):
        sPr = ''
        if self.ageB <= maxAgeIncLK:
            sPr += '\nList of coordinates of "Knoten" objects:\n'
            for cK in self.lK[:-1]:
                sPr += (str(cK.pKC) + ', ')
            sPr += str(self.lK[-1].pKC)
        print(sPr)
    
    def printAllKnoten(self, sPrWhich = 'All'):
        cFlTarg = False
        if sPrWhich == 'Active':
            cFlTarg = True
        for cK in self.lK:
            if sPrWhich == 'All':
                print(cK)
            elif sPrWhich in ['Inactive', 'Active']:
                if cK.fAct == cFlTarg:
                    print(cK)

    def printAllZweige(self):
        for cK in self.lK:
            for cZw in cK.lZw:
                print(cZw)
    
    def printAllBlaetter(self):
        for cK in self.lK:
            for cBt in cK.lBt:
                print(cBt)

    def getDictCKtNKKt(self, sPlW = 'Inactive'):
        dDatKt = {k: [np.zeros(self.lNumK[2]) for _ in range(3)]
                  for k in range(1, self.dIA['nKKtMax'] + 1)}
        cFlTarg, lNTarg = False, [0 for _ in range(self.dIA['nKKtMax'])]
        if sPlW == 'Active':
            cFlTarg = True
        for cKt in self.lK:
            if cKt.fAct == cFlTarg:
                for k in range(3):
                    dDatKt[cKt.nKKt][k][lNTarg[cKt.nKKt - 1]] = cKt.pKC[k]
                lNTarg[cKt.nKKt - 1] += 1
        for cK in dDatKt:
            for k in range(3):
                dDatKt[cK][k] = dDatKt[cK][k][:lNTarg[cK - 1]]
        return dDatKt
    
    def ageBaum(self):
        self.lIDZwPinch, lKN, iKN = [], [], 0
        self.ageB += 1
        for cK in self.lK:
            cK.ageB += 1
            for cKKt in cK.lKKt:
                cKKt.ageB += 1
            for cZw in cK.lZw:
                cZw.ageB += 1
        if self.ageB > 1:
            self.descB = 'Baum'
        elif self.ageB == 1:
            self.descB = 'Schoessling'
        else:
            self.descB = 'Keim'
        return lKN, iKN

    def adjLNumK(self, cK):
        if cK.fAct:
            self.lNumK[1] -= 1
        else:
            self.lNumK[0] -= 1

    def updateLKnoten(self, lKN = [], iKN = 0):
        lKKeep = []
        for cK in self.lK:
            if cK.pinchIt:
                self.adjLNumK(cK)
            else:
                lKKeep.append(cK)
        self.lK = [cKt for cKt in lKKeep]
        self.lK += lKN
        self.lNumK[1] += iKN
        self.lNumK[2] = len(self.lK)
        self.lNumK[3] += iKN

    def wachse1Y(self, cY):
        dMnMxSTD = self.dIA['dMinMax']['STD']
        lKN, iKN = self.ageBaum()
        for cK in self.lK:
            cK.pinchZweige(dMnMxSTD, self.lNumK, self.lIDZwPinch, True)
        self.updateLKnoten()
        for cK in self.lK:
            if len(cK.lZw) > 0:
                cK.pinchZweige(dMnMxSTD, self.lNumK, self.lIDZwPinch)
        self.updateLKnoten()
        for cK in self.lK:
            cK.formPinchKnospen(self.dITp['dPrpPinch']['Knospe'], dMnMxSTD)
            cK.ageBlaetter()
            cK.ageZweige()
            cK.growZweige()
            iKN = cK.growKnoten(self.lNumK, lKN, iKN, cY)
        self.updateLKnoten(lKN, iKN)
        if self.iT == 5:
            print('Age of Baum:', self.ageB)
            print('"Knoten" remaining (ID, ageZ, ageB, isAct):',
                  sorted([(cK.IDKt, cK.ageZ, cK.ageB, cK.fAct)
                          for cK in self.lK]))
            print('"Knospen" remaining (ID, ageZ, ageB):',
                  sorted([(cKs.IDKs, cKs.ageZ, cKs.ageB)
                          for cKs in self.getLKs()[0]]))
            print('"Zweige" remaining (ID, ageZ, ageB):',
                  sorted([(cZw.IDZ, cZw.ageZ, cZw.ageB)
                          for cZw in self.getLZw()[0]]))

    def plotZweige(self, cAx):
        fWdthZw, offsZWd = self.dIA['fWdthZw'], self.dIA['offsWdthZw']
        lClrZw = self.dIA['lClrZweig']
        for cK in self.lK:
            for cZw in cK.lZw:
                cLwd = cZw.ageZ*fWdthZw + offsZWd
                cCol = Fkt.getCol(lClrZw, self.dIA['colModeZw'], cZw.ageZ)
                cAx.plot(cZw.arrX, cZw.arrY, cZw.arrZ, linestyle = 'solid',
                         linewidth = cLwd, color = cCol)

    def plotBlaetter(self, cAx):
        lClrB, sPlWhich = self.dIA['lClrBltS1'], self.dIA['dPlot']['Blatt'][1]
        mEW = self.dITp['wdEdgeBl']
        if self.dIA['colSetBl'] == 'Autumn':
            lClrB = self.dIA['lClrBltS2']
        for cK in self.lK:
            for cBt in cK.lBt:
                if ((sPlWhich in ['All', 'Current'] and cBt.ageBt == 1) or
                    (sPlWhich in ['All', 'Previous'] and cBt.ageBt > 1)):
                    cCol = Fkt.getCol(lClrB, self.dIA['colModeBl'], cBt.ageBt)
                    mSz = np.average([cBt.lenBt, cBt.widBt])
                    mSz *= self.dITp['fMarkSzBl']
                    lX, lY, lZ = Fkt.getCCMidP(cBt.pS, cBt.vDirBt, cBt.lenBt)
                    cAx.plot(lX, lY, lZ, linestyle = 'None', marker = 'H',
                             ms = mSz, markeredgewidth = mEW, color = cCol)

    def plotSelKnoten(self, cAx, dDatKt, lClrKt):
        for cK, cL in dDatKt.items():
            if min([len(cL[k]) for k in range(len(cL))]) > 0:
                cCol = lClrKt[(cK - 1)%len(lClrKt)]
                cAx.plot(cL[0], cL[1], cL[2], linestyle = 'None', marker = 'o',
                         ms = self.dITp['fMarkSzKt'],
                         mew = self.dITp['wdEdgeKt'], color = cCol)

    def plotKnoten(self, cAx):
        lClrKtS1, lClrKtS2 = self.dIA['lClrKntnS1'], self.dIA['lClrKntnS2']
        sPlWhich = self.dIA['dPlot']['Knoten'][1]
        if sPlWhich in ['All', 'Inactive']:
            dDataKt = self.getDictCKtNKKt('Inactive')
            self.plotSelKnoten(cAx, dDataKt, lClrKtS1)
        if sPlWhich in ['All', 'Active']:
            dDataKt = self.getDictCKtNKKt('Active')
            self.plotSelKnoten(cAx, dDataKt, lClrKtS2)

    def decoratePlot(self, nF = 'Plot', pTitle = ''):
        plt.title(pTitle)
#         plt.legend(loc = 'best')
        plt.xlabel('x')
        plt.ylabel('y')
#         plt.zlabel('z')
        plt.savefig(Fkt.joinToPath(nF + self.dIA['nFEndPDF'],
                                   [self.dIA['nDPlots']]))
        plt.close()

    def plotBaum3D(self, cElev = 15., cAzim = -55):
        sAge, sPlt = '__' + str(self.ageB) + '_Jahre', '__LinesPlot__E_'
        sElev, sAzim = str(round(cElev)), str(round(cAzim))
        nF = self.tpB + sAge +  sPlt + sElev + '__A_' + sAzim + '__' + self.cM
        plt.figure()
        ax = plt.axes(projection = '3d')
        ax.view_init(elev = cElev, azim = cAzim)
        ax.set_zlim3d(bottom = 0)
        if self.dIA['dPlot']['Zweig']:
            self.plotZweige(ax)
        if self.dIA['dPlot']['Blatt'][0]:
            self.plotBlaetter(ax)
        if self.dIA['dPlot']['Knoten'][0]:
            self.plotKnoten(ax)
        self.decoratePlot(nF, self.tpB + sAge + ' (Struktur)')

################################################################################
class BaumGruppe:
    # create a "BaumGruppe" base object
    def __init__(self, inpDat):
        descrBG, ageBG = 'BaumGruppe', 0
        self.dIA = inpDat.dI
        self.cMk = Mosaik(self.dIA)
        self.cM = self.dIA['Mode']
        self.dBG = self.dIA['dBaumGruppe']
        self.addInitialBaeume(inpDat)
        self.nYrs = self.dIA['nYears']
        self.lViewPlt = self.dIA['lViewPlt']
        self.lYPltBG = self.dIA['lYPltBaumGruppe']
        self.descBG = descrBG
        self.ageBG = ageBG
        self.cSonne = Sonne(self.dIA)
        Fkt.seedRNG(self.cM)

    def __str__(self):
        sIn = ('~'*24 + ' ' + str(self.descBG) +
               ' of age ' + str(self.ageBG) + ' ' + '~'*24 +
               '\nMode: ' + str(self.cM) +
               '\nNumber of years modelled: ' + str(self.nYrs) +
               '\n"BaumGruppe" input: ' + str(self.dBG) +
               '\n"BaumGruppe" not yet germinated: ' + str(self.dBGNotGerm) +
               '\nPlot views [List of (elevation, azimuthal angle)]: ' +
               str(self.lViewPlt) + 
               '\n' + '~'*80 + '\n')
        return sIn
    
    def addBaum(self, inpDat, iTp, cP, yrG = 0):
        angP = Fkt.drawDst(inpDat.dI[iTp]['dAngKPlr_E'][1]['k'], self.cM,
                           self.dIA['dMinMax']['AngPol'])
        angA = Fkt.drawDst(inpDat.dI[iTp]['dAngKAzm_E'][1]['k'], self.cM,
                           self.dIA['dMinMax']['AngAzm'])
        Fkt.adjustAngles(angP, angA)
        self.lB.append(Baum(inpDat, self.cMk, iTp, np.array(cP), yrG, angP[0],
                            angA[0]))
    
    def addInitialBaeume(self, inpDat):
        self.lB, self.dBGNotGerm = [], {}
        for iTpB, lSPosSYB in self.dBG.items():
            for k in range(len(lSPosSYB)):
                cPos, yrGerm = lSPosSYB[k]
                if yrGerm == 0:
                    self.addBaum(inpDat, iTpB, cPos, yrGerm)
                else:
                    Fkt.addToDictL(self.dBGNotGerm, iTpB, lSPosSYB[k])
    
    def addNewBaeume(self, inpDat, yrC = 0):
        for iTpB, lSPosSYB in self.dBGNotGerm.items():
            for k in range(len(lSPosSYB)):
                cPos, yrGerm = lSPosSYB[k]
                if yrGerm == yrC:
                    self.addBaum(inpDat, iTpB, cPos, yrGerm)
    
    def printBaeume(self):
        for cB in self.lB:
            print(cB)
    
    def getLBlaetter(self):
        lBt = []
        for cB in self.lB:
            for cK in cB.lK:
                for cBt in cK.lBt:
                    lBt.append(cBt)
    
    def growBaeume(self, inpDat, prSelIExt = False):
        self.plotBaumGruppe()
        print('Distributing light...')
        self.cMk.distributeLight()
        for cTS in range(1, self.nYrs + 1):
            print('-'*24, 'Year:', cTS, '-'*24)
            for cB in self.lB:
                cB.wachse1Y(cTS)
            self.addNewBaeume(inpDat, cTS)
            self.cMk.distributeLight()
            self.ageBG += 1
            for cB in self.lB:
                if prSelIExt:
                    print(cB)
                    cB.printSelInfoExt()
                else:
                    cB.printSelInfo()
                print('# "Knoten":', cB.lNumK[2], '/', len(cB.lK), '- active:',
                      cB.lNumK[1], '- inactive:', cB.lNumK[0],
                      '- max. "Knoten" ID:', cB.lNumK[3])
                print('-'*40)
            self.plotBaumGruppe()
            if self.dIA['dPrint']['Knoten'][0]:
                cB.printAllKnoten(self.dIA['dPrint']['Knoten'][1])
            if self.dIA['dPrint']['Zweig']:
                cB.printAllZweige()
            if self.dIA['dPrint']['Blatt']:
                cB.printAllBlaetter()
            if self.dIA['lvlDbg'] > 0:
                print(self.cMk)

    def eqDstScaling(self, cAx):
        dD = {'x': [0, None, None], 'y': [1, None, None], 'z': [2, None, None]}
        for cB in self.lB:
            for cKt in cB.lK:
                Fkt.fillDictMinMax(dD, cKt.pKC)
                for cZw in cKt.lZw:
                    Fkt.fillDictMinMax(dD, cZw.pS)
                    Fkt.fillDictMinMax(dD, cZw.pE)
        cRg_2 = math.ceil(max([dD[cC][2] - dD[cC][1] for cC in dD])/2.)
        dMid = {cC: (dD[cC][2] + dD[cC][1])/2. for cC in dD}
        if cRg_2 > 0:
            cAx.set_xlim3d(dMid['x'] - cRg_2, dMid['x'] + cRg_2)
            cAx.set_ylim3d(dMid['y'] - cRg_2, dMid['y'] + cRg_2)
            cAx.set_zlim3d(0, 2*cRg_2)

    def decoratePlot(self, nF = 'Plot', pTitle = ''):
        plt.title(pTitle)
#         plt.legend(loc = 'best')
        plt.xlabel('x')
        plt.ylabel('y')
#         plt.zlabel('z')
        plt.savefig(Fkt.joinToPath(nF + self.dIA['nFEndPDF'],
                                   [self.dIA['nDPlots']]))
        plt.close()
    
    def plotBaumGruppe(self):
        if self.ageBG in self.lYPltBG:
            sStart = self.descBG + '__' + str(self.ageBG) + '_Jahre'
            sTitle = self.descBG + ' (' + str(self.ageBG) + ' Jahre)'
            for (cElev, cAngAzm) in self.lViewPlt:
                sElev, sAzim = str(round(cElev)), str(round(cAngAzm))
                nF = sStart + '__E_' + sElev + '__A_' + sAzim + '__' + self.cM
                plt.figure()
                ax = plt.axes(projection = '3d')
                ax.view_init(elev = cElev, azim = cAngAzm)
                if self.dIA['eqDstScl']:
                    self.eqDstScaling(ax)
                for cB in self.lB:
                    if cB.dIA['dPlot']['Zweig']:
                        cB.plotZweige(ax)
                    if cB.dIA['dPlot']['Blatt'][0]:
                        cB.plotBlaetter(ax)
                    if cB.dIA['dPlot']['Knoten'][0]:
                        cB.plotKnoten(ax)
                self.decoratePlot(nF, sTitle)
        
################################################################################
