#!/usr/bin/env python3

import sys
import numpy as np
import nibabel as nib
from DARTS import Segmentation

#seg_obj = Segmentation(model_wts_path='./saved_model_wts/dense_unet_saggital_finetuned.pth', model_type='dense-unet', use_gpu=False)
seg_obj = Segmentation(model_wts_path='/N/u/davhunt/Carbonate/app-darts/saved_model_wts/dense_unet_saggital_finetuned.pth', model_type='dense-unet', use_gpu=False)
seg_out, seg_proba_out = seg_obj.predict(inputs=sys.argv[1])

nib.save(seg_out,'parc/parc.nii.gz')
nib.save(seg_proba_out, 'softmax_prob_map.nii.gz')
