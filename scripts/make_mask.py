import nibabel as nib
import numpy as np

# 1. Input & output paths
in_path  = "aparc.DKTatlas+aseg.deep.mgz"   # or aseg.auto_noCCseg.mgz
out_path = "ossdbs_segmask.nii.gz"

# 2. Load FastSurfer aseg
seg_img  = nib.load(in_path)
seg_data = seg_img.get_fdata().astype(np.int32)

# 3. Create empty mask
mask = np.zeros_like(seg_data, dtype=np.int16)

# ---- MATERIAL LABEL GROUPS ----

# Gray matter labels (common FS labels)
gray_labels = [
    3, 42,                # cerebral cortex L/R
    8, 47,                # cerebellar cortex L/R
    10, 11, 12, 13,       # thal, caud, put, pall L
    49, 50, 51, 52,       # thal, caud, put, pall R
    17, 18, 53, 54,       # hippo, amyg L/R
    26, 58,               # accumbens L/R
    28, 60,               # ventralDC L/R
    16                    # brainstem
]

# White matter labels
white_labels = [
    2, 41,                # cerebral WM L/R
    7, 46,                # cerebellar WM L/R
    251, 252, 253
]

# CSF / ventricles
csf_labels = [
    4, 43, 5, 44,         # lateral & inferior ventricles
    14,                   # 4th ventricle
    24,                   # CSF
    31, 63                # choroid plexus L/R
]

# 4. Apply mapping
mask[np.isin(seg_data, gray_labels)] = 1
mask[np.isin(seg_data, white_labels)] = 2
mask[np.isin(seg_data, csf_labels)]  = 3

# 5. Save as .nii.gz
out_img = nib.Nifti1Image(mask, seg_img.affine, seg_img.header)
nib.save(out_img, out_path)

print(">>> Saved OSS-DBS mask to:", out_path)
