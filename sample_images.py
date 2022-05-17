import random
import shutil
import glob
import os


def sample_images():
    root_folder = f"/home/projects/talide/splicing_shape_texture/shir/htmls/baselines/sd_horses_inference/splice"
    target_folder = "./splice"
#     indices =  [110, 119, 122, 135, 149, 164, 171, 186, 193, 197, 202, 208, 215, 222, 229, 247, 264, 275, 277 ]
    indices = [1,10,16, 23,25, 28,29, 34, 37, 43, 45,47,59, 67, 72, 74, 99 ]
    cur_idx = 37

    for idx in indices:
#         shutil.copy(f"{root_folder}/ours/{idx}.png", f"{target_folder}/ours/{cur_idx}.png")
#         shutil.copy(f"{root_folder}/wct2/{idx}.png", f"{target_folder}/wct2/{cur_idx}.png")
#         shutil.copy(f"{root_folder}/SA/{idx}.png", f"{target_folder}/sa/{cur_idx}.png")
#         shutil.copy(f"{root_folder}/korean/{idx}.png", f"{target_folder}/sd/{cur_idx}.png")
        shutil.copy(f"{root_folder}/splice/{idx}.png", f"{target_folder}/splice/{cur_idx}.png")
#         shutil.copy(f"{root_folder}/appearance/{idx}.png", f"{target_folder}/structures/{cur_idx}.png")
#         shutil.copy(f"{root_folder}/structure/{idx}.png", f"{target_folder}/textures/{cur_idx}.png")
        cur_idx += 1


sample_images()
