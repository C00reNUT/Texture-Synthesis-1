from skimage import io
import os

NEW_IMG_SIZE = (256, 256)
WIN_SIZE = 5

# Values described here: https://people.eecs.berkeley.edu/~efros/research/NPS/alg.html
SIGMA = WIN_SIZE / 6.4
ERR_THOLD = 1e-1
MAX_ERR_THOLD = 3e-1


def read_texs():
    """
    Compiles a dict with the format filename:image
    for all the textures in the /textures folder
    """
    texs = {}
    d = os.path.dirname(os.path.realpath(__file__))
    tex_path = os.path.join(d, "textures")
    for filename in os.listdir(tex_path):
        name = filename.split(".")[0]
        texs[name] = io.imread(fname=os.path.join(
            tex_path, filename), as_gray=True)
    return texs
