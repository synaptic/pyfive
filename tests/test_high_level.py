""" Unit tests for pyfive's high_level module. """

import os

import numpy as np
from numpy.testing import assert_array_equal, assert_almost_equal
from numpy.testing import assert_raises

import pyfive

DIRNAME = os.path.dirname(__file__)
EARLIEST_HDF5_FILE = os.path.join(DIRNAME, 'earliest.hdf5')

# Polyglot string type for representing unicode
try:
    string_type = unicode
except NameError:
    string_type = str


def test_file_class():

    hfile = pyfive.File(EARLIEST_HDF5_FILE)

    assert hfile.filename == EARLIEST_HDF5_FILE
    assert hfile.mode == 'r'
    assert hfile.userblock_size == 0
    hfile.close()


def test_group_class():

    hfile = pyfive.File(EARLIEST_HDF5_FILE)
    grp = hfile['group1']
    subgrp = grp['subgroup1']

    ################
    # class methods
    ################

    # __iter__()
    count = 0
    for i in grp:
        count += 1
    assert count == 2

    # __contains__()
    assert 'dataset2' in grp
    assert 'subgroup1' in grp
    assert 'foobar' not in grp

    # __getitem__()
    assert grp['subgroup1'].name == '/group1/subgroup1'
    assert_raises(KeyError, grp.__getitem__, 'foobar')

    # keys()
    assert 'dataset2' in grp.keys()
    assert 'subgroup1' in grp.keys()
    assert 'foobar' not in grp.keys()

    # values()
    assert len(grp.values()) == 2

    # items()
    assert len(grp.items()) == 2

    # get()
    assert grp.get('subgroup1').name == '/group1/subgroup1'
    assert grp.get('foobar') is None

    ####################
    # class attributes
    ####################
    attrs = grp.attrs
    assert isinstance(attrs, dict)
    assert_almost_equal(attrs['attr3'], 12.34, 2)
    assert attrs['attr3'].dtype == np.dtype('float32')

    assert grp.name == '/group1'
    assert grp.file is hfile
    assert grp.parent is hfile

    assert subgrp.name == '/group1/subgroup1'
    assert grp.file is hfile
    assert subgrp.parent is grp

    hfile.close()


def test_dataset_class():

    hfile = pyfive.File(EARLIEST_HDF5_FILE)
    dset1 = hfile['dataset1']
    grp = hfile['group1']
    dset2 = grp['dataset2']

    assert_array_equal(dset1[:], np.arange(4))
    assert_array_equal(dset2[:], np.arange(4))

    assert dset1.len() == 4
    assert dset2.len() == 4

    assert dset1.shape == (4, )
    assert dset2.shape == (4, )

    assert dset1.dtype == np.dtype('<i4')
    assert dset2.dtype == np.dtype('>u8')

    assert dset1.size == 4
    assert dset2.size == 4

    assert dset1.chunks is None
    assert dset2.chunks is None

    assert dset1.compression is None
    assert dset2.compression is None

    assert dset1.compression_opts is None
    assert dset2.compression_opts is None

    assert dset1.scaleoffset is None
    assert dset2.scaleoffset is None

    assert dset1.shuffle is False
    assert dset2.shuffle is False

    assert dset1.fletcher32 is False
    assert dset2.fletcher32 is False

    assert isinstance(dset1.attrs, dict)
    assert dset1.attrs['attr2'] == 130
    assert isinstance(dset2.attrs, dict)
    assert dset2.attrs['attr4'] == b'Hi'

    assert dset1.name == '/dataset1'
    assert dset2.name == '/group1/dataset2'

    assert dset1.file is hfile
    assert dset2.file is hfile

    assert dset1.parent.name == '/'
    assert dset2.parent.name == '/group1'

    hfile.close()
