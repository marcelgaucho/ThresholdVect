# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""
from PyQt5.QtCore import QCoreApplication
import processing
from qgis.core import (QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource, 
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterVectorLayer,
                       QgsProcessingParameterFeatureSink,
                       QgsFeatureSink
                       )

class Aggregation(QgsProcessingAlgorithm):

    VECTOR = 'VECTOR'
    BUFFER = 'BUFFER'
    OUTPUT = 'OUTPUT'


    def createInstance(self):
        return Aggregation()

    def group(self):
        return 'ThresholdVect'

    def groupId(self):
        return 'thresholdvect'

    def tags(self):
        return [QCoreApplication.translate("BinarizationThreshold", 'aggregation')]

    def name(self):
        return 'aggregation'

    def displayName(self):
        return 'Aggregation'
        
    def shortHelpString(self):
        return "Do the aggregation of features where the buffer intersects."
        
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterFeatureSource(
            self.VECTOR,
            'Vector'))
            
        self.addParameter(QgsProcessingParameterNumber(
            self.BUFFER,
            'Buffer',
            QgsProcessingParameterNumber.Double,
            ))  
  
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT,
            'Output'))         
        
            
    def processAlgorithm(self, parameters, context, feedback):
        # Dummy function to enable running an alg inside an alg
        def no_post_process(alg, context, feedback):
            pass
            
        # Buffer
        buffer = processing.run("native:buffer", {'INPUT':parameters[self.VECTOR], 'DISTANCE':parameters[self.BUFFER], 'DISSOLVE': True, 'OUTPUT':'memory:'}, context=context, feedback=feedback, onFinish=no_post_process)
        buffered = buffer['OUTPUT']
        feedback.pushInfo('buffered = ' + str(buffered))

        # Debuffer
        debuffer = processing.run("native:buffer", {'INPUT':buffered, 'DISTANCE':-parameters[self.BUFFER], 'OUTPUT':'memory:'}, context=context, feedback=feedback, onFinish=no_post_process)
        debuffered = debuffer['OUTPUT']
        feedback.pushInfo('debuffered = ' + str(debuffered))

        # Explode multiparts to simple parts
        part = processing.run("native:multiparttosingleparts", {'INPUT':debuffered, 'OUTPUT':parameters[self.OUTPUT]}, context=context, feedback=feedback, onFinish=no_post_process)
        parted = part['OUTPUT']

        return {self.OUTPUT: parted}
