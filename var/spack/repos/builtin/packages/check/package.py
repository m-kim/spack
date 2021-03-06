##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the LICENSE file for our notice and the LGPL.
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
from spack import *


class Check(AutotoolsPackage):
    """Check is a unit testing framework for C. It features a simple interface
    for defining unit tests, putting little in the way of the developer. Tests
    are run in a separate address space, so both assertion failures and code
    errors that cause segmentation faults or other signals can be caught. Test
    results are reportable in the following: Subunit, TAP, XML, and a generic
    logging format."""

    homepage = "https://libcheck.github.io/check/index.html"
    url      = "https://downloads.sourceforge.net/project/check/check/0.10.0/check-0.10.0.tar.gz"

    version('0.10.0', '53c5e5c77d090e103a17f3ed7fd7d8b8')
