# Results Directory

## 📊 Analysis Outputs

This directory will contain example outputs and visualizations from the gender differences analysis in MDD speech biomarkers.

### 🚧 Coming Soon

The following results will be added once the analysis scripts are finalized:

#### 📈 figures/
- **correlation_heatmaps.png** - Gender-stratified correlation matrices
- **scatter_plots_significant.png** - Scatter plots of significant correlations
- **effect_size_comparison.png** - Cohen's d effect sizes by gender
- **demographics_visualization.png** - Sample characteristics visualization
- **interaction_plots.png** - Gender × Feature interaction effects

#### 📋 tables/
- **demographics_table.csv** - Sample demographics by gender and group
- **correlation_results.csv** - All correlation coefficients and p-values
- **mann_whitney_results.csv** - Gender difference test results
- **fdr_corrected_results.csv** - Multiple comparisons corrected results
- **effect_sizes.csv** - Cohen's d calculations for all comparisons

### 📊 Expected Results Preview

Based on our analysis, results will show:

#### Key Findings
- **No significant gender differences** in speech features after FDR correction
- **Distinct correlation patterns:**
  - Males: 1 significant correlation (mean sentiment: ρ = -0.287)
  - Females: 4 significant correlations (sentiment + linguistic features)
- **No significant Gender × Feature interactions** after correction
- **Notable effect sizes** for sentiment-related features

#### Statistical Summary
- **Sample Size**: 67 MDD participants (30 male, 37 female)
- **Features Analyzed**: 27 linguistic features across 4 categories
- **Statistical Methods**: Spearman correlations, Mann-Whitney U, FDR correction
- **Significance Threshold**: p < 0.05 after Benjamini-Hochberg correction

### 🔒 Privacy Protection

All results in this directory will be:
- ✅ **Aggregated data only** (no individual participant information)
- ✅ **Statistical summaries** (means, correlations, p-values)
- ✅ **Anonymized visualizations** (no identifying information)
- ✅ **Publication-ready format** (suitable for academic papers)

### 📁 File Organization

```
results/
├── figures/
│   ├── correlation_analysis/       # Correlation heatmaps and plots
│   ├── group_comparisons/         # Gender difference visualizations
│   ├── effect_sizes/              # Effect size comparisons
│   └── demographics/              # Sample characteristics plots
└── tables/
    ├── statistical_tests/         # All statistical test results
    ├── demographics/              # Sample description tables
    └── correlations/              # Correlation matrices and summaries
```

### 🎯 Usage

Once available, these results can be used for:
- **Manuscript preparation** - Tables and figures for publication
- **Presentation materials** - Conference slides and posters
- **Further analysis** - Secondary analyses and meta-analyses
- **Replication studies** - Comparison with future research

### ⚠️ Important Note

**No raw participant data will ever be included in this repository.** All outputs are statistical summaries and aggregated results that protect participant privacy while enabling scientific reproducibility.
