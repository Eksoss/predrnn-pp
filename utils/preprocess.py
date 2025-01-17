__author__ = 'yunbo'

import numpy as np

def reshape_patch(img_tensor, patch_size):
    assert 5 == img_tensor.ndim
    batch_size = np.shape(img_tensor)[0]
    seq_length = np.shape(img_tensor)[1]
    img_height = np.shape(img_tensor)[2]
    img_width = np.shape(img_tensor)[3]
    num_channels = np.shape(img_tensor)[4]
    a = np.reshape(img_tensor, [int(batch_size), int(seq_length),
                                int(img_height/patch_size), int(patch_size),
                                int(img_width/patch_size), int(patch_size),
                                int(num_channels)])
    b = np.transpose(a, [0,1,2,4,3,5,6])
    patch_tensor = np.reshape(b, [int(batch_size), int(seq_length),
                                  int(img_height/patch_size),
                                  int(img_width/patch_size),
                                  int(patch_size*patch_size*num_channels)])
    return patch_tensor

def reshape_patch_back(patch_tensor, patch_size):
    assert 5 == patch_tensor.ndim
    batch_size = np.shape(patch_tensor)[0]
    seq_length = np.shape(patch_tensor)[1]
    patch_height = np.shape(patch_tensor)[2]
    patch_width = np.shape(patch_tensor)[3]
    channels = np.shape(patch_tensor)[4]
    img_channels = channels / (patch_size*patch_size)
    a = np.reshape(patch_tensor, [int(batch_size), int(seq_length),
                                  int(patch_height), int(patch_width),
                                  int(patch_size), int(patch_size),
                                  int(img_channels)])
    b = np.transpose(a, [0,1,2,4,3,5,6])
    img_tensor = np.reshape(b, [int(batch_size), int(seq_length),
                                int(patch_height * patch_size),
                                int(patch_width * patch_size),
                                int(img_channels)])
    return img_tensor

