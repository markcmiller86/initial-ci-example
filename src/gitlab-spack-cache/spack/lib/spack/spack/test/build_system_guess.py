# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import pytest
import spack.cmd.create
import spack.util.executable
import spack.stage


@pytest.fixture(
    scope='function',
    params=[
        ('configure',      'autotools'),
        ('CMakeLists.txt', 'cmake'),
        ('project.pro',    'qmake'),
        ('SConstruct',     'scons'),
        ('waf',            'waf'),
        ('setup.py',       'python'),
        ('NAMESPACE',      'r'),
        ('WORKSPACE',      'bazel'),
        ('Makefile.PL',    'perlmake'),
        ('Build.PL',       'perlbuild'),
        ('GNUmakefile',    'makefile'),
        ('makefile',       'makefile'),
        ('Makefile',       'makefile'),
        ('meson.build',    'meson'),
        ('foobar',         'generic')
    ]
)
def url_and_build_system(request, tmpdir):
    """Sets up the resources to be pulled by the stage with
    the appropriate file name and returns their url along with
    the correct build-system guess
    """
    tar = spack.util.executable.which('tar')
    orig_dir = tmpdir.chdir()
    filename, system = request.param
    tmpdir.ensure('archive', filename)
    tar('czf', 'archive.tar.gz', 'archive')
    url = 'file://' + str(tmpdir.join('archive.tar.gz'))
    yield url, system
    orig_dir.chdir()


def test_build_systems(url_and_build_system):
    url, build_system = url_and_build_system
    with spack.stage.Stage(url) as stage:
        stage.fetch()
        guesser = spack.cmd.create.BuildSystemGuesser()
        guesser(stage, url)
        assert build_system == guesser.build_system