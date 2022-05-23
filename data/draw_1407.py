import os, sys
sys.path.insert(0, os.path.abspath(".."))
from analysis.annotations import draw_images, random_colors, read_vatic
import glog as log
from glob import glob
from skimage.io import imread

image_paths = glob("001407/*.jpg")
image_paths.sort(key=lambda k: int(os.path.basename(k).split(".")[0]))
print("# Frames = {}".format(len(image_paths)))

nf = len(image_paths)
if not os.path.exists("1407_annotated"):
    os.makedirs("1407_annotated")
a = read_vatic("1407.txt")
cs = random_colors(N=len(a), bright=True)
for i in range(nf):
    img = imread(image_paths[i])
    attrs = []
    boxes = []
    labels = []
    colors = []
    tidx = []
    j = 0
    for t in a:
        for f in a[t]["frames"]:
            if f == i and a[t]["frames"][f]["visible"]:
                boxes.append(a[t]["frames"][f]["box"])
                attrs.append(a[t]["frames"][f]["attribute"])
                labels.append(a[t]["label"])
                colors.append(cs[t])
                tidx.append(t)
                j += 1
                break
        j += 1
    log.info(len(boxes))
    fig = draw_images(img, boxes, labels, attrs, colors, tidx)
    fig.savefig("1407_annotated/{}.jpg".format(i), dpi=300)
