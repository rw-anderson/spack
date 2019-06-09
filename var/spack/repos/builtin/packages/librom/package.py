# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import glob


class Librom(AutotoolsPackage):
    """libROM: library for computing large-scale reduced order models"""

    homepage = "https://github.com/LLNL/libROM"
    git      = "https://github.com/LLNL/libROM.git"

    version('develop', branch='automake-dev')

    depends_on('lapack')
    depends_on('mpi')
    depends_on('zlib')
    depends_on('libszip')
    depends_on('hdf5~mpi+cxx')
    depends_on('perl')
    depends_on('graphviz')
    depends_on('doxygen')
    depends_on('boost')

    depends_on('autoconf')
    depends_on('automake')
    depends_on('libtool')
    depends_on('m4')

    def autoreconf(self,spec,args):
        bash = which('bash')
        bash('./autogen.sh')

    def configure_args(self):
        spec = self.spec
        args = ['--with-hdf5={0}/h5cc'.format(spec['hdf5'].prefix.bin),
                '--with-lapack={0}'.format(spec['lapack'].prefix),
                '--with-mpi={0}'.format(spec['mpi'].prefix),
                '--with-perl={0}'.format(spec['perl'].prefix),
                '--with-doxygen={0}'.format(spec['doxygen'].prefix)]
        return args
