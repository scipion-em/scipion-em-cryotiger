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

import pwem
import pyworkflow.utils as pwutils

from .constants import *

__version__ = '3.0.0'
_logo = ""
_references = ['turonova2024']

class Plugin(pwem.Plugin):

    @classmethod
    def getCryoTigerEnvActivation(cls):
        return cls.getVar(CRYOTIGER_ENV_ACTIVATION)
    
    @classmethod
    def getModelFn(cls, modelKey):
        return os.path.abspath(str(cls.getVar(modelKey)))
    
    @classmethod
    def getDependencies(cls):
        """ Return a list of dependencies. Include conda if
            activation command was not found. """
        condaActivationCmd = cls.getCondaActivationCmd()
        neededProgs = ['wget']
        if not condaActivationCmd:
            neededProgs.append('conda')

        return neededProgs
    
    @classmethod
    def runCryoTiger(cls, protocol, program, args, cwd=None, useCpu=False):
        """ Run CryoTiger command from a given protocol. """
        fullProgram = '%s %s && %s' % (cls.getCondaActivationCmd(),
                                       cls.getCryoTigerEnvActivation(), program)
        protocol.runJob(fullProgram, args, env=cls.getEnviron(), cwd=cwd,
                        numberOfMpi=1)