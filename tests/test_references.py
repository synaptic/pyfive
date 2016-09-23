""" Unit tests for pyfive. """
import os

import numpy as np
from numpy.testing import assert_array_equal

import pyfive

DIRNAME = os.path.dirname(__file__)
REFERENCES_HDF5_FILE = os.path.join(DIRNAME, 'references.hdf5')


def test_reference_attrs():

    hfile = pyfive.File(REFERENCES_HDF5_FILE)

    root_ref = hfile.attrs['root_group_reference']
    dset_ref = hfile.attrs['dataset1_reference']
    group_ref = hfile.attrs['group1_reference']

    # check references
    root = hfile[root_ref]
    assert root.attrs['root_attr'] == 123

    dset1 = hfile[dset_ref]
    assert_array_equal(dset1[:], [0, 1, 2, 3])
    assert dset1.attrs['dset_attr'] == 456

    group = hfile[group_ref]
    assert group.attrs['group_attr'] == 789

    hfile.close()


def test_reference_dataset():

    hfile = pyfive.File(REFERENCES_HDF5_FILE)

    ref_dataset = hfile['ref_dataset']
    root_ref = ref_dataset[0]
    dset_ref = ref_dataset[1]
    group_ref = ref_dataset[2]
    null_ref = ref_dataset[3]

    # check references
    root = hfile[root_ref]
    assert root.attrs['root_attr'] == 123

    dset1 = hfile[dset_ref]
    assert_array_equal(dset1[:], [0, 1, 2, 3])
    assert dset1.attrs['dset_attr'] == 456

    group = hfile[group_ref]
    assert group.attrs['group_attr'] == 789

    assert bool(root_ref)
    assert bool(dset_ref)
    assert bool(group_ref)
    assert not bool(null_ref)

    hfile.close()


# Region Reference not yet supported by pyfive
"""
def test_region_reference_dataset():

    hfile = pyfive.File(REFERENCES_HDF5_FILE)

    regionref_dataset = hfile['regionref_dataset']
    region_ref = regionref_dataset[0]
    null_ref = regionref_dataset[1]

    assert bool(region_ref)
    assert not bool(null_ref)

    hfile.close()


def test_region_reference_attrs():

    hfile = pyfive.File(REFERENCES_HDF5_FILE)
    region_ref = hfile.attrs['dataset1_region_reference']

    dset1 = hfile['dataset1']
    subset = dset1[region_ref]
    assert_array_equal(subset, [0, 2])

    hfile.close()
"""
