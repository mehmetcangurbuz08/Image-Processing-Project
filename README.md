# Image Processing Project

## Overview
This project focuses on image processing tasks such as high-pass filtering, alignment correction, and pixel sorting using `.pgm` format images. It applies various transformations to images programmatically to enhance or analyze key features.

---

## Features
- **High-Pass Filtering:** Enhances edges and fine details in the image.
- **Alignment Correction:** Fixes misaligned images by detecting and correcting pixel shifts.
- **Pixel Sorting:** Sorts pixels either row-wise or column-wise for specific visual effects.
- **PGM Image Processing:** Handles image processing using the Portable Gray Map format.

---

## Project Structure

```
ImageProcessingProject/
|-- question01/
|   |-- src/
|   |   |-- Main.py                     # Core implementation of image processing algorithms
|   |   |-- animals.pgm, lenna.pgm      # Input images in PGM format
|-- WebContent/                         # Web interface for visualization (if applicable)
```

---

## How It Works

1. **Image Loading:**
    - PGM images are loaded and parsed using the custom logic within **Main.py**.

2. **Image Processing Functions:**
    - **High-Pass Filter:** Enhances high-frequency components like edges.
    - **Alignment Correction:** Detects misalignments and shifts pixels accordingly.
    - **Pixel Sorting:** Rearranges pixel intensities either by rows or columns.

3. **Result Generation:**
    - Processed images are saved back in PGM format for easy visualization and analysis.

---

## Example Workflow
1. The user provides an input PGM image.
2. The system applies the selected processing operation (e.g., high-pass filtering).
3. The processed image is saved and can be viewed for comparison.

---

## Installation and Usage

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd ImageProcessingProject/question01/src
    ```

2. Run the Python script:
    ```bash
    python Main.py
    ```

3. Provide the input image path and select the desired processing operation.

---

## Future Improvements
- Expand support for additional image formats (e.g., PNG, JPEG).
- Implement noise reduction and denoising filters.
- Add a graphical user interface (GUI) for easier image selection and operation.
