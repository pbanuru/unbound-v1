# Data Management

This directory contains datasets and preprocessing code for voice conversion experiments.

## Directory Structure

```
data/
├── raw/                    # Original datasets (gitignored)
│   ├── VCTK/
│   ├── LibriTTS/
│   └── AISHELL-3/
├── processed/              # Preprocessed features (gitignored)
│   ├── vctk_train/
│   ├── vctk_val/
│   ├── vctk_test/
│   └── metadata/
└── preprocessing/          # Preprocessing scripts
    ├── preprocess_vctk.py
    ├── extract_features.py
    └── split_speakers.py
```

## Datasets

### Primary Dataset: VCTK

**CSTR VCTK Corpus**
- **Description**: Multi-speaker English corpus
- **Speakers**: 109 native English speakers
- **Recording**: High-quality studio recordings
- **Size**: ~11GB
- **License**: Open (free for research/commercial)
- **URL**: https://datashare.ed.ac.uk/handle/10283/3443

**Statistics**:
- 109 speakers (male: 53, female: 56)
- ~400 utterances per speaker
- 48kHz sampling rate
- Total ~44,000 utterances

**Usage**:
- Training: 90 speakers (~36,000 utterances)
- Validation: 10 speakers (~4,000 utterances)
- Test: 9 speakers (~3,600 utterances)

**Advantages**:
- High recording quality
- Good speaker diversity (accents, ages)
- Standard benchmark for VC
- Manageable size

**Limitations**:
- Only English
- Read speech (not conversational)
- Single recording condition

### Secondary Dataset: LibriTTS (Optional)

**LibriTTS**
- **Description**: Multi-speaker audiobook corpus
- **Speakers**: 1000+ speakers
- **Size**: ~50GB
- **License**: Public domain
- **URL**: https://openslr.org/60/

**Usage**: May add for increased speaker diversity if needed

### Cross-Lingual Dataset: AISHELL-3 (Future)

**AISHELL-3**
- **Description**: Mandarin multi-speaker corpus
- **Speakers**: 218 speakers
- **Size**: ~85GB
- **License**: Apache 2.0
- **URL**: https://openslr.org/93/

**Usage**: For cross-lingual evaluation (Phase 3)

---

## Dataset Comparison (Deep Research Findings)

**Research Date**: 2025-10-18 | **Web Searches**: 110

### VCTK vs LibriTTS vs AISHELL-3

| Criteria | VCTK | LibriTTS | AISHELL-3 |
|----------|------|----------|-----------|
| **Speakers** | 109 (balanced gender) | 2,456+ (male-heavy) | 218 (80% female, 80% <25yo) |
| **Language** | English (UK accents) | English (US/UK) | Mandarin Chinese |
| **Recording Quality** | Very high (studio, 96kHz) | High but variable (audiobooks) | Very high (controlled, 44.1kHz) |
| **Consistency** | Excellent | Moderate (multi-source) | Excellent |
| **Speaking Style** | Read speech (neutral) | Read speech (audiobook) | Read speech (neutral) |
| **Generalization** | Good for UK English | Best for diverse English | Good for Mandarin only |
| **Biases** | UK accent bias | Audiobook/formal text bias | Young female Mandarin bias |

### Detailed Comparison

#### Speaker Diversity
- **VCTK**: ~110 English speakers, gender roughly balanced, various UK accents, broad adult ages
- **LibriTTS**: **Several thousand** English speakers from diverse backgrounds (best for generalization to new English voices)
- **AISHELL-3**: 218 Chinese speakers, heavily skewed (175 female/43 male, 175 under 25/43 over 25, 165 northern/51 southern)

#### Recording Quality & Consistency
- **VCTK**: Recorded in controlled studio at 96 kHz, very clean and uniform
- **LibriTTS**: Compiled from audiobook recordings at 24 kHz, quality varies by speaker/equipment
- **AISHELL-3**: Recorded in single professional setup at 44.1 kHz, minimal noise/reverb

#### Speaking Style Variety
- **All three are read speech only** - none contain conversational dialogue
- VCTK: Newspaper text, "Rainbow" passage (accent elicitation)
- LibriTTS: Classic literature/audiobook narration
- AISHELL-3: Neutral scripted prompts

#### Generalization to Unseen Speakers
- **LibriTTS**: Best suited for English VC due to huge speaker count and variety
- **VCTK**: Good for English but may overfit to UK accents (limited speaker count)
- **AISHELL-3**: Useful only for Mandarin voices, language-specific

#### Known Issues and Biases
- **VCTK**: UK accent dominance, formal text only, one missing transcript (p315)
- **LibriTTS**: Audiobook reader bias, male-heavy, classic literature style, no slang/casual speech
- **AISHELL-3**: Young female northern Mandarin dominance, some speakers "hesitant or mechanical"

### Recommendation for Our Project
**Primary**: Start with VCTK for standard benchmarking and controlled experiments
**Secondary**: Add LibriTTS for better generalization to diverse English voices
**Future**: Use AISHELL-3 only if pursuing cross-lingual capabilities

## Data Download

### For Human Assistant

VCTK dataset is too large for Claude to download efficiently. Please download manually:

```bash
# Download VCTK
wget https://datashare.ed.ac.uk/bitstream/handle/10283/3443/VCTK-Corpus-0.92.zip

# Unzip
unzip VCTK-Corpus-0.92.zip -d data/raw/

# Verify
ls data/raw/VCTK-Corpus-0.92/
# Should see: wav48_silence_trimmed/, txt/, speaker-info.txt
```

**Then upload to GCS bucket** for persistent storage and Claude's access.

### For Claude

If dataset is on GCS bucket:
```bash
# Download from GCS (example)
gsutil -m cp -r gs://your-bucket/VCTK data/raw/
```

## Data Preprocessing

### Step 1: Speaker Splits

Split speakers into train/val/test sets:

```python
# preprocessing/split_speakers.py
python data/preprocessing/split_speakers.py \
  --dataset data/raw/VCTK-Corpus-0.92 \
  --output data/processed/metadata/splits.json \
  --train 90 --val 10 --test 9
```

Output: `splits.json`
```json
{
  "train": ["p225", "p226", ...],
  "val": ["p360", "p361", ...],
  "test": ["p362", "p363", ...]
}
```

### Step 2: Audio Preprocessing

Clean and normalize audio:

```python
# preprocessing/preprocess_vctk.py
python data/preprocessing/preprocess_vctk.py \
  --input data/raw/VCTK-Corpus-0.92 \
  --output data/processed/ \
  --sample_rate 16000 \
  --trim_silence \
  --normalize
```

Operations:
- Resample to 16kHz (from 48kHz)
- Trim leading/trailing silence
- Normalize volume
- Verify audio quality (detect corrupted files)

### Step 3: Feature Extraction

Extract features for training:

```python
# preprocessing/extract_features.py
python data/preprocessing/extract_features.py \
  --input data/processed/audio/ \
  --output data/processed/features/ \
  --features mel,f0,energy \
  --splits data/processed/metadata/splits.json
```

Features to extract:
- **Mel-spectrograms** (80 bins)
- **F0** (fundamental frequency/pitch)
- **Energy** (loudness)
- **Speaker embeddings** (ECAPA-TDNN or WavLM)

Output structure:
```
data/processed/
├── vctk_train/
│   ├── p225/
│   │   ├── p225_001.mel.npy
│   │   ├── p225_001.f0.npy
│   │   └── p225_001.energy.npy
│   └── ...
├── vctk_val/
└── vctk_test/
```

## Data Loading

### PyTorch DataLoader

Example usage in training:

```python
from torch.utils.data import DataLoader
from src.data.voice_dataset import VoiceDataset

train_dataset = VoiceDataset(
    data_dir='data/processed/vctk_train',
    split='train',
    sample_rate=16000,
    segment_length=16000  # 1 second segments
)

train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True,
    num_workers=4
)
```

### Data Augmentation

**Research-Backed Augmentation Strategies** (2025-10-18 Deep Research):

Apply these augmentations during training to improve one-shot VC robustness and generalization:

#### Recommended Augmentations

1. **Pitch Shifting** ⭐ *Highly Effective*
   - Randomly raise/lower F0 by ±2-4 semitones
   - Simulates speakers with different voice pitch (male vs. female vs. child)
   - Helps model disentangle pitch from timbre
   - *Research note*: "Invaluable tool for audio augmentation"

2. **Time Stretching (Speed Perturbation)** ⭐ *Highly Effective*
   - Speed up or slow down by ±10-20% without changing pitch
   - Creates variation in speaking rate and prosody
   - *Research note*: "Widely used to cover variations machines must tolerate"

3. **Noise Injection** ⭐ *Critical for Robustness*
   - Add background noise at various SNRs (15-40 dB)
   - Use diverse noise types: urban, music, crowd, office
   - Recommendation: Use MUSAN or real-world noise corpora
   - Makes model robust to real-world conditions
   - *Research note*: "Significantly improves robustness"

4. **Room Reverberation**
   - Convolve with room impulse responses (RIRs)
   - Simulates different acoustic spaces (small room, hall, etc.)
   - Forces model to handle echo and distance variations
   - *Research note*: "Prepares models for varied acoustic environments"

5. **Volume Perturbation**
   - Random gain changes (±6 dB)
   - Helps model handle recording level differences

6. **Spectral Shaping**
   - Equalization adjustments
   - Simulates different microphone characteristics

7. **SpecAugment-Style Masking**
   - Time/frequency masking on spectrograms
   - Common in speech recognition, can help VC too

#### Implementation Strategy
```python
# Example augmentation pipeline
augmentations = [
    PitchShift(semitones=(-3, 3)),       # ±3 semitones
    TimeStretch(rate=(0.9, 1.1)),         # ±10% speed
    AddNoise(snr=(15, 40), noise_dir='noise_corpus/'),
    AddReverb(rir_dir='rir_corpus/'),
    RandomGain(min_gain=-6, max_gain=6)
]
```

#### Evidence from Research
Recent VC studies show that **"simple data augmentation techniques"** combined with diverse training data vastly improved VC robustness to:
- New accents
- Noisy environments
- Different recording conditions

*Sources*: 110 web searches on data augmentation for voice conversion (2025-10-18)

---

### Legacy Augmentation List (Pre-Research)
~~- **Time stretching** (0.9x - 1.1x)~~
~~- **Pitch shifting** (±2 semitones)~~
~~- **Noise addition** (SNR: 20-40dB)~~
~~- **Formant shifting** (for cross-gender)~~
~~- **Reverberation** (small room impulse responses)~~

*Updated with research-backed strategies above*

## Data Statistics

### VCTK Statistics (to be computed)

After preprocessing, compute and save:
- Mean/std of mel-spectrograms
- F0 range per speaker
- Gender distribution
- Average utterance length
- Speaking rate statistics

Save to: `data/processed/metadata/statistics.json`

## Storage Strategy

### Local Storage (~20GB limit)
- Keep processed features only (not raw audio)
- Delete after uploading to GCS/Modal
- Keep metadata and splits locally

### GCS Bucket (Human manages)
- Raw datasets (VCTK, LibriTTS)
- Full processed features
- Experiment checkpoints
- Generated samples

### Modal Volumes (Claude manages)
- Active training data
- Temporary experiment outputs
- Can be deleted after experiment

## Data Splits

### Train/Val/Test Split

**Principle**: Split by speaker, not utterance

- **Train**: 90 speakers (82%)
- **Val**: 10 speakers (9%)
- **Test**: 9 speakers (9%)

**Important**:
- No speaker overlap between splits
- Test speakers never seen during training
- Evaluate generalization to unseen voices

### Cross-Dataset Evaluation

For robustness, also evaluate:
- Train on VCTK, test on LibriTTS subset
- Tests cross-dataset generalization

## Data Quality

### Checks to Implement

```python
# Verify data quality
python data/preprocessing/verify_data.py \
  --input data/processed/vctk_train/ \
  --checks audio_quality,feature_shape,no_nans
```

Checks:
- ✅ No corrupted audio files
- ✅ All features same shape/format
- ✅ No NaN or Inf values
- ✅ F0 in reasonable range (80-500 Hz)
- ✅ Mel values in expected range

## Benchmarks

### Processing Time (Estimates)

- Download VCTK: ~10 minutes (11GB)
- Unzip: ~2 minutes
- Audio preprocessing: ~30 minutes (VCTK full)
- Feature extraction: ~1-2 hours (VCTK full)

### Storage Requirements

- VCTK raw: 11GB
- VCTK processed audio (16kHz): ~4GB
- VCTK features (mel+f0+energy): ~6GB
- Total for VCTK: ~21GB (before cleanup)

**Strategy**: Delete raw after processing, keep only features

## Data Access for Claude

### GCS Bucket (CONFIGURED ✅)

**Bucket Details:**
- **Name**: `gs://unbound-v1-data/`
- **Project**: `unbound-v1`
- **Location**: `us-west1` (California region)
- **Storage Class**: `STANDARD`
- **Billing**: YN Billing Account
- **Created**: 2025-10-18

**Usage:**
```bash
# List datasets
gsutil ls gs://unbound-v1-data/

# Download preprocessed data
gsutil -m cp -r gs://unbound-v1-data/data/processed/vctk_train data/processed/

# Upload results
gsutil -m cp -r results/exp_025 gs://unbound-v1-data/results/

# Upload datasets (for human)
gsutil -m cp -r data/raw/VCTK gs://unbound-v1-data/data/raw/
```

### Alternative: Modal Volumes

```python
# In Modal script
import modal

volume = modal.Volume.from_name("voice-conversion-data")

@app.function(volumes={"/data": volume})
def train():
    # Data available at /data/
    pass
```

## Next Steps

### For Human
1. Download VCTK dataset
2. Upload to GCS bucket
3. Provide Claude with GCS credentials
4. Confirm storage strategy

### For Claude
1. Write preprocessing scripts
2. Process VCTK data
3. Verify data quality
4. Create dataloaders
5. Document statistics

---

**Status**: Awaiting dataset download and GCS bucket setup
**Last Updated**: 2025-10-18
