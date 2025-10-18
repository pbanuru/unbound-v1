# Project Handoff - Voice Conversion Research

**Last Updated**: 2025-10-18 16:05 by AI (Claude)
**Project Week**: 0 of 12
**Current Phase**: Phase 0 - Setup & Infrastructure

---

## Quick Status 🚦

- ✅ **Project structure created** (folders, docs, workflows)
- ✅ **Documentation framework** (CLAUDE.md, RESEARCH_PLAN.md, this file)
- ✅ **GCS bucket setup complete** (gs://unbound-v1-data/ in us-west1)
- 🔄 **VCTK dataset downloading** (curl running in background, ~14 min remaining as of 16:03)
- ⏸️ **Ready for Phase 0 research** (can start Deep Research queries next session)

---

## What Was Just Completed

### Session: 2025-10-18 Afternoon - Infrastructure Setup

**Completed**:
1. ✅ **Project Documentation**:
   - Analyzed existing research sessions (3 sessions on voice conversion)
   - Researched async collaboration best practices for AI-human research
   - Created CLAUDE.md - Complete AI researcher guide
   - Created RESEARCH_PLAN.md - 12-week research roadmap
   - Created HANDOFF.md - Async communication protocol
   - Created supporting docs (experiments/README.md, data/README.md, research_logs/README.md)
   - Created first research log (research_logs/2025-10/2025-10-18.md)

2. ✅ **Folder Structure**:
   - Created all project folders (docs/, experiments/, data/, src/, configs/, results/, scripts/, paper/)
   - Set up .gitignore for large files
   - Git commits for all setup work

3. ✅ **GCP/GCS Setup**:
   - Created GCP project: `unbound-v1`
   - Linked billing account (YN Billing Account)
   - Created GCS bucket: `gs://unbound-v1-data/`
   - Location: us-west1 (California region)
   - Storage class: STANDARD
   - Documented bucket details in data/README.md and CLAUDE.md

4. ✅ **VCTK Dataset Download** (IN PROGRESS):
   - Started download: VCTK-Corpus-0.92.zip (10.9GB)
   - Using curl (server doesn't support parallel downloads)
   - Download speed: ramped up to 13+ MB/s
   - Progress as of 16:03: ~7-8GB downloaded, ~14 min remaining
   - Background process running (bash ID: ad13d1)

**Key Decisions Made**:
- Budget corrected to $4971 (from $5000)
- Using markdown + git for tracking (not W&B initially)
- GCS bucket in us-west1 (California) instead of multi-region
- Phase 0 focus on strategic research before coding

**Files Created/Modified**:
- CLAUDE.md, RESEARCH_PLAN.md, HANDOFF.md
- data/README.md, experiments/README.md, research_logs/README.md
- research_logs/2025-10/2025-10-18.md
- .gitignore (updated)
- Git commits: 3 total

---

## What Needs to Be Done Next

### Priority: HIGH 🔴

1. **[AI - NEXT SESSION]** Complete VCTK dataset setup
   - **Status**: Download running in background (curl, bash ID: ad13d1)
   - **Next steps**:
     - Check if download completed
     - Unzip VCTK-Corpus-0.92.zip
     - Upload to gs://unbound-v1-data/data/raw/VCTK/
     - Verify dataset integrity
     - Document in data/README.md

2. **[AI]** Run Deep Research: Seed-VC Architecture
   - **Query**: "Seed-VC claims 0.8676 similarity and 11.99% WER. What is their exact architecture, training recipe, and datasets? What are known weaknesses or failure cases? What architectural improvements have been proposed since their publication?"
   - **Purpose**: Understand SOTA before designing our approach
   - **Output**: Save to `docs/seed_vc_analysis.md`
   - **Timeline**: This week (Phase 0)
   - **Time**: ~10-15 minutes

3. **[AI]** Run Deep Research: Data Strategy
   - **Query**: "For training a one-shot voice conversion model, compare VCTK, LibriTTS, and AISHELL-3 in terms of: speaker diversity, recording quality, speaking style variety, and suitability for generalization. What data augmentation strategies are most effective?"
   - **Purpose**: Choose optimal dataset(s) for training
   - **Output**: Update `data/README.md` with findings
   - **Timeline**: This week (Phase 0)

### Priority: MEDIUM 🟡

4. **[AI]** Architecture Comparison Analysis
   - **Task**: Compare diffusion vs flow vs GAN decoders for voice conversion
   - **Include**: WavLM vs HuBERT vs Whisper for content encoding
   - **Output**: Write `docs/architecture.md` with trade-offs
   - **Timeline**: This week (Phase 0)

5. **[AI]** Draft Architecture Proposal
   - **Task**: 1-page proposal with design decisions and rationale
   - **Include**: Content encoder, style encoder, decoder, losses, training strategy
   - **Include**: Budget estimate for experiments
   - **Output**: Add to RESEARCH_PLAN.md or separate doc
   - **Requires**: Human review and approval before implementation

### Priority: LOW 🟢

6. **[HUMAN - PENDING]** Modal Credentials Verification
   - **What**: Confirm Claude can run `modal run` commands
   - **Why**: Need GPU compute for experiments ($4971 budget)
   - **Blocking**: All GPU experiments (Phase 1+)
   - **Status**: Not yet verified

---

## Current Blockers / Decisions Needed

### Blockers

1. ~~**[RESOLVED]** GCS bucket setup~~ ✅
   - **Resolution**: Created `gs://unbound-v1-data/` in us-west1
   - **Project**: unbound-v1 (with YN Billing Account)
   - **Details**: See data/README.md

2. **[BLOCKING PHASE 1+]** Modal credentials
   - **Impact**: Cannot run GPU experiments
   - **Owner**: Human
   - **Urgency**: Medium (need before Phase 1 Week 2-3)
   - **Note**: Can do Phase 0 research without this

### Decisions Needed

1. **[STRATEGIC]** Research vs Implementation Balance
   - **Question**: How much time in Phase 0? Deep research can take hours.
   - **Context**: 1 week planned, but can adjust
   - **Your input**: Stick with 1 week of research, or move faster?

2. **[STRATEGIC]** Paper Target Venue
   - **Question**: Arxiv only, or submit to conference (ICASSP, Interspeech)?
   - **Context**: Affects rigor and timeline requirements
   - **Your input**: What's the publication goal?

3. **[PRACTICAL]** Quality vs Speed Priority
   - **Question**: If forced to choose, prioritize quality or inference speed?
   - **Context**: Diffusion (higher quality, slower) vs Flow (good quality, faster)
   - **Your input**: Which matters more for this project?

---

## Questions / Observations

### Questions for Human

1. Do you have a Modal account already? Are $4971 credits already loaded?
2. Any time constraints on the 12-week timeline?
3. Preference for inference speed vs quality if tradeoff needed?

### Observations

- GCS bucket setup went smoothly
- VCTK download accelerated nicely (13+ MB/s after slow start)
- Project has ~78GB local disk space (plenty for work)
- The existing research sessions (DeepResearcher) are extremely high quality
- We have solid understanding of the problem space from prior research
- Phase 0 (research) will be low-cost but time-intensive
- Budget ($4971) should be sufficient for 12-week plan if managed carefully

---

## Files to Review

### Important Documents
- **CLAUDE.md** - Read this first if you're a new Claude instance
- **RESEARCH_PLAN.md** - Full 12-week roadmap with phases and goals
- **HANDOFF.md** - This file, for async status updates

### Previous Research
- `DeepResearcher/research_sessions/one_shot_voice_conversion/` - Comprehensive VC research
- `DeepResearcher/research_sessions/voice_conversion_benchmark/` - Benchmark research
- `ai_research_guide.md` - Research methodology guide

### New Documentation
- `data/README.md` - Data management guide (includes GCS bucket info)
- `experiments/README.md` - Experiment tracking guide
- `research_logs/README.md` - Daily research log guide
- `research_logs/2025-10/2025-10-18.md` - Today's detailed session log

---

## Budget Status

**Starting Balance**: $4971 Modal credits
**Spent This Session**: $0
**Remaining (Estimated)**: $4971
**Note**: Budget shared with low-usage system; may request actual balance when needed

**Planned Allocation**:
- Phase 0 (Research): $20 API calls
- Phase 1 (Foundation): $500
- Phase 2 (Competitive): $2000
- Phase 3 (Novel): $1950
- Phase 4 (Production): $500
- **Total**: ~$4970

---

## Git Commits This Session

```
[2025-10-18] feat: Initial research collaboration infrastructure
- Created folder structure and documentation framework
- 10 files changed, 2456 insertions(+)

[2025-10-18] fix: Correct starting budget to $4971 Modal credits
- Updated budget across all docs
- 4 files changed, 20 insertions(+), 11 deletions(-)

[2025-10-18] docs: Clarify human response handling in CLAUDE.md
- Added instructions for transferring chat responses to HANDOFF.md
- 1 file changed, 10 insertions(+)

[2025-10-18] feat: Set up GCS bucket for data storage
- Created GCP project unbound-v1, linked billing, created bucket
- 3 files changed, 23 insertions(+), 10 deletions(-)
```

---

## Background Processes

**Active Downloads**:
- **Bash ID**: ad13d1
- **Command**: `curl -L -o VCTK-Corpus-0.92.zip "https://datashare.ed.ac.uk/bitstream/handle/10283/3443/VCTK-Corpus-0.92.zip?sequence=2&isAllowed=y"`
- **Status**: Running
- **Progress** (as of 16:03): ~7-8GB of 10.9GB downloaded
- **Speed**: 13+ MB/s
- **ETA**: ~14 minutes remaining
- **Location**: `/Users/yn/Documents/code/unbound-v1/data/raw/`

**Next session**: Check download status with `BashOutput` tool

---

## Next Session Preview

**For AI (Claude)**:
1. Check VCTK download status (BashOutput bash ID: ad13d1)
2. If complete: unzip and upload to GCS
3. If not complete: wait or resume
4. Run Seed-VC deep research query
5. Run data strategy deep research query
6. Update HANDOFF.md with progress

**For Human**:
1. Review this handoff document
2. Verify Modal credentials if possible
3. Answer strategic decision questions (timeline, paper venue, quality vs speed)
4. Provide any other input/priorities

---

## Status Summary

| Category | Status | Details |
|----------|--------|---------|
| **Phase** | Phase 0 | Setup & Infrastructure |
| **Week** | 0 of 12 | Foundation week |
| **Budget** | $4971 / $4971 | No spending yet |
| **Blockers** | 1 medium | Modal credentials (not urgent) |
| **Next Milestone** | Complete dataset download | Then start research queries |

---

**Infrastructure setup complete! Dataset downloading. Ready for Phase 0 research next session.** 🚀
