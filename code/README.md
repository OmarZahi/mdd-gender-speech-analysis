# Code Directory

## 📋 Analysis Scripts

This directory will contain the main analysis scripts for the gender differences in MDD speech biomarkers research.

### 🚧 Coming Soon (In Development)

The following scripts are currently being finalized and will be added to this repository:

#### Main Analysis Pipeline
- **`gender_differences_mdd_analysis.py`** - Complete statistical analysis pipeline
  - Gender-stratified correlation analysis
  - Mann-Whitney U tests for group comparisons
  - Benjamini-Hochberg FDR correction
  - Linear regression with interaction terms
  - Effect size calculations (Cohen's d)
  - Publication-quality visualizations

#### Demographics Analysis  
- **`calculate_demographics.py`** - Demographics calculation and comparison utilities
  - Age and PHQ-8 score comparisons by gender
  - Sample size calculations and descriptive statistics
  - Statistical significance testing
  - Demographics table generation

#### Feature Extraction Pipeline
- **`feature_extraction_pipeline.py`** - Linguistic feature extraction from E-DAIC-WOZ transcripts
  - Text preprocessing and cleaning
  - Lexical richness calculations (TTR, MTLD, etc.)
  - Syntactic complexity analysis
  - Word type and sentiment analysis
  - Data integration and quality control

### 📦 Dependencies

Install required packages:
```bash
pip install -r requirements.txt
```

### 🔄 Usage (Once Available)

```bash
# Calculate demographics
python calculate_demographics.py

# Run main gender differences analysis
python gender_differences_mdd_analysis.py

# Extract features from transcripts (requires E-DAIC-WOZ data)
python feature_extraction_pipeline.py
```

### 📊 Expected Outputs

When scripts are run, they will generate:
- Statistical results tables (CSV format)
- Correlation matrices and heatmaps
- Demographics comparison tables
- Publication-ready figures
- Comprehensive analysis reports

### ⚠️ Data Requirements

These scripts require preprocessed data from the E-DAIC-WOZ dataset:
- `lexical_richness_FINAL_CLEAN.csv`
- `syntactic_complexity_features.csv`
- `word_types_sentiment_features.csv`
- `prepared_labels.csv`

See `/data/README_DATA.md` for data access and preprocessing instructions.

### 🔒 Privacy Note

The actual analysis scripts are being finalized to ensure:
- No hardcoded file paths or personal information
- Proper error handling and documentation
- Compliance with data privacy requirements
- Reproducible and well-commented code

**Scripts will be added once final review is complete.**
