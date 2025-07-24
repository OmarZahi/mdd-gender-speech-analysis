# Research Pipeline: Gender Differences in MDD Speech Biomarkers

## Pipeline Overview
```
E-DAIC-WOZ Dataset (274 participants)
            ↓
    Feature Extraction Success
         (212 participants)
            ↓
    MDD Participant Selection
      (67 MDD participants)
            ↓
    Gender Stratification
   (30 Male, 37 Female MDD)
            ↓
    Statistical Analysis Pipeline
            ↓
        Results & Findings
```

---

## Detailed Pipeline Steps

### 1. Data Preparation
**Input:** E-DAIC-WOZ Dataset
- **Initial Sample:** 274 participants
- **Transcription Success:** 212 participants (77.4% success rate)
- **Final Sample:** 67 MDD participants (30 male, 37 female) + 145 controls

### 2. Feature Categories Analyzed
**Linguistic Features (27 total):**
- **Lexical Richness:** TTR, MTLD, vocabulary diversity measures
- **Syntactic Complexity:** Dependency parsing, grammatical structures
- **Word Types:** Content vs. function word ratios
- **Sentiment Analysis:** Positive/negative sentiment ratios

### 3. Statistical Analysis Pipeline
```
Demographics Analysis
        ↓
Overall Correlation Analysis (Pearson)
        ↓
Gender Group Comparisons (Mann-Whitney U)
        ↓
Gender-Stratified Correlations (Spearman)
        ↓
Multiple Comparisons Correction (FDR)
        ↓
Linear Regression (Gender × Feature Interactions)
        ↓
Effect Size Calculations (Cohen's d)
```

### 4. Statistical Methods Applied
- **Correlation Analysis:** Pearson correlations between speech features and PHQ-8 scores
- **Group Comparisons:** Mann-Whitney U tests for gender differences
- **Multiple Testing:** Benjamini-Hochberg False Discovery Rate correction
- **Interaction Testing:** Linear regression models with Gender × Feature interactions
- **Effect Sizes:** Cohen's d for magnitude assessment

### 5. Key Analytical Components
1. **Demographics Comparison:** Age and PHQ-8 scores by gender
2. **Overall Speech-Depression Correlations:** All participants combined
3. **Gender-Specific Correlations:** Separate analysis for male vs. female MDD
4. **Statistical Significance Testing:** FDR-corrected p-values
5. **Interaction Effects:** Gender moderation of speech-depression relationships

### 6. Results Generated
**Primary Findings:**
- **No significant gender differences** in speech features after multiple comparisons correction
- **Distinct correlation patterns by gender:**
  - Males: 1 significant correlation (mean sentiment: ρ = -0.287)
  - Females: 4 significant correlations (sentiment + linguistic features)
- **No significant Gender × Feature interactions** after correction
- **Notable effect sizes** for sentiment-related features

---

## Visualization Components for Figures

### Figure 1: Study Flow Diagram
```
E-DAIC-WOZ Dataset (n=274)
         ↓
Feature Extraction Successful (n=212, 77.4%)
         ↓
MDD Participants Selected (n=67)
    ↙        ↘
Male MDD     Female MDD
(n=30)       (n=37)
    ↘        ↙
Statistical Analysis Pipeline
```

### Figure 2: Analysis Pipeline
```
[Demographics] → [Overall Correlations] → [Gender Comparisons]
                                ↓
[Gender-Stratified Correlations] → [FDR Correction] → [Interaction Testing]
```

### Figure 3: Results Structure
```
Correlation Heatmaps (Male vs Female)
         ↓
Scatter Plots (Significant Correlations)
         ↓
Effect Size Comparisons
         ↓
Interaction Plots (Top Features)
```

---

## Key Methodological Strengths
1. **Robust Sample Size:** 67 MDD participants with balanced gender distribution
2. **Comprehensive Feature Set:** 27 linguistic features across 4 categories
3. **Rigorous Statistics:** Multiple comparisons correction, effect sizes
4. **Gender-Specific Analysis:** Separate correlation analysis by gender
5. **Interaction Testing:** Formal statistical testing of gender moderation effects

## Scientific Contributions
- **Novel Gender Analysis:** First comprehensive gender differences study in MDD speech biomarkers
- **Linguistic Focus:** Emphasis on linguistic rather than acoustic features
- **Methodological Rigor:** FDR correction and interaction testing
- **Clinical Relevance:** Implications for gender-specific speech assessment tools
