# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-07-24

### Added
- Initial release of gender differences analysis in MDD speech biomarkers
- Complete statistical analysis pipeline with correlation-based methodology
- Gender-stratified analysis with Benjamini-Hochberg FDR correction
- Demographics calculation and comparison utilities
- Comprehensive documentation and methodology guide
- Publication-ready visualizations and results tables
- Data access guide for E-DAIC-WOZ dataset
- MIT License for open source distribution

### Features
- **Statistical Analysis Pipeline** - Complete implementation of correlation-based methodology
  - Pearson correlations for overall associations
  - Mann-Whitney U tests for gender group comparisons
  - Gender-stratified Spearman correlations
  - False Discovery Rate (FDR) multiple comparisons correction
  - Linear regression for Gender × Feature interactions
  - Cohen's d effect size calculations
  - Statistical visualization components

- **Feature Extraction Utilities** - Speech analysis tools
  - Energy-based acoustic feature extraction algorithms
  - Frequency domain analysis capabilities
  - Integration with E-DAIC-WOZ dataset processing

- **Documentation Framework** - Comprehensive research documentation
  - Detailed methodology documentation
  - Feature descriptions and explanations
  - Research pipeline visualization
  - Data access and preprocessing guides
  - Reproducibility instructions

### Statistical Methods
- Correlation analysis (Pearson and Spearman)
- Mann-Whitney U tests for group comparisons
- Benjamini-Hochberg False Discovery Rate correction
- Linear regression with interaction terms
- Effect size calculations (Cohen's d)
- Descriptive statistics and confidence intervals

### Results
- No significant gender differences in speech features after correction
- Male MDD participants: 1 significant correlation (mean sentiment)
- Female MDD participants: 4 significant correlations
- No significant Gender × Feature interactions after correction
- Notable effect sizes for sentiment-related features

---

## Development Notes

### Version 1.0.0 Release Status
- [x] Complete statistical analysis implementation
- [x] Comprehensive methodology documentation
- [x] Data access instructions and guidelines
- [x] MIT License for open science accessibility
- [x] Reproducibility verification and documentation
- [x] Professional repository structure

### Research Extensions (Future Work)
- Additional validation datasets for cross-study replication
- Cross-cultural analysis extensions with diverse populations
- Longitudinal analysis capabilities for depression progression tracking
- Real-time assessment tool development for clinical applications

### Known Limitations
- Analysis limited to English-speaking participants
- Cross-sectional design (no longitudinal data)
- Specific to E-DAIC-WOZ dataset structure
- Requires manual data preprocessing steps

---

## Contributors
- Omar Zahi - Principal Investigator and Lead Developer ([omar.2123039@stemobour.moe.edu.eg](mailto:omar.2123039@stemobour.moe.edu.eg))

For detailed commit history, see: [GitHub Commits](https://github.com/OmarZahi/mdd-gender-speech-analysis/commits/main)
