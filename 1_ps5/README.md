# PSet 5 — Image Processing and Hidden Image Extraction

## Overview

This project implements fundamental image processing techniques using Python, including color transformation, pixel manipulation, and hidden image extraction using Least Significant Bit (LSB) steganography.

The implementation uses **PIL (Pillow)** and **NumPy** to process images at the pixel level.

---

## Features

### 1. Color Vision Simulation
Applies transformation matrices to simulate different types of color blindness:

- Red deficiency
- Green deficiency
- Blue deficiency
- No filter (original image)

Each pixel is transformed using matrix multiplication.

---

### 2. Image ↔ Pixel Conversion
Provides utilities to convert between images and pixel lists:

- RGB images → list of `(R, G, B)` tuples  
- Grayscale images → list of integer values  

Supports:
- Flattening image data into pixel lists
- Reconstructing images from pixel lists

---

### 3. Image Filtering via Matrix Operations
Each pixel is multiplied by a predefined transformation matrix to simulate visual deficiencies.

---

### 4. Hidden Image Extraction (LSB Steganography)

This project extracts hidden images encoded in the least significant bits of pixel values.

#### Grayscale Images
- Extracts 1 least significant bit per pixel
- Rescales values to full intensity range (0–255)

#### RGB Images
- Extracts 3 least significant bits per channel
- Rescales each channel independently

---

## Core Concepts

### Matrix Transformation
\[
new\_pixel = M \times pixel
\]

Used for simulating color perception changes.

---

### Least Significant Bit (LSB) Extraction
Hidden information is stored in the lowest bits of pixel values:

\[
value \bmod 2^{n}
\]

Where `n` is the number of extracted bits.

---

### Normalization / Scaling
Extracted values are stretched to full brightness range:

\[
scaled = value \times \frac{255}{2^n - 1}
\]

This restores visibility of the hidden image.

---

## Functions

### `img_to_pix(filename)`
Converts an image into a flat list of pixel values.

---

### `pix_to_img(pixels_list, size, mode)`
Reconstructs an image from a list of pixels.

---

### `filter(pixels_list, color)`
Applies a color deficiency transformation using matrix multiplication.

---

### `extract_end_bits(num_end_bits, pixel)`
Extracts the last `n` bits from each pixel value.

Supports:
- Integer pixels (grayscale)
- Tuple pixels (RGB)

---

### `reveal_bw_image(filename)`
Reconstructs hidden grayscale images using 1-bit LSB extraction.

---

### `reveal_color_image(filename)`
Reconstructs hidden RGB images using 3-bit LSB extraction.

---

### `reveal_image(filename)`
Automatically detects image mode and applies the correct reconstruction method.

---

### `draw_kerb(filename, kerb)`
Draws text onto an image and saves the modified version.

---

## Repository Structure

- `ps5.py` → Main implementation file
- `test_ps5_student.py` → Automated test suite
- `image_15.png` → Sample image for color filtering
- `hidden1.bmp` → Grayscale image with hidden data
- `hidden2.bmp` → RGB image with hidden data

---

## Testing

Run tests using:

```bash
python test_ps5_student.py
