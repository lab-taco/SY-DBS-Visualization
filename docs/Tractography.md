# 7T dMRI → MRtrix (CSD) → Tractography
Tractography results are stored separately because it uses a diffusion MRI data, which is not part of the main pipeline inputs.

## Data Source
Diffusion MRI data were obtained from the following public dataset:

- https://purl.stanford.edu/ng782rw8378


## Tractography Estimation

- Whole-brain tractography was generated from diffusion MRI using MRtrix.
- The total number of streamlines was specified explicitly  
  (e.g., **1,000,000 streamlines** were generated in this experiment).
- Streamlines can be selectively filtered based on anatomical masks:
  
  - Streamlines **passing through** a given mask
  - Streamlines **excluding** a given mask

---

## Relation to DBS Pipelines

- In many DBS studies (e.g., Lead-DBS), **normative connectomes** are commonly used.
- In such cases, tractography is **not estimated directly from patient diffusion MRI**.
- But for a more patient-specific approach, **patient-derived tracts** were used to incorporate individual white-matter anatomy into the DBS personalization framework

---

## Anatomical Masks from FastSurfer

To enable anatomically informed tract selection:

- Large-scale anatomical masks were generated from **T1-weighted MRI** using FastSurfer.
- These masks were used to filter tractography results via MRtrix.

<img width="800" height="570" alt="image" src="https://github.com/user-attachments/assets/d30fa2a4-4322-44f4-9b7a-6222ae3bf323" />


### Notes on Mask Resolution
- The FastSurfer-derived masks provide **large subcortical structures**.
- Fine-grained DBS-relevant nuclei (e.g., **STN**, **GPi/GPe subdivisions**) are **not included**.
- The masks are therefore suitable for **coarse anatomical filtering**, but not for precise DBS target delineation.

---


## Example: Pallidal Tract Selection

An example of tractography filtered using a pallidum mask is shown below:


<img width="800" height="570" alt="tract" src="https://github.com/user-attachments/assets/59bdbfab-bda1-4d34-9f60-58fd35e10aed" />

