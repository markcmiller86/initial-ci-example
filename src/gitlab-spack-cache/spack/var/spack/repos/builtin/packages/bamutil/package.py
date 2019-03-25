# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bamutil(MakefilePackage):
    """bamUtil is a repository that contains several programs
       that perform operations on SAM/BAM files. All of these programs
       are built into a single executable, bam.
    """

    homepage = "http://genome.sph.umich.edu/wiki/BamUtil"
    url      = "http://genome.sph.umich.edu/w/images/7/70/BamUtilLibStatGen.1.0.13.tgz"

    version('1.0.13', '08b7d0bb1d60be104a11f0e54ddf4a79')

    depends_on('zlib', type=('build', 'link'))

    # Looks like this will be fixed in 1.0.14.
    # https://github.com/statgen/libStatGen/issues/9
    patch('libstatgen-issue-9.patch', when='@1.0.13:')
    # These are fixed in the standalone libStatGen,
    # but bamutil@1.0.13 embeds its own copy, so fix 'em here.
    patch('libstatgen-issue-19.patch', when='@1.0.13')
    patch('libstatgen-issue-17.patch', when='@1.0.13')
    patch('libstatgen-issue-7.patch', when='@1.0.13')
    patch('verifybamid-issue-8.patch', when='@1.0.13')

    parallel = False

    @property
    def install_targets(self):
        return ['install', 'INSTALLDIR={0}'.format(self.prefix.bin)]