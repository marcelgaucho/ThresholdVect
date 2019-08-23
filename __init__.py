# -*- coding: utf-8 -*-
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
def classFactory(iface):
    from .threshold_vect_plugin import ThresholdVect
    return ThresholdVect(iface)
