""" Test pyfive's abililty to read multidimensional datasets. """
import os

import numpy as np
from numpy.testing import assert_array_equal

import pyfive

DIRNAME = os.path.dirname(__file__)
DATASET_COMPRESSED_HDF5_FILE = os.path.join(DIRNAME, 'compressed.hdf5')


def test_compressed_dataset():

    hfile = pyfive.File(DATASET_COMPRESSED_HDF5_FILE)

    # check data
    dset1 = hfile['dataset1']
    assert dset1.shape == (21, 16)
    assert dset1.dtype == np.dtype('<i4')
    assert_array_equal(dset1[:], np.arange(21*16).reshape((21, 16)))

    hfile.close()
