# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import glob


class Guidance(MakefilePackage):
    """Guidance: Accurate detection of unreliable alignment regions accounting
       for the uncertainty of multiple parameters."""

    homepage = "http://guidance.tau.ac.il/ver2/"
    url      = "http://guidance.tau.ac.il/ver2/guidance.v2.02.tar.gz"

    version('2.02', 'aa6ae2168e8e0237ee56bc2ac81202cf')

    depends_on('perl', type=('build', 'run'))
    depends_on('perl-bio-perl', type=('build', 'run'))
    depends_on('ruby')
    depends_on('prank')
    depends_on('clustalw')
    depends_on('mafft')
    depends_on('muscle')

    conflicts('%gcc@6.2.0:')

    def edit(self, spec, prefix):
        for dir in 'Guidance', 'Selecton', 'bioSequence_scripts_and_constants':
            with working_dir(join_path('www', dir)):
                files = glob.iglob('*.pl')
                for file in files:
                    perl = FileFilter(file)
                    perl.filter('#!/usr/bin/perl -w', '#!/usr/bin/env perl')

    def install(self, spac, prefix):
        mkdir(prefix.bin)
        install_tree('libs', prefix.bin.libs)
        install_tree('programs', prefix.bin.programs)
        install_tree('www', prefix.bin.www)
        with working_dir(join_path('www', 'Guidance')):  # copy without suffix
            install('guidance.pl', join_path(prefix.bin.www.Guidance,
                                             'guidance'))

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', prefix.bin.www.Guidance)