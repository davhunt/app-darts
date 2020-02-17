#!/usr/bin/env python3

import sys
import os
import numpy as np
import nibabel as nib
from DARTS import Segmentation

t1 = os.path.join(sys.argv[1],'mri','T1.nii.gz')

#seg_obj = Segmentation(model_wts_path='./saved_model_wts/dense_unet_saggital_finetuned.pth', model_type='dense-unet', use_gpu=False)
seg_obj = Segmentation(model_wts_path='/N/u/davhunt/Carbonate/app-darts/saved_model_wts/dense_unet_back2front_finetuned.pth', model_type='dense-unet', use_gpu=False)
seg_out, seg_proba_out = seg_obj.predict(t1)

t1_img = nib.load(t1)
parc_img = nib.Nifti1Image(seg_out, t1_img.affine, header=t1_img.header)
prob_map_img = nib.Nifti1Image(seg_proba_out, t1_img.affine, header=t1_img.header)

nib.save(parc_img,'parc/parc.nii.gz')
nib.save(prob_map_img, 'softmax_prob_map.nii.gz') # This is a map of the probabilities in each voxel of being in each ROI (#1-103)
