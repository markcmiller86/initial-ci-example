# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

import pytest

from llnl.util.filesystem import working_dir, touch

import spack.repo
import spack.config
from spack.spec import Spec
from spack.version import ver
from spack.util.executable import which


pytestmark = pytest.mark.skipif(
    not which('hg'), reason='requires mercurial to be installed')


@pytest.mark.parametrize("type_of_test", ['default', 'rev0'])
@pytest.mark.parametrize("secure", [True, False])
def test_fetch(
        type_of_test,
        secure,
        mock_hg_repository,
        config,
        mutable_mock_packages
):
    """Tries to:

    1. Fetch the repo using a fetch strategy constructed with
       supplied args (they depend on type_of_test).
    2. Check if the test_file is in the checked out repository.
    3. Assert that the repository is at the revision supplied.
    4. Add and remove some files, then reset the repo, and
       ensure it's all there again.
    """
    # Retrieve the right test parameters
    t = mock_hg_repository.checks[type_of_test]
    h = mock_hg_repository.hash

    # Construct the package under test
    spec = Spec('hg-test')
    spec.concretize()
    pkg = spack.repo.get(spec)
    pkg.versions[ver('hg')] = t.args

    # Enter the stage directory and check some properties
    with pkg.stage:
        with spack.config.override('config:verify_ssl', secure):
            pkg.do_stage()

        with working_dir(pkg.stage.source_path):
            assert h() == t.revision

            file_path = os.path.join(pkg.stage.source_path, t.file)
            assert os.path.isdir(pkg.stage.source_path)
            assert os.path.isfile(file_path)

            os.unlink(file_path)
            assert not os.path.isfile(file_path)

            untracked_file = 'foobarbaz'
            touch(untracked_file)
            assert os.path.isfile(untracked_file)
            pkg.do_restage()
            assert not os.path.isfile(untracked_file)

            assert os.path.isdir(pkg.stage.source_path)
            assert os.path.isfile(file_path)

            assert h() == t.revision