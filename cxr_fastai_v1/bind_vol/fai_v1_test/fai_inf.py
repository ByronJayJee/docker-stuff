# This module contains routines used for basic image data manipulation
from PIL import Image
import re
from io import BytesIO
import base64

from fastai import *
from fastai.vision import *

'''
from fastai.transforms import *
from fastai.model import *
from fastai.dataset import *
from fastai.conv_learner import *
from fastai.sgdr import *
from fastai.plots import *
'''

def img_inf(img_path):
    '''
    Takes an image and runs it through a trained ResNext model using the fastai framework

    Input
    :img_path: string, the path to the image

    Returns
    :prob: float, the probability that the image is drug resistant
    '''
    sz = 340
    arch = 'resnext101_64'
    learn = ConvLearner.load('./models/latest')
    '''
    trn_tfms, val_tfms = tfms_from_model(arch, sz)
    im = val_tfms(open_image(img_path))
    preds = learn.predict_array(im[None])
    probs = np.exp(preds) # probs[0] is the probability of resistance, probs[1] is the probability of sensitivity
    
    return probs[0]
    '''

print('Starting Fastai V1 Inference')
img_inf('./test.png')
