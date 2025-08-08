# 🛰️ Lodged Rice Region Segmentation

## 📚 1. Project Overview
This project focuses on the segmentation of lodged rice regions, providing two improved semantic segmentation models — **Improved Deeplabv3+** and **Improved U-Net** — along with complete training logs, model weights, and dataset documentation.  
The aim is to support research and applications in lodged rice detection within agricultural scenarios, enabling precision agriculture analysis, yield estimation, and related studies.

---

## 🤖 2. Core Content

### 🔹 (1) Models and Implementation
- **Improved Deeplabv3+**: Includes full training logs (`epoch_loss.png` / `epoch_miou.png` visualization curves, `epoch_loss.txt` / `epoch_miou.txt` textual logs) to record the entire training process.  
  The trained model weights are provided as `Improved Deeplabv3+.pth`.

- **Improved U-Net**: Similarly provides visualization logs (`epoch_loss.png`, etc.) and textual logs (`epoch_loss.txt`, etc.) to present detailed training metrics.  
  The trained model file is `Improved U-Net.pth`.

---

### 📂 (2) Dataset Description
The project is associated with a **custom agricultural dataset** (linked to the `Datasets` directory).  
It contains annotated images of lodged rice regions and corresponding segmentation masks.

**📌 Usage Restrictions**:  
To use the dataset, you must:
- Send an email request to the corresponding author with:
- Your name, institution, and research purpose.
- How you plan to use the dataset.

**Agree to the Dataset Usage Agreement, which prohibits:**
- Commercial use without written consent.
- Redistribution of the dataset to third parties.
- Modifying or sublicensing the dataset without permission.

---

### ⚙️ (3) Auxiliary Tools
- **`Area calculation.py`**: A post-processing script for segmentation results, used to calculate the proportion of lodged area based on model outputs, aiding further analysis and evaluation.

---

## 🙏 3. Acknowledgements
We would like to thank all team members for their contributions, as well as the open-source projects and technical communities referenced during dataset annotation and model optimization.  
Special thanks to the corresponding authors and institutions for supporting the sharing of this dataset.
