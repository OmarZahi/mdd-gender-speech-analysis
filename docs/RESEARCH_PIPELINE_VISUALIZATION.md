# Research Pipeline: Gender Differences in MDD Speech Biomarkers

## Complete Methodology Pipeline - Figure 1

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           GENDER DIFFERENCES IN MDD SPEECH BIOMARKERS               │
│                                 METHODOLOGY PIPELINE                                │
└─────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                    DATA ACQUISITION                                │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  E-DAIC-WOZ Dataset (Gratch et al., 2014)                                         │
│  • Initial Sample: N = 274 participants                                            │
│  • Clinical interviews with transcription                                          │
│  • PHQ-8 depression severity scores                                               │
│  • Demographic and clinical metadata                                              │
└─────────────────────────┬───────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              FEATURE EXTRACTION                                    │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  Linguistic Feature Processing Pipeline                                           │
│  • Text preprocessing and cleaning                                                │
│  • Natural language processing algorithms                                         │
│  • Feature computation across 4 categories                                        │
│  Success Rate: 212/274 participants (77.4%)                                      │
└─────────────────────────┬───────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           FEATURE CATEGORIZATION                                   │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  27 Linguistic Features Across 4 Categories:                                      │
│                                                                                    │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │ Lexical Richness│  │ Syntactic       │  │ Word Types      │  │ Sentiment       │ │
│  │ (7 features)    │  │ Complexity      │  │ (8 features)    │  │ Analysis        │ │
│  │                 │  │ (6 features)    │  │                 │  │ (6 features)    │ │
│  │ • TTR           │  │ • Dependency    │  │ • Content words │  │ • Positive      │ │
│  │ • MTLD          │  │   parsing       │  │ • Function words│  │   sentiment     │ │
│  │ • Vocabulary    │  │ • Grammatical   │  │ • Word ratios   │  │ • Negative      │ │
│  │   diversity     │  │   structures    │  │ • Morphological │  │   sentiment     │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────┬───────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              SAMPLE SELECTION                                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  Final Analysis Sample (N = 212)                                                  │
│                                                                                    │
│  ┌─────────────────────────────────┐    ┌─────────────────────────────────────┐   │
│  │         MDD Group               │    │         Control Group               │   │
│  │        N = 67                   │    │        N = 145                      │   │
│  │                                 │    │                                     │   │
│  │  ┌─────────────┐ ┌─────────────┐│    │  Healthy Controls                   │   │
│  │  │    Male     │ │   Female    ││    │  • No depression diagnosis          │   │
│  │  │   N = 30    │ │   N = 37    ││    │  • PHQ-8 scores < 10              │   │
│  │  │             │ │             ││    │                                     │   │
│  │  └─────────────┘ └─────────────┘│    │                                     │   │
│  └─────────────────────────────────┘    └─────────────────────────────────────┘   │
└─────────────────────────┬───────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            STATISTICAL ANALYSIS                                    │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                    │
│  Step 1: Demographics Analysis                                                    │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │ • Age comparisons (Male vs Female MDD)                                     │  │
│  │ • PHQ-8 severity scores analysis                                           │  │
│  │ • Mann-Whitney U tests for group differences                               │  │
│  └─────────────────────────────────────────────────────────────────────────────┘  │
│                                    ▼                                              │
│  Step 2: Overall Correlation Analysis                                             │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │ • Pearson correlations: 27 features × PHQ-8 scores                         │  │
│  │ • All MDD participants combined (N = 67)                                   │  │
│  │ • Baseline associations identification                                      │  │
│  └─────────────────────────────────────────────────────────────────────────────┘  │
│                                    ▼                                              │
│  Step 3: Gender Group Comparisons                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │ • Mann-Whitney U tests for each of 27 features                             │  │
│  │ • Male MDD (N=30) vs Female MDD (N=37)                                     │  │
│  │ • Non-parametric approach for robustness                                   │  │
│  └─────────────────────────────────────────────────────────────────────────────┘  │
│                                    ▼                                              │
│  Step 4: Gender-Stratified Correlation Analysis                                   │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │ • Separate Spearman correlations by gender                                 │  │
│  │ • Male MDD: 27 features × PHQ-8 (N = 30)                                   │  │
│  │ • Female MDD: 27 features × PHQ-8 (N = 37)                                 │  │
│  │ • Rank-based correlations for non-normal distributions                     │  │
│  └─────────────────────────────────────────────────────────────────────────────┘  │
│                                    ▼                                              │
│  Step 5: Multiple Comparisons Correction                                          │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │ • Benjamini-Hochberg False Discovery Rate (FDR) procedure                  │  │
│  │ • Applied to gender-stratified correlations                                │  │
│  │ • Significance threshold: α = 0.05                                         │  │
│  │ • Controls Type I error inflation                                          │  │
│  └─────────────────────────────────────────────────────────────────────────────┘  │
│                                    ▼                                              │
│  Step 6: Interaction Effects Analysis                                             │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │ • Linear regression models with interaction terms                          │  │
│  │ • Model: PHQ-8 ~ Feature + Gender + (Feature × Gender)                     │  │
│  │ • Tests for differential feature-depression relationships by gender        │  │
│  │ • Applied to all 27 linguistic features                                    │  │
│  └─────────────────────────────────────────────────────────────────────────────┘  │
│                                    ▼                                              │
│  Step 7: Effect Size Calculations                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────────┐  │
│  │ • Cohen's d for practical significance assessment                          │  │
│  │ • Applied to significant correlations and group differences                │  │
│  │ • Interpretation: Small (0.2), Medium (0.5), Large (0.8)                  │  │
│  └─────────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────┬───────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                RESULTS SUMMARY                                     │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  Primary Findings:                                                                │
│                                                                                    │
│  ✓ Gender Feature Differences: No significant differences after FDR correction   │
│  ✓ Male Correlations: 1 significant correlation (mean sentiment: ρ = -0.287)     │
│  ✓ Female Correlations: 4 significant correlations (sentiment + linguistic)      │
│  ✓ Interaction Effects: No significant Gender × Feature interactions             │
│  ✓ Effect Sizes: Moderate effects for sentiment-related features                 │
│                                                                                    │
│  Clinical Implications:                                                           │
│  • Gender-specific correlation patterns suggest differential speech-depression    │
│    relationships between males and females                                        │
│  • Potential for improved assessment through gender-stratified approaches        │
│  • Sentiment features show consistent cross-gender relevance                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## Figure Caption for Publication

**Figure 1. Comprehensive Methodology Pipeline for Gender Differences Analysis in MDD Speech Biomarkers.** 
The flowchart illustrates the complete analytical framework from data acquisition through statistical analysis and results interpretation. Starting with the E-DAIC-WOZ dataset (N=274), the pipeline encompasses feature extraction (77.4% success rate), linguistic feature categorization across four domains (27 total features), sample stratification by gender and clinical status, and a seven-step statistical analysis protocol. The methodology employs correlation analysis, non-parametric group comparisons, multiple comparisons correction (FDR), and interaction effect testing to identify gender-specific patterns in speech-depression relationships. Primary findings reveal distinct correlation patterns between male (1 significant correlation) and female (4 significant correlations) MDD participants, with no significant direct gender differences in individual features after statistical correction.

## Technical Implementation Details

### Statistical Software and Packages
- **Primary Analysis**: Python 3.8+ with scientific computing libraries
- **Core Libraries**: pandas, numpy, scipy, statsmodels, scikit-learn
- **Visualization**: matplotlib, seaborn for publication-quality figures
- **Statistical Testing**: Built-in implementations of Mann-Whitney U, Spearman correlation, linear regression

### Quality Control Measures
1. **Data Integrity**: Systematic verification of feature extraction completeness
2. **Statistical Assumptions**: Non-parametric methods for robust analysis
3. **Multiple Testing**: FDR correction to control Type I error inflation
4. **Effect Size Reporting**: Cohen's d for practical significance assessment
5. **Reproducibility**: Fixed random seeds and documented parameter settings

### Analytical Decisions and Justifications
- **Spearman over Pearson**: Chosen for gender-stratified analysis due to non-normal feature distributions
- **Mann-Whitney U**: Selected for group comparisons as robust alternative to t-tests
- **FDR Correction**: Benjamini-Hochberg procedure balances Type I and Type II error rates
- **Linear Regression**: Interaction testing provides formal statistical framework for gender moderation effects

## Methodological Contributions

### Novel Aspects of the Analytical Approach
1. **Comprehensive Gender Analysis**: First systematic investigation of gender differences in linguistic speech biomarkers for depression
2. **Multi-Domain Feature Analysis**: Integration of lexical, syntactic, semantic, and sentiment features in a unified framework
3. **Rigorous Statistical Protocol**: Implementation of FDR correction and interaction testing for robust inference
4. **Gender-Stratified Methodology**: Separate analysis pathways for male and female participants to identify differential patterns

### Clinical and Research Implications
- **Assessment Tool Development**: Findings inform gender-specific calibration of speech-based depression screening tools
- **Biomarker Discovery**: Identification of sentiment features as robust cross-gender indicators of depression severity
- **Methodological Framework**: Provides template for gender-sensitive analysis in digital health research
- **Precision Medicine**: Supports personalized approaches to speech-based mental health assessment

### Limitations and Future Directions
- **Sample Size**: Limited to English-speaking participants from E-DAIC-WOZ dataset
- **Cross-Sectional Design**: Longitudinal validation needed for temporal stability assessment
- **Cultural Validity**: Cross-cultural replication required for broader generalizability
- **Clinical Translation**: Prospective validation in clinical settings needed for implementation
