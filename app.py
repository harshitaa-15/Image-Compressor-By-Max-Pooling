import streamlit as st
import numpy as np
from PIL import Image

#=============================================================
#                         ALGORITHM
#=============================================================


def image_compression_algorithm(arr, stride_x, stride_y, sub_rows, sub_cols):
    rows, cols = arr.shape 

    max_pooling_rows = int(np.floor((rows - sub_rows) / stride_x ) + 1 )
    max_pooling_cols = int(np.floor((cols - sub_cols) / stride_y ) + 1 )                     

    max_pooling_array = np.zeros((max_pooling_rows, max_pooling_cols))

    rr = 0
    for i in range (0, rows - sub_rows + 1, stride_x ):
        cc = 0
        for j in range(0, cols - sub_cols + 1, stride_y):
            max_pooling_array[rr][cc] = np.max(arr[0 + i : 3 + i, 0 + j : 3 + j])
            cc = cc + 1
        rr = rr + 1

    return max_pooling_array

#==============================================================
#                     Page Configuration
#==============================================================

page_config = st.set_page_config(
    page_title = "Image Compression Using Max Pooling",
    page_icon = "✨"
)

#==============================================================
#                    Main Page UI
#==============================================================

st.image("img_compressor1.png")
st.title("✨Compress Your Image!")
st.info("An app for compressing Images using the Max Pooling Technique.")
st.markdown("---")

upload_image = st.file_uploader("Upload Your Image", type = ["jpg","jpeg", "png"])
st.markdown("---")

if upload_image:
    img = Image.open(upload_image)
    img_array = np.array(img)
    R_array = img_array[:, :, 0]
    G_array = img_array[:, :, 1]
    B_array = img_array[:, :, 2]

    R_max_pooling = image_compression_algorithm(R_array, 3, 3, 3, 3)
    G_max_pooling = image_compression_algorithm(G_array, 3, 3, 3, 3)
    B_max_pooling = image_compression_algorithm(B_array, 3, 3, 3, 3)

    stacked_array = np.dstack((R_max_pooling, G_max_pooling, B_max_pooling ))

    new_image = Image.fromarray(stacked_array.astype(np.uint8))

    cols = st.columns(2)

    with cols[0]:
        st.success("#### Before Compression")
        st.image(img)
        row, col = img.size
        st.info(f"{((row * col) / (1024 * 1024)):.2f} MB")
    with cols[1]:
        st.success("#### After Compression")
        st.image(new_image)
        row, col = new_image.size
        st.info(f"{((row * col) / (1024 * 1024)):.4f} MB")






