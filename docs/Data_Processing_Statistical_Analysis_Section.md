## 2.4 Data Processing and Statistical Analysis

We conducted a comprehensive analysis of various speech components which were previously associated with symptoms of Major Depressive Disorder (MDD) and related mood disorders. Speech features were further grouped into four primary categories: Lexical Richness, Syntactic Complexity, Word Types, and Sentiment Analysis. The 27 extracted features across these categories are detailed in the methodology section and have demonstrated relevance to depression detection in prior research.

**Audio Processing and Transcription**
Audio recordings from clinical interviews were processed using OpenAI Whisper "tiny" model for automatic speech recognition and transcription. This approach enabled conversion of spoken language into text format suitable for linguistic feature extraction. The Whisper model was selected for its robust performance across diverse audio conditions and speakers, achieving a 77.4% successful transcription rate from the initial 274 audio files, resulting in 212 participants with complete speech feature data.

**Lexical Richness Features**
We extracted measures of vocabulary diversity and complexity, including Type-Token Ratio (TTR), Brunet's Index, and Honoré's statistic. These features capture lexical sophistication and have been associated with cognitive function and depression severity in previous studies. Additionally, we computed word frequency statistics (mean, range, standard deviation) and consecutive repetition counts as indicators of speech disfluency, which may reflect cognitive processing difficulties in depression.

**Syntactic Complexity Features**
To capture grammatical sophistication and sentence structure complexity, we analyzed syntactic patterns using spaCy's dependency parser. Features included mean number of subordinate clauses per sentence, proportion of verb phrases with direct objects, and rates of auxiliary verb constructions. These measures reflect linguistic complexity that may be altered in depression due to cognitive changes affecting language production.

**Word Types and Part-of-Speech Analysis**
Furthermore, we focused on linguistic features such as pronouns, adjectives, adverbs, nouns, and conjunctions. These categories capture grammatical patterns and word usage preferences that may differ between individuals with and without depression. Part-of-speech tagging was performed using the Natural Language Toolkit (NLTK) with the averaged perceptron tagger, providing relative frequencies for each word category normalized by total word count.

**Sentiment Analysis**
Lastly, to capture emotional response patterns, we investigated sentiment valence (positive, negative, or neutral), which has been consistently linked to depression in previous research. To assess these emotional aspects, we employed the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool, which is specifically designed for social media text and informal language. VADER provides compound sentiment scores and categorizes sentences into positive, negative, or neutral sentiment classes. We computed mean sentiment scores across all sentences and calculated proportions of positive, negative, and neutral sentences for each participant.

**Feature Extraction Pipeline**
Linguistic features were extracted from participants' audio-recorded responses provided during clinical interviews with a virtual avatar. The extraction pipeline was implemented in Python 3.11.9, utilizing established natural language processing libraries including NLTK for tokenization and part-of-speech tagging, spaCy for syntactic parsing, and VADER for sentiment analysis. This multi-step approach ensured comprehensive capture of speech biomarkers relevant to depression assessment.

**Statistical Analysis Methods**
Statistical analyses included Pearson correlation coefficients to examine relationships between speech features and depression severity (PHQ-8 scores), with Bonferroni correction for multiple comparisons (α = 0.05/27 = 0.0019). For gender differences analysis, we employed Mann-Whitney U tests to compare speech features between male and female MDD participants, followed by gender-stratified Spearman rank correlations with False Discovery Rate (FDR) correction using the Benjamini-Hochberg procedure. Linear regression models were used to test Gender × Feature interaction effects on depression severity. All analyses were conducted using Python with scientific computing libraries (pandas, numpy, scipy, scikit-learn, statsmodels) ensuring reproducible and robust statistical inference.
