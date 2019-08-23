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
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterRasterDestination)


class BinarizationThreshold(QgsProcessingAlgorithm):

    RASTER = 'RASTER'
    UPPER_THRESHOLD = 'UPPER_THRESHOLD'
    LOWER_THRESHOLD = 'LOWER_THRESHOLD'
    RASTER_BIN = 'RASTER_BIN'



    def createInstance(self):
        return BinarizationThreshold()

    def group(self):
        return 'ThresholdVect'

    def groupId(self):
        return 'thresholdvect'

    def tags(self):
        return [QCoreApplication.translate("BinarizationThreshold", 'binarization')]

    def name(self):
        return 'binarizationthreshold'

    def displayName(self):
        return 'Binarization Threshold'

    def shortHelpString(self):
        return """The algorithm binarizes the raster based on a lower and an upper threshold"""

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterRasterLayer(
            self.RASTER,
            'Raster'))

        self.addParameter(
        QgsProcessingParameterRasterDestination(
            self.RASTER_BIN,
            "Binary Raster"
            )
        )        
        
        self.addParameter(QgsProcessingParameterNumber(
        self.UPPER_THRESHOLD, "Upper Threshold",
        QgsProcessingParameterNumber.Double,
        1))

        self.addParameter(QgsProcessingParameterNumber(
        self.LOWER_THRESHOLD, "Lower Threshold",
        QgsProcessingParameterNumber.Double,
        0))

    def processAlgorithm(self, parameters, context, feedback):
        # Retrieving parameters
        upper_threshold = parameters[self.UPPER_THRESHOLD]
        lower_threshold = parameters[self.LOWER_THRESHOLD]
        output = self.parameterAsOutputLayer(parameters, self.RASTER_BIN, context)
        raster = self.parameterAsRasterLayer(parameters, self.RASTER, context)
        
        # Binarization
        raster_bin = processing.run("gdal:rastercalculator", {'INPUT_A': raster, 'BAND_A': 1, 'INPUT_B': None, 'BAND_B': 1, 'INPUT_C': None, 'BAND_C': 1, 'INPUT_D': None, 'BAND_D': 1, 
        'INPUT_E': None, 'BAND_E': 1, 'INPUT_F': None, 'BAND_F': 1, 'FORMULA': "logical_and(A >= " + str(lower_threshold) + ", A <= " + str(upper_threshold) + ")" , 'NO_DATA': 0, 'RTYPE': 0, 'OPTIONS': None,
        'OUTPUT': output}, context=context, feedback=feedback)
        raster_bin = raster_bin['OUTPUT']
        
        return {self.RASTER_BIN: raster_bin}
