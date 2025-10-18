# Project Handoff - Voice Conversion Research

**Last Updated**: 2025-10-18 16:10 by AI (Claude)
**Project Week**: 0 of 12
**Current Phase**: Phase 0 - Setup & Infrastructure

---

## Current Status 🚦

- ✅ Infrastructure complete (GCP project, GCS bucket, folder structure, docs)
- 🔄 VCTK dataset downloading (curl background process, ~14 min remaining as of 16:03)
- ⏸️ Ready for Phase 0 research (Deep Research queries on Seed-VC, data strategy, architecture)

**Latest Session**: 2025-10-18 Afternoon
- See detailed notes in `research_logs/2025-10/2025-10-18.md`
- Git commits: 4 commits (infrastructure setup, GCS bucket, docs)

---

## What's Next (Priority Order)

### HIGH Priority 🔴

1. **[AI - NEXT SESSION]** Complete VCTK Dataset Setup
   - Check download status (BashOutput, bash ID: ad13d1)
   - Unzip VCTK-Corpus-0.92.zip
   - Upload to gs://unbound-v1-data/data/raw/VCTK/
   - Verify integrity and document

2. **[AI]** Deep Research: Seed-VC Architecture
   - Query: Architecture, training recipe, weaknesses, improvements
   - Output: `docs/seed_vc_analysis.md`
   - Time: ~10-15 minutes

3. **[AI]** Deep Research: Data Strategy
   - Query: Compare VCTK, LibriTTS, AISHELL-3 for one-shot VC
   - Output: Update `data/README.md`
   - Time: ~10-15 minutes

### MEDIUM Priority 🟡

4. **[AI]** Architecture Comparison Analysis
   - Compare: Diffusion vs Flow vs GAN decoders
   - Compare: WavLM vs HuBERT vs Whisper encoders
   - Output: `docs/architecture.md`

5. **[AI]** Draft Architecture Proposal
   - Design decisions + rationale + budget estimate
   - Requires human review/approval before implementation

### LOW Priority 🟢

6. **[HUMAN]** Verify Modal Credentials
   - Not blocking Phase 0 research
   - Needed before Phase 1 GPU experiments

---

## Blockers & Decisions Needed

### Blockers
- None currently blocking Phase 0 work
- Modal credentials needed before Phase 1 (Week 2-3)

### Decisions Needed from Human

1. **Research Duration**: Spend 1 week on Phase 0 research, or move faster?
2. **Paper Venue**: Target Arxiv only, or conference (ICASSP/Interspeech)?
3. **Quality vs Speed**: If tradeoff needed, prioritize which?

---

## Active Background Processes

**VCTK Download**:
- Bash ID: `ad13d1`
- Command: `curl -L -o VCTK-Corpus-0.92.zip "..."`
- Status: Running (as of 16:03)
- Progress: ~7-8GB of 10.9GB
- Speed: 13+ MB/s
- ETA: ~14 minutes
- Location: `/Users/yn/Documents/code/unbound-v1/data/raw/`
- **Next session**: Check with `BashOutput` tool

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
**Target**: Beat Seed-VC (0.8676 similarity, 11.99% WER)

---

**For detailed session notes, see `research_logs/2025-10/2025-10-18.md`**
**For full research plan, see `RESEARCH_PLAN.md`**
