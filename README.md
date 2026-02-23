# DBS-Visualization
This repository documents a patient-specific deep brain stimulation (DBS) visualization pipeline, covering imaging, electrode localization, tissue segmentation, electric field simulation, and tractography

<img width="600" height="422" alt="Head 4" src="https://github.com/user-attachments/assets/68c9de37-4319-43c1-9837-1f8811810d39" />


## Project Overview
1. Localize DBS electrodes from post-op CT and pre-op MRI 
2. Build patient-specific tissue conductivity models 
3. Simulate electric fields and VTA using finite-element methods 
4. Compare contact-level stimulation configurations (mono/bipolar)
5. Estimate tractography using dMRI

<img width="881" height="114" alt="image" src="https://github.com/user-attachments/assets/a62c810d-5f72-413f-87cf-f8dd85410fce" />


### Tools & Frameworks
This pipeline integrates:
- Imaging and electrode localization using
  [3D Slicer](https://www.slicer.org/)
- MRI-based tissue segmentation with
  [FastSurfer](https://github.com/Deep-MI/FastSurfer)
- Finite-element electric-field simulation via
  [OSS-DBS](https://github.com/SFB-ELAINE/OSS-DBSv2)
- Diffusion MRI processing and tractography with
  [MRtrix3](https://www.mrtrix.org/)

---
### 📄 Detailed pipeline & setup: [Pipeline](docs/pipeline.md), [Tractography](docs/Tractography.md)  
### ⚙️ Stimulation configuration examples: [Stimulation Configs](docs/stimulation_configs.md)

