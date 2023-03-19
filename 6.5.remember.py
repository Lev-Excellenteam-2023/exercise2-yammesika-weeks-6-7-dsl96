import numpy as np
from PIL import Image


def img_encode(txt, path = None):
    matrix = np.array([[255] * len(txt) for _ in range(ord('z'))])

    for i in range(len(txt)):
        matrix[ord(txt[i])][i] = 1

    im = Image.fromarray(matrix)
    im.show()

    if path:
        im.save(os.path.join(path, code_img.jpg))

    return im


def decode_img(im):
    np_img_trans = np.array(im).transpose()

    ans = []
    for row in np_img_trans:
        if 1 in row:
            ans.append(chr(np.where(row == 1)[0][0]))

    return ''.join(ans)


im = img_encode( "n na nach nachma nchman")
print(decode_img(im))
