# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RGgplot2(RPackage):
    """An implementation of the grammar of graphics in R. It combines the
    advantages of both base and lattice graphics: conditioning and shared axes
    are handled automatically, and you can still build up a plot step by step
    from multiple data sources. It also implements a sophisticated
    multidimensional conditioning system and a consistent interface to map data
    to aesthetic attributes. See http://ggplot2.org for more information,
    documentation and examples."""

    homepage = "http://ggplot2.org/"
    url      = "https://cran.r-project.org/src/contrib/ggplot2_2.2.1.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/ggplot2"

    version('2.2.1', '14c5a3507bc123c6e7e9ad3bef7cee5c')
    version('2.1.0', '771928cfb97c649c720423deb3ec7fd3')

    depends_on('r@3.1:')

    depends_on('r-digest', type=('build', 'run'))
    depends_on('r-gtable@0.1.1:', type=('build', 'run'))
    depends_on('r-mass', type=('build', 'run'))
    depends_on('r-plyr@1.7.1:', type=('build', 'run'))
    depends_on('r-reshape2', type=('build', 'run'))
    depends_on('r-scales@0.4.1:', type=('build', 'run'))
    depends_on('r-tibble', type=('build', 'run'))
    depends_on('r-lazyeval', type=('build', 'run'))