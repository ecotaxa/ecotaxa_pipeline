import numpy as np
import cv2
import skimage
from skimage import filters, morphology, measure, color, feature
from skimage.filters import gaussian, threshold_otsu
from scipy import ndimage, interpolate
import sys
import glob
import os
from math import pi
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import pandas as pd

def get_features(path, imag_name) :
    # get the file path of the image in the directory 
    ptf = glob.glob(path+imag_name)

    #read the image
    img = cv2.imread(ptf[0])

    # make the image gray
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # compute the edges
    edges_mag = filters.scharr(img_gray)


    # convert gray scale to binary 
    edges_med = np.median(edges_mag)

    # setting the threshhold to 3 times the median value in the array so that mask is more apt to retain edges.
    edges_thresh = 3*edges_med  
    edges = edges_mag >= edges_thresh

    # these will fill in some of the holes
    edges_closed = morphology.closing(edges, morphology.square(3))
    filled_edges = ndimage.binary_fill_holes(edges_closed)

    # erode the bloated mask
    #img_eroded = morphology.erosion(filled_edges, morphology.square(3))

    # pass the label routine the closed image to register connected regions.
    label_img = morphology.label(filled_edges, connectivity=2, background=0)
    #label_img = morphology.label(img_eroded, connectivity=2, background=0)
    lab_img_color = color.label2rgb(label_img, image=img_gray)
    regions = skimage.measure.regionprops(label_image=label_img)
    areas = [fast_particle_area(r) for r in regions]
    i = np.argmax(areas)
    im_label_one = label_img == (i+1)

    # get relevant properties for the largest object
    props = skimage.measure.regionprops_table(label_image=im_label_one.astype(np.uint8), intensity_image=img, \
    properties=('area', 'area_filled', 'axis_major_length','axis_minor_length','orientation','eccentricity','feret_diameter_max', 'centroid_local','centroid_weighted_local','moments_hu','moments_weighted_hu'))
    props = pd.DataFrame(props)
    props.head()
    props['img_file_name'] = str(imag_name)
    img_masked = get_img_masked(label_img, img_gray)
    # copy masked images 
    copy_image(path, imag_name, img_masked)
    return props

def fast_particle_area(x):
    return(np.sum(x._label_image[x._slice] == x.label))

def get_img_masked(label_img, img_gray):
    # use region props. Have it retain all the properties it can measure
    props = measure.regionprops(label_img, img_gray)
    max_area = 0
    max_area_ind = 0
    for f in range(0,len(props)):
        if props[f].area > max_area:
            max_area = props[f].area
            max_area_ind = f

    ii = max_area_ind

    # this selects only the pixels in the labeled image that are in the region with the biggest area
    bw_mask = (label_img) == props[ii].label

    # plt.figure()
    # plt.xticks([])
    # plt.yticks([])
    # plt.imshow(bw_mask, cmap='gray')
    # see the masked image
    img_masked = img_gray * bw_mask

    # plt.figure()
    # plt.xticks([])
    # plt.yticks([])
    # plt.imshow(img_masked, cmap='gray')
    return img_masked

def copy_image(path, imag_name, img_masked):
    try :
        cv2.imwrite(path+"masked_"+imag_name, img_masked)
    except Exception as e :
        print(e)