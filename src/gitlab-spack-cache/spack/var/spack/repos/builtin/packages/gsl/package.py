# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Gsl(AutotoolsPackage):
    """The GNU Scientific Library (GSL) is a numerical library for C and C++
    programmers. It is free software under the GNU General Public License. The
    library provides a wide range of mathematical routines such as random
    number generators, special functions and least-squares fitting. There are
    over 1000 functions in total with an extensive test suite."""

    homepage = "http://www.gnu.org/software/gsl"
    url      = "https://ftpmirror.gnu.org/gsl/gsl-2.3.tar.gz"

    version('2.5', sha256='0460ad7c2542caaddc6729762952d345374784100223995eb14d614861f2258d')
    version('2.4',   'dba736f15404807834dc1c7b93e83b92')
    version('2.3',   '905fcbbb97bc552d1037e34d200931a0')
    version('2.2.1', '3d90650b7cfe0a6f4b29c2d7b0f86458')
    version('2.1',   'd8f70abafd3e9f0bae03c52d1f4e8de5')
    version('2.0',   'ae44cdfed78ece40e73411b63a78c375')
    version('1.16',  'e49a664db13d81c968415cd53f62bc8b')