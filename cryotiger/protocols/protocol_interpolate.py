# **************************************************************************
# *
# * Author:    EP Murillo (ep.murillo@usp.ceu.es)
# * Author:    Mikel iceta (miceta@cnb.csic.es)
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 3 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************

import logging
import os
import mrcfile
import numpy as np

import pyworkflow.utils as pwutils
import pyworkflow.protocol.params as params

from pwem.protocols import EMProtocol
# TODO: Nos valdra con estas clases? Son necesarias?
from pyworkflow.object import Set, Pointer
# TODO: Nos valdra con estas clases para definir el form?
from pyworkflow.protocol import PointerParam, IntParam, GPU_LIST, \
    STEPS_PARALLEL, ProtStreamingBase

from tomo.objects import SetOfTiltSeries, TiltSeries, TiltImage

logger = logging.getLogger(__name__)

# TODO: Te vendra bien definir una clase para los modelos
# Dado que hay varios y pueden tener versiones!
# from ..objects import CryoTigerModel

class CryoTigerProtTSInterpolate(EMProtocol):
    """ Protocol to interpolate Tilt Series using CryoTIGER.
    The TS will be outputted with a higher density of TS Images, making it
    possible to get better reconstructions later on.
    """
    # TODO: Tras leer el paper y repo... 
    # Que params necesitamos en el form?
    # En que pasos se reflejaria a nivel Scipion?
    # Revisar: entrada y salida, formatos, conversiones necesarias?
    # TODO: Extra - Y si quisieramos hacerlo en streaming?
    _label = 'tilt-series interpolation'

    # -------------------------- DEFINE param functions -----------------------
    def _defineParams(self, form : params.Form):
        form.addSection(label="Main")
        # TODO: Rellenar con lo que necesita CryoTIGER para funcionar
        # form.addParam(...)
        
    # -------------------------- INSERT steps functions -----------------------
    def _insertAllSteps(self):
        self._initialize()
        # TODO: Steps entre medias para preparar
        self._insertFunctionStep(self.runCryoTigerStep)
        # TODO: Step para convertir de vuelta a Scipion si necesario
        self._insertFunctionStep(self.createOutputStep)
        pass


    # -------------------------- STEPS functions ------------------------------
    def _initialize(self):
        # Sacar los parametros del formulario a proper variables
        pass

    def convertInputStep(self):
        pass
    
    def runCryoTigerStep(self):
        pass

    def createOutputStep(self):
        pass

    # def miStep(self):
        # hacercosas...

    # -------------------------- UTILS functions ------------------------------
    def _getInTSPath(self, *args) -> str:
        return self._getExtraPath('input', *args)
    
    def _getOutputPath(self, *args) -> str:
        return "patatasfritassmmmmmquerico"

    # --------------------------- INFO functions ------------------------------
