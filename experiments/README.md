# Experiments

This directory contains all experimental runs for the voice conversion project.

## Organization

Each experiment lives in its own folder with a standardized structure:

```
experiments/
├── exp_001_baseline/
│   ├── config.yaml           # Complete configuration
│   ├── notes.md             # Experiment documentation
│   ├── results.json         # Quantitative metrics
│   ├── samples/             # Generated audio samples
│   └── checkpoints/         # Model weights (if small)
└── exp_002_next_experiment/
    └── ...
```

## Naming Convention

**Format**: `exp_XXX_short_description`

- `XXX` = Three-digit experiment number (001, 002, ..., 099, 100, ...)
- `short_description` = Brief name (e.g., `baseline`, `triplet_loss`, `wavlm_encoder`)

**Examples**:
- `exp_001_baseline` - Initial baseline model
- `exp_025_triplet_loss` - Testing triplet loss addition
- `exp_042_cross_lingual` - Cross-lingual evaluation

## Experiment Structure

### Required Files

#### 1. `config.yaml`
Complete configuration for reproducibility:
```yaml
experiment:
  id: "exp_025"
  name: "Triplet Loss Addition"
  date: "2025-10-20"
  baseline: "exp_020"

model:
  content_encoder: "wavlm"
  style_encoder: "ecapa_tdnn"
  decoder: "hifigan"
  # ... all architecture params

training:
  batch_size: 32
  learning_rate: 0.0001
  # ... all training params

data:
  dataset: "vctk"
  train_speakers: 90
  val_speakers: 10
  # ... all data params
```

#### 2. `notes.md`
Human-readable experiment documentation:
```markdown
# Experiment XXX: Title

## Hypothesis
What are you testing and why?

## Baseline
What are you comparing against?

## Changes
What's different from baseline?

## Expected Outcome
What metrics should improve?

## Results
### Quantitative
- Metric 1: X.XX
- Metric 2: Y.YY

### Qualitative
- Observation 1
- Observation 2

## Analysis
Why did this work or not work?

## Conclusions
What did we learn?

## Next Steps
What to try next based on these results?

## Paper Relevance
[methods] / [results] / [ablation] / [not for paper]
```

#### 3. `results.json`
Structured metrics for easy parsing:
```json
{
  "experiment_id": "exp_025",
  "date": "2025-10-20",
  "baseline": "exp_020",
  "metrics": {
    "speaker_similarity": 0.78,
    "wer": 14.2,
    "mos": 3.4,
    "inference_speed_rtf": 0.15
  },
  "training": {
    "steps": 50000,
    "duration_hours": 8.5,
    "gpu": "A100",
    "cost_usd": 22.50
  },
  "checkpoint": "results/checkpoints/exp_025_final.pt"
}
```

### Optional Files

- `samples/` - Audio samples for qualitative review
- `checkpoints/` - Model weights (only if < 1GB, otherwise use GCS/Modal)
- `logs/` - Training logs if needed
- `figures/` - Any plots or visualizations

## Experiment Workflow

### 1. Planning
```bash
# Create experiment folder
mkdir experiments/exp_026_new_idea

# Copy config template
cp experiments/exp_001_baseline/config.yaml experiments/exp_026_new_idea/

# Edit config for new experiment
# Write notes.md with hypothesis
```

### 2. Running
```bash
# Local testing (small scale)
python src/training/train.py --config experiments/exp_026_new_idea/config.yaml

# Or Modal (GPU)
modal run experiments/exp_026_new_idea/train.py
```

### 3. Evaluation
```bash
# Run evaluation script
python src/evaluation/eval.py \
  --checkpoint results/checkpoints/exp_026.pt \
  --output experiments/exp_026_new_idea/results.json
```

### 4. Documentation
```bash
# Update notes.md with results
# Save sample audio to samples/
# Update RESEARCH_PLAN.md
# Update HANDOFF.md
# Git commit with descriptive message
git commit -m "exp_026: [brief summary of findings]"
```

## Experiment Types

### Baseline Experiments
- **Purpose**: Establish starting point
- **Examples**: exp_001_baseline
- **Document**: Architecture, training procedure, metrics

### Ablation Experiments
- **Purpose**: Test component contribution
- **Examples**: exp_024_no_triplet, exp_025_with_triplet
- **Document**: What was added/removed, impact on metrics

### Hyperparameter Experiments
- **Purpose**: Optimize training
- **Examples**: exp_030_lr_tuning
- **Document**: Parameter sweep, best configuration

### Architecture Experiments
- **Purpose**: Test design choices
- **Examples**: exp_040_diffusion_decoder
- **Document**: Architecture comparison, tradeoffs

### Robustness Experiments
- **Purpose**: Test generalization
- **Examples**: exp_050_cross_gender, exp_051_noisy_audio
- **Document**: Test conditions, failure cases

## Tracking Experiments

### Summary Table
Maintain in RESEARCH_PLAN.md:

| Exp ID | Description | Similarity | WER | Notes | Paper |
|--------|-------------|------------|-----|-------|-------|
| 001 | Baseline | 0.70 | 18% | Works | [methods] |
| 025 | + Triplet loss | 0.78 | 14% | Better | [ablation] |
| ... | ... | ... | ... | ... | ... |

### Paper Mapping
Tag experiments for paper sections:
- `[methods]` - Describe in methods section
- `[results]` - Include in main results table
- `[ablation]` - Include in ablation study
- `[analysis]` - Use for qualitative analysis
- `[not for paper]` - Debugging or failed experiment

## Best Practices

### Reproducibility
- ✅ Set random seeds in config
- ✅ Document exact package versions
- ✅ Save complete config, not just changes
- ✅ Use git commit hash in results.json
- ✅ Document data splits explicitly

### Organization
- ✅ One experiment = one folder
- ✅ Sequential numbering (no gaps)
- ✅ Descriptive names
- ✅ Complete documentation before moving on
- ✅ Link related experiments (baseline, variations)

### Efficiency
- ✅ Start with small-scale test before full training
- ✅ Monitor training, stop early if failing
- ✅ Reuse successful components
- ✅ Track compute costs in results.json
- ✅ Delete large checkpoint files after evaluation (keep on GCS/Modal)

### Analysis
- ✅ Compare to baseline, not just absolute metrics
- ✅ Listen to audio samples, don't just trust numbers
- ✅ Document qualitative observations
- ✅ Note unexpected results or bugs
- ✅ Form hypotheses about why results occurred

## Common Issues

### Experiment Failed
- Document failure in notes.md
- Analyze why (bug, bad config, wrong approach)
- Don't delete - failed experiments are valuable
- Update RESEARCH_PLAN.md with lessons learned

### Experiment Succeeded
- Celebrate! 🎉
- Document thoroughly
- Save samples for paper
- Set as baseline for future experiments
- Update comparison table in RESEARCH_PLAN.md

### Unclear Results
- Need more analysis (ablations, visualizations)
- May need human listening test
- Document uncertainty in notes.md
- Flag for discussion in HANDOFF.md

## Tools

### Compare Experiments
```bash
python scripts/compare_experiments.py exp_020 exp_025 exp_026
```

### Generate Paper Tables
```bash
python scripts/generate_paper_table.py --experiments exp_020,exp_025,exp_030 --output paper/tables/ablation.tex
```

### Find Best Model
```bash
python scripts/find_best.py --metric similarity
```

---

**Remember**: Every experiment teaches us something. Document thoroughly, be honest about results, and build systematically toward SOTA.
