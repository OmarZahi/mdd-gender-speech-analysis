# Gender Differences in Speech Biomarkers for Major Depressive Disorder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Research](https://img.shields.io/badge/Research-Reproducible-green.svg)](https://github.com/OmarZahi/mdd-gender-speech-analysis)

## Abstract

This repository contains the complete research framework for analyzing gender-specific patterns in speech biomarkers for Major Depressive Disorder (MDD). The study employs correlation-based statistical analysis of linguistic features extracted from the E-DAIC-WOZ dataset to investigate differential speech-depression relationships between male and female participants. Our findings reveal distinct gender-specific correlation patterns that may inform the development of more effective, personalized speech-based assessment tools for depression.


## Citation

If you use this research methodology or findings in your work, please cite:

```bibtex
@article{zahi2025gender,
  title={Gender Differences in Speech Biomarkers for Major Depressive Disorder: A Correlation-Based Analysis of Linguistic Features},
  author={Omar Zahi},
  journal={[Journal Name]},
  year={2025},
  publisher={[Publisher]},
  doi={[DOI when available]},
  url={https://github.com/OmarZahi/mdd-gender-speech-analysis}
}
```

## Key Findings

Our statistical analysis revealed significant gender-specific patterns in speech biomarkers for depression:

- **Gender Differences**: No statistically significant differences in individual speech features after multiple comparisons correction (Benjamini-Hochberg FDR)
- **Male Participants**: One significant correlation between speech features and depression severity (mean sentiment: ρ = -0.287, p < 0.05)
- **Female Participants**: Four significant correlations identified, including sentiment-based and linguistic complexity measures
- **Interaction Effects**: No significant Gender × Feature interactions after statistical correction
- **Effect Sizes**: Moderate effect sizes observed for sentiment-related features, suggesting clinical relevance

## Repository Structure

```
mdd-gender-speech-analysis/
├── code/                                       # Analysis implementation
│   ├── requirements.txt                        # Python dependencies
│   ├── energy_features.py                      # Energy-based feature extraction
│   ├── frequency_features.py                   # Frequency domain analysis
│   └── README.md                              # Code documentation
├── data/                                       # Data access documentation
│   └── README_DATA.md                         # E-DAIC-WOZ access guide
├── docs/                                       # Research methodology
│   ├── methodology_section.md                 # Detailed methodology
│   ├── RESEARCH_PIPELINE_VISUALIZATION.md     # Analysis pipeline
│   ├── ACTUAL_methodology_conducted.md        # Implementation details
│   ├── Data_Processing_Statistical_Analysis_Section.md  # Processing guide
│   └── RESULTS_SECTION_COMPLETE.md           # Complete results
├── results/                                    # Analysis outputs
│   └── README.md                              # Results documentation
├── supplementary/                              # Additional materials
│   └── ACOUSTIC_FEATURES_EXPLANATIONS.md     # Feature definitions
├── LICENSE                                     # MIT License
├── README.md                                  # This documentation
└── CHANGELOG.md                               # Version history
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

## Methodology

### Participants and Data
- **Dataset**: E-DAIC-WOZ Extended Distress Analysis Interview Corpus (Gratch et al., 2014)
- **Sample Size**: 212 participants with successful feature extraction (77.4% transcription success rate)
- **MDD Group**: 67 participants (30 male, 37 female) with clinically significant depression
- **Control Group**: 145 healthy control participants
- **Assessment**: PHQ-8 Patient Health Questionnaire for depression severity

### Feature Extraction
Analysis focused on 27 linguistic features across four categories:
- **Lexical Richness (7 features)**: Type-token ratio, MTLD, vocabulary diversity measures
- **Syntactic Complexity (6 features)**: Dependency parsing metrics, grammatical structure analysis
- **Word Types (8 features)**: Content versus function word ratios, morphological analysis
- **Sentiment Analysis (6 features)**: Positive/negative sentiment ratios, emotional valence measures

### Statistical Analysis Pipeline
1. **Descriptive Analysis**: Demographic and clinical characteristic comparisons
2. **Correlation Analysis**: Pearson correlations between speech features and PHQ-8 scores
3. **Group Comparisons**: Mann-Whitney U tests for gender-based feature differences
4. **Gender-Stratified Analysis**: Separate Spearman correlations for male and female participants
5. **Multiple Comparisons Correction**: Benjamini-Hochberg False Discovery Rate procedure
6. **Interaction Testing**: Linear regression models with Gender × Feature interaction terms
7. **Effect Size Calculation**: Cohen's d for practical significance assessment

## Results

| Analysis Component | Finding | Statistical Details |
|-------------------|---------|-------------------|
| **Gender Feature Differences** | No significant differences | Mann-Whitney U tests, p > 0.05 after FDR correction |
| **Male Correlations** | 1 significant correlation | Mean sentiment: ρ = -0.287, p < 0.05 |
| **Female Correlations** | 4 significant correlations | Sentiment and linguistic features, p < 0.05 |
| **Interaction Effects** | No significant interactions | Linear regression, p > 0.05 after correction |
| **Effect Sizes** | Moderate for sentiment features | Cohen's d = 0.3-0.5 range |

## Technical Requirements

```
Python >= 3.8
pandas >= 1.3.0
numpy >= 1.21.0  
scipy >= 1.7.0
scikit-learn >= 1.0.0
matplotlib >= 3.4.0
seaborn >= 0.11.0
statsmodels >= 0.12.0
```

## Data Access

**Important**: The E-DAIC-WOZ dataset is not included in this repository due to privacy and licensing restrictions.

**Dataset Access Procedure**:
1. Visit the [USC ICT DCAPS portal](https://dcapswoz.ict.usc.edu/)
2. Complete the required Data Use Agreement
3. Submit institutional and research purpose documentation
4. Follow preprocessing guidelines in `data/README_DATA.md`

## Reproducibility

This research implements best practices for reproducible science:
- **Deterministic Methods**: All statistical procedures use fixed parameters
- **Version Control**: Complete methodology and code documentation
- **Open Documentation**: Detailed implementation guides available
- **Standard Tools**: Widely-used Python scientific computing libraries

## 🤝 Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Omar Zahi**  
*Principal Investigator*  
📧 [omar.2123039@stemobour.moe.edu.eg](mailto:omar.2123039@stemobour.moe.edu.eg)  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/omar-zahi/)  
🏛️ STEM October University, Egypt

**Research Focus**: Speech biomarkers for mental health assessment, gender differences in computational linguistics, natural language processing applications in clinical psychology.

## Research Collaboration

This research welcomes collaboration with:

### Academic Researchers
- Computational linguists working on clinical applications
- Mental health researchers investigating speech biomarkers  
- Gender differences researchers in psychology and psychiatry
- Cross-cultural validation studies

### Clinical Applications
- Mental health practitioners developing objective assessment tools
- Healthcare institutions implementing digital therapeutics
- Researchers working on speech-based screening instruments

### Technical Development
- Machine learning researchers for predictive model development
- Speech processing specialists for advanced feature extraction
- Data scientists for cross-dataset validation studies

**Contact**: For research collaboration inquiries, please contact [omar.2123039@stemobour.moe.edu.eg](mailto:omar.2123039@stemobour.moe.edu.eg)

## Acknowledgments

- USC Institute for Creative Technologies for providing the E-DAIC-WOZ dataset
- STEM October University for institutional support
- Open source scientific computing community for software tools

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Repository**: https://github.com/OmarZahi/mdd-gender-speech-analysis  
**Research Impact**: Advancing gender-sensitive approaches to mental health assessment through computational linguistics
