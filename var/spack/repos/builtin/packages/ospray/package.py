##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install ospray
#
# You can edit this file again by typing:
#
#     spack edit ospray
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import os

class Ospray(CMakePackage):
    """build ospray"""

    homepage = "https://www.ospray.org/"
    url      = "https://github.com/ospray/OSPRay"
    #version('1.4.3',git='https://github.com/ospray/ospray.git', tag='v1.4.3')
    version('1.5.0',git='https://github.com/ospray/ospray.git', tag='v1.5.0')

    depends_on('ispc')
    depends_on('embree',type=('build','link'))

    def cmake_args(self):
        cmake_args = ['-D embree_DIR=' + self.embree_DIR
        ]
        print('-----------------------------'+ str(cmake_args))
        return cmake_args
    # def install(self, spec, prefix):
    #     #cmake("-DOSPRAY_TASKING_SYSTEM:STRING=Internal")
    #     cmake('-D embree_DIR=' + self.embree_DIR)
    #     make()
    #     #make('install')
    # def cmake_args(self):
    #     spec = self.spec

    #     cmake_args = [
    #         '-DOSPRAY_TASKING_SYSTEM:STRING=Internal',
    #     ]
    def setup_environment(self, spack_env, run_env):
        self.embree_DIR = self.spec.embree_DIR
            