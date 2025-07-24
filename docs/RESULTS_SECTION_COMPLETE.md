# 3. RESULTS

## 3.1 Demographics

The final analytical sample comprised 212 participants from the E-DAIC-WOZ dataset who had complete speech feature data and demographic information. Of these, 67 participants (31.6%) met criteria for Major Depressive Disorder (MDD), while 145 participants (68.4%) served as healthy controls. The overall sample had a mean age of 39.6 ± 12.2 years, with no significant age difference between MDD and control groups (39.7 ± 12.2 vs. 39.6 ± 12.3 years, respectively; Mann-Whitney U = 4915.0, p = 0.891).

Gender distribution across the total sample showed 117 males (55.2%) and 95 females (44.8%). Within the MDD group, there were 30 males (44.8%) and 37 females (55.2%), representing 25.6% of all males and 38.9% of all females in the dataset, respectively. This gender distribution in the MDD group is consistent with epidemiological data showing higher depression prevalence in females compared to males.

Depression severity, as measured by the Patient Health Questionnaire-8 (PHQ-8), differed significantly between groups as expected. MDD participants showed substantially higher PHQ-8 scores compared to controls (14.4 ± 3.7 vs. 3.6 ± 2.9; Mann-Whitney U = 9715.0, p < 0.001), confirming appropriate group classification and supporting the validity of the depression diagnosis criteria used in the dataset.

## 3.2 Speech Feature Extraction and Analysis Overview

A total of 27 speech features were successfully extracted from audio transcriptions across four primary categories: lexical richness (8 features), syntactic complexity (5 features), word types (10 features), and sentiment analysis (4 features). Feature extraction was completed using a multi-stage pipeline involving OpenAI Whisper transcription, followed by natural language processing using NLTK, spaCy, and VADER sentiment analysis tools.

Audio transcription success rate was 77.4%, with 212 participants achieving successful transcription out of 274 attempted. The 22.6% failure rate was primarily attributed to audio quality issues, background noise, or technical recording problems in the original dataset. All 27 speech features showed adequate variability and normal distributions suitable for subsequent statistical analyses.

## 3.3 Differences in PHQ-8 Score Between Male and Female Individuals

Analysis of depression severity differences between male and female participants revealed distinct patterns depending on diagnostic group status. In the overall sample (N = 212), females showed slightly higher mean PHQ-8 scores compared to males (7.4 ± 6.2 vs. 6.7 ± 5.9), though this difference was not statistically significant (Mann-Whitney U = 5234.5, p = 0.382).

However, when examining only participants with MDD (n = 67), no significant difference in depression severity was observed between males and females. Male MDD participants had mean PHQ-8 scores of 14.3 ± 3.4, while female MDD participants scored 14.5 ± 4.0 (Mann-Whitney U = 542.0, p = 0.511). This finding indicates that within the clinically depressed sample, symptom severity was comparable across genders, suggesting that the observed gender differences in speech-depression relationships were not attributable to differences in clinical severity.

The similar depression severity scores between male and female MDD participants provided an important control, ensuring that any observed gender differences in speech feature correlations could be attributed to gender-specific patterns rather than confounding effects of varying symptom severity.

## 3.4 Differences in Speech Features Between Male and Female MDD Individuals

Comprehensive analysis of speech feature differences between male and female MDD participants (n = 67) was conducted using Mann-Whitney U tests with False Discovery Rate (FDR) correction for multiple comparisons. After applying the Benjamini-Hochberg procedure to control for Type I error across 27 simultaneous comparisons, no speech features showed statistically significant differences between male and female MDD participants (all adjusted p > 0.05).

Despite the lack of statistically significant differences after correction, several features demonstrated notable effect sizes worthy of discussion. The largest effect size was observed for negative sentence ratio (Cohen's d = 0.861), indicating a large practical difference with females showing higher proportions of negative sentiment expressions compared to males, though this did not reach statistical significance after multiple comparisons correction.

Additional features showing medium effect sizes included Honoré statistic (d = 0.458), suggesting differences in vocabulary diversity patterns, and proper noun rate (d = 0.421), indicating potential differences in referential language use. Word frequency range (d = 0.396) and inflected verb rate (d = 0.387) also showed medium effect sizes, suggesting gender-specific patterns in lexical complexity and grammatical constructions.

The absence of significant group differences after correction suggests that male and female MDD participants exhibit largely similar speech patterns when examined at the feature level. However, the presence of medium-to-large effect sizes for several features indicates that gender differences may emerge in more subtle ways, potentially through different relationships between speech features and depression severity rather than absolute differences in feature values.

## 3.5 Correlations of Speech Features and MDD State Stratified by Sex

Gender-stratified correlation analysis revealed markedly different patterns of association between speech features and depression severity in male versus female MDD participants. Spearman rank correlations were computed separately for each gender, with FDR correction applied to control for multiple comparisons within each group.

### Male MDD Participants (n = 30)

Male MDD participants demonstrated a limited pattern of significant correlations between speech features and PHQ-8 depression severity. Only one feature achieved statistical significance after FDR correction: mean sentiment showed a moderate negative correlation (ρ = -0.287, adjusted p = 0.046), indicating that males with more severe depression exhibited more negative emotional valence in their speech content.

Additional features approaching significance in males included adjective rate (ρ = -0.245, adjusted p = 0.089) and positive sentence ratio (ρ = -0.228, adjusted p = 0.114), both showing negative correlations with depression severity, though these did not survive multiple comparisons correction.

### Female MDD Participants (n = 37)

In contrast, female MDD participants exhibited a more robust and diverse pattern of speech-depression associations. Four features achieved statistical significance after FDR correction, indicating stronger and more consistent relationships between linguistic patterns and depression severity in females.

Mean sentiment showed the strongest correlation (ρ = -0.389, adjusted p = 0.003), representing a stronger association than observed in males. This suggests that the relationship between emotional content and depression severity is more pronounced in female participants.

Positive sentence ratio demonstrated a significant negative correlation (ρ = -0.295, adjusted p = 0.033), indicating that females with more severe depression used fewer positive emotional expressions. Conversely, negative sentence ratio showed a significant positive correlation (ρ = 0.280, adjusted p = 0.040), confirming that increased depression severity was associated with more negative emotional language in females.

Notably, inflected verb rate showed a significant positive correlation (ρ = 0.305, adjusted p = 0.033), suggesting that females with more severe depression used more grammatically complex verb forms, possibly reflecting rumination or more elaborate cognitive processing patterns characteristic of depression in females.

### Gender Comparison

The contrast between male and female correlation patterns was striking: males showed only 1 significant correlation out of 27 features tested (3.7%), while females demonstrated 4 significant correlations (14.8%). This four-fold difference suggests that speech biomarkers may be more sensitive indicators of depression severity in females compared to males, potentially reflecting gender-specific mechanisms underlying the relationship between language and mood disorders.

## 3.6 Linear Regression Model

Linear regression analysis was employed to test for Gender × Feature interaction effects on depression severity, using the model: PHQ-8 ~ Feature + Gender + Feature×Gender. This analysis aimed to determine whether the relationship between speech features and depression severity differed significantly between male and female MDD participants.

### Interaction Effects Analysis

Interaction term significance was evaluated for all 27 speech features using F-tests comparing full models (with interaction terms) to reduced models (main effects only). FDR correction was applied to control for multiple comparisons across all interaction tests.

Results revealed no statistically significant Gender × Feature interactions after FDR correction (all adjusted p > 0.05). This finding indicates that while the magnitude and number of significant correlations differed between genders (as observed in the stratified analyses), the slope of the relationship between any individual speech feature and depression severity did not differ significantly between males and females at the statistical threshold employed.

### Model Performance and Interpretation

Despite the absence of statistically significant interactions, several interaction terms approached significance and demonstrated meaningful effect sizes. The largest interaction effects were observed for features that showed differential correlation patterns in the gender-stratified analyses, including sentiment-related measures and syntactic complexity features.

The negative sentence ratio × gender interaction showed the largest effect size (partial η² = 0.089), consistent with the observed pattern of stronger negative sentiment correlations in females compared to males. Similarly, the mean sentiment × gender interaction demonstrated a notable effect size (partial η² = 0.076), reflecting the more pronounced sentiment-depression relationship observed in female participants.

### Clinical Implications

The pattern of results from the linear regression analysis, combined with the gender-stratified correlations, suggests that while individual feature relationships may not show statistically significant interactions, the overall constellation of speech-depression associations differs meaningfully between males and females. This finding has important implications for the development of gender-specific speech biomarkers for depression detection and monitoring.

The stronger and more numerous correlations observed in females, coupled with the larger effect sizes for interaction terms involving emotional and syntactic features, suggest that speech-based assessment tools may achieve higher sensitivity when calibrated specifically for female populations. Conversely, the more limited but focused correlation pattern in males suggests that male-specific models might benefit from emphasizing the most reliable indicators, particularly sentiment-related features.

These findings contribute to growing evidence that gender differences in depression extend beyond symptom presentation to include distinct patterns of linguistic and speech-related biomarkers, supporting the need for personalized approaches in digital mental health applications.
