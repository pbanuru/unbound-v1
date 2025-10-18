# Research Logs

Daily logs of research activities, observations, and progress.

## Purpose

Research logs capture:
- **Daily work**: What was done each session
- **Observations**: Qualitative findings and insights
- **Hypotheses**: Ideas to test in future experiments
- **Questions**: Things to investigate or discuss
- **Debugging**: Issues encountered and solutions
- **Learning**: Technical insights gained

## Organization

Logs are organized by month:

```
research_logs/
├── 2025-10/
│   ├── 2025-10-18.md
│   ├── 2025-10-19.md
│   └── 2025-10-20.md
├── 2025-11/
└── README.md (this file)
```

## Log Format

Each daily log follows this template:

```markdown
# Research Log - YYYY-MM-DD

**Session Time**: HH:MM - HH:MM (X hours)
**Phase**: Phase N - Description
**Focus**: Main task or experiment

---

## Work Completed

### Major Tasks
1. Task 1 description
2. Task 2 description

### Experiments Run
- exp_XXX: Brief description, outcome

### Code Written
- File/module: What was implemented

---

## Key Findings

### Quantitative
- Metric improvements or results
- Comparisons to baseline

### Qualitative
- Observations from listening to samples
- Patterns noticed in training
- Unexpected behaviors

---

## Observations

- Observation 1
- Observation 2

---

## Hypotheses Formed

- Hypothesis 1: Why something works/doesn't work
- Hypothesis 2: What to try next

---

## Questions / Issues

- Question 1 for human or future investigation
- Issue 1 encountered and how resolved (or not)

---

## Next Session Plans

1. Priority task 1
2. Priority task 2

---

## Links

- Related experiments: exp_XXX, exp_YYY
- Updated docs: RESEARCH_PLAN.md, HANDOFF.md
- Deep Research: link to relevant research session
```

## Usage

### At Start of Session

1. Read latest log to see what was done
2. Check "Next Session Plans" from last log
3. Review HANDOFF.md for priorities

### During Session

- Take quick notes as you work
- Log significant findings immediately
- Don't worry about polish - capture info

### At End of Session

1. Write/complete today's log
2. Update "Next Session Plans"
3. Update HANDOFF.md with status
4. Commit log to git

## Example Log

See `2025-10/2025-10-18.md` for the initial project setup log.

## Log vs Other Docs

### Research Logs (here)
- **Frequency**: Daily
- **Audience**: Future self, human reviewer
- **Content**: Detailed work, observations, raw thoughts
- **Format**: Chronological, conversational

### HANDOFF.md
- **Frequency**: Per session (same as logs)
- **Audience**: Human collaborator
- **Content**: Status, next steps, blockers, decisions
- **Format**: Structured, action-oriented

### RESEARCH_PLAN.md
- **Frequency**: Weekly or after major milestones
- **Audience**: Both (strategic overview)
- **Content**: Phases, experiments, overall progress
- **Format**: Living document, high-level

### Experiment Notes
- **Frequency**: Per experiment
- **Audience**: Future researchers
- **Content**: Hypothesis, setup, results, conclusions
- **Format**: Structured, formal

## Best Practices

### Be Honest
- Document failures, not just successes
- Note uncertainty and confusion
- Admit when you don't understand something

### Be Detailed
- Future you won't remember details
- Include specific numbers, file paths, commands
- Link to experiments and commits

### Be Reflective
- Why did something work or not work?
- What surprised you?
- What would you do differently?

### Be Forward-Looking
- What to try next?
- What questions arose?
- What needs human input?

## Common Scenarios

### Experiment Failed
```markdown
## Experiment Failure: exp_025

Attempted to add triplet loss but training diverged after 10k steps.

**What went wrong**:
- Loss spiked suddenly
- Generated audio became noisy
- Likely cause: margin too high (0.5)

**Lessons learned**:
- Need to tune margin carefully
- Should start with smaller margin (0.2)
- May need gradient clipping

**Next steps**:
- Try exp_026 with margin=0.2
- Add gradient monitoring
```

### Breakthrough
```markdown
## Breakthrough: Speaker Similarity +0.08

exp_030 achieved 0.85 similarity (was 0.77)!

**What changed**:
- Added triplet loss (margin=0.2)
- Increased style encoder capacity
- Used contrastive learning on speaker embeddings

**Why it worked**:
- Better speaker disentanglement
- Style encoder has more capacity to capture nuances
- Contrastive loss prevents embedding collapse

**Questions**:
- Can we push further to 0.87?
- Does this generalize to cross-gender?
- What's the compute cost tradeoff?
```

### Stuck / Confused
```markdown
## Confusion: WER Increasing

Not sure why WER went from 14% to 17% in exp_031.

**Changes made**:
- Increased style embedding dimension (256 → 512)
- Added dropout (0.1)

**Expected**: No impact on content preservation
**Actual**: WER got worse

**Hypotheses**:
1. More style capacity leads to style leakage into content?
2. Dropout hurting content encoder training?
3. Could be random variation (need more seeds)

**Need to investigate**:
- Run ablation: just dimension increase
- Run ablation: just dropout
- Check content encoder gradients
- Listen to samples - is it phoneme errors or style leakage?

**Flagging for human review**: See HANDOFF.md
```

### Literature Review
```markdown
## Deep Research: Diffusion Models for VC

Ran Deep Research on diffusion-based voice conversion.

**Key findings**:
- Seed-VC uses diffusion transformer (DiT)
- DiffVC uses conditional DDPM
- Trade-off: Quality vs speed

**Relevant papers**:
- Seed-VC (2024): Current SOTA
- DiffVC (2023): Earlier approach
- CoMoSpeech (2023): Consistency models for speed

**Takeaways**:
- Diffusion = high quality but slow (50-100 steps)
- Can use distillation to speed up (10 steps)
- Alternative: Flow matching (faster, similar quality)

**Decision needed**:
- Should we use diffusion or flow matching?
- See HANDOFF.md for discussion
```

## Searching Logs

### Find by Topic
```bash
grep -r "triplet loss" research_logs/
```

### Find by Experiment
```bash
grep -r "exp_025" research_logs/
```

### Find by Date Range
```bash
ls research_logs/2025-10/
```

## Maintenance

- Archive old logs (>3 months) to keep repo lean
- Periodically review logs to identify patterns
- Extract important insights to docs/decisions.md
- Reference logs in paper when describing development process

---

**Remember**: Logs are for capturing everything. You can organize and synthesize later. Write freely!
