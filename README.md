<h1 align="center">DenseUnet-based Automatic Rapid Tool for brain Segmentation (DARTS)</h1>

<p align="center">
  Segments a T1-weighted image into 102 brain regions, similar to FreeSurfer aparc+aseg, with the DARTS DenseUNet deep learning model and outputs a volumetric parcellation.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.276"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.276-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Segments a T1-weighted image into 102 brain regions, similar to FreeSurfer aparc+aseg, with the DARTS DenseUNet deep learning model and outputs a volumetric parcellation.**

Runs the DARTS (DenseUnet-based Automatic Rapid Tool for brain Segmentation) pretrained dense-unet model on CPU to label a T1w image into 102 regions with a FreeSurfer-like key. Use it when a fast aparc+aseg-like parcellation is needed without running recon-all. The model weights are loaded from a fixed path on the original HPC system, so the App only runs where that path exists.

| | |
|---|---|
| **Inputs** | `neuro/anat/t1w` |
| **Outputs** | `neuro/parcellation/volume` |
| **Container** | `davhunt/darts:1.0.2` |
| **Resources** | 4 CPUs · 50 GB memory · 0.75 h walltime |
| **Requires** | `FREESURFER_LICENSE` |
| **Run it** | [doi.org/10.25663/brainlife.app.276](https://doi.org/10.25663/brainlife.app.276) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `t1` | `neuro/anat/t1w` | yes | T1-weighted image to segment. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `parc` | `neuro/parcellation/volume` | Volumetric parcellation (parc.nii.gz) in the T1w space with key.txt and label.json describing the 102 regions. |

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.276](https://doi.org/10.25663/brainlife.app.276), choose `neuro/anat/t1w` from your project and press **Execute**. The results are saved to your project as `neuro/parcellation/volume`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `davhunt/darts:1.0.2`), [`jq`](https://jqlang.github.io/jq/), `FREESURFER_LICENSE`.

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "t1": "/path/to/t1/t1"
   }
   ```

3. Run `./main`.

## Troubleshooting

- **Please set FREESURFER_LICENSE in .bashrc**: Set FREESURFER_LICENSE on the compute resource.

## Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brainlife/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download 5a05288dd76a2a002737e576 && mv 5a05288dd76a2a002737e576 input
```

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- DenseUnet-based Automatic Rapid Tool for brain Segmentation (DARTS). brainlife.io App. [doi:10.25663/brainlife.app.276](https://doi.org/10.25663/brainlife.app.276)
- Kaku A., Hegde C. V., Huang J., Chung S., Wang X., Young M., Radmanesh A., Lui Y. W., Razavian N. DARTS: DenseUnet-based Automatic Rapid Tool for Brain Segmentation. arXiv:1911.05567 (2019).
- Aakash Kaku, Chaitra V. Hegde, Jeffrey Huang, Sohae Chung, Xiuyuan Wang, Matthew Young, Alireza Radmanesh, Yvonne W. Lui, Narges Razavian. DARTS: DenseUnet-based Automatic Rapid Tool for Brain Segmentation. [https://arxiv.org/abs/1911.05567](https://arxiv.org/abs/1911.05567)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- David Hunt

#### Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
