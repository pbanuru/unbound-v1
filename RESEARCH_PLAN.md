# Voice Conversion Research Plan

**Project**: unbound-v1 - Single-Shot Voice Conversion
**Last Updated**: 2025-10-18
**Current Phase**: Phase 0 - Strategic Research
**Week**: 0 of 12

---

## Project Overview

### Primary Objective
Build a **state-of-the-art single-shot voice conversion model** that can convert any source speaker's voice to a target speaker's voice using only **one reference utterance**.

### Success Criteria
1. **Speaker Similarity** > 0.87 (beat Seed-VC's 0.8676)
2. **Word Error Rate (WER)** < 12% (match/beat Seed-VC's 11.99%)
3. **Naturalness (MOS)** > 3.8 (on 5-point scale)
4. **Inference Speed** < 0.2 RTF (real-time factor)
5. **Novel Contribution** for paper publication
6. **Open Source** release under Apache 2.0

### Constraints
- **Budget**: $5000 Modal compute credits
- **Storage**: ~20GB local (use GCS bucket for large datasets)
- **Datasets**: Open-source only (VCTK, LibriTTS, AISHELL-3, etc.)
- **Timeline**: ~12 weeks target

---

## Current Status

### What's Working
- ✅ Deep Research tool set up and functional
- ✅ Previous research sessions analyzed (3 sessions completed)
- ✅ Project structure created
- ✅ Documentation framework established

### What's In Progress
- 🔄 Phase 0: Strategic research and architecture design

### What's Blocked
- ⏸️ Dataset download (need GCS bucket setup from human)
- ⏸️ Modal credentials verification

### Current Metrics
- Baseline: Not yet established
- Target: Seed-VC (Similarity: 0.8676, WER: 11.99%)

---

## Research Phases

### Phase 0: Strategic Research (Week 1) - **CURRENT PHASE**
**Goal**: Make informed architectural decisions before spending compute budget

**Budget**: $0 compute, ~$20 Deep Research API calls
**Status**: In Progress

#### Tasks
- [ ] **Literature Review**: Deep dive on Seed-VC architecture and weaknesses
- [ ] **Architecture Analysis**: Compare diffusion vs flow vs GAN decoders
- [ ] **Feature Analysis**: WavLM vs HuBERT vs Whisper for content encoding
- [ ] **Data Strategy**: Compare VCTK, LibriTTS, AISHELL-3 for training
- [ ] **Architecture Proposal**: 1-page proposal with design decisions

#### Deliverables
- [ ] Seed-VC analysis report (DeepResearcher output)
- [ ] Architecture comparison document (docs/architecture.md)
- [ ] Data strategy document (data/README.md)
- [ ] **Final**: Architecture proposal for human review

#### Success Criteria
- Understanding of SOTA strengths/weaknesses
- Clear architectural choices with rationale
- Budget estimate for Phase 1-3

---

### Phase 1: Foundation (Week 2-3)
**Goal**: Get baseline working end-to-end

**Budget**: ~$500
**Status**: Not Started

#### Tasks
- [ ] Data pipeline
  - [ ] Human downloads VCTK to GCS bucket
  - [ ] Write preprocessing scripts (trim silence, normalize)
  - [ ] Extract features (mel-spectrograms, F0, etc.)
  - [ ] Create train/val/test splits
  - [ ] Build efficient dataloaders
- [ ] Evaluation harness
  - [ ] Set up speaker verification (ECAPA-TDNN or WavLM)
  - [ ] Set up ASR (Whisper-small for WER)
  - [ ] Implement metrics: cosine similarity, WER, MCD, F0 correlation
  - [ ] Create evaluation scripts
- [ ] Baseline model
  - [ ] Implement simplest viable architecture
  - [ ] Train on small subset (10 speakers)
  - [ ] Verify end-to-end pipeline

#### Deliverables
- [ ] Working data preprocessing pipeline
- [ ] Automated evaluation scripts
- [ ] Baseline model (doesn't need SOTA numbers yet)
- [ ] First experiment: exp_001_baseline

#### Success Criteria
- Can convert voices with > 0.7 similarity
- Pipeline is debugged and reproducible
- Clear path to scaling up

---

### Phase 2: Competitive Model (Week 4-6)
**Goal**: Match or beat Seed-VC

**Budget**: ~$2000
**Status**: Not Started

#### Tasks
- [ ] Full architecture implementation (based on Phase 0 decisions)
- [ ] Train on full VCTK dataset (~100 speakers)
- [ ] Potentially add LibriTTS subset for diversity
- [ ] Aggressive data augmentation
- [ ] Multiple training runs (3-5) with different seeds/hyperparameters
- [ ] Hyperparameter tuning
- [ ] Cross-dataset evaluation (train VCTK, test LibriTTS)

#### Deliverables
- [ ] Production-quality model architecture
- [ ] Multiple trained models (experiments exp_010-020 range)
- [ ] Comprehensive evaluation on held-out speakers
- [ ] Comparison to Seed-VC baselines

#### Success Criteria
- Speaker similarity ≥ 0.85
- WER ≤ 15%
- Naturalness MOS ≥ 3.5
- Competitive with current SOTA

---

### Phase 3: Novel Improvements (Week 7-9)
**Goal**: Beat SOTA with novel contributions

**Budget**: ~$2000
**Status**: Not Started

#### Potential Directions (TBD based on Phase 2 results)
- Better prosody modeling (explicit F0 conditioning)
- Multi-scale speaker disentanglement
- Cross-lingual capabilities (add AISHELL-3)
- Improved one-shot adaptation (meta-learning, few-shot techniques)
- Efficient inference (distillation, pruning)

#### Tasks
- [ ] Identify weaknesses from Phase 2
- [ ] Design hypothesis-driven improvements
- [ ] Systematic ablation studies
- [ ] Robustness testing:
  - [ ] Cross-gender conversion
  - [ ] Emotional speech
  - [ ] Noisy audio
  - [ ] Different languages (if applicable)

#### Deliverables
- [ ] Novel architectural contribution
- [ ] Ablation study results
- [ ] Robustness evaluation
- [ ] Clear evidence for paper

#### Success Criteria
- Speaker similarity > 0.87
- WER < 12%
- Naturalness MOS > 3.8
- Novel contribution identified and validated

---

### Phase 4: Productionization & Paper (Week 10-12)
**Goal**: Ship model and paper

**Budget**: ~$500
**Status**: Not Started

#### Tasks
- [ ] Model optimization
  - [ ] Final training run on best architecture
  - [ ] Inference optimization
  - [ ] Model checkpoints and model card
- [ ] Benchmark & Leaderboard
  - [ ] Create HuggingFace leaderboard (per earlier research)
  - [ ] Submit our model
  - [ ] Compare against all baselines
- [ ] Paper writing
  - [ ] Draft based on experiments (AI + human collab)
  - [ ] Figures and tables
  - [ ] Related work section
  - [ ] Target: Arxiv + potentially ICASSP/Interspeech
- [ ] Open-source release
  - [ ] Clean codebase
  - [ ] README, examples, Colab notebook
  - [ ] Apache 2.0 license
  - [ ] HuggingFace model hub upload

#### Deliverables
- [ ] Final model released
- [ ] Research paper published (Arxiv minimum)
- [ ] Open-source repository
- [ ] Demo and documentation

#### Success Criteria
- Model meets all success criteria
- Paper accepted or published
- Community can reproduce results
- Project visibility and impact

---

## Experiments Log

### Completed Experiments
*None yet*

### In Progress
*None yet*

### Planned
- **exp_001_baseline**: Initial baseline model (Phase 1)
- *(More to be added as we progress)*

---

## Comparison to SOTA

| Model | Similarity | WER | MOS | Speed | Notes |
|-------|------------|-----|-----|-------|-------|
| **Seed-VC** (SOTA) | 0.8676 | 11.99% | ~3.8 | Slow | Diffusion-transformer, current best |
| OpenVoice | ~0.83 | ~15% | ~3.7 | Fast | Cross-lingual, versatile |
| FreeVC | ~0.80 | ~13% | ~3.6 | Fast | VITS + WavLM bottleneck |
| RVC | 0.9+ | Low | High | Fast | **Multi-shot** (not comparable) |
| **Ours (exp_001)** | TBD | TBD | TBD | TBD | Baseline |
| **Ours (target)** | >0.87 | <12% | >3.8 | <0.2 RTF | Goal |

**Current Gap to SOTA**: Not yet measured

---

## Decisions Log

### Key Decisions Made

#### 2025-10-18: Project Structure
- **Decision**: Use markdown-based tracking + git (no W&B initially)
- **Rationale**: Simple, async-friendly, no external dependencies
- **Impact**: Easy to collaborate asynchronously

#### 2025-10-18: Research Approach
- **Decision**: Start with strategic research (Phase 0) before coding
- **Rationale**: $5000 budget is limited, avoid wasting compute
- **Impact**: Week 1 spent on literature review and architecture design

### Pending Decisions

#### Architecture: Content Encoder
- **Options**: WavLM, HuBERT, Whisper encoder
- **Status**: Researching (Phase 0)
- **Deadline**: Before Phase 1 implementation

#### Architecture: Decoder
- **Options**: Diffusion, flow-based, GAN-based
- **Status**: Researching (Phase 0)
- **Tradeoff**: Quality vs speed vs training stability

#### Data: Primary Dataset
- **Options**: Start with VCTK only, or VCTK + LibriTTS
- **Status**: Pending data strategy research
- **Constraint**: Storage (~20GB local, need GCS)

---

## Open Questions

### Technical
- [ ] What are Seed-VC's specific weaknesses we can exploit?
- [ ] Which SSL features generalize best to one-shot scenarios?
- [ ] How much data augmentation is optimal?
- [ ] What's the minimum dataset size for competitive results?

### Strategic
- [ ] Should we prioritize quality or inference speed?
- [ ] Cross-lingual capabilities: necessary or nice-to-have?
- [ ] Paper venue: Arxiv only, or submit to conference?

### Practical
- [ ] GCS bucket setup status? (blocking data pipeline)
- [ ] Modal credentials working? (blocking GPU experiments)
- [ ] Human bandwidth for listening tests?

---

## Blockers

### Current Blockers
1. **[HIGH]** GCS bucket not set up - Need for dataset storage
2. **[MEDIUM]** Modal credentials not verified - Need for GPU compute

### Upcoming Potential Blockers
- Listening test participants (Phase 2+)
- GPU quota limits on Modal
- Dataset access (AISHELL-3 if needed)

---

## Budget Tracking

### Total Budget
- **Allocated**: $5000 Modal compute credits
- **Spent**: $0
- **Remaining**: $5000

### Budget by Phase
| Phase | Planned | Spent | Remaining |
|-------|---------|-------|-----------|
| Phase 0 | $20 (API) | $0 | $20 |
| Phase 1 | $500 | $0 | $500 |
| Phase 2 | $2000 | $0 | $2000 |
| Phase 3 | $2000 | $0 | $2000 |
| Phase 4 | $500 | $0 | $500 |

### Recent Spending
*No spending yet*

---

## Paper Preparation

### Paper Outline (Preliminary)

#### Abstract
- Problem: One-shot voice conversion challenge
- Approach: [TBD based on architecture]
- Results: [TBD based on experiments]
- Contribution: [TBD based on novel improvements]

#### 1. Introduction
- Voice conversion applications
- One-shot vs multi-shot challenge
- Our contribution and results

#### 2. Related Work
- Survey of VC approaches (from earlier research)
- Seed-VC and current SOTA
- Gap we're addressing

#### 3. Method
- Architecture overview
- Content encoder [TBD]
- Style encoder [TBD]
- Decoder [TBD]
- Training procedure

#### 4. Experiments
- Datasets (VCTK, LibriTTS, etc.)
- Evaluation metrics
- Baselines
- Implementation details

#### 5. Results
- Main comparison (Table 1)
- Ablation studies (Table 2)
- Qualitative analysis
- Cross-lingual/cross-gender results

#### 6. Analysis
- What works and why
- Failure cases
- Limitations

#### 7. Conclusion
- Summary
- Future work
- Release information

### Experiments Mapped to Paper Sections

#### Methods Section
- exp_001-020: Architecture evolution

#### Results Section
- Main comparison: Best model vs SOTA
- Ablation studies: [TBD]

#### Analysis Section
- Qualitative samples: [TBD]
- Failure case analysis: [TBD]

---

## Next Steps

### Immediate (This Week)
1. Run Deep Research on Seed-VC architecture
2. Run Deep Research on data strategy
3. Analyze architectural options (diffusion vs flow vs GAN)
4. Draft architecture proposal
5. Present proposal to human for approval

### Short-term (Next 2 Weeks)
1. Human sets up GCS bucket
2. Human downloads VCTK dataset
3. Implement data preprocessing pipeline
4. Set up evaluation harness
5. Implement baseline model

### Medium-term (Next 4-6 Weeks)
1. Full architecture implementation
2. Training runs on full dataset
3. Match SOTA performance

---

## Notes

### Research Philosophy
- **Experiment-driven**: Every major decision backed by experiments
- **Ablation-focused**: Understand what each component contributes
- **Honest reporting**: Document failures and limitations
- **Reproducible**: Everything documented and version-controlled

### Collaboration Notes
- Check HANDOFF.md for async communication
- Update this plan after major milestones
- Tag experiments with paper section relevance
- Ask human for input on strategic decisions

---

**This is a living document. Update regularly as the project evolves.**
