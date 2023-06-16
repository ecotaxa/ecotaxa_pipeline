import plotly
import plotly.express as px
import plotly.graph_objects as go
from skimage import filters, measure, morphology
from PIL import Image
import numpy as np

path= "/Users/jcoustenoble/Desktop/CPICS_RAW/WORKSHOP_SMALL_CPICS_PROJECT/cpics/rois/20191128/20191128_0000"
#img_path = path+"20191124_211829.122.1.png"
img_path = path+"/20191128_001913.653.0.png"

img_color  = np.array(Image.open(img_path))
img = np.dot(img_color[...,:3], [0.2989, 0.5870, 0.1140])

# Binary image, post-process the binary mask and compute labels
threshold = filters.threshold_otsu(img)
print(threshold)
mask = img > threshold
mask = morphology.remove_small_objects(mask, 150)
mask = morphology.remove_small_holes(mask, 150)

# Binary image, post-process the binary mask and compute labels
# threshold = filters.threshold_otsu(img)
# mask = img > 50#threshold
# mask = morphology.remove_small_objects(mask, 150)
#mask = morphology.remove_small_holes(mask, 150)

labels = measure.label(mask)

fig = px.imshow(img, binary_string=True)
fig.update_traces(hoverinfo='skip') # hover is only for label info

props = measure.regionprops(labels, img)
#properties = ['area', 'eccentricity', 'perimeter', 'intensity_mean']
properties=['area', 'area_filled', 'perimeter', 'axis_major_length', 'axis_minor_length', 'eccentricity', 'orientation', 'feret_diameter_max', 'centroid_local', 'centroid_weighted_local', 'intensity_max', 'intensity_mean', 'intensity_min', 'moments_hu', 'moments_weighted_hu', 'solidity']
print(props)
# For each label, add a filled scatter trace for its contour,
# and display the properties of the label in the hover of this trace.
for index in range(1, labels.max()):
    label_i = props[index].label
    contour = measure.find_contours(labels == label_i, 0.5)[0]
    y, x = contour.T
    hoverinfo = ''
    for prop_name in properties:
        #print(prop_name, " : ",getattr(props[index], prop_name))
        hoverinfo += f'<b>{prop_name}: {getattr(props[index], prop_name)}</b><br>'
    fig.add_trace(go.Scatter(
        x=x, y=y, name=label_i,
        mode='lines', fill='toself', showlegend=False,
        hovertemplate=hoverinfo, hoveron='points+fills'))

plotly.io.show(fig)
