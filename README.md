# Gender Differences in Speech Biomarkers for Major Depressive Disorder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Research](https://img.shields.io/badge/Research-Reproducible-green.svg)](https://github.com/your-username/mdd-gender-speech-analysis)

## 🎯 Overview

This repository contains the complete codebase and documentation for our research on **gender-specific patterns in speech biomarkers for Major Depressive Disorder (MDD)**. Our study analyzes linguistic features from the E-DAIC-WOZ dataset to examine how speech-depression relationships differ between male and female participants.

## 📑 Citation

If you use this code or methodology in your research, please cite:

```bibtex
@article{zahi2025gender,
  title={Gender Differences in Speech Biomarkers for Major Depressive Disorder: A Correlation-Based Analysis of Linguistic Features},
  author={Omar Zahi and [Co-authors]},
  journal={[Journal Name]},
  year={2025},
  publisher={[Publisher]},
  doi={[DOI when available]},
  url={https://github.com/omarzahi/mdd-gender-speech-analysis}
}
```

## 🔍 Key Findings

- ✅ **No significant gender differences** in individual speech features after multiple comparisons correction
- 🔄 **Distinct correlation patterns:** Males (1 significant correlation) vs. Females (4 significant correlations)  
- 🎯 **Gender-specific patterns** suggest potential for improved assessment through gender-stratified models
- 📊 **Effect sizes** indicate meaningful differences in sentiment-related features

## 📁 Repository Structure

```
mdd-gender-speech-analysis/
├── 📂 code/
│   ├── 🐍 gender_differences_mdd_analysis.py    # Main analysis pipeline
│   ├── 🐍 calculate_demographics.py             # Demographics calculations  
│   ├── 📋 requirements.txt                      # Python dependencies
│   └── 📝 README_CODE.md                       # Code documentation
├── 📂 data/
│   ├── 📄 README_DATA.md                       # Data access guide
│   ├── 📄 feature_descriptions.md              # Comprehensive feature guide
│   └── 📄 data_preprocessing_steps.md          # Preprocessing pipeline
├── 📂 results/
│   ├── 📊 figures/                             # Publication-ready figures
│   ├── 📋 tables/                              # Statistical results tables
│   ├── 📈 correlation_matrices/                # Correlation analysis outputs
│   └── 📄 demographics_summary.csv             # Demographics table
├── 📂 docs/
│   ├── 📖 methodology.md                       # Detailed methodology
│   ├── 📊 pipeline_visualization.md            # Research pipeline diagram
│   ├── 🔬 statistical_methods.md               # Statistical analysis details
│   └── 📚 literature_review.md                 # Background literature
├── 📂 supplementary/
│   ├── 📄 acoustic_features_guide.md           # Acoustic feature explanations
│   ├── 📊 additional_analyses.md               # Supplementary analyses
│   └── 📋 validation_results.md                # Cross-validation results
├── ⚖️ LICENSE                                  # MIT License
├── 📖 README.md                                # This file
└── 🔄 CHANGELOG.md                             # Version history
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/your-username/mdd-gender-speech-analysis.git
cd mdd-gender-speech-analysis

# Install dependencies
pip install -r code/requirements.txt

# Run demographics analysis
python code/calculate_demographics.py

# Run main gender differences analysis  
python code/gender_differences_mdd_analysis.py
```

## 📊 Dataset Information

- **Source:** E-DAIC-WOZ Dataset (Gratch et al., 2014)
- **Final Sample:** 212 participants (77.4% transcription success)
  - **MDD Group:** 67 participants (30 male, 37 female)
  - **Control Group:** 145 healthy participants
- **Features:** 27 linguistic features across 4 categories
- **Assessment:** PHQ-8 depression severity scores

## 🔬 Methodology

### Statistical Pipeline
1. **Data Preparation** → Sample selection and feature extraction
2. **Demographics Analysis** → Age and PHQ-8 comparisons  
3. **Overall Correlations** → Pearson correlations (all participants)
4. **Gender Comparisons** → Mann-Whitney U tests
5. **Gender-Stratified Analysis** → Separate correlations by gender
6. **Multiple Testing Correction** → Benjamini-Hochberg FDR
7. **Interaction Testing** → Linear regression (Gender × Feature)
8. **Effect Size Calculation** → Cohen's d for practical significance

### Feature Categories
- **Lexical Richness (7):** TTR, MTLD, vocabulary diversity
- **Syntactic Complexity (6):** Dependency parsing, grammatical structures
- **Word Types (8):** Content vs. function word ratios
- **Sentiment Analysis (6):** Positive/negative sentiment measures

## 📈 Results Summary

| Analysis Component | Key Finding |
|-------------------|-------------|
| **Gender Differences** | No significant differences after FDR correction |
| **Male Correlations** | 1 significant: Mean sentiment (ρ = -0.287) |
| **Female Correlations** | 4 significant: Sentiment + linguistic features |
| **Interaction Effects** | No significant Gender × Feature interactions |
| **Effect Sizes** | Notable effects for sentiment-related features |

## 🔧 Dependencies

```txt
pandas >= 1.3.0
numpy >= 1.21.0  
scipy >= 1.7.0
scikit-learn >= 1.0.0
matplotlib >= 3.4.0
seaborn >= 0.11.0
statsmodels >= 0.12.0
```

## 📁 Data Access

⚠️ **Important:** The E-DAIC-WOZ dataset is not included due to privacy restrictions.

**To access the data:**
1. Visit [USC ICT DCAPS](https://dcapswoz.ict.usc.edu/)
2. Complete the data use agreement
3. Follow preprocessing steps in `data/README_DATA.md`

## 🔄 Reproducibility

All analyses are **fully reproducible**:
- ✅ Deterministic statistical methods
- ✅ Fixed random seeds where applicable  
- ✅ Comprehensive documentation
- ✅ Step-by-step preprocessing guide
- ✅ Version-controlled dependencies

## 🤝 Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Omar Zahi** - *Principal Investigator* - [omar.zahi@email.com]
- **[Co-author 1]** - *Co-Investigator* - [coauthor1@institution.edu]
- **[Co-author 2]** - *Statistician* - [coauthor2@institution.edu]

## 🙏 Acknowledgments

- **USC Institute for Creative Technologies** for the E-DAIC-WOZ dataset
- **[Funding Agency]** for research support (Grant #[Number])
- **[Institution]** for computational resources
- **Open source community** for excellent Python packages

## 📧 Contact

For questions about this research:
- 📧 **Email:** omar.zahi@email.com
- 🔗 **LinkedIn:** [Omar Zahi LinkedIn Profile]
- 🏛️ **Institution:** [Your Institution Website]

## 📚 Related Publications

- [Previous related work 1]
- [Previous related work 2]
- [Preprint if available]

---

⭐ **Star this repository** if you find it useful for your research!

📢 **Share** this work to help advance depression research and gender-sensitive healthcare!
