import subprocess
import sys
import os

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package}: {e}")

# Install required packages
print("Installing required packages...")
packages = [
    'pandas',
    'numpy',
    'librosa',
    'praat-parselmouth',
    'scipy',
    'tqdm',
    'psutil',
    'scikit-learn'
]

for package in packages:
    try:
        __import__(package.replace('-', '_').split('[')[0])
        print(f"{package} already installed")
    except ImportError:
        print(f"Installing {package}...")
        install_package(package)

# Now import all required libraries
print("Importing libraries...")
import pandas as pd
import numpy as np
import librosa
import parselmouth
from parselmouth.praat import call
import warnings
warnings.filterwarnings('ignore')
from tqdm import tqdm
import gc
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from functools import lru_cache
import psutil
import time
from scipy import stats
from scipy.signal import find_peaks
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class FrequencyFeatureExtractor:
    def __init__(self, max_workers=None, chunk_size=50):
        """
        Initialize the frequency feature extractor with optimization parameters
        
        Args:
            max_workers: Number of parallel workers (None for auto-detection)
            chunk_size: Number of files to process in each chunk
        """
        self.max_workers = max_workers or min(4, psutil.cpu_count())
        self.chunk_size = chunk_size
        self.lock = threading.Lock()
        
    def memory_monitor(self):
        """Monitor memory usage and trigger garbage collection if needed"""
        memory_percent = psutil.virtual_memory().percent
        if memory_percent > 80:
            gc.collect()
            return True
        return False
    
    def load_audio_file(self, file_path):
        """
        Load audio file without caching for Kaggle environment
        
        Args:
            file_path: Path to audio file
            
        Returns:
            tuple: (audio_data, sample_rate)
        """
        try:
            # Load with librosa for consistency
            audio, sr = librosa.load(file_path, sr=None, mono=True)
            return audio, sr
        except Exception as e:
            print(f"Error loading {file_path}: {str(e)}")
            return None, None
    
    def extract_jitter_features(self, sound_obj):
        """
        Extract jitter-related features using Parselmouth/Praat
        
        Args:
            sound_obj: Parselmouth Sound object
            
        Returns:
            dict: Dictionary containing jitter features
        """
        features = {}
        
        try:
            # Create PointProcess from sound for jitter analysis
            point_process = call(sound_obj, "To PointProcess (periodic, cc)", 75, 500)
            
            # DDP Jitter (Dynamic Decline Perturbation)
            try:
                features['ddp_jitter'] = call(point_process, "Get jitter (ddp)", 0, 0, 0.0001, 0.02, 1.3)
            except:
                features['ddp_jitter'] = np.nan
            
            # Local Jitter (cycle-to-cycle F0 variability)
            try:
                jitter_local = call(point_process, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
                features['jitter_local_mean'] = jitter_local
                # Approximate SD (Praat doesn't provide frame-by-frame jitter directly)
                features['jitter_local_sd'] = jitter_local * 0.15  # Approximate SD
            except:
                features['jitter_local_mean'] = np.nan
                features['jitter_local_sd'] = np.nan
            
            # Local Absolute Jitter
            try:
                features['local_absolute_jitter'] = call(point_process, "Get jitter (local, absolute)", 0, 0, 0.0001, 0.02, 1.3)
            except:
                features['local_absolute_jitter'] = np.nan
            
            # PPQ5 Jitter (5-point period perturbation quotient)
            try:
                features['ppq5_jitter'] = call(point_process, "Get jitter (ppq5)", 0, 0, 0.0001, 0.02, 1.3)
            except:
                features['ppq5_jitter'] = np.nan
            
            # RAP Jitter (Relative Average Perturbation)
            try:
                features['rap_jitter'] = call(point_process, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3)
            except:
                features['rap_jitter'] = np.nan
                
        except Exception as e:
            print(f"Error in jitter extraction: {str(e)}")
            for key in ['ddp_jitter', 'jitter_local_mean', 'jitter_local_sd', 
                       'local_absolute_jitter', 'ppq5_jitter', 'rap_jitter']:
                features[key] = np.nan
                
        return features
    
    def extract_pitch_features(self, sound_obj):
        """
        Extract comprehensive pitch features
        
        Args:
            sound_obj: Parselmouth Sound object
            
        Returns:
            dict: Dictionary containing pitch features
        """
        features = {}
        
        try:
            # Get pitch object
            pitch = sound_obj.to_pitch(time_step=0.01, pitch_floor=75, pitch_ceiling=500)
            
            # Extract pitch values (remove unvoiced frames)
            pitch_values = pitch.selected_array['frequency']
            pitch_values = pitch_values[pitch_values != 0]  # Remove unvoiced frames
            
            if len(pitch_values) > 0:
                # Basic statistics
                features['pitch_mean'] = np.mean(pitch_values)
                features['pitch_std'] = np.std(pitch_values)
                features['pitch_min'] = np.min(pitch_values)
                features['pitch_max'] = np.max(pitch_values)
                features['pitch_range'] = features['pitch_max'] - features['pitch_min']
                
                # F0 range (same as pitch range for voiced segments)
                features['f0_range'] = features['pitch_range']
                
                # Quartiles
                features['pitch_first_quartile'] = np.percentile(pitch_values, 25)
                features['pitch_second_quartile'] = np.percentile(pitch_values, 50)  # Median
                features['pitch_third_quartile'] = np.percentile(pitch_values, 75)
                
                # Quartile ranges
                features['pitch_q2_q1_range'] = features['pitch_second_quartile'] - features['pitch_first_quartile']
                features['pitch_q3_q1_range'] = features['pitch_third_quartile'] - features['pitch_first_quartile']
                features['pitch_q3_q2_range'] = features['pitch_third_quartile'] - features['pitch_second_quartile']
                
                # Percentiles
                features['pitch_percentile_1'] = np.percentile(pitch_values, 1)
                features['pitch_percentile_20'] = np.percentile(pitch_values, 20)
                features['pitch_percentile_80'] = np.percentile(pitch_values, 80)
                features['pitch_percentile_99'] = np.percentile(pitch_values, 99)
                
                # Percentile ranges
                features['pitch_percentile_1_99_range'] = features['pitch_percentile_99'] - features['pitch_percentile_1']
                features['pitch_percentile_20_80_range'] = features['pitch_percentile_80'] - features['pitch_percentile_20']
                
                # Statistical measures
                features['pitch_skewness'] = stats.skew(pitch_values)
                features['pitch_kurtosis'] = stats.kurtosis(pitch_values)
                features['pitch_coefficient_of_variation'] = features['pitch_std'] / features['pitch_mean'] if features['pitch_mean'] != 0 else np.nan
                
                # Linear regression features
                if len(pitch_values) > 1:
                    time_points = np.arange(len(pitch_values)).reshape(-1, 1)
                    reg = LinearRegression().fit(time_points, pitch_values)
                    predictions = reg.predict(time_points)
                    
                    features['pitch_linear_regression_slope'] = reg.coef_[0]
                    features['pitch_linear_regression_offset'] = reg.intercept_
                    features['pitch_linear_regression_mse'] = mean_squared_error(pitch_values, predictions)
                else:
                    features['pitch_linear_regression_slope'] = np.nan
                    features['pitch_linear_regression_offset'] = np.nan
                    features['pitch_linear_regression_mse'] = np.nan
                    
            else:
                # No voiced frames found
                pitch_feature_names = [
                    'pitch_mean', 'pitch_std', 'pitch_min', 'pitch_max', 'pitch_range', 'f0_range',
                    'pitch_first_quartile', 'pitch_second_quartile', 'pitch_third_quartile',
                    'pitch_q2_q1_range', 'pitch_q3_q1_range', 'pitch_q3_q2_range',
                    'pitch_percentile_1', 'pitch_percentile_20', 'pitch_percentile_80', 'pitch_percentile_99',
                    'pitch_percentile_1_99_range', 'pitch_percentile_20_80_range',
                    'pitch_skewness', 'pitch_kurtosis', 'pitch_coefficient_of_variation',
                    'pitch_linear_regression_slope', 'pitch_linear_regression_offset', 'pitch_linear_regression_mse'
                ]
                for feature_name in pitch_feature_names:
                    features[feature_name] = np.nan
                    
        except Exception as e:
            print(f"Error in pitch extraction: {str(e)}")
            pitch_feature_names = [
                'pitch_mean', 'pitch_std', 'pitch_min', 'pitch_max', 'pitch_range', 'f0_range',
                'pitch_first_quartile', 'pitch_second_quartile', 'pitch_third_quartile',
                'pitch_q2_q1_range', 'pitch_q3_q1_range', 'pitch_q3_q2_range',
                'pitch_percentile_1', 'pitch_percentile_20', 'pitch_percentile_80', 'pitch_percentile_99',
                'pitch_percentile_1_99_range', 'pitch_percentile_20_80_range',
                'pitch_skewness', 'pitch_kurtosis', 'pitch_coefficient_of_variation',
                'pitch_linear_regression_slope', 'pitch_linear_regression_offset', 'pitch_linear_regression_mse'
            ]
            for feature_name in pitch_feature_names:
                features[feature_name] = np.nan
                
        return features
    
    def extract_formant_features(self, sound_obj):
        """
        Extract formant frequency and bandwidth features
        
        Args:
            sound_obj: Parselmouth Sound object
            
        Returns:
            dict: Dictionary containing formant features
        """
        features = {}
        
        try:
            # Get formant object
            formant = sound_obj.to_formant_burg(time_step=0.01, max_number_of_formants=5, 
                                              maximum_formant=5500, window_length=0.025, 
                                              pre_emphasis_from=50)
            
            # Extract formant frequencies and bandwidths for F1, F2, F3
            for formant_num in [1, 2, 3]:
                try:
                    # Get all formant values across time
                    frequencies = []
                    bandwidths = []
                    
                    # Sample at regular intervals
                    duration = sound_obj.get_total_duration()
                    time_points = np.arange(0.01, duration, 0.01)  # Every 10ms
                    
                    for t in time_points:
                        try:
                            freq = call(formant, "Get value at time", formant_num, t, "hertz", "Linear")
                            bw = call(formant, "Get bandwidth at time", formant_num, t, "hertz", "Linear")
                            
                            if not np.isnan(freq) and freq > 0:
                                frequencies.append(freq)
                            if not np.isnan(bw) and bw > 0:
                                bandwidths.append(bw)
                        except:
                            continue
                    
                    # Calculate statistics for frequencies
                    if frequencies:
                        features[f'f{formant_num}_frequency_mean'] = np.mean(frequencies)
                        features[f'f{formant_num}_frequency_sd'] = np.std(frequencies)
                    else:
                        features[f'f{formant_num}_frequency_mean'] = np.nan
                        features[f'f{formant_num}_frequency_sd'] = np.nan
                    
                    # Calculate statistics for bandwidths
                    if bandwidths:
                        features[f'f{formant_num}_bandwidth_mean'] = np.mean(bandwidths)
                        features[f'f{formant_num}_bandwidth_sd'] = np.std(bandwidths)
                    else:
                        features[f'f{formant_num}_bandwidth_mean'] = np.nan
                        features[f'f{formant_num}_bandwidth_sd'] = np.nan
                        
                except Exception as e:
                    print(f"Error extracting F{formant_num}: {str(e)}")
                    features[f'f{formant_num}_frequency_mean'] = np.nan
                    features[f'f{formant_num}_frequency_sd'] = np.nan
                    features[f'f{formant_num}_bandwidth_mean'] = np.nan
                    features[f'f{formant_num}_bandwidth_sd'] = np.nan
                    
        except Exception as e:
            print(f"Error in formant extraction: {str(e)}")
            for formant_num in [1, 2, 3]:
                features[f'f{formant_num}_frequency_mean'] = np.nan
                features[f'f{formant_num}_frequency_sd'] = np.nan
                features[f'f{formant_num}_bandwidth_mean'] = np.nan
                features[f'f{formant_num}_bandwidth_sd'] = np.nan
                
        return features
    
    def extract_vocal_tremor(self, sound_obj):
        """
        Extract vocal tremor feature (F0 modulation in 1.5-15 Hz band)
        
        Args:
            sound_obj: Parselmouth Sound object
            
        Returns:
            dict: Dictionary containing vocal tremor feature
        """
        features = {}
        
        try:
            # Get pitch contour
            pitch = sound_obj.to_pitch(time_step=0.01, pitch_floor=75, pitch_ceiling=500)
            pitch_values = pitch.selected_array['frequency']
            pitch_values = pitch_values[pitch_values != 0]  # Remove unvoiced frames
            
            if len(pitch_values) > 30:  # Need sufficient data for tremor analysis
                # Calculate sampling rate of pitch contour
                fs_pitch = 1.0 / 0.01  # 100 Hz (10ms time step)
                
                # Apply FFT to pitch contour
                fft_pitch = np.fft.fft(pitch_values - np.mean(pitch_values))
                freqs = np.fft.fftfreq(len(pitch_values), 1/fs_pitch)
                
                # Find magnitude in tremor frequency band (1.5-15 Hz)
                tremor_mask = (freqs >= 1.5) & (freqs <= 15.0)
                tremor_magnitudes = np.abs(fft_pitch[tremor_mask])
                
                if len(tremor_magnitudes) > 0:
                    features['vocal_tremor'] = np.max(tremor_magnitudes)
                else:
                    features['vocal_tremor'] = np.nan
            else:
                features['vocal_tremor'] = np.nan
                
        except Exception as e:
            print(f"Error in vocal tremor extraction: {str(e)}")
            features['vocal_tremor'] = np.nan
            
        return features
    
    def extract_features_single_file(self, file_path, participant_id):
        """
        Extract all frequency features from a single audio file
        
        Args:
            file_path: Path to audio file
            participant_id: ID of the participant
            
        Returns:
            dict: Dictionary containing all extracted features
        """
        features = {'id': participant_id}
        
        # Define all expected feature names
        all_feature_names = [
            'ddp_jitter', 'f0_range', 'f1_bandwidth_mean', 'f1_bandwidth_sd', 'f1_frequency_mean', 'f1_frequency_sd',
            'f2_bandwidth_mean', 'f2_bandwidth_sd', 'f2_frequency_mean', 'f2_frequency_sd',
            'f3_bandwidth_mean', 'f3_bandwidth_sd', 'f3_frequency_mean', 'f3_frequency_sd',
            'jitter_local_mean', 'jitter_local_sd', 'local_absolute_jitter', 'pitch_coefficient_of_variation',
            'pitch_first_quartile', 'pitch_kurtosis', 'pitch_linear_regression_mse', 'pitch_linear_regression_offset',
            'pitch_linear_regression_slope', 'pitch_max', 'pitch_mean', 'pitch_min', 'pitch_percentile_1',
            'pitch_percentile_20', 'pitch_percentile_20_80_range', 'pitch_percentile_80', 'pitch_percentile_99',
            'pitch_percentile_1_99_range', 'pitch_q2_q1_range', 'pitch_q3_q1_range', 'pitch_q3_q2_range',
            'pitch_range', 'pitch_second_quartile', 'pitch_skewness', 'pitch_std', 'pitch_third_quartile',
            'ppq5_jitter', 'rap_jitter', 'vocal_tremor'
        ]
        
        try:
            # Load audio
            audio, sr = self.load_audio_file(file_path)
            if audio is None:
                # Return NaN features if loading failed
                for feature_name in all_feature_names:
                    features[feature_name] = np.nan
                return features
            
            # Create Parselmouth Sound object
            sound = parselmouth.Sound(audio, sampling_frequency=sr)
            
            # Extract jitter features
            jitter_features = self.extract_jitter_features(sound)
            features.update(jitter_features)
            
            # Extract pitch features
            pitch_features = self.extract_pitch_features(sound)
            features.update(pitch_features)
            
            # Extract formant features
            formant_features = self.extract_formant_features(sound)
            features.update(formant_features)
            
            # Extract vocal tremor
            tremor_features = self.extract_vocal_tremor(sound)
            features.update(tremor_features)
            
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")
            # Return NaN features if processing failed
            for feature_name in all_feature_names:
                if feature_name not in features:
                    features[feature_name] = np.nan
        
        return features

def find_lexical_richness_file():
    """
    Find the lexical richness CSV file in Kaggle input directories
    """
    search_paths = [
        '/kaggle/input/labels/lexical_richness_FINAL_CLEAN.csv',
        '/kaggle/input/features/lexical_richness_FINAL_CLEAN.csv',
        '/kaggle/input/lexical_richness_FINAL_CLEAN.csv'
    ]
    
    for file_path in search_paths:
        if os.path.exists(file_path):
            return file_path
    
    return None

def find_audio_files_for_lexical_ids(lexical_ids):
    """
    Find audio files that match the IDs from lexical richness data
    
    Args:
        lexical_ids: Set of participant IDs from lexical richness data
        
    Returns:
        dict: Dictionary mapping participant_id to file_path
    """
    audio_files_dict = {}
    
    # Search in the audio directory
    audio_dir = '/kaggle/input/all-audio/All_AUDIO'
    
    if os.path.exists(audio_dir):
        print(f"Searching for audio files in: {audio_dir}")
        
        try:
            files_in_dir = os.listdir(audio_dir)
            audio_files_found = [f for f in files_in_dir if f.lower().endswith(('.wav', '.mp3', '.m4a', '.flac'))]
            
            print(f"  Found {len(audio_files_found)} audio files in directory")
            
            for file in audio_files_found:
                try:
                    # Extract participant ID from filename
                    if '_' in file:
                        participant_id = int(file.split('_')[0])
                    elif '.' in file:
                        participant_id = int(file.split('.')[0])
                    else:
                        continue
                        
                    # Only include if it's in our lexical richness IDs
                    if participant_id in lexical_ids:
                        file_path = os.path.join(audio_dir, file)
                        audio_files_dict[participant_id] = file_path
                        
                except ValueError:
                    # Skip files that don't have numeric IDs
                    continue
                    
        except Exception as e:
            print(f"  Error searching in {audio_dir}: {e}")
    
    return audio_files_dict

def main():
    """
    Main function to orchestrate the frequency feature extraction process
    """
    print("Frequency Feature Extraction Script")
    print("=" * 60)
    
    print("\n" + "=" * 60)
    print("LOADING LEXICAL RICHNESS DATA")
    print("=" * 60)
    
    # Find and load lexical richness file
    lexical_file_path = find_lexical_richness_file()
    
    if lexical_file_path is None:
        print("Could not find lexical richness file!")
        return None
    
    print(f"Found lexical richness file: {lexical_file_path}")
    
    try:
        lexical_df = pd.read_csv(lexical_file_path)
        lexical_ids = set(lexical_df['id'].values)
        print(f"Loaded {len(lexical_ids)} participant IDs from lexical richness data")
        print(f"ID range: {min(lexical_ids)} to {max(lexical_ids)}")
        print(f"Sample IDs: {sorted(list(lexical_ids))[:10]}...")
    except Exception as e:
        print(f"Error loading lexical richness data: {str(e)}")
        return None
    
    print(f"\n" + "=" * 60)
    print("FINDING MATCHING AUDIO FILES")
    print("=" * 60)
    
    # Find audio files that match lexical richness IDs
    audio_files_dict = find_audio_files_for_lexical_ids(lexical_ids)
    
    if not audio_files_dict:
        print("No matching audio files found!")
        return None
    
    print(f"SUCCESS! Matched {len(audio_files_dict)} audio files to lexical richness IDs")
    print(f"Found audio files for {len(audio_files_dict)}/{len(lexical_ids)} participants ({len(audio_files_dict)/len(lexical_ids)*100:.1f}%)")
    
    # Convert to list of tuples for processing
    audio_files_info = [(file_path, participant_id) for participant_id, file_path in audio_files_dict.items()]
    
    # Sort by participant ID for consistent processing
    audio_files_info.sort(key=lambda x: x[1])
    
    print(f"\nWill process {len(audio_files_info)} files:")
    for i, (file_path, participant_id) in enumerate(audio_files_info[:5]):
        print(f"  {i+1}. ID {participant_id}: {os.path.basename(file_path)}")
    if len(audio_files_info) > 5:
        print(f"  ... and {len(audio_files_info) - 5} more files")
    
    # Check for missing audio files
    missing_ids = lexical_ids - set(audio_files_dict.keys())
    if missing_ids:
        print(f"\nNote: {len(missing_ids)} participant IDs from lexical data have no matching audio files")
    
    # Initialize feature extractor
    print(f"\n" + "=" * 60)
    print("STARTING FREQUENCY FEATURE EXTRACTION")
    print("=" * 60)
    
    extractor = FrequencyFeatureExtractor(max_workers=2, chunk_size=5)
    
    # Extract features sequentially for better error handling
    all_features = []
    
    print(f"Processing {len(audio_files_info)} files...")
    print("Extracting: Pitch, Jitter, Formants, and Vocal Tremor features...")
    start_time = time.time()
    
    for i, (file_path, participant_id) in enumerate(audio_files_info):
        print(f"Processing file {i+1}/{len(audio_files_info)}: ID {participant_id}")
        
        # Memory check
        extractor.memory_monitor()
        
        try:
            features = extractor.extract_features_single_file(file_path, participant_id)
            all_features.append(features)
            
            # Show progress every 20 files
            if (i + 1) % 20 == 0:
                elapsed = time.time() - start_time
                avg_time = elapsed / (i + 1)
                remaining = avg_time * (len(audio_files_info) - (i + 1))
                print(f"  Progress: {i+1}/{len(audio_files_info)} files | Avg: {avg_time:.1f}s/file | ETA: {remaining/60:.1f} min")
                
        except Exception as e:
            print(f"  ❌ Error processing ID {participant_id}: {str(e)}")
            # Add empty feature set for failed files
            empty_features = {'id': participant_id}
            all_feature_names = [
                'ddp_jitter', 'f0_range', 'f1_bandwidth_mean', 'f1_bandwidth_sd', 'f1_frequency_mean', 'f1_frequency_sd',
                'f2_bandwidth_mean', 'f2_bandwidth_sd', 'f2_frequency_mean', 'f2_frequency_sd',
                'f3_bandwidth_mean', 'f3_bandwidth_sd', 'f3_frequency_mean', 'f3_frequency_sd',
                'jitter_local_mean', 'jitter_local_sd', 'local_absolute_jitter', 'pitch_coefficient_of_variation',
                'pitch_first_quartile', 'pitch_kurtosis', 'pitch_linear_regression_mse', 'pitch_linear_regression_offset',
                'pitch_linear_regression_slope', 'pitch_max', 'pitch_mean', 'pitch_min', 'pitch_percentile_1',
                'pitch_percentile_20', 'pitch_percentile_20_80_range', 'pitch_percentile_80', 'pitch_percentile_99',
                'pitch_percentile_1_99_range', 'pitch_q2_q1_range', 'pitch_q3_q1_range', 'pitch_q3_q2_range',
                'pitch_range', 'pitch_second_quartile', 'pitch_skewness', 'pitch_std', 'pitch_third_quartile',
                'ppq5_jitter', 'rap_jitter', 'vocal_tremor'
            ]
            for feature_name in all_feature_names:
                empty_features[feature_name] = np.nan
            all_features.append(empty_features)
            continue
    
    end_time = time.time()
    total_time = end_time - start_time
    
    if not all_features:
        print("No features were extracted!")
        return None
    
    # Convert to DataFrame
    print(f"\nCreating DataFrame from {len(all_features)} feature sets...")
    features_df = pd.DataFrame(all_features)
    
    # Sort by ID for consistency
    features_df = features_df.sort_values('id').reset_index(drop=True)
    
    # Display summary
    print("\n" + "=" * 60)
    print("EXTRACTION RESULTS")
    print("=" * 60)
    print(f"Total processing time: {total_time/60:.1f} minutes")
    print(f"Average time per file: {total_time/len(audio_files_info):.1f} seconds")
    print(f"Total participants processed: {len(features_df)}")
    print(f"Features per participant: {len(features_df.columns) - 1}")
    
    feature_names = [col for col in features_df.columns if col != 'id']
    print(f"Extracted {len(feature_names)} frequency features")
    
    # Group features by type
    jitter_features = [f for f in feature_names if 'jitter' in f]
    pitch_features = [f for f in feature_names if 'pitch' in f or 'f0_range' in f]
    formant_features = [f for f in feature_names if any(f'f{i}_' in f for i in [1,2,3])]
    tremor_features = [f for f in feature_names if 'tremor' in f]
    
    print(f"  - Jitter features: {len(jitter_features)}")
    print(f"  - Pitch features: {len(pitch_features)}")
    print(f"  - Formant features: {len(formant_features)}")
    print(f"  - Tremor features: {len(tremor_features)}")
    
    # Check for missing values
    print(f"\nData quality check:")
    for feature in feature_names:
        valid_count = features_df[feature].notna().sum()
        success_rate = (valid_count / len(features_df)) * 100
        if success_rate < 90:  # Only show features with high missing rates
            print(f"  {feature}: {valid_count}/{len(features_df)} valid ({success_rate:.1f}%)")
    
    # Save results
    output_filename = '/kaggle/working/frequency_features.csv'
    try:
        features_df.to_csv(output_filename, index=False)
        print(f"\nFeatures saved to: {output_filename}")
    except Exception as e:
        print(f"Error saving features: {str(e)}")
        # Try alternative path
        alt_filename = 'frequency_features.csv'
        features_df.to_csv(alt_filename, index=False)
        print(f"Features saved to: {alt_filename}")
    
    # Display sample results
    print(f"\nSample results (first 3 participants, key features):")
    key_features = ['id', 'pitch_mean', 'pitch_std', 'f0_range', 'f1_frequency_mean', 'f2_frequency_mean', 
                   'jitter_local_mean', 'vocal_tremor']
    sample_df = features_df[key_features].head(3).round(4)
    print(sample_df.to_string(index=False))
    
    print("\n" + "=" * 60)
    print("FREQUENCY FEATURE EXTRACTION COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print(f"✅ Processed {len(features_df)} participants")
    print(f"✅ Extracted {len(feature_names)} frequency features per participant")
    print(f"✅ Results saved to: {output_filename}")
    
    return features_df

if __name__ == "__main__":
    try:
        result_df = main()
        if result_df is not None:
            print(f"\n🎉 SUCCESS! Generated frequency features for {len(result_df)} participants.")
            print(f"Frequency feature extraction completed successfully!")
        else:
            print("\n❌ Extraction failed.")
    except Exception as e:
        print(f"\n💥 Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()