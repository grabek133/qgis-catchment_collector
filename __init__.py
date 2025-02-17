# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CatchmentCollector
                                 A QGIS plugin
 Downloads data sheets for selected catchments
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-02-17
        copyright            : (C) 2025 by DG Plugins
        email                : grabowski_darek@wp.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CatchmentCollector class from file CatchmentCollector.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .catchment_collector import CatchmentCollector
    return CatchmentCollector(iface)
