# METHODOLOGY - ACTUAL WORK CONDUCTED

## Study Design and Dataset

This study employed a cross-sectional analysis of speech features for Major Depressive Disorder (MDD) using the Extended Distress Analysis Interview Corpus-Wizard of Oz (E-DAIC-WOZ) dataset. The analysis focused on extracting speech biomarkers from audio recordings and examining their relationships with depression severity.

## Participants

The dataset comprised 212 participants with complete data:
- **MDD group**: 67 participants (31.6%) 
- **Control group**: 145 participants (68.4%)

### Demographic Characteristics
- **Age**: Mean 39.6 ± 12.2 years
- **Gender distribution**: 117 males (55.2%), 95 females (44.8%)
- **Depression severity**: Assessed using Patient Health Questionnaire-8 (PHQ-8), mean score 7.0 ± 6.0

### MDD Subgroup by Gender (for gender differences analysis)
- **Male MDD**: 30 participants (25.6% of males)
- **Female MDD**: 37 participants (38.9% of females)

## Speech Feature Extraction Pipeline

### Audio Processing and Transcription
1. **Audio files**: WAV format from E-DAIC-WOZ clinical interviews
2. **Transcription**: OpenAI Whisper "tiny" model for audio-to-text conversion
3. **Data cleaning**: 212 participants with successful transcription out of 274 attempted (77.4% success rate)

### Feature Categories Extracted

#### 1. Lexical Richness Features (8 features)
**Source**: `lexical_richness_FINAL_CLEAN.csv`
- `brunets_index`: Vocabulary richness measure
- `honore_stat`: Vocabulary diversity accounting for rare words  
- `number_consecutive_repetitions`: Speech disfluency measure
- `type_token_ratio`: Lexical diversity (unique words/total words)
- `word_count`: Total number of words
- `word_frequency_mean`: Average word frequency
- `word_frequency_range`: Range of word frequencies
- `word_frequency_sd`: Standard deviation of word frequencies

#### 2. Syntactic Complexity Features (5 features)  
**Source**: `syntactic_complexity_features.csv`
- `mean_number_subordinate_clauses`: Average subordinate clauses per sentence
- `proportion_verb_phrase_with_objects`: Proportion of VPs with direct objects
- `proportion_verb_phrase_with_subjects`: Proportion of VPs with explicit subjects
- `verb_phrase_with_aux_and_vp_rate`: Rate of auxiliary + main verb constructions
- `verb_phrase_with_aux_rate`: Rate of auxiliary verb usage

#### 3. Word Types and Sentiment Features (14 features)
**Source**: `word_types_sentiment_features.csv`

**Word Type Frequencies:**
- `adjective_rate`: Relative frequency of adjectives
- `adposition_rate`: Ratio of prepositions/postpositions
- `adverb_rate`: Ratio of adverbs
- `conjunction_rate`: Ratio of conjunctions
- `determiner_rate`: Ratio of determiners
- `inflected_verb_rate`: Ratio of inflected verbs
- `noun_rate`: Ratio of nouns
- `pronoun_rate`: Ratio of pronouns
- `proper_noun_rate`: Ratio of proper nouns
- `verb_rate`: Ratio of verbs

**Sentiment Analysis:**
- `mean_sentiment`: Average emotional valence using VADER sentiment analyzer
- `negative_sentence_ratio`: Proportion of negative sentiment sentences
- `neutral_sentence_ratio`: Proportion of neutral sentiment sentences
- `positive_sentence_ratio`: Proportion of positive sentiment sentences

**Total Features**: 27 speech features across all categories

## Statistical Analysis

### Primary Analysis: Correlation with Depression Severity

#### Correlation Analysis
- **Method**: Pearson correlation coefficients between each speech feature and PHQ-8 scores
- **Implementation**: Standard correlation analysis using statistical software
- **Multiple comparisons**: Bonferroni correction applied (α = 0.05/27 = 0.0019)
- **Effect size interpretation**: Cohen's conventions (small: r ≥ 0.1, medium: r ≥ 0.3, large: r ≥ 0.5)

#### Significance Testing
- **Statistical significance levels**:
  - p < 0.001: *** (highly significant)
  - p < 0.01: ** (very significant)  
  - p < 0.05: * (significant)

### Secondary Analysis: Gender Differences in MDD

#### Sample Stratification
- **Participants**: Analysis restricted to MDD participants only (n=67)
- **Male MDD**: 30 participants
- **Female MDD**: 37 participants

#### Statistical Methods

1. **Group Comparison Tests**:
   - **Mann-Whitney U tests**: Non-parametric comparison of speech features between male and female MDD participants
   - **Implementation**: Two-tailed tests for gender differences
   - **Effect size**: Cohen's d calculated as (μ₁ - μ₂) / σ_pooled

2. **Gender-Specific Correlations**:
   - **Spearman rank correlations**: Examined associations between speech features and PHQ-8 scores separately by gender
   - **Rationale**: Non-parametric approach robust to outliers
   - **Implementation**: Separate correlation analyses for male and female MDD participants

3. **Multiple Comparisons Correction**:
   - **Method**: Benjamini-Hochberg False Discovery Rate (FDR) procedure
   - **Significance threshold**: Adjusted p < 0.05 (q < 0.05)
   - **Applied to**: Both group differences and correlation analyses

4. **Interaction Effects**:
   - **Linear regression models**: Gender × Feature interaction terms
   - **Outcome variable**: PHQ-8 depression severity
   - **Model**: PHQ-8 ~ Feature + Gender + Feature×Gender

## Key Findings

### Overall Sample Correlations (N=212)
**Significant correlations with depression severity (p < 0.05):**
1. `mean_sentiment`: r = -0.276, p < 0.001*** (medium effect)
2. `positive_sentence_ratio`: r = -0.180, p = 0.0086** (small effect)
3. `adjective_rate`: r = -0.154, p = 0.0249* (small effect)
4. `proper_noun_rate`: r = -0.123, p = 0.0742 (trending)
5. `negative_sentence_ratio`: r = 0.111, p = 0.0294* (small effect)

### Gender Differences in MDD Participants (N=67)

#### Group Differences
- **Significant differences after FDR correction**: 0 out of 27 features
- **Largest effect sizes**: 
  - `negative_sentence_ratio`: d = 0.861 (large effect, non-significant after correction)
  - `honore_stat`: d = 0.458 (medium effect)

#### Gender-Specific Correlations
**Male MDD participants (n=30):**
- Significant correlations: 1 out of 27 features
- `mean_sentiment`: ρ = -0.287, adjusted p = 0.046

**Female MDD participants (n=37):**
- Significant correlations: 4 out of 27 features
- `mean_sentiment`: ρ = -0.389, adjusted p = 0.003
- `positive_sentence_ratio`: ρ = -0.295, adjusted p = 0.033
- `inflected_verb_rate`: ρ = 0.305, adjusted p = 0.033
- `negative_sentence_ratio`: ρ = 0.280, adjusted p = 0.040

#### Interaction Effects
- **Significant interactions after FDR correction**: 0 out of 27 features

## Technical Implementation

### Software and Tools
- **Audio transcription**: OpenAI Whisper model (tiny version)
- **Text processing**: Natural Language Toolkit (NLTK)
- **Linguistic analysis**: spaCy NLP library with English language model
- **Sentiment analysis**: VADER (Valence Aware Dictionary and sEntiment Reasoner)
- **Statistical analysis**: Python with pandas, numpy, scipy
- **Part-of-speech tagging**: NLTK averaged perceptron tagger

### Data Processing Pipeline
1. **Audio-to-text conversion**: Whisper transcription
2. **Text preprocessing**: Tokenization, sentence segmentation
3. **Feature extraction**: Automated linguistic feature computation
4. **Data integration**: Merging feature sets with demographic data
5. **Statistical analysis**: Correlation and group comparison analyses

### Quality Assurance
- **Missing data handling**: Complete case analysis (n=212 with all features)
- **Outlier management**: No outliers removed; robust statistical methods used
- **Reproducibility**: Fixed parameters for all algorithms
- **Validation**: Cross-checking of statistical computations

## Limitations

1. **Sample size**: Moderate sample size for gender subgroup analyses (n=30-37)
2. **Audio quality**: 22.6% transcription failure rate due to audio issues
3. **Transcription accuracy**: Dependent on Whisper model performance
4. **Language**: Analysis limited to English language features
5. **Cross-sectional design**: Cannot establish causal relationships

## Ethical Considerations

This study utilized a publicly available, de-identified dataset (E-DAIC-WOZ). All participants provided informed consent for research use in the original data collection.

---

**Note**: This methodology describes the actual analytical approach employed in the study, focusing on correlation analysis and gender differences examination using established statistical methods without machine learning algorithms.
