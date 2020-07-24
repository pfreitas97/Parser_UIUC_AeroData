#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:35:42 2020

@author: pedroaugustofreitasdearaujo
"""

import numpy as np

import scipy.interpolate

import pandas as pd

import os


def _rescaleLinearly(targetVector,newLength):
    ''' Take a vector with an undersirable number of data points (e.g. twist/beta matrix) and rescales it to
    the desired dimension, assumes equally spaced data points.
    
    targetVector: Vector of points that need to be rescaled to the appropriate number
    newLength: Desired number of points
    '''
    
    assert(np.isscalar(newLength))
    
    
    x_old = np.linspace(0,1,len(targetVector))
    
    x_new = np.linspace(0,1,newLength)
    
    interp = scipy.interpolate.interp1d(x_old,targetVector,fill_value="extrapolate")
    
    return interp(x_new)



class UIUC_Propeller:
    def __init__(self,PropellerData):
        ''' Creates a propeller object to abstract away some of the complexity of integrating UIUC data into a project.
        PropellerData should be a list, or panda.series and have the format [Prop_Name,Diameter,Pitch,geom_path,static_path]
        
        Params
        PropellerData = [str,float,float,str(path),str(path)]   
        '''
        
        assert(os.path.exists(PropellerData[3]))
        
        assert(os.path.exists(PropellerData[4]))
        
        
        ''' Assuming all UIUC_Propellers have 2 blades only for now '''
        
        self.b = 2
        


        
        self.NAME =  PropellerData[0]
        
        self.Radius = PropellerData[1]/2 # Note choosing to store radius instead of diameter for convinience
        
        self.pitch = PropellerData[2]
        
        
        #self.twist = twist partitions, locations should match the rR elements
        
        #self.rR =  r/R blade element partitions
        
        #self.cR = non dimensionalized chord (c/R) partitions. Should match r/R
        
        self.rR,self.cR,self.twist = self._extractGeometricAttributes(PropellerData[3])
        
        self.RPMs, self.CTs, self.CQs = self._extractStaticTestResults(PropellerData[4])
        
        
        pass
    
    
    
    
    def _extractGeometricAttributes(self,geom_path):
        
        geodf = pd.read_csv(geom_path,delim_whitespace=True)
        
        # just in case one of the files has a typo.
        geodf.columns = ['r/R','c/R','beta']
        
        return [tuple(geodf['r/R']), tuple(geodf['c/R']), tuple(geodf['beta'])]
            
    
    
    
    def _extractStaticTestResults(self,static_path):
        
        statdf = pd.read_csv(static_path,delim_whitespace=True)
        
        statdf.columns = ['RPM','CT','CQ']
        
        return [tuple(statdf['RPM']), tuple(statdf['CT']), tuple(statdf['CQ'])]
    
    
    def _getMaxChord(self):
        
        return self.Radius * max(self.cR)
        
        pass
    
    
    
    
    def getTrainingData(self,blade_elements=15):
        ''' Return propeller data in a format that is more convinient to use with tensorflow/pytorch.
        Return 2 numpy 2d ndarrays, the first one will contain all attributes of the propeller instance that called, 
        attributes will either be there in their standard form or one that is most convinient 
        (i.e. RPM will be converted to radians/sec, twist will be returned in radians, r/R , c/R and twist
        will be rescaled to a fixed number of data points).
        This first matrix will be of the form:
        [b,Radius,Chord,RPM[in rad/s], r/R_rescaled,c/R_rescaled,twist_rescaled[rad]]
        
        In regression terms, this first matrix can be thought of as the 'predictors' or 'x'
        The dependent variables will be included in the second matrix and will be:
        [CT,CQ]
        A single UIUC_Propeller object will thus correspond to several datapoints as each RPM and its associated CT,CQ
        will be included in separate rows.
        
        Parameters
        
        rescaled_blade_elements: The number of points in r/R,c/R,twist, these will be rescaled using '_rescaleLinearly'
                                    and will therefore utilize the same assumptions.
        
        Return:
            [x_mat,y_mat]
        '''
        
        C = self._getMaxChord()
        
        # conversion: 1RPM =  0.104719755 rad/s , 1 degree = pi/180 radians
        
        omega =  0.104719755 * np.array([self.RPMs])
        
        rR_rescaled = _rescaleLinearly(self.rR, blade_elements)
        
        cR_rescaled = _rescaleLinearly(self.cR, blade_elements)
        
        twist_rescaled = (np.pi/180) * _rescaleLinearly(self.twist, blade_elements)
        
        
        
        
        # length column is based on : [b , R , C ,omega  ,rR[len = blade_elm],cr,twist] Thus: 4 + 3*rblade_element
        num_columns = blade_elements*3 + 4
        
        num_rows = len(self.RPMs)
        
        x_mat = np.zeros(shape=(num_rows,num_columns))
        
        y_mat = np.zeros(shape=(num_rows,2))
        

        
        for i, CURR_RPM in np.ndenumerate(omega):
            
            
                        
            y_mat[i[1],] = np.array([self.CTs[i[1]],self.CQs[i[1]]])

            
            x_mat[i[1],] = np.array([self.b,self.Radius, C ,CURR_RPM,*rR_rescaled,*cR_rescaled,*twist_rescaled])
            
            pass
        
        
        
        return [x_mat,y_mat]
    
    def getRotorData(self):
        ''' Return list of propeller values in a format that is more convinient for directly calculating propeller 
        hover performance. Similar to getTrainingData function, except results are returned as a list of 
        objects with different types.
        
        Return: [b,radius,C,omega[rad/s],rR,cR,twist[degrees]]. Note: Angular velocity is returned in radians/sec and
        r/R,c/R and twist are returned as tuples with no rescaling.
        '''
        C = self._getMaxChord()
        
        # conversion: 1RPM =  0.104719755 rad/s
        
        omega =  0.104719755 * np.array([self.RPMs])   
        
        return [self.b,self.Radius,C,omega,self.rR, self.cR, self.twist]
    
    pass
