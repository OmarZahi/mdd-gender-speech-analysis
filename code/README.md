# Analysis Code Documentation

## Overview

This directory contains the core implementation components for the gender differences analysis in MDD speech biomarkers research.

## Available Scripts

### Feature Extraction Utilities
- **`energy_features.py`** - Energy-based acoustic feature extraction algorithms
- **`frequency_features.py`** - Frequency domain analysis and spectral feature computation

### Dependencies
Install required Python packages using:
```bash
pip install -r requirements.txt
```

## Implementation Details

### Energy Features (`energy_features.py`)
Implements algorithms for extracting energy-based acoustic characteristics from speech signals, including:
- Root Mean Square (RMS) energy calculations
- Short-time energy analysis
- Energy distribution patterns
- Dynamic range measurements

### Frequency Features (`frequency_features.py`) 
Provides frequency domain analysis capabilities for speech signal processing:
- Spectral centroid and bandwidth calculations
- Formant frequency estimation
- Harmonic analysis algorithms
- Spectral roll-off measurements

## Usage

These utilities are designed for integration with speech analysis pipelines processing the E-DAIC-WOZ dataset. Each module contains well-documented functions with parameter specifications and return value descriptions.

## Requirements

- Python >= 3.8
- NumPy >= 1.21.0
- SciPy >= 1.7.0
- Additional dependencies as specified in requirements.txt

## Documentation

Comprehensive function documentation is provided within each module using standard Python docstring conventions. For specific implementation details, refer to the inline comments and docstrings in each file.
