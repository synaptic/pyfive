#! /usr/bin/env python

""" Create a HDF5 file with all the supported attribute types. """
import h5py
import numpy as np


f = h5py.File('attr_datatypes.hdf5', 'w')
attrs = f.attrs

# intergers
attrs.create('int08_little', -123, dtype='<i1')
attrs.create('int16_little', -123, dtype='<i2')
attrs.create('int32_little', -123, dtype='<i4')
attrs.create('int64_little', -123, dtype='<i8')

attrs.create('uint08_little', 130, dtype='<u1')
attrs.create('uint16_little', 32770, dtype='<u2')
attrs.create('uint32_little', 2147483650, dtype='<u4')
attrs.create('uint64_little', 9223372036854775810, dtype='<u8')

attrs.create('int08_big', -123, dtype='>i1')
attrs.create('int16_big', -123, dtype='>i2')
attrs.create('int32_big', -123, dtype='>i4')
attrs.create('int64_big', -123, dtype='>i8')

attrs.create('uint08_big', 130, dtype='>u1')
attrs.create('uint16_big', 32770, dtype='>u2')
attrs.create('uint32_big', 2147483650, dtype='>u4')
attrs.create('uint64_big', 9223372036854775810, dtype='>u8')

# floating point
attrs.create('float32_little', 123, dtype='<f4')
attrs.create('float64_little', 123, dtype='<f8')

attrs.create('float32_big', 123, dtype='>f4')
attrs.create('float64_big', 123, dtype='>f8')

# fixed-length strings
attrs.create('string_one', b'H', dtype='|S1')
attrs.create('string_two', b'Hi', dtype='|S2')

# variable length strings
attrs['vlen_string'] = b'Hello'

# variable length unicode
attrs['vlen_unicode'] = u'Hello' + chr(0x00A7)

# TODO more complex datatypes
# complex H5T_COMPOUND
#attrs.create('complex64_little', 123+456.j, dtype='<c8')
#attrs.create('complex128_little', 123+456.j, dtype='<c16')

#attrs.create('complex64_big', 123+456.j, dtype='<c8')
#attrs.create('complex128_big', 123+456.j, dtype='<c16')

# booleans  HT5_ENUM
#attrs.create('bool', True, dtype=np.bool_)

# arrayed numeric types

# arrayed variable length strings

f.close()
