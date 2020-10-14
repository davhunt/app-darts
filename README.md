[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.276-blue.svg)](https://doi.org/10.25663/bl.app.276)

# app-DARTS

This app performs a deep learning-based segmentation of an anatomical T1-weighted MR image into 102 brain regions, similar to Freesurfer's aparc+aseg. The segmentation is quicker than a typical Freesurfer recon-all. The app requires a T1 image and outputs a parcellation of the image.

The method is described in [this paper](https://arxiv.org/abs/1911.05567) and [this github repo](https://github.com/NYUMedML/DARTS).

### Authors
- [David Hunt](davhunt@iu.edu)

#### Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your code and publications. Copy and past the following lines into your repository when using this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations

1. Aakash Kaku, Chaitra V. Hegde, Jeffrey Huang, Sohae Chung, Xiuyuan Wang, Matthew Young, Alireza Radmanesh, Yvonne W. Lui, Narges Razavian. DARTS: DenseUnet-based Automatic Rapid Tool for Brain Segmentation. [https://arxiv.org/abs/1911.05567](https://arxiv.org/abs/1911.05567)

## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/bl.app.276](https://doi.org/10.25663/bl.app.276) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
  "t1": "./input/t1.nii.gz"
}
```

3. Launch the App by executing `main`

```bash
./main
```

### Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brain-life/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download 5a05288dd76a2a002737e576 && mv 5a05288dd76a2a002737e576 input
```

## Output

All output files will be generated under the current working directory (pwd). The main output of this App is a folder called `parc` that contains a parcellation parc.nii.gz and a key key.txt with the corresponding brain areas / labels.
```
    .
    ├── parc
    │   ├── parc.nii.gz
    │   ├── key.txt
```

### Dependencies

This App requires [singularity](https://www.sylabs.io/singularity/) to run.
