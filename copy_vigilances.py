import shutil

vigilance_indices = [10, 21, 32, 43]
img_1_indices = [0, 2, 4, 14]
img_2_indices = [1, 3, 6, 16]

for i in range(4):
    v_idx = vigilance_indices[i]
    i1_idx = img_1_indices[i]
    i2_idx = img_2_indices[i]
    im1 = f"../shir/htmls_80/inputs/sd_horses_inference/structure/{i1_idx}.jpg"
    im2 = f"../shir/htmls_80/inputs/sd_horses_inference/structure/{i2_idx}.jpg"
    shutil.copy(im1, f"./sd_horses/structures/{v_idx}.jpg")
    shutil.copy(im1, f"./sd_horses/textures/{v_idx}.jpg")
    shutil.copy(im1, f"./sd_horses/ours/{v_idx}.jpg")
    shutil.copy(im2, f"./sd_horses/sa/{v_idx}.jpg")
    shutil.copy(im2, f"./sd_horses/sd/{v_idx}.jpg")
#     shutil.copy(im2, f"./sd_dogs/splice/{v_idx}.jpg")
    shutil.copy(im2, f"./sd_horses/wct2/{v_idx}.jpg")
