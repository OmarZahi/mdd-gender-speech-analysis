# Data Access Guide - E-DAIC-WOZ Dataset

## ⚠️ Important Notice
The E-DAIC-WOZ dataset is **not included** in this repository due to privacy and licensing restrictions. This guide explains how to obtain and prepare the data.

## 📋 Data Access Steps

### 1. Request Dataset Access
1. Visit the [USC ICT DCAPS website](https://dcapswoz.ict.usc.edu/)
2. Register for an account
3. Complete the **Data Use Agreement (DUA)**
4. Submit your research proposal and institutional affiliation
5. Wait for approval (typically 1-2 weeks)

### 2. Download Dataset
Once approved, you will receive:
- Audio files (.wav format)
- Transcription files (.txt format)
- Participant metadata (demographics, PHQ-8 scores)
- Clinical assessment data

### 3. Data Preprocessing Pipeline

#### Required Data Files
After obtaining the dataset, ensure you have:
```
├── transcripts/
│   ├── participant_XXX.txt
│   └── ...
├── metadata/
│   ├── participant_info.csv
│   └── phq8_scores.csv
└── audio/ (optional - not used in this analysis)
    ├── participant_XXX.wav
    └── ...
```

#### Preprocessing Steps
1. **Text Extraction**: Extract transcripts from interview sessions
2. **Feature Calculation**: Run linguistic feature extraction pipeline
3. **Data Integration**: Merge features with demographic and clinical data
4. **Quality Control**: Remove participants with incomplete data
5. **Final Dataset**: Create analysis-ready CSV files

### 4. Expected Data Structure
Your final preprocessed files should match:
- `lexical_richness_FINAL_CLEAN.csv` (7 features)
- `syntactic_complexity_features.csv` (6 features)  
- `word_types_sentiment_features.csv` (8 features)
- `prepared_labels.csv` (demographics + PHQ-8 scores)

## 📊 Dataset Statistics
- **Original Sample**: 274 participants
- **Successful Transcriptions**: 212 participants (77.4% success rate)
- **MDD Participants**: 67 (30 male, 37 female)
- **Control Participants**: 145
- **Age Range**: 18-65 years
- **PHQ-8 Range**: 0-24 (depression severity)

## 🔧 Preprocessing Code
The preprocessing steps are implemented in:
- `feature_extraction_pipeline.py` (not included - contact authors)
- Text processing utilities
- Linguistic feature calculators

## ✅ Data Quality Checks
Before running the analysis, verify:
- [ ] All 212 participants have complete feature data
- [ ] PHQ-8 scores are available for all participants
- [ ] Gender information is coded (0=Male, 1=Female)
- [ ] No missing values in critical variables
- [ ] Feature distributions appear reasonable

## 📧 Support
For data access issues:
- **USC ICT Support**: [support email from USC website]
- **Research Team**: [your.email@institution.edu]

## 📝 Citation Requirements
When using the E-DAIC-WOZ dataset, please cite:
```
Gratch, J., Artstein, R., Lucas, G., Stratou, G., Scherer, S., Nazarian, A., ... & Morency, L. P. (2014). 
The Distress Analysis Interview Corpus of human and computer interviews. 
In Proceedings of the 9th International Conference on Language Resources and Evaluation (LREC'14).
```

## ⚖️ Ethical Considerations
- Follow your institution's IRB guidelines
- Respect participant privacy and confidentiality
- Use data only for approved research purposes
- Do not attempt to re-identify participants
- Securely store and handle all data files
