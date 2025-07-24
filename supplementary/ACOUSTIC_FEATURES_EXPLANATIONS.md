# Acoustic Speech Features Explanations

| Feature | Explanation |
|---------|-------------|
| apq3_shimmer | 3-point Amplitude Perturbation Quotient - measures short-term amplitude variation |
| apq5_shimmer | 5-point Amplitude Perturbation Quotient - measures medium-term amplitude variation |
| apq11_shimmer | 11-point Amplitude Perturbation Quotient - measures long-term amplitude variation |
| dda_shimmer | Directional Derivative Algorithm shimmer - alternative amplitude variation measure |
| hnr_mean | Mean harmonics-to-noise ratio - voice clarity/breathiness measure |
| hnr_sd | Standard deviation of harmonics-to-noise ratio |
| local_shimmer | Local shimmer - cycle-to-cycle amplitude variation |
| loudness_mean | Mean perceived loudness level |
| loudness_sd | Standard deviation of perceived loudness |
| rate_loudness_peaks | Frequency of loudness peaks per unit time |
| shimmer_local_dB_mean | Mean local shimmer in decibels |
| shimmer_local_dB_sd | Standard deviation of local shimmer in decibels |
| ddp_jitter | Directional Derivative of Period jitter - frequency variation measure |
| f0_range | Range of fundamental frequency (pitch range) |
| f1_bandwidth_mean | Mean bandwidth of first formant (tongue height) |
| f1_bandwidth_sd | Standard deviation of first formant bandwidth |
| f1_frequency_mean | Mean frequency of first formant |
| f1_frequency_sd | Standard deviation of first formant frequency |
| f2_bandwidth_mean | Mean bandwidth of second formant (tongue position) |
| f2_bandwidth_sd | Standard deviation of second formant bandwidth |
| f2_frequency_mean | Mean frequency of second formant |
| f2_frequency_sd | Standard deviation of second formant frequency |
| f3_bandwidth_mean | Mean bandwidth of third formant (lip rounding) |
| f3_bandwidth_sd | Standard deviation of third formant bandwidth |
| f3_frequency_mean | Mean frequency of third formant |
| f3_frequency_sd | Standard deviation of third formant frequency |
| jitter_local_mean | Mean local jitter - cycle-to-cycle frequency variation |
| jitter_local_sd | Standard deviation of local jitter |
| local_absolute_jitter | Absolute local jitter in microseconds |
| pitch_coefficient_of_variation | Coefficient of variation of pitch (normalized variability) |
| pitch_first_quartile | 25th percentile of pitch distribution |
| pitch_kurtosis | Kurtosis of pitch distribution (peakedness) |
| pitch_linear_regression_mse | Mean squared error of pitch linear trend |
| pitch_linear_regression_offset | Y-intercept of pitch linear trend |
| pitch_linear_regression_slope | Slope of pitch linear trend |
| pitch_max | Maximum pitch value |
| pitch_mean | Mean pitch value |
| pitch_min | Minimum pitch value |
| pitch_percentile_1 | 1st percentile of pitch distribution |
| pitch_percentile_20 | 20th percentile of pitch distribution |
| pitch_percentile_20_80_range | Range between 20th and 80th percentiles |
| pitch_percentile_80 | 80th percentile of pitch distribution |
| pitch_percentile_99 | 99th percentile of pitch distribution |
| pitch_percentile_1_99_range | Range between 1st and 99th percentiles |
| pitch_q2_q1_range | Range between 1st and 2nd quartiles |
| pitch_q3_q1_range | Range between 1st and 3rd quartiles |
| pitch_q3_q2_range | Range between 2nd and 3rd quartiles |
| pitch_range | Overall pitch range (max - min) |
| pitch_second_quartile | 50th percentile (median) of pitch distribution |
| pitch_skewness | Skewness of pitch distribution (asymmetry) |
| pitch_std | Standard deviation of pitch |
| pitch_third_quartile | 75th percentile of pitch distribution |
| ppq5_jitter | 5-point Period Perturbation Quotient - medium-term frequency variation |
| rap_jitter | Relative Average Perturbation jitter - short-term frequency variation |
| vocal_tremor | Measure of involuntary voice tremor/oscillation |

---

## Feature Categories Summary:
- **Shimmer Features (7)**: apq3_shimmer, apq5_shimmer, apq11_shimmer, dda_shimmer, local_shimmer, shimmer_local_dB_mean, shimmer_local_dB_sd
- **Jitter Features (6)**: ddp_jitter, jitter_local_mean, jitter_local_sd, local_absolute_jitter, ppq5_jitter, rap_jitter  
- **Pitch Features (25)**: f0_range, pitch_* (22 features), vocal_tremor
- **Formant Features (12)**: f1_*, f2_*, f3_* (4 features each)
- **Voice Quality (2)**: hnr_mean, hnr_sd
- **Loudness Features (3)**: loudness_mean, loudness_sd, rate_loudness_peaks
- **Tremor (1)**: vocal_tremor

**Total: 56 acoustic features** in the exact order provided.
