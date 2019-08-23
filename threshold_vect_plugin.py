#-*- coding: utf-8 -*-
"""
/***************************************************************************
                           Threshold Vect
                             --------------------
        begin                : 2019-22-07
        git sha              : :%H$
        copyright            : (C) 2019 by Marcel Rotunno (IBGE)
        email                : marcel.rotunno@gmail.com
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License v3.0 as          *
 *   published by the Free Software Foundation.                            *
 *                                                                         *
 ***************************************************************************/
"""
import os.path
import glob
import shutil

from qgis.core import QgsApplication, QgsProcessingModelAlgorithm

from processing.modeler.ModelerUtils import ModelerUtils
from .processing.tv_load_provider import TVLoadAlgorithmProvider

class ThresholdVect:

    def __init__(self, iface):
        self.iface = iface
        self.provider = None

    def initGui(self):
        # Add provider and models to QGIS
        self.provider = TVLoadAlgorithmProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)
        if QgsApplication.processingRegistry().providerById('model'):
            self.add_processing_models(None)
        else: # We need to wait until processing is initialized
            QgsApplication.processingRegistry().providerAdded.connect(self.add_processing_models)

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)

    def add_processing_models(self, provider_id):
        if not (provider_id == 'model' or provider_id is None):
            return

        if provider_id is not None: # If method acted as slot
            QgsApplication.processingRegistry().providerAdded.disconnect(self.add_processing_models)

        # Add etl-model
        basepath = os.path.dirname(os.path.abspath(__file__))
        plugin_models_dir = os.path.join(basepath, "processing", "models")

        for filename in glob.glob(os.path.join(plugin_models_dir, '*.model3')):
            alg = QgsProcessingModelAlgorithm()
            if not alg.fromFile(filename):
                print("ERROR: Couldn't load model from {}".format(filename))
                return

            destFilename = os.path.join(ModelerUtils.modelsFolders()[0], os.path.basename(filename))
            shutil.copyfile(filename, destFilename)

        QgsApplication.processingRegistry().providerById('model').refreshAlgorithms()
