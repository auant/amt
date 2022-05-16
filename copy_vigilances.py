import shutil

vigilance_indices = [10, 21, 32, 43]
img_1_indices = [0, 2, 4, 6]
img_2_indices = [1, 3, 5, 7]

for i in range(4):
    v_idx = vigilance_indices[i]
    i1_idx = img_1_indices[i]
    i2_idx = img_2_indices[i]
    im1 = f"../shir/htmls_80/inputs/sd_dogs_inference/structure/{i1_idx}.jpg"
    im2 = f"../shir/htmls_80/inputs/sd_dogs_inference/structure/{i2_idx}.jpg"
    shutil.copy(im1, f"./sd_dogs/structures/{v_idx}.jpg")
    shutil.copy(im1, f"./sd_dogs/textures/{v_idx}.jpg")
    shutil.copy(im1, f"./sd_dogs/ours/{v_idx}.jpg")
    shutil.copy(im2, f"./sd_dogs/sa/{v_idx}.jpg")
    shutil.copy(im2, f"./sd_dogs/sd/{v_idx}.jpg")
#     shutil.copy(im2, f"./sd_dogs/splice/{v_idx}.jpg")
    shutil.copy(im2, f"./sd_dogs/wct2/{v_idx}.jpg")
