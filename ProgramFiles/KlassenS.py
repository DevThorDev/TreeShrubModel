################################################################################
# ### KLASSENS (BAUMWACHSTUM) ##################################################
# ### KlassenS.py             ##################################################
################################################################################
# import os, pprint
# import math
import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D     # necessary for 3d-plots

# from Konstanten import NF_BAUM_PRE, EPS
# import InputAllgemein as InpA
import Funktionen as Fkt

################################################################################
class Block:
    # create a "Block" base object
    def __init__(self, dInA, aDm, tSgRs, lAEdXtM, pRSlt = 0.,
                 vPMid = (0., 0., 0.5), tLyrC = (0, 0, 0), iB = 0):
        self.dIA = dInA
        assert len(vPMid) == 3
        self.iBk = iB
        self.aDim = aDm
        self.tSgR = tSgRs
        self.pRS = pRSlt
        self.pM = vPMid
        self.xL = self.aDim[0]
        self.yL = self.aDim[1]
        self.zL = self.aDim[2]
        self.lAEXtM = lAEdXtM
        self.getLAEdgeXtr()
        self.tLyr = tLyrC
        self.lIDBt = []
        self.cLtC = 0.
        self.aLtP = np.array([0.]*3)
        self.getIDSunNeighbours()
#         self.calcLightCollected(aLtCl)
    
    def __str__(self):
        sIn = ('*'*12 + ' "Block" ' + str(self.iBk) + ' ' + '-'*8 + ' ID ' +
               str(str(self.tLyr)) + ' ' + '*'*12 +
               '\nRelative position to sunlight: ' + str(self.pRS) +
               '\nMid position: ' + str(self.pM) +
               '\nDimensions: ' + str(self.aDim) +
               '\nSignature of rays: ' + str(self.tSgR) +
               '\nLength: ' + str(self.xL) +
               '\nWidth: ' + str(self.yL) +
               '\nHeight: ' + str(self.zL) +
               '\nExtreme edges: ' + str(self.lAEdgeXtr) +
               '\nLayer (x, y, z): ' + str(self.tLyr) +
               '\nList of "Blatt" IDs:' + str(self.lIDBt) +
               '\nNumber of "Blatt" objects:' + str(len(self.lIDBt)) +
               '\nList of sun neighbours (ID, iDim):' + str(self.lIDSunN) +
               '\nLight collected: ' + str(self.cLtC) +
               '\nLight propagated: ' + str(self.aLtP))
        return sIn
    
    def getLAEdgeXtr(self):
        self.lAEdgeXtr = [np.array((0., 0., 0.)), np.array((0., 0., 0.))]
        for i, cSig in enumerate([-1, 1]):
            for k in range(3):
                self.lAEdgeXtr[i][k] = self.pM[k] + cSig*self.aDim[k]/2.
    
    def getIDSunNeighbours(self):
#         print('self.lAEXtM =', self.lAEXtM, '- self.tSgR =', self.tSgR)
        assert len(self.tSgR) == len(self.aDim)
        self.lIDSunN = []
        lIDSunN = [[self.tLyr[k] for k in range(3)]
                   for _ in range(len(self.tSgR))]
        lPMidN = [np.array([self.pM[k] for k in range(3)])
                  for _ in range(len(self.tSgR))]
        for k in range(len(self.tSgR)):
            lPMidN[k][k] -= self.tSgR[k]*self.aDim[k]
            lIDSunN[k][k] -= 1
#             print('lPMidN[', k, '] =', lPMidN[k], '- lIDSunN[', k, '] =', lIDSunN[k])
            if Fkt.isInRange(self.lAEXtM, self.tSgR, lPMidN[k]):
                self.lIDSunN.append((tuple(lIDSunN[k]), k))
    
    def addIDBlatt(self, cIDBt):
        self.lIDBt.append(cIDBt)
#         print('After adding', cIDBt, 'the list of Blatt IDs of Block',
#               self.iBk, '(layer', self.tLyr, ') is:', self.lIDBt)
    
    def calcLightCollected(self, aLP):
#         aLtC = np.array([0.]*3)
#         for k, cLP in enumerate(aLP):
#             aLtC[k] = cLP*(self.dIA['tLtDilF'][k]**(self.tLyr[k]))
#         self.cLtc = sum(aLtC)
        for cIDSunN in self.lIDSunN:
            self.cLtC += self.dABk[cIDSunN[0]].aLtP[cIDSunN[1]]
        if len(self.lIDSunN) == 0:
            self.cLtC = sum(aLP)
        # TODO - change formula (sigmoid?)
        self.cLtC *= len(self.lIDBt)/1000.
        self.aLtP = aLP - self.aLtC

################################################################################
class Mosaik:
    # create a "Mosaik" base object
    def __init__(self, dInA):
        self.dIA = dInA
        self.aNEl = np.array(self.dIA['tNumBk'])
        self.nX = self.aNEl[0]
        self.nY = self.aNEl[1]
        self.nZ = self.aNEl[2]
        self.aDim = np.array(self.dIA['tDimBkG'])
        self.cSonne = Sonne(self.dIA)
        self.tSigRays = self.goDirRay(retTup = True)
        self.calcLightPropag()
        self.getDBlocks()
    
    def __str__(self):
        sIn = ('*'*24 + ' "Mosaik" type ' + '*'*24 +
               '\nNumber of "Block" elements (x, y, z): ' + str(self.aNEl) +
               '\nNumber of "Block" elements in x-direction: ' + str(self.nX) +
               '\nNumber of "Block" elements in y-direction: ' + str(self.nY) +
               '\nNumber of "Block" elements in z-direction: ' + str(self.nZ) +
               '\nDimensions of a "Block" element: ' + str(self.aDim) +
               '\nExtreme edges: ' + str(self.lAEdgeXtr) +
               '\nLight propagated: ' + str(self.aLtPrgt) +
#                '\nDictionary of blocks: ' + str(self.dBk) + 
               '\nList of block IDs: ' + str(self.lBkID))
        return sIn
    
    def printDBlocks(self):
        print('Elements in list of "Blocks":')
        for i, cBk in sorted(self.dBk.items()):
            print('Block', i, '-'*16)
            print(cBk)
            print('-'*24)

    def goDirRay(self, aK = np.array((1, 1, 1)), retTup = False, inv = False):
        assert len(aK) == len(self.cSonne.aDR)
#         print('aK:', aK, '- type:', type(aK))
        aK = np.array(aK)
        for k in range(len(aK)):
            if ((not inv and self.cSonne.aDR[k] < 0) or
                (inv and self.cSonne.aDR[k] > 0)):
                aK[k] *= -1
        if retTup:
            return tuple(aK)
        else:
            return aK

    def getTLayer(self, tX, tY, tZ):
        lLC = [tX[0], tY[0], tZ[0]]
        if self.cSonne.aDR[0] < 0:
            lLC[0] = tX[1]
        if self.cSonne.aDR[1] < 0:
            lLC[1] = tY[1]
        if self.cSonne.aDR[2] < 0:
            lLC[2] = tZ[1]
        return tuple(lLC)
    
    def getLAEdgeXtr(self, lTM):
        self.lAEdgeXtr = [np.array((0., 0., 0.)), np.array((0., 0., 0.))]
        for i, cSig in enumerate([-1, 1]):
#             self.lAEdgeXtr[i] = cSig*self.goDirRay(self.aDim/2.)
            self.lAEdgeXtr[i] = cSig*np.array(self.tSigRays)*self.aDim/2.
            self.lAEdgeXtr[i] += np.array(lTM[i])

    def calcLightPropag(self):
        aDRI = self.cSonne.aDRInv
        aPD = np.array(self.dIA['basisR3'] + [-v for v in self.dIA['basisR3']])
        aArea = np.array([self.aDim[1]*self.aDim[2], self.aDim[0]*self.aDim[2],
                          self.aDim[0]*self.aDim[1]]*2)
        aLtP = [np.dot(cPD, aDRI)*aArea[k] for k, cPD in enumerate(aPD)]
        aLtP = np.array([max(aLtP[k], aLtP[k + 3]) for k in range(3)])
        self.aLtPrgt = aLtP/sum(aLtP)

    def updateBlock(self, kBk):
        self.dBk[kBk].dABk = self.dBk

    def getDBlocks(self):
        self.dBk, self.lBkID, lTT, tD = {}, [], [], self.dIA['tDimBkG']
        nX, nY, aDRI = self.nX, self.nY, self.cSonne.aDRInv
#         aPD = np.array(self.dIA['basisR3'] + [-v for v in self.dIA['basisR3']])
#         aArea = np.array([self.aDim[1]*self.aDim[2], self.aDim[0]*self.aDim[2],
#                           self.aDim[0]*self.aDim[1]]*2)
#         aLtCol = [np.dot(cPD, aDRI)*aArea[k] for k, cPD in enumerate(aPD)]
#         aLtCol = np.array([max(aLtCol[k], aLtCol[k + 3]) for k in range(3)])
#         aLtCol /= sum(aLtCol)
        for i in reversed(range(self.nZ)):
            tLZ = (i, self.nZ - i - 1)
            for j in range(self.nY):
                tLY = (j, self.nY - j - 1)
                for k in range(self.nX):
                    tLX = (k, self.nX - k - 1)
                    tPMid = (-(nX//2)*tD[0] + ((nX + 1)%2)*tD[0]/2. + k*tD[0],
                             -(nY//2)*tD[1] + ((nY + 1)%2)*tD[1]/2. + j*tD[1],
                             tD[2]/2. + i*tD[2])
                    pRSunl = Fkt.getLenNewCS(tPMid, aDRI)
                    lTT.append((pRSunl, tPMid, self.getTLayer(tLX, tLY, tLZ)))
        self.getLAEdgeXtr([lTT[0][1], lTT[-1][1]])
        lTT.sort(reverse = True)
        for (i, (pRSunl, tPMid, tLC)) in enumerate(lTT):
            self.lBkID.append((pRSunl, tLC))
            self.dBk[tLC] = Block(self.dIA, self.aDim, self.tSigRays,
                                  self.lAEdgeXtr, pRSunl, tPMid, tLC, i)
        for keyBk in self.dBk:
            self.updateBlock(keyBk)

    def addBlattToBlock(self, cKBk, cIDBt):
        self.dBk[cKBk].addIDBlatt(cIDBt)
        
    def distributeLight(self):
        for cBkID in self.lBkID:
            self.dBk[cBkID[1]].calcLightCollected(self.aLtPrgt)
            print(self.dBk[cBkID[1]])
    
################################################################################
class Sonne:
    # create a "Sonne" base object
    def __init__(self, dInA, cTime = 0.):
        self.dIA = dInA
        self.aDR = Fkt.normaliseV(np.array(self.dIA['tDirRay']))
        self.aDRInv = Fkt.normaliseV(np.array(self.dIA['tDirRayInv']))
        self.itR = self.dIA['intRay']
        self.cT = cTime
    
    def __str__(self):
        sIn = ('*'*24 + ' "Sonne" type ' + '*'*24 +
               '\nDirection of sun rays: ' + str(self.aDR) +
               '\nIntensity of sun rays: ' + str(self.itR) +
               '\nCurrent time: ' + str(self.cT))
        return sIn

################################################################################
