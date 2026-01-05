## Software Dependencies

This pipeline relies on the following external software packages:

- **3D Slicer**  
  https://www.slicer.org/

- **FastSurfer**  
  https://github.com/Deep-MI/FastSurfer

- **OSS-DBS (v2)**  
  https://github.com/SFB-ELAINE/OSS-DBSv2  

  OSS-DBS is used for finite-element electric-field simulations.
  This repository does not redistribute OSS-DBS source code.
  Users are expected to install and run OSS-DBS separately.

- **MRtrix3** (for diffusion MRI tractography)  
  https://www.mrtrix.org/

---

## A. Imaging & Electrode Localization

1. Load **T1** MRI(Pre-op) and **CT**(Post-op) to 3D Slicer
    - Data used: [Lead-Tutor: An open-access educational resource for deep brain stimulation electrode localizations](https://apertureneuro.org/article/129658-lead-tutor-an-open-access-educational-resource-for-deep-brain-stimulation-electrode-localizations)
    
2. **Register CT → T1** using *General Registration (BRAINS)*.
    - *All subsequent data will be aligned to **T1 space**.*
3. **Segment Left and Right electrodes** from CT.
    - Threshold → clean with paint/erase
    - Keep Left/Right in separate segments
    - Tutorial on segmentation: https://www.youtube.com/watch?v=ZRYMItzwg8g
    - Export electrode segmentation to a model(.vtk) inside segmentation module  
   
    <img width="600" height="370" alt="image" src="https://github.com/user-attachments/assets/2017da24-c80d-446d-bd83-027a47336a0a" />

    
4. **Create a Markups point list** for each electrode.
5. **Place 3 fiducials** for each electrode:
    - Tip point = for **TipPosition**
    - Point on middle of shaft = for **Direction**
    - Point for the end of the electrode (Opposite of tip)
    
    <img width="600" height="370" alt="image" src="https://github.com/user-attachments/assets/4b07f318-437f-4090-ad50-5dfb02fd1ca7" />

    

---

## B. Tissue Segmentation (FastSurfer → OSS-DBS Material Mask)

1. Use  https://github.com/Deep-MI/FastSurfer
    - Follow the instruction to use fastsurfer
2. Run **FastSurfer** on the T1 MRI.
    - FastSurfer creates a mask of anatomical labels
    - Make sure to set the maximum allocation in Docker to 16GB or higher
3. Convert FastSurfer’s **aparc.DKTaltlas+aseg.deep.mgz.** file
    
    anatomical labels (aseg) → **material labels(OSS-DBS)**:
    
    - `Gray Matter = 1`
    - `White Matter = 2`
    - `CSF = 3`
    - `Unknown = 0`
    
    **→ Using the Make_mask.py in scripts**
    
    
    Resulting mask should look like this in Slicer:
    
    <img width="600" height="370" alt="image" src="https://github.com/user-attachments/assets/051b361f-3c06-467b-ad07-6bc853c7e177" />

    

---

## **C. OSS-DBS Simulation (Right & Left Electrodes Separately)**

1. Set up the **JSON configuration** for the ***right*** electrode:
    - Electrode model (from `OSS-DBSv2/docs/electrode_files`)
        - Electrode used for experiment: Medtronic3389
    - **TipPosition** and **Direction coordinates** from Slicer fiducials
        - Tip coordinates can be used directly from Slicer
        - Direction coordinates have to be calculated by subtracting the Mid coordinate and Tip coordinate
          
    - Example of json file can be found in DBS-Visualization/conifg/examples

        
2. Run **OSS-DBS** using the JSON.
3. Save results and change the names:
    - `electrode1.vtu` -> `electrode1_right.vtu`
    - `potentials.vtu` -> `potentials_right.vtu`
4. Repeat Step C for the **left** electrode.

---

## **D. Import OSS-DBS Results Back into Slicer**

1. Load two result files into Slicer:
    - Right: `electrode1_right.vtu`, `potentials_right.vtu`
    - **When loading, make sure to load coordinate system as RAS!!**
2. **Register OSS-DBS electrode model to the segmented CT electrode**
    - If you correctly created the models with the right coordinates, the electrodes should be almost registered when you load them in
    - Slight alterations should be made to ensure correct registration
        
     <img width="600" height="370" alt="image" src="https://github.com/user-attachments/assets/5dc6a218-55cf-4f24-afea-0d4643f52231" />

        
3. VTA can also be visualized using Point model analysis(Lattice = true), if needed

     <img width="600" height="370" alt="image" src="https://github.com/user-attachments/assets/69e6118d-1a3a-4faf-b873-fd7a59db92e8" />

