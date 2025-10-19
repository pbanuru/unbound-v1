# Project Handoff - Voice Conversion Research

**Last Updated**: 2025-10-18 17:30 by AI (Claude)
**Project Week**: 0 of 12
**Current Phase**: Phase 0 - Strategic Research

---

## Current Status 🚦

- ✅ Infrastructure complete (GCP project, GCS bucket, folder structure, docs)
- ✅ Deep Research: Seed-VC architecture complete (`docs/seed_vc_analysis.md`)
- ✅ Deep Research: Data strategy complete (`data/README.md` updated)
- 🔄 VCTK dataset downloading (4.7GB/10.9GB, ~43% complete, bash ID: ad13d1)

**Latest Session**: 2025-10-18 (2 sessions today)
- Session 1: Infrastructure setup
- Session 2: Deep Research execution
- See detailed notes in `research_logs/2025-10/2025-10-18.md`

---

## What's Next (Priority Order)

### HIGH Priority 🔴

1. **[AI - NEXT SESSION]** Complete VCTK Dataset Setup
   - Check download status (BashOutput, bash ID: ad13d1)
   - Should be complete or close to complete
   - Unzip VCTK-Corpus-0.92.zip
   - Upload to gs://unbound-v1-data/data/raw/VCTK/
   - Verify integrity and document

2. **[AI]** Deep Research: Architecture Comparison
   - Query: Compare diffusion vs flow vs GAN decoders
   - Query: Compare WavLM vs HuBERT vs Whisper content encoders
   - Output: `docs/architecture_comparison.md`
   - Time: ~10-15 minutes per query

3. **[AI]** Draft Architecture Proposal
   - Based on Seed-VC findings and architecture comparison
   - Include: Design decisions, rationale, budget estimate
   - Output: Add to `README.md`
   - Requires human review/approval before implementation

### MEDIUM Priority 🟡

4. **[AI]** Create preprocessing scripts outline
   - Based on data strategy research
   - Implement augmentation strategies (pitch shift, time stretch, noise, reverb)

5. **[AI]** Set up Modal configuration template
   - Test Modal access
   - Create basic training script template

### LOW Priority 🟢

6. **[HUMAN]** Verify Modal credentials (not blocking Phase 0)

---

## Completed This Session ✅

### Deep Research
1. **Seed-VC Architecture Analysis** (87 web searches)
   - Output: `docs/seed_vc_analysis.md`
   - Key finding: Weaknesses in noise robustness, audio fidelity, inference speed
   - Opportunities: Timbre masking, flow-based decoders, better vocoder

2. **Data Strategy Analysis** (110 web searches)
   - Output: Updated `data/README.md`
   - Recommendation: Start with VCTK, add LibriTTS for generalization
   - Augmentation: Pitch shift, time stretch, noise injection, reverb (research-backed)

### Documentation
- Created `docs/seed_vc_analysis.md`
- Updated `data/README.md` with dataset comparison and augmentation
- Updated `CLAUDE.md` with aria2c download best practices
- Updated research log `research_logs/2025-10/2025-10-18.md`

---

## Blockers & Decisions Needed

### Blockers
- None currently blocking Phase 0 work
- Modal credentials needed before Phase 1 (Week 2-3)

### Decisions Needed from Human

1. **Research Duration**: Spend 1 week on Phase 0 research, or move faster?
   - Current plan: Complete architecture analysis + proposal this week
   - Alternative: Move to implementation sooner

2. **Paper Venue**: Target Arxiv only, or conference (ICASSP/Interspeech)?
   - Affects rigor and timeline requirements

3. **Quality vs Speed**: If tradeoff needed, prioritize which?
   - High quality + slow: Diffusion decoder
   - Good quality + fast: Flow decoder
   - Will inform architecture proposal

---

## Active Background Processes

**VCTK Download**:
- Bash ID: `ad13d1`
- Command: `curl -L -o VCTK-Corpus-0.92.zip "..."`
- Status: Running
- Progress: 4.7GB / 10.9GB (~43%)
- ETA: ~30-40 minutes (as of 17:30)
- Location: `/Users/yn/Documents/code/unbound-v1/data/raw/`
- **Next session**: Check with `BashOutput` tool or `ls -lh` to verify completion

---

## Budget Tracker

- **Starting**: $4971 Modal credits
- **Spent**: $0
- **Remaining**: $4971
- Note: Budget shared with low-usage system

---

## Key Info

**GCS Bucket**: `gs://unbound-v1-data/` (us-west1)
**GCP Project**: `unbound-v1`
**Success Criteria**: >0.87 similarity, <12% WER, >3.8 MOS, <0.2 RTF
**Target to Beat**: Seed-VC (0.8676 similarity, 11.99% WER)

---

## Research Findings Summary

### Seed-VC Weaknesses (Our Opportunities)
1. **Noise sensitivity** → Implement timbre masking or implicit alignment
2. **Slow inference** → Use flow-based decoder instead of diffusion
3. **Audio fidelity** → Optimize vocoder or decoder architecture
4. **Content-timbre disentanglement** → Better SSL representations

### Data Strategy
- **Primary dataset**: VCTK (benchmarking, controlled)
- **Secondary dataset**: LibriTTS (generalization to diverse voices)
- **Augmentation**: Pitch shift (±2-4 semitones), time stretch (±10-20%), noise (SNR 15-40dB), reverb

### Architecture Insights
- Seed-VC uses DiT + Wav2Vec2-XLSR/Whisper + CAMPplus speaker encoder
- Training: Flow-matching loss + L1 mel (λ=45) + KL (λ=1)
- Key technique: External timbre shifter during training

---

**For detailed session notes, see `research_logs/2025-10/2025-10-18.md`**
**For full research plan, see `README.md`**
