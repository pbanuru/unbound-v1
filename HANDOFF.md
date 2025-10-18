# Project Handoff - Voice Conversion Research

**Last Updated**: 2025-10-18 15:00 by AI (Claude)
**Project Week**: 0 of 12
**Current Phase**: Phase 0 - Strategic Research

---

## Quick Status 🚦

- ✅ **Project structure created** (folders, docs, workflows)
- ✅ **Documentation framework** (CLAUDE.md, RESEARCH_PLAN.md, this file)
- 🔄 **Phase 0 in progress** (strategic research before coding)
- ⏸️ **Blocked on** GCS bucket setup (need for datasets)

---

## What Was Just Completed

### Session: 2025-10-18 Afternoon - Project Setup

**Completed**:
1. ✅ Analyzed existing research sessions (3 sessions on voice conversion)
2. ✅ Researched async collaboration best practices for AI-human research
3. ✅ Designed folder structure for research project
4. ✅ Created all folders (`docs/`, `experiments/`, `data/`, `src/`, etc.)
5. ✅ Wrote **CLAUDE.md** - Instructions for AI researcher across sessions
6. ✅ Wrote **RESEARCH_PLAN.md** - 12-week research roadmap with phases
7. ✅ Wrote **HANDOFF.md** (this file) - Async communication protocol

**Key Decisions Made**:
- Using markdown + git for tracking (simple, async-friendly)
- 5-phase approach: Research → Foundation → Competitive → Novel → Production
- $5000 budget allocated across phases
- Target: Beat Seed-VC (0.8676 similarity, 11.99% WER)

**Files Created**:
- `/CLAUDE.md` - Complete AI researcher guide
- `/RESEARCH_PLAN.md` - Living research plan
- `/HANDOFF.md` - This file
- Folder structure: `docs/`, `research_logs/`, `experiments/`, `data/`, `src/`, etc.

---

## What Needs to Be Done Next

### Priority: HIGH 🔴

1. **[HUMAN]** Set up Google Cloud Storage bucket
   - **Why**: Need persistent storage for datasets (VCTK ~11GB, LibriTTS ~50GB)
   - **What**: Create GCS bucket, provide Claude with access credentials
   - **Blocking**: Data pipeline development (Phase 1)

2. **[HUMAN]** Verify Modal credentials work
   - **Why**: Need GPU compute for experiments ($5000 budget)
   - **What**: Confirm Claude can run `modal run` commands
   - **Blocking**: All GPU experiments (Phase 1+)

3. **[AI]** Run Deep Research: Seed-VC Architecture
   - **Query**: "Seed-VC claims 0.8676 similarity and 11.99% WER. What is their exact architecture, training recipe, and datasets? What are known weaknesses or failure cases? What architectural improvements have been proposed since their publication?"
   - **Purpose**: Understand SOTA before designing our approach
   - **Output**: Save to `docs/seed_vc_analysis.md`
   - **Timeline**: This week (Phase 0)

### Priority: MEDIUM 🟡

4. **[AI]** Run Deep Research: Data Strategy
   - **Query**: "For training a one-shot voice conversion model, compare VCTK, LibriTTS, and AISHELL-3 in terms of: speaker diversity, recording quality, speaking style variety, and suitability for generalization. What data augmentation strategies are most effective?"
   - **Purpose**: Choose optimal dataset(s) for training
   - **Output**: Update `data/README.md` with findings
   - **Timeline**: This week (Phase 0)

5. **[AI]** Architecture Comparison Analysis
   - **Task**: Compare diffusion vs flow vs GAN decoders for voice conversion
   - **Include**: WavLM vs HuBERT vs Whisper for content encoding
   - **Output**: Write `docs/architecture.md` with trade-offs
   - **Timeline**: This week (Phase 0)

6. **[AI]** Draft Architecture Proposal
   - **Task**: 1-page proposal with design decisions and rationale
   - **Include**: Content encoder, style encoder, decoder, losses, training strategy
   - **Include**: Budget estimate for experiments
   - **Output**: Add to RESEARCH_PLAN.md or separate doc
   - **Requires**: Human review and approval before implementation

### Priority: LOW 🟢

7. **[HUMAN]** Download VCTK dataset to GCS
   - **When**: After GCS bucket is set up
   - **Size**: ~11GB
   - **URL**: https://datashare.ed.ac.uk/handle/10283/3443
   - **Why**: Faster than Claude downloading, persistent storage

8. **[HUMAN]** Clone reference codebases (optional)
   - **Repos**: Seed-VC, FreeVC, others as identified
   - **Why**: Study implementations, potentially adapt components
   - **Note**: Claude can do this, but might be faster if you do

---

## Current Blockers / Decisions Needed

### Blockers

1. **[BLOCKING PHASE 1]** GCS bucket setup
   - **Impact**: Cannot start data pipeline
   - **Owner**: Human
   - **Urgency**: High (need before Phase 1 Week 2-3)

2. **[BLOCKING PHASE 1+]** Modal credentials
   - **Impact**: Cannot run GPU experiments
   - **Owner**: Human
   - **Urgency**: High (need before Phase 1 Week 2-3)

### Decisions Needed

1. **[STRATEGIC]** Research vs Implementation Balance
   - **Question**: How much time in Phase 0? Deep research can take hours.
   - **Context**: 1 week planned, but can adjust
   - **Your input**: Prefer quick start with less research, or thorough research first?

2. **[STRATEGIC]** Paper Target Venue
   - **Question**: Arxiv only, or submit to conference (ICASSP, Interspeech)?
   - **Context**: Affects timeline and rigor requirements
   - **Your input**: What's the publication goal?

3. **[PRACTICAL]** Storage Strategy
   - **Question**: Use GCS bucket, Modal Volumes, or both?
   - **Context**: Need persistent storage for datasets and results
   - **Your input**: What's easiest for you to set up?

---

## Questions / Observations

### Questions for Human

1. Do you have a Modal account already? Are credits already loaded?
2. Preferred cloud provider for storage (GCP, AWS, other)?
3. Any time constraints on the 12-week timeline?
4. Preference for inference speed vs quality if tradeoff needed?

### Observations

- The existing research sessions (DeepResearcher) are extremely high quality
- We have solid understanding of the problem space from prior research
- Phase 0 (research) will be low-cost but time-intensive
- Budget ($5000) should be sufficient for 12-week plan if managed carefully

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

### To Be Created
- `docs/seed_vc_analysis.md` - SOTA analysis (pending Deep Research)
- `docs/architecture.md` - Architecture comparison (pending analysis)
- `data/README.md` - Data strategy (pending Deep Research)

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
[2025-10-18] Initial project structure and documentation
- Created folder structure (docs/, experiments/, data/, src/, etc.)
- Added CLAUDE.md (AI researcher instructions)
- Added RESEARCH_PLAN.md (12-week research roadmap)
- Added HANDOFF.md (async communication protocol)
```

---

## Next Session Preview

**For AI (Claude)**:
1. Run Seed-VC deep research (if human approves)
2. Run data strategy deep research
3. Analyze architecture options
4. Draft architecture proposal
5. Update HANDOFF.md with findings

**For Human**:
1. Review this handoff document
2. Set up GCS bucket (blocking)
3. Verify Modal credentials (blocking)
4. Answer decision questions above (strategic)
5. Provide any other input/priorities

---

## Communication

### How to Use This File

**AI Updates** (end of each session):
- What was completed
- What's next
- Blockers and decisions needed
- Questions and observations

**Human Updates** (when reviewing):
- Decisions made
- New priorities
- Blockers resolved
- Answers to questions

### Response Template for Human

You can respond right here in this file:

```markdown
## Human Response - [DATE]

### Decisions Made
- [Decision 1]
- [Decision 2]

### Blockers Resolved
- [Blocker 1]: Resolution

### New Priorities
- [Any changes to priorities]

### Answers to Questions
1. Modal account: [answer]
2. Cloud storage: [answer]
3. Timeline: [answer]
4. Quality vs speed: [answer]

### Other Notes
[Anything else]
```

---

## Status Summary

| Category | Status | Details |
|----------|--------|---------|
| **Phase** | Phase 0 | Strategic Research |
| **Week** | 0 of 12 | Project setup complete |
| **Budget** | $5000 / $5000 | No spending yet |
| **Blockers** | 2 high | GCS bucket, Modal credentials |
| **Next Milestone** | Architecture proposal | End of Week 1 |

---

**Ready for async collaboration! Check this file for status updates and next steps.**
