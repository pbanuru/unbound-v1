# AI Research for Dummies in the Age of AI

*A practical guide for builders who want to do research without a PhD*

---

## Table of Contents
1. [The New Paradigm](#the-new-paradigm)
2. [What Research Actually Means Now](#what-research-actually-means-now)
3. [Skills You Actually Need](#skills-you-actually-need)
4. [Skills You Don't Need (Let AI Handle These)](#skills-you-dont-need)
5. [The Research Process](#the-research-process)
6. [Reading Papers Efficiently](#reading-papers-efficiently)
7. [Designing Experiments](#designing-experiments)
8. [Evaluation & Metrics](#evaluation-and-metrics)
9. [Writing It Up](#writing-it-up)
10. [Open-Sourcing Strategically](#open-sourcing-strategically)
11. [Building Credibility](#building-credibility)
12. [Common Pitfalls](#common-pitfalls)
13. [The Business Model (Optional)](#the-business-model)
14. [Timeline to Hirability](#timeline-to-hirability)

---

## The New Paradigm

### Traditional Path (Pre-AI):
1. Get CS degree (4 years)
2. Get PhD in ML (5-7 years)
3. Publish papers (2-3 years)
4. Get hired at research lab

**Total: ~12 years**

### Modern Path (With AI):
1. Learn Python basics (3-6 months)
2. Build something real with AI assistance (6-12 months)
3. Document it like research (1 month)
4. Engage with community (ongoing)
5. Get hired at research lab

**Total: ~12-18 months**

### What Changed?

**Before:** You needed to understand everything before you could build anything.

**Now:** You can build while learning, with AI filling knowledge gaps just-in-time.

**The moat shifted from:**
- Knowledge accumulation → Judgment and taste
- Implementation skills → System design
- Isolated work → Community engagement
- Credentials → Demonstrated capability

---

## What Research Actually Means Now

Research is **NOT**:
- ❌ Only for people with PhDs
- ❌ Purely theoretical math
- ❌ Working in an ivory tower
- ❌ Publishing in top-tier conferences (though nice)

Research **IS**:
- ✅ Trying something new and documenting what happens
- ✅ Comparing your approach to existing solutions rigorously
- ✅ Understanding *why* something works or doesn't
- ✅ Sharing findings so others can build on them
- ✅ Being honest about limitations

### The Core Research Loop:

```
1. Identify a problem/question
   ↓
2. Survey what others have tried
   ↓
3. Design your approach
   ↓
4. Implement and experiment
   ↓
5. Measure results honestly
   ↓
6. Understand why it worked/failed
   ↓
7. Document and share
   ↓
8. Repeat
```

**You've probably done this building products.** Research just adds:
- More rigorous comparison to alternatives
- Systematic ablations (testing each component)
- Clear documentation of the process
- Honest reporting of failures

---

## Skills You Actually Need

### 1. **Conceptual Understanding (High Priority)**

**What this means:**
- Understanding *why* techniques work, not just *how* to implement them
- Knowing when to use approach A vs approach B
- Building mental models of how systems fit together

**Example:**
- Don't need to: Derive transformer attention math by hand
- Do need to: Understand "attention lets the model focus on relevant parts of input"
- Application: "My voice model needs to attend to pitch differently than phonemes, so I'll use separate attention heads"

**How to build this:**
- Read paper abstracts and conclusions (skip the math)
- Watch YouTube explanations (Yannic Kilcher, Two Minute Papers)
- Implement things and see what breaks
- Ask Claude "explain like I'm 5" questions

### 2. **System Design Thinking (Critical)**

**What this means:**
- Breaking complex problems into components
- Understanding data flow through a system
- Identifying bottlenecks and failure modes
- Making architectural tradeoffs

**Example:**
Voice conversion system:
```
Audio Input → Feature Extraction → Content Encoder →
                                          ↓
Target Reference → Style Encoder → Decoder → Vocoder → Output
```

You need to understand:
- What each component does
- Where errors might propagate
- Which pieces are slow/expensive
- What happens if one component fails

**This is like your SaaS architecture:**
- Database → API → Frontend
- Except now it's: Data → Model → Inference

### 3. **Experimental Design (Learnable)**

**What this means:**
- Changing one variable at a time
- Having proper baselines for comparison
- Knowing what metrics actually matter
- Documenting what you tried

**Bad experiment:**
> "I changed the model architecture, dataset, and learning rate. It works better now!"
>
> *You have no idea which change mattered.*

**Good experiment:**
> "Baseline: Model A gets 0.75 similarity score.
> Changed only the style encoder to use triplet loss.
> New score: 0.82 similarity.
> Conclusion: Triplet loss improved speaker similarity by 9%."

**How to do this:**
1. Establish baseline (measure current approach)
2. Change ONE thing
3. Measure again
4. Document the delta
5. Repeat

This is like A/B testing in product, but for model components.

### 4. **Debugging Methodology (You Probably Have This)**

**What this means:**
- Isolating where failures occur
- Forming hypotheses about causes
- Testing hypotheses systematically
- Knowing when to cut losses and try something else

**Example:**
```
Problem: "Converted voice sounds robotic"

Hypotheses:
1. Vocoder issue (waveform generation)
2. Content encoder losing prosody
3. Style encoder not capturing emotion
4. Training data too clean/synthetic

Tests:
1. Feed ground-truth mel-spec to vocoder
   → Still robotic? It's the vocoder.
   → Sounds fine? Continue testing.

2. Compare content embeddings of emotional vs neutral speech
   → Same embeddings? Encoder is stripping prosody.
   → Different? Issue is elsewhere.

... etc
```

**This is exactly like debugging a web app**, just with different failure modes.

### 5. **Taste & Judgment (Develops with Experience)**

**What this means:**
- Recognizing good vs bad outputs
- Knowing when "metrics look good but something is off"
- Prioritizing what to work on next
- Identifying promising vs dead-end directions

**Example:**
- Metrics say: "Speaker similarity 0.88 (great!)"
- Listening test: "This sounds uncanny and weird"
- Judgment: "The metric is measuring the wrong thing. I need to add a prosody evaluation."

**How to build this:**
- Listen to/use LOTS of examples in your domain
- Study what "good" looks like (SOTA models)
- Pay attention to edge cases
- Get feedback from domain experts

**This is like product sense for SaaS**, but for ML outputs.

### 6. **Communication (Underrated, Critical)**

**What this means:**
- Explaining technical concepts clearly
- Writing docs that others can follow
- Engaging with community without being a jerk
- Asking for help effectively

**Where this matters:**
- Writing your preprint/blog posts
- GitHub README and docs
- Twitter/Reddit discussions
- Asking Claude good questions
- Networking with researchers

**Good communication =**
- More citations (people understand your work)
- More users (people can implement it)
- More job offers (you seem competent)
- Faster help when stuck (clear questions get answers)

---

## Skills You Don't Need (Let AI Handle These)

### 1. **Deep Math/Theory**
- ❌ Deriving backprop equations
- ❌ Proving convergence theorems
- ❌ Memorizing optimization formulas
- ✅ Ask Claude when you need to understand something specific

### 2. **Low-Level Implementation Details**
- ❌ PyTorch API memorization
- ❌ CUDA kernel optimization (unless that's your research focus)
- ❌ Boilerplate code patterns
- ✅ Claude writes the code, you review and understand what it does

### 3. **Exhaustive Literature Review**
- ❌ Reading every paper in the field
- ❌ Memorizing all prior work
- ❌ Perfect academic writing
- ✅ Read strategically (recent SOTA papers + surveys), Claude helps summarize

### 4. **Perfect Code**
- ❌ Production-grade engineering (initially)
- ❌ Optimal efficiency (unless that's your contribution)
- ❌ Zero technical debt
- ✅ Working code that's good enough to run experiments, refactor later

**The Pattern:**
If it's **mechanical/lookup-able**, let AI handle it.
If it requires **judgment/creativity/taste**, you need to develop it.

---

## The Research Process

### Phase 1: Problem Selection (Week 1-2)

**Goal:** Pick something worth working on.

**Criteria for a good research problem:**
1. **Interesting to you** (you'll spend months on this)
2. **Has existing work** (not completely novel - you need baselines)
3. **Measurable improvement possible** (clear metrics exist)
4. **Practical value** (even if academic, should matter to someone)
5. **Scoped appropriately** (achievable in 6-12 months solo)

**How to find problems:**
- Look at "limitations" sections in recent papers
- Find areas where SOTA is still unsatisfying
- Notice gaps: "Method A is fast but low quality, Method B is high quality but slow - can we get both?"
- Follow your curiosity: "Why doesn't X work for Y?"

**Red flags:**
- ❌ "No one has ever tried this" (maybe for good reason)
- ❌ "I'll solve AGI" (too broad)
- ❌ "I have no way to evaluate this" (unmeasurable)
- ❌ "This seems boring but I should do it" (you'll quit)

**Your example:** Single-shot voice conversion
- ✅ Interesting (voice cloning is cool)
- ✅ Existing work (Seed-VC, FreeVC, etc.)
- ✅ Measurable (MOS, speaker similarity, WER)
- ✅ Practical (apps want this)
- ✅ Scoped (known architectures exist, you're improving them)

### Phase 2: Literature Survey (Week 2-4)

**Goal:** Understand the landscape without drowning in papers.

**Efficient paper reading strategy:**

**Step 1: Find the key papers (1-2 days)**
- Search "your topic + SOTA" or "your topic + survey"
- Check Papers with Code leaderboards
- Look at recent ArXiv papers (last 6-12 months)
- Find 5-10 most cited/recent papers

**Step 2: Skim strategically (1 week)**
For each paper, read in this order:
1. **Abstract** (2 min) - What did they do?
2. **Conclusion** (5 min) - Did it work? What are limitations?
3. **Figures/Tables** (5 min) - What are the results?
4. **Introduction** (10 min) - Why does this matter?
5. **Related work** (optional) - What else is out there?
6. **Method** (only if you'll implement this) - How does it work?

**Skip:**
- Proofs and derivations (unless that's your thing)
- Dense math sections (ask Claude if you need clarification)
- Most of the related work (it's usually padding)

**Step 3: Create a comparison table (2-3 days)**

| Model | Approach | Metrics | Strengths | Weaknesses | Open Source? |
|-------|----------|---------|-----------|------------|--------------|
| Seed-VC | Diffusion | Sim: 0.867 | SOTA quality | Slow inference | ✅ Yes |
| FreeVC | VITS+WavLM | MOS: 3.8 | Fast, clean | English only? | ✅ Yes |
| ... | ... | ... | ... | ... | ... |

**This table becomes the "Related Work" section of your paper.**

**Step 4: Identify your angle (1-2 days)**
- What do existing approaches struggle with?
- What tradeoff can you improve? (speed vs quality, data efficiency, etc.)
- What combination hasn't been tried?

**Example:**
> "Seed-VC has SOTA quality but is slow (diffusion). FreeVC is fast but lower similarity. Can I combine WavLM features (FreeVC) with triplet loss and better style encoding to match Seed-VC quality at FreeVC speed?"

**Time-saving with Claude:**
- "Summarize this paper's approach in 3 bullet points"
- "What are the key differences between paper A and paper B?"
- "What evaluation metrics does this paper use?"

**Total time: ~2-3 weeks** (not 6 months)

### Phase 3: Initial Implementation (Week 5-12)

**Goal:** Get something working end-to-end, even if quality is bad.

**Milestones:**

**Week 5-6: Data pipeline**
- Download datasets (VCTK, LibriTTS, etc.)
- Write preprocessing scripts (resampling, VAD, feature extraction)
- Verify data loading works (visualize spectrograms, listen to audio)
- Split into train/val/test (BY SPEAKER - critical for zero-shot)

**Week 7-8: Baseline model**
- Implement simplest viable architecture
- Don't optimize yet - just get gradients flowing
- Overfit on a single batch (sanity check)
- Train on small subset (10 speakers)

**Week 9-10: End-to-end inference**
- Generate converted audio samples
- Listen to outputs (they'll sound bad - that's fine)
- Compute basic metrics (even if bad)
- Identify obvious failure modes

**Week 11-12: First real training run**
- Scale to full dataset
- Train for enough iterations to see learning
- Evaluate on held-out speakers
- Document what works/doesn't

**Tips:**
- Start small (overfit on one example first)
- Use pre-trained components when possible (speaker encoder, vocoder)
- Don't parallelize experiments yet - get one thing working
- Log everything (losses, metrics, sample outputs)
- Checkpoint frequently (you WILL want to roll back)

**Working with Claude:**
- "Implement a mel-spectrogram extractor in PyTorch"
- "Why is my loss NaN after 100 steps?"
- "Write a data loader that batches variable-length audio"

**Success criteria:**
✅ Audio goes in, audio comes out (even if quality is terrible)
✅ Model learns *something* (loss decreases)
✅ You understand each component's purpose
✅ You have a baseline metric to improve upon

### Phase 4: Iterative Improvement (Week 13-20)

**Goal:** Make it actually good through systematic experiments.

**The experiment loop:**

```
1. Identify bottleneck
   "Speaker similarity is only 0.65 (vs SOTA 0.87)"

2. Form hypothesis
   "Maybe the style encoder needs triplet loss to better separate speakers"

3. Design experiment
   "Add triplet loss with margin=0.2, weight=0.1, train for 50k steps"

4. Run experiment
   Train new model variant, keep everything else identical

5. Evaluate
   "Speaker similarity improved to 0.73 (+0.08)"

6. Document
   Add to experiment log: "Triplet loss helped, but still below SOTA"

7. Next hypothesis
   "Maybe I need more style encoder capacity..."
```

**Keep an experiment log:**

```markdown
## Experiment 1: Baseline
- Config: 6-layer content encoder, d-vector style encoder, flow decoder
- Results: MOS 3.2, Similarity 0.65, WER 18%
- Notes: Content is decent, but speaker identity is weak

## Experiment 2: Add triplet loss
- Changed: Added triplet loss (margin=0.2, weight=0.1) to style encoder
- Results: MOS 3.1, Similarity 0.73, WER 18%
- Notes: Similarity improved (+0.08), MOS slightly down (noise?), WER unchanged
- Conclusion: Keep triplet loss

## Experiment 3: Increase style encoder size
- Changed: Style encoder 256 → 512 dims
- Results: MOS 3.3, Similarity 0.78, WER 17%
- Notes: All metrics improved! But training is slower.
- Conclusion: Worth it, adopt as new baseline
...
```

**Common experiments to try:**
- Architecture changes (layer count, hidden dims, attention heads)
- Loss function variants (weights, margins, additional terms)
- Training hyperparameters (learning rate, batch size, schedule)
- Data augmentation (noise, pitch shift, speed perturbation)
- Pre-trained component swapping (different vocoders, speaker encoders)

**How to prioritize:**
1. Fix the biggest problem first (lowest metric)
2. Try cheapest experiments first (hyperparameters before architecture)
3. Follow the literature (if everyone uses triplet loss, there's a reason)
4. Trust your ears (metrics lie, audio doesn't)

**Ablation studies:**
Once you have a good model, remove components one at a time to prove they matter:

```
Full model:           MOS 3.8, Sim 0.85
Without triplet loss: MOS 3.7, Sim 0.78  → triplet adds +0.07 similarity
Without augmentation: MOS 3.6, Sim 0.83  → augmentation adds +0.2 MOS
Without WavLM:        MOS 3.2, Sim 0.81  → WavLM adds +0.6 MOS
```

This proves each component is necessary (critical for papers).

**Time management:**
- Each experiment: 1-3 days (train + evaluate)
- Run 2-3 experiments per week
- 8 weeks = 16-24 experiments
- Should be enough to get competitive results

### Phase 5: Comparison to SOTA (Week 21-24)

**Goal:** Honestly measure how you stack up.

**Do this properly:**

1. **Reproduce baselines yourself** (don't just trust paper numbers)
   - Download Seed-VC, FreeVC, etc. checkpoints
   - Run on YOUR test set (same speakers)
   - Compute metrics with YOUR evaluation code
   - Papers often cherry-pick - you need apples-to-apples

2. **Use multiple metrics**
   - Subjective: MOS (naturalness), SMOS (similarity)
   - Objective: Speaker embedding cosine, WER, F0 RMSE
   - Don't rely on just one (it might be misleading)

3. **Test multiple scenarios**
   - Same-language, same-gender (easiest)
   - Cross-language (harder)
   - Cross-gender (hardest)
   - Emotional speech (edge case)
   - Singing (if relevant)

4. **Be honest about failures**
   - Where do you win? Where do you lose?
   - Don't hide bad results
   - Understanding failures is often more valuable than successes

**Example comparison table (for your paper):**

| Model | MOS ↑ | Similarity ↑ | WER ↓ | Inference Speed |
|-------|-------|--------------|-------|-----------------|
| Seed-VC | 3.9 | **0.867** | 12.0% | 2.3 RTF (slow) |
| FreeVC | 3.8 | 0.782 | 15.2% | **0.08 RTF** (fast) |
| **Yours** | **4.0** | 0.845 | **11.5%** | 0.12 RTF |

(Bold = best in column)

**Your positioning:**
> "Our approach achieves quality comparable to Seed-VC (SOTA) while maintaining near-FreeVC inference speed, and improves content preservation (WER) over both baselines."

**If you don't win:**
That's okay! Be honest:
> "While our model doesn't achieve SOTA speaker similarity, it offers a better speed/quality tradeoff and is fully open-source with reproducible training."

**Credibility comes from honesty, not hype.**

---

## Reading Papers Efficiently

### The 3-Pass Method

**Pass 1: The 5-Minute Skim (Do this for every paper)**
- Read: Title, abstract, conclusion
- Look at: Figures, tables
- Decision: Is this relevant? If yes → Pass 2. If no → skip.

**Pass 2: The 30-Minute Understanding (Do this for relevant papers)**
- Read: Introduction, method overview (not details), results
- Skip: Proofs, dense math, most related work
- Goal: Understand WHAT they did and WHY it worked
- Take notes in your own words

**Pass 3: The Deep Dive (Only for papers you'll implement/build on)**
- Read: Everything, including supplements
- Reproduce: Key figures/results if possible
- Understand: Implementation details, edge cases
- Goal: Could you reimplement this?

### What to Extract from Papers

**For your comparison table:**
- Approach (1 sentence)
- Key innovation
- Metrics (quantitative results)
- Limitations (from their discussion)
- Code availability

**For your implementation:**
- Architecture diagram (often Figure 1 or 2)
- Loss functions (usually in Method section)
- Hyperparameters (often in supplement/appendix)
- Training details (dataset, batch size, iterations)

**For your intuition:**
- Why this approach makes sense
- When it would fail
- What tradeoffs they made

### Using Claude for Paper Reading

**Good prompts:**
- "Summarize the key contribution of this paper in 3 bullet points: [paste abstract]"
- "What's the difference between approach A (paper 1) and approach B (paper 2)?"
- "Explain this architecture diagram in simple terms: [paste figure]"
- "What datasets did they use for evaluation?"

**Don't ask:**
- "Is this paper good?" (Claude doesn't have judgment on novelty)
- "Should I implement this?" (that's your decision)

### Red Flags in Papers

🚩 "We achieve SOTA but don't compare to the most recent work"
🚩 "We only test on one dataset"
🚩 "No code or reproducibility information"
🚩 "Cherry-picked examples with no systematic evaluation"
🚩 "Huge improvement over baselines (seems too good to be true)"

**These don't mean the paper is worthless**, but be skeptical and verify claims yourself.

---

## Designing Experiments

### The Scientific Method for ML

1. **Observation:** "My converted voices sound robotic"
2. **Question:** "Why do they sound robotic?"
3. **Hypothesis:** "The vocoder is introducing artifacts"
4. **Prediction:** "If I use a better vocoder, quality will improve"
5. **Experiment:** Train with HiFi-GAN instead of WaveNet
6. **Analysis:** Measure MOS before/after
7. **Conclusion:** "HiFi-GAN improved MOS by 0.4 → vocoder was the bottleneck"

### Types of Experiments

**1. Ablation Studies**
*Remove components to prove they're necessary*

```
Full model:            Metric = 0.85
Remove component A:    Metric = 0.78  → A contributes +0.07
Remove component B:    Metric = 0.82  → B contributes +0.03
Remove both A and B:   Metric = 0.73  → They contribute +0.12 together
```

**2. Hyperparameter Tuning**
*Find optimal settings*

```
Learning rate: 1e-3 → loss diverges
Learning rate: 1e-4 → converges, final loss 0.5
Learning rate: 1e-5 → converges slower, final loss 0.5
Conclusion: Use 1e-4
```

**3. Architecture Search**
*Compare structural variants*

```
6 transformer layers:  MOS 3.5, speed 0.1 RTF
12 transformer layers: MOS 3.7, speed 0.3 RTF
24 transformer layers: MOS 3.75, speed 0.8 RTF
Conclusion: 12 layers is best quality/speed tradeoff
```

**4. Data Experiments**
*Understand data requirements*

```
Train on 10 speakers:   Similarity 0.65
Train on 50 speakers:   Similarity 0.78
Train on 100 speakers:  Similarity 0.82
Train on 200 speakers:  Similarity 0.83
Conclusion: Diminishing returns after 100 speakers
```

### Keeping Good Experiment Records

**Minimum viable experiment log:**

```markdown
## Experiment ID: exp_025
**Date:** 2025-10-15
**Goal:** Test if triplet loss improves speaker similarity
**Baseline:** exp_020 (similarity 0.73)

**Changes:**
- Added triplet loss to style encoder
- Margin: 0.2
- Weight: 0.1
- All other hyperparameters unchanged

**Training:**
- Ran for 50k steps (8 hours on A100)
- No crashes or anomalies
- Loss curves look normal

**Results:**
- Similarity: 0.78 (+0.05 vs baseline)
- MOS: 3.2 (unchanged)
- WER: 17% (unchanged)

**Samples:** /experiments/exp_025/samples/
**Checkpoint:** /experiments/exp_025/ckpt_50k.pt

**Conclusions:**
- Triplet loss helps speaker similarity without hurting other metrics
- ADOPT for future experiments
- Next: try increasing margin to 0.3

**Notes:**
- Listened to samples - definitely sounds more like target
- Slight increase in training time (~10%)
```

**Use version control:**
- Git commit for each experiment
- Tag with experiment ID
- Branches for major changes

### Common Experimental Mistakes

❌ **Changing multiple things at once**
"I changed the architecture AND the loss AND the learning rate"
→ You have no idea what helped

✅ **Change one thing, measure, repeat**

❌ **Not saving checkpoints/configs**
"This worked great but I forgot the hyperparameters"
→ Unrecoverable

✅ **Save everything: code, config, checkpoints, logs**

❌ **Trusting metrics without listening/looking**
"WER is low so content is preserved!"
→ But it sounds like gibberish

✅ **Always sanity-check metrics with human evaluation**

❌ **Cherry-picking results**
"It worked on these 3 examples, ship it!"
→ Systematically test on full test set

✅ **Evaluate on diverse, representative examples**

❌ **Stopping after first success**
"It works, I'm done!"
→ No ablations, no understanding of why

✅ **Understand what matters through ablations**

---

## Evaluation and Metrics

### Why Evaluation Matters

**In product:** Users vote with their wallets/usage
**In research:** Metrics are your only "proof" something works

**Bad evaluation = no credibility** even if your model is actually good.

### Types of Metrics

**1. Subjective (Human Evaluation)**

**Mean Opinion Score (MOS):**
- Play samples to humans
- Ask: "Rate naturalness from 1 (bad) to 5 (excellent)"
- Average across listeners and samples
- **When to use:** Measuring perceptual quality
- **Pros:** Captures what actually matters (how it sounds)
- **Cons:** Expensive, slow, high variance

**Speaker Similarity MOS (SMOS):**
- Give listeners: target reference + converted sample
- Ask: "How similar are these voices? 1-5"
- **When to use:** Measuring voice cloning quality
- **Pros:** Direct measure of task success
- **Cons:** Same as MOS

**ABX Test:**
- Give listeners: Sample A, Sample B, Sample X
- Ask: "Is X more similar to A or B?"
- **When to use:** Comparing two models
- **Pros:** Easier for listeners than rating
- **Cons:** Only relative, not absolute quality

**How to run listening tests:**
1. Use platform: Prolific, MTurk, or volunteer researchers
2. Need: ~20 listeners per sample for stability
3. Cost: ~$200-500 for a proper study (100 samples, 20 listeners)
4. Tips:
   - Include attention checks ("select 4 for this sample")
   - Randomize order
   - Give examples of each rating level
   - Keep sessions short (<30 min)

**2. Objective (Automatic Metrics)**

**Speaker Similarity (Embedding Cosine):**
- Extract speaker embeddings (ECAPA-TDNN, d-vector)
- Compute: cosine_similarity(embedding_converted, embedding_target)
- Range: 0 (different) to 1 (identical)
- **Pros:** Fast, cheap, reproducible
- **Cons:** Doesn't capture all aspects of similarity

**Word Error Rate (WER):**
- Run ASR (Whisper, Wav2Vec2) on converted audio
- Compare transcript to source transcript
- WER = (insertions + deletions + substitutions) / total_words
- Lower is better
- **Pros:** Measures content preservation
- **Cons:** Depends on ASR quality

**Mel-Cepstral Distortion (MCD):**
- Spectral distance between converted and reference audio
- Lower is better
- **Pros:** Widely used, reproducible
- **Cons:** Doesn't correlate perfectly with perception

**F0 Frame Error / RMSE:**
- Compare fundamental frequency (pitch) contours
- **Pros:** Measures prosody preservation
- **Cons:** Needs pitch estimation (can be noisy)

**Inference Speed (Real-Time Factor):**
- RTF = time_to_process / audio_duration
- RTF < 1.0 means faster than real-time
- **Pros:** Practical importance
- **Cons:** Hardware-dependent

### Choosing the Right Metrics

**For voice conversion, you need:**

| Aspect | Subjective | Objective |
|--------|-----------|-----------|
| **Naturalness** | MOS | (none perfect - use WER as proxy) |
| **Speaker Similarity** | SMOS | Embedding cosine |
| **Content Preservation** | (implicit in MOS) | WER, CER |
| **Prosody** | (implicit in MOS) | F0 RMSE, correlation |
| **Efficiency** | n/a | RTF, model size |

**Minimum viable evaluation:**
- ✅ Embedding cosine similarity (automatic)
- ✅ WER (automatic)
- ✅ RTF (automatic)
- ✅ Small MOS study (~50 samples, 10-20 listeners)

**Gold standard evaluation:**
- ✅ All of the above
- ✅ Multiple datasets (VCTK + LibriTTS)
- ✅ Multiple scenarios (same/cross gender, language)
- ✅ Large MOS study (100+ samples, 20+ listeners)
- ✅ Ablation studies showing what contributes

### Setting Up Evaluation Code Early

**Don't wait until the end to evaluate!** Set this up in Week 2-3.

```python
# eval.py - run this after every experiment

def evaluate_model(model, test_set):
    results = {
        'speaker_similarity': [],
        'wer': [],
        'rtf': []
    }

    for source, target_ref in test_set:
        # Generate conversion
        start = time.time()
        converted = model.convert(source, target_ref)
        duration = time.time() - start

        # Speaker similarity
        emb_converted = speaker_encoder(converted)
        emb_target = speaker_encoder(target_ref)
        similarity = cosine_similarity(emb_converted, emb_target)
        results['speaker_similarity'].append(similarity)

        # WER
        asr_output = asr_model(converted)
        wer = compute_wer(asr_output, source_transcript)
        results['wer'].append(wer)

        # RTF
        rtf = duration / audio_length(source)
        results['rtf'].append(rtf)

    # Aggregate
    return {
        'mean_similarity': np.mean(results['speaker_similarity']),
        'mean_wer': np.mean(results['wer']),
        'mean_rtf': np.mean(results['rtf'])
    }
```

**Run this after every experiment** to track progress.

### Benchmark Datasets

Use standard datasets so others can compare to your work:

**For voice conversion:**
- **VCTK:** Most common (108 speakers, English)
- **LibriTTS:** Large-scale (multiple speakers)
- **Voice Conversion Challenge (VCC) sets:** Official benchmark

**Split carefully:**
- Train/val/test by SPEAKER (not utterances)
- Test speakers must be completely unseen
- Consistent test set across all experiments

---

## Writing It Up

### Why Writing Matters

**"If it's not documented, it didn't happen."**

Your model could be amazing, but if you can't explain it, you won't:
- Get cited
- Get hired
- Get users
- Get credit

**Good writing is the difference between:**
- "Some person made a voice thing"
- "Researcher X achieved SOTA with novel approach Y"

### What to Write

**1. Technical Report / Preprint (Primary)**

**Structure (standard ML paper format):**

```markdown
# Title
One-Shot Voice Conversion with Triplet-Enhanced Style Encoding

## Abstract (150-250 words)
- What's the problem?
- What did you do?
- What were the results?
- Why does it matter?

## Introduction
- Motivation: Why is one-shot VC important?
- Problem: What's hard about it?
- Current approaches: What exists?
- Limitations: What's missing?
- Your contribution: What did you do differently?
- Results preview: How much better is it?

## Related Work
- Subsections for categories (VAE-based, Transformer-based, etc.)
- For each approach: brief description, strengths, weaknesses
- Your comparison table
- How your work differs

## Method
- Overall architecture (diagram!)
- Component 1: Content Encoder
  - Input/output
  - Architecture details
  - Design choices
- Component 2: Style Encoder
  - ...
- Component 3: Decoder
  - ...
- Loss functions
  - Each loss term explained
  - Weighting
- Training procedure

## Experiments
- Datasets (what you used, how you split)
- Baselines (what you compared against)
- Metrics (how you measured)
- Implementation details (hyperparameters, hardware)

## Results
- Main results table (vs baselines)
- Ablation studies
- Qualitative examples
- Failure cases

## Discussion
- What worked and why
- What didn't work and why
- Limitations
- Future work

## Conclusion
- Summary of contributions
- Impact/takeaways

## References
```

**Length:** 8-12 pages typical (with figures)

**Tone:**
- Clear, direct, technical
- Not overly formal or flowery
- "We propose..." not "One might consider the possibility that..."

**2. Blog Post (Secondary, for wider audience)**

**Structure:**

```markdown
# Catchy Title
"Building a Voice Cloning Model from Scratch (and What I Learned)"

## TL;DR
- 3-5 bullet points of key takeaways

## The Problem
- Explain in simple terms why this matters
- Use analogies, examples
- "Imagine you want to..."

## What Others Have Tried
- Brief overview of existing approaches
- What works, what doesn't
- No heavy math

## My Approach
- High-level architecture explanation
- Key innovations in plain English
- Diagrams!

## Results
- Numbers in context ("previous best was X, mine is Y")
- Audio demos (embedded)
- Honest limitations

## How You Can Use It
- Link to code
- Quick start guide
- Invitation to contribute

## What I Learned
- Insights from the process
- Surprising findings
- Advice for others

## Next Steps
- What you're working on
- Open questions
```

**Length:** 1500-3000 words
**Tone:** Conversational, accessible, honest
**Audience:** Developers, ML practitioners, hobbyists

**3. README (Critical for adoption)**

```markdown
# Project Name

One-sentence description.

[Badges: License, Stars, etc.]

## Audio Demos
[Embedded examples or links]

## Features
- ✅ One-shot voice conversion
- ✅ Multi-lingual support
- ✅ Fast inference (0.1 RTF)
- ✅ Pre-trained checkpoints

## Installation
```bash
pip install your-package
```

## Quick Start
```python
# Minimal example
```

## Results
| Model | Similarity | MOS | RTF |
|-------|------------|-----|-----|
| Ours  | ...        | ... | ... |

## Citation
```bibtex
@article{...}
```

## License
MIT

## Acknowledgments
```

**Length:** Short (1-2 screens)
**Tone:** Practical, easy to follow
**Goal:** Get someone using it in 5 minutes

### Writing Tips

**For technical writing:**
- ✅ Start with an outline
- ✅ One idea per paragraph
- ✅ Use active voice ("We propose" not "It is proposed")
- ✅ Define jargon on first use
- ✅ Use figures liberally (architecture diagrams, result plots)
- ✅ Be precise with numbers (0.847, not "about 0.85")
- ✅ Be honest about limitations

**Common mistakes:**
- ❌ Burying the key contribution
- ❌ Over-claiming results
- ❌ No comparison to prior work
- ❌ Vague method descriptions
- ❌ Cherry-picked results
- ❌ Walls of text (use subsections, bullet points)

**Using Claude for writing:**
- "Revise this paragraph for clarity: [paste]"
- "Suggest a better structure for this section"
- "Is this claim too strong? [paste]"
- "Help me describe this architecture in simpler terms"

**Don't ask Claude to write the whole thing** - it'll be generic. Use it for polishing.

### Where to Publish

**ArXiv (Recommended for you):**
- Free, open preprint server
- Anyone can submit (no peer review)
- Gets you a citable paper
- Commonly checked by researchers
- How: Upload PDF to arxiv.org (need endorsement for first submission, easy to get)

**Conferences (Optional):**
- Peer-reviewed, prestigious
- Examples: ICML, NeurIPS, ICLR (ML general), Interspeech, ICASSP (speech)
- Pros: Credibility, networking
- Cons: Slow (6-9 month review), high bar, often rejected
- **You can submit after having ArXiv preprint**

**Your blog (Recommended):**
- Immediate, full control
- Wider audience than ArXiv
- Good for SEO

**Medium / Towards Data Science:**
- Built-in audience
- Less control

**For your goal (getting hired):**
- ✅ ArXiv preprint (shows you can do research)
- ✅ Blog post (shows you can communicate)
- ⚠️ Conference (nice but not necessary - takes too long)

---

## Open-Sourcing Strategically

### Why Open-Source?

**For your goal (get hired at labs):**
- ✅ Proves you can build real systems
- ✅ Shows code quality
- ✅ Demonstrates collaboration skills (issues, PRs)
- ✅ Builds community credibility
- ✅ Gets your work used/cited

**Additional benefits:**
- Others find bugs you missed
- Contributors improve your work
- Network effects (more users → more visibility → more users)

### What to Open-Source

**Minimum:**
- ✅ Model code (architecture definitions)
- ✅ Training code (enough to reproduce)
- ✅ Pre-trained checkpoint(s)
- ✅ Inference code (how to use the model)
- ✅ README with instructions

**Better:**
- ✅ All of the above
- ✅ Data preprocessing scripts
- ✅ Evaluation code
- ✅ Requirements file (dependencies)
- ✅ Example notebooks
- ✅ Documentation site

**Best:**
- ✅ All of the above
- ✅ Configs for experiments
- ✅ Training logs (TensorBoard, WandB)
- ✅ Unit tests
- ✅ Docker container
- ✅ Demo web app

**Don't let perfect be the enemy of good** - start with minimum, improve over time.

### Code Quality Standards

**You don't need production-grade code, but:**

✅ **It should run**
- Someone else can clone and use it
- Dependencies are specified
- Paths are not hard-coded

✅ **It should be readable**
- Reasonable variable names
- Some comments on non-obvious parts
- Modular structure (not one 5000-line file)

✅ **It should be reproducible**
- Seeds are set
- Hyperparameters are documented
- Results can be regenerated

**You can skip:**
- ❌ Perfect type hints everywhere
- ❌ 100% test coverage
- ❌ Microservice architecture
- ❌ Production optimization

**Think: "Could a PhD student use this for their research?" not "Could this handle 1M users?"**

### Repository Structure

```
your-voice-conversion/
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py (optional)
├── data/
│   ├── download_vctk.sh
│   └── preprocess.py
├── models/
│   ├── content_encoder.py
│   ├── style_encoder.py
│   ├── decoder.py
│   └── vocoder.py
├── training/
│   ├── train.py
│   ├── losses.py
│   └── config.yaml
├── inference/
│   ├── convert.py
│   └── demo.py
├── evaluation/
│   ├── eval_metrics.py
│   └── run_eval.sh
├── checkpoints/
│   └── pretrained_model.pt (or link to download)
├── notebooks/
│   └── quickstart.ipynb
└── docs/
    └── ... (optional)
```

### Choosing a License

**For research code, use permissive licenses:**

**MIT or Apache 2.0 (Recommended):**
- People can do anything with your code
- Commercial use allowed
- Easy to understand
- Encourages adoption

**GPL (Avoid for your use case):**
- Requires derivatives to be open-source
- Can limit adoption (companies avoid)
- More complex

**For your goals: Use MIT.**
- Labs prefer it (no legal headaches)
- Maximizes usage/citations
- Simple

### Release Strategy

**Phase 1: Soft launch**
- Push code to GitHub
- Write README
- Share with friends / small communities (Discord, Reddit)
- Get feedback, fix obvious issues

**Phase 2: Public release**
- Announce on Twitter
- Post on Reddit (r/MachineLearning, r/LanguageTechnology)
- Share on HN (if ready for traffic)
- Write blog post

**Phase 3: Maintenance**
- Respond to issues (quickly at first)
- Accept good PRs
- Update based on feedback
- Keep a changelog

**Don't disappear after release** - engagement shows you're serious.

### Getting Users / Stars

**Quality gets you the first users, engagement gets you growth.**

**What drives stars:**
- ✅ Good README with clear value prop
- ✅ Working demos (audio examples!)
- ✅ Easy quick start
- ✅ Solves a real problem
- ✅ Better than alternatives (or different tradeoff)
- ✅ Active maintenance

**How to promote (without being spammy):**
- Tweet with demo video
- Write blog post explaining approach
- Comment on related GitHub issues ("you might find this useful...")
- Answer Stack Overflow questions, link when relevant
- Present at meetups / Discord communities

**Realistic expectations:**
- Week 1: 10-50 stars (friends, early interest)
- Month 1: 50-200 stars (if it's good)
- Month 6: 200-1000 stars (if it gains traction)
- 500+ stars = top 5% of ML repos (very respectable)

**Don't obsess over star count** - 100 stars from real users is better than 10k from HN hype.

---

## Building Credibility

### The Credibility Stack

**For getting hired at labs, you need to signal:**
1. ✅ Technical competence (can you build things?)
2. ✅ Research ability (can you find and solve novel problems?)
3. ✅ Communication (can you explain your work?)
4. ✅ Community fit (are you someone we'd want to work with?)

**How to build each:**

### 1. Technical Competence

**Signals:**
- ✅ Open-source code that works
- ✅ System design that makes sense
- ✅ Thoughtful engineering choices (documented)

**How to demonstrate:**
- Clean, modular code
- Architecture diagrams
- Thoughtful README explaining design decisions
- Good performance (speed, efficiency)

**Anti-signals:**
- ❌ Code that doesn't run
- ❌ Obvious bugs
- ❌ Copy-paste without understanding
- ❌ No documentation

### 2. Research Ability

**Signals:**
- ✅ Preprint / technical report
- ✅ Novel contribution (even if small)
- ✅ Rigorous evaluation
- ✅ Honest comparison to baselines
- ✅ Understanding of limitations

**How to demonstrate:**
- ArXiv paper
- Ablation studies in repo
- Comparison tables
- Discussion of what didn't work

**Anti-signals:**
- ❌ No comparison to prior work
- ❌ Overclaiming results
- ❌ Cherry-picked examples
- ❌ Not understanding why something works

### 3. Communication

**Signals:**
- ✅ Clear writing (paper, blog, README)
- ✅ Good visualizations
- ✅ Public engagement (Twitter, Reddit)
- ✅ Helpful to others (issues, comments)

**How to demonstrate:**
- Blog posts explaining your work
- Twitter threads with visuals
- Respond helpfully to GitHub issues
- Give talks (even informal, e.g. Discord communities)

**Anti-signals:**
- ❌ Impenetrable technical jargon
- ❌ No response to questions
- ❌ Defensive about criticism
- ❌ "Read the code" instead of explaining

### 4. Community Fit

**Signals:**
- ✅ Collaborative (accept PRs, credit others)
- ✅ Humble (acknowledge limitations)
- ✅ Curious (ask questions, engage with others' work)
- ✅ Open (share findings, help others)

**How to demonstrate:**
- Thank contributors in README
- Cite related work generously
- Ask thoughtful questions on Twitter/forums
- Share interesting papers you found
- Help beginners (shows you can mentor)

**Anti-signals:**
- ❌ Claiming sole credit for collaborative work
- ❌ Dismissive of others' approaches
- ❌ Secretive about methods
- ❌ Only promoting your own work

### Building Your Public Presence

**Twitter (Small but engaged following)**

**What to post:**
- Progress updates ("Day 20: finally got triplet loss working...")
- Results (charts, audio demos)
- Interesting papers you read (with your take)
- Lessons learned ("Spent 3 days debugging this, turned out to be...")
- Help others (answer questions)

**How often:** 2-3x per week (don't spam)

**Engage:**
- Comment on researchers' work
- Share others' interesting findings
- Join conversations (don't just broadcast)

**Goal:** 100-500 followers in your niche (quality over quantity)

**Blog (Deeper thoughts)**

**Post frequency:** 1-2x per month

**Topics:**
- Detailed technical deep-dives
- "How I built..." stories
- Comparisons ("FreeVC vs Seed-VC: What I learned")
- Lessons / retrospectives

**Goal:** 1-2k views per post (SEO builds over time)

**GitHub (Your portfolio)**

**Activity:**
- Commit regularly (shows consistency)
- Respond to issues within 24-48 hrs (shows reliability)
- Accept good PRs (shows collaboration)
- Star/follow related projects (shows engagement)

**Goal:** Active green squares, 100+ stars on main project

**Reddit / HN (Strategic launches)**

**Don't spam**, but do share:
- Major releases
- Interesting findings
- Helpful tutorials

**How to post:**
- Be humble ("I built this, would love feedback")
- Engage in comments
- Accept criticism gracefully

**Discord / Slack (Community building)**

**Join communities:**
- HuggingFace Discord
- EleutherAI
- Speech/audio specific channels

**Contribute:**
- Answer questions
- Share your work when relevant (not spammy)
- Collaborate on projects

**Goal:** Be known in 2-3 communities (people recognize your name)

### The Snowball Effect

**Month 1-2:** Mostly invisible (that's okay)
**Month 3-4:** A few people notice your work
**Month 5-6:** Small community forms around your project
**Month 7-9:** Cited in a paper, or used in another project
**Month 10-12:** Recognized in the niche, recruiter emails start

**Consistency > virality.**
One HN post gets you 1000 stars but no credibility.
12 months of quality work gets you 300 stars and 5 job offers.

---

## Common Pitfalls

### 1. **Analysis Paralysis**

**Symptom:** "I need to read 50 more papers before I start coding"

**Why it's wrong:**
- You learn more from building than reading
- Papers omit critical details (you'll need to experiment anyway)
- The field moves fast (your lit review is outdated in 3 months)

**Fix:**
- Read 5-10 key papers → start building
- Learn additional details just-in-time as needed

---

### 2. **Perfectionism**

**Symptom:** "I can't release until the code is perfect and results are SOTA"

**Why it's wrong:**
- Perfect is the enemy of done
- Community feedback improves your work faster than solo polishing
- "Good enough" open-source work gets you hired; perfect secret work doesn't

**Fix:**
- Ship when it works, even if it's not perfect
- Iterate based on feedback
- "Release early, release often"

---

### 3. **Scope Creep**

**Symptom:** "I'll also add real-time streaming, emotion control, and multi-speaker..."

**Why it's wrong:**
- Dilutes focus
- Nothing gets finished
- Better to do one thing well

**Fix:**
- Define MVP (minimum viable project) scope
- Ship that first
- Add features later based on feedback

---

### 4. **Ignoring Evaluation**

**Symptom:** "The samples sound good to me, that's enough"

**Why it's wrong:**
- Your ears aren't calibrated (you get used to artifacts)
- No credibility without numbers
- Can't compare to baselines

**Fix:**
- Set up evaluation pipeline early (week 2-3)
- Run metrics after every experiment
- Do listening tests with others

---

### 5. **Not Documenting Experiments**

**Symptom:** "I'll remember what I tried"

**Why it's wrong:**
- You won't remember
- Can't write paper without experiment history
- Can't debug when something breaks

**Fix:**
- Keep experiment log from day 1
- Use version control (git)
- Save configs, checkpoints, results for every run

---

### 6. **Cherry-Picking Results**

**Symptom:** "I'll only show the best examples"

**Why it's wrong:**
- Kills credibility when people try your model
- You're lying to yourself about performance
- Researchers can tell

**Fix:**
- Report metrics on full test set
- Show failure cases
- Be honest about limitations

---

### 7. **Reinventing the Wheel**

**Symptom:** "I'll implement my own vocoder/speaker encoder/everything"

**Why it's wrong:**
- Wastes time
- Your version will likely be worse (initially)
- Distracts from your actual contribution

**Fix:**
- Use pre-trained components when possible
- Focus on your novel contribution
- You can always swap components later

---

### 8. **Ignoring the Community**

**Symptom:** "I'll build in secret and release when perfect"

**Why it's wrong:**
- No feedback until too late
- No network effects
- Harder to get hired (no one knows you)

**Fix:**
- Build in public
- Share progress updates
- Engage with others' work

---

### 9. **Comparing to Stale Baselines**

**Symptom:** "My model beats this 2019 paper!"

**Why it's wrong:**
- Field moves fast
- Beating old work doesn't prove your approach is good
- Reviewers / hirers will notice

**Fix:**
- Compare to most recent SOTA (last 1-2 years)
- Reproduce baselines yourself if possible
- Be honest if you don't beat SOTA (explain tradeoffs)

---

### 10. **Optimizing for Wrong Metrics**

**Symptom:** "My WER is amazing but it sounds terrible"

**Why it's wrong:**
- Metrics are proxies, not the goal
- Users care about perceptual quality
- Goodhart's law: "When a measure becomes a target, it ceases to be a good measure"

**Fix:**
- Use multiple metrics
- Always listen / look at outputs
- Get human evaluations
- Prioritize metrics that correlate with user experience

---

### 11. **Underestimating Data Work**

**Symptom:** "Data preprocessing is boring, I'll rush it"

**Why it's wrong:**
- Garbage in, garbage out
- Data bugs are hardest to find
- Often 50% of the work

**Fix:**
- Take data seriously from day 1
- Visualize inputs (spectrograms, waveforms)
- Verify splits (test speakers not in train)
- Sanity-check constantly

---

### 12. **Not Using Version Control**

**Symptom:** "I'll just save different folders: model_v1, model_v2, model_final, model_final_FINAL..."

**Why it's wrong:**
- Can't track what changed
- Can't roll back
- Impossible to collaborate
- Looks unprofessional

**Fix:**
- Use git from day 1
- Commit frequently
- Write meaningful commit messages
- Tag important versions

---

## The Business Model (Optional)

*If you want to monetize alongside open-source*

### The Hybrid Model

**Open-Source (Free):**
- Code (MIT/Apache)
- Pre-trained weights
- Documentation
- Self-hosting instructions

**Commercial API (Paid):**
- Hosted inference
- No setup required
- Pay-per-use or subscription
- Optional: premium features

### Why This Works

**For users:**
- Hobbyists self-host (free)
- Researchers use for free (citation/credibility)
- Developers pay for convenience (no DevOps)
- Companies pay for reliability (SLA, support)

**For you:**
- Open-source builds distribution
- API captures revenue from those who can pay
- Aligned incentives (better model → more users → more revenue)

### Pricing Strategy

**Research the competition:**
- ElevenLabs: ~$5-300/mo subscription
- PlayHT: ~$0.30 per 1000 chars
- Replicate: ~$0.0001-0.01 per second of audio

**Your positioning: Undercut incumbents**
- Free tier: 100 conversions/month
- Hobby: $19/mo (2,000 conversions)
- Pro: $49/mo (10,000 conversions)
- Pay-as-you-go: $0.02 per conversion

**Why cheaper:**
- Lower overhead (solo/small team)
- Open-source reduces support burden (community helps)
- Focused offering (not full TTS platform)

### Tech Stack for API

**Inference hosting:**
- [Modal](https://modal.com): Serverless GPU (easiest)
- [Replicate](https://replicate.com): Host your model on their platform
- [Banana.dev](https://banana.dev): Serverless ML
- DIY: FastAPI + AWS/GCP GPU instances

**Auth & billing:**
- [Clerk](https://clerk.com) or [Auth0](https://auth0.com): Authentication
- [Stripe](https://stripe.com): Billing
- [Quotas](https://github.com/vutran/fastify-rate-limit): Rate limiting

**Monitoring:**
- [Sentry](https://sentry.io): Error tracking
- [PostHog](https://posthog.com): Analytics
- [Better Stack](https://betterstack.com): Uptime

**Time to build API layer: 2-4 weeks** (after model is working)

### Revenue Expectations

**Conservative (Month 6):**
- 1,000 free users
- 20 paying ($25 avg)
- **Revenue: $500/mo**

**Moderate (Month 12):**
- 5,000 free users
- 100 paying ($35 avg)
- **Revenue: $3,500/mo**

**Optimistic (Month 18):**
- 20,000 free users
- 500 paying ($50 avg)
- **Revenue: $25,000/mo**

**This is not "quit your job" money quickly**, but:
- Validates commercial viability
- Covers your costs
- Shows labs you can monetize research
- Could grow into sustainable income

### When to Build the API

**Don't build it too early:**
- ❌ Month 1-2: Model doesn't work yet
- ❌ Month 3-4: Still iterating on quality

**Sweet spot:**
- ✅ Month 6-8: Model is competitive
- ✅ Open-source release has traction
- ✅ People are asking "can you host this?"

**Build API when:**
1. Model quality is solid (competitive with SOTA)
2. GitHub has 100+ stars (demand signal)
3. You have time (model isn't consuming 100% of effort)

---

## Timeline to Hirability

### The 12-Month Plan

**Month 1-2: Foundation**
- ✅ Literature survey (5-10 key papers)
- ✅ Data pipeline setup
- ✅ Baseline model training (even if bad)
- ✅ Evaluation framework set up
- **Deliverable:** End-to-end system that produces audio (quality: bad, that's okay)

**Month 3-5: Iteration**
- ✅ Systematic experiments (architecture, losses, data)
- ✅ Ablation studies
- ✅ Approach competitive quality
- **Deliverable:** Model that matches or beats some baselines

**Month 6-7: Polish**
- ✅ Compare to latest SOTA rigorously
- ✅ Clean up code
- ✅ Write technical report / preprint
- **Deliverable:** ArXiv paper + clean repo

**Month 8: Release**
- ✅ Open-source launch
- ✅ Blog post
- ✅ Social media promotion
- **Deliverable:** Public project with docs, demos, checkpoints

**Month 9-10: Grow & Engage**
- ✅ Respond to issues, accept PRs
- ✅ Write follow-up blog posts
- ✅ Engage on Twitter/Reddit
- ✅ (Optional) Build API if there's demand
- **Deliverable:** Active project with community

**Month 11-12: Job Search**
- ✅ Apply to labs with portfolio
- ✅ Get warm intros from network
- ✅ Interview prep
- **Deliverable:** Job offers

### What Your Portfolio Looks Like at Month 12

**GitHub:**
- ✅ Main project: 200-500 stars
- ✅ Clean, well-documented code
- ✅ Active contributions (green squares)
- ✅ 2-3 other smaller projects (shows range)

**Writing:**
- ✅ ArXiv preprint (shows research ability)
- ✅ 3-5 blog posts (shows communication)
- ✅ Good README/docs (shows you care about users)

**Social:**
- ✅ Twitter: 200-500 followers (small but engaged)
- ✅ Known in 2-3 Discord/Slack communities
- ✅ Some researchers recognize your name

**Metrics:**
- ✅ Model is competitive with SOTA (or close)
- ✅ 1-2 other papers cite your work
- ✅ 50+ people have used your code

### This Gets You Hired At

**Tier 1 (Stretch):** OpenAI, Anthropic, DeepMind
- Possible but competitive
- Need exceptional results or connections

**Tier 2 (Realistic):** HuggingFace, Stability, Cohere, Adept
- Very achievable with this portfolio
- They value open-source contributions highly

**Tier 3 (Very Likely):** AI startups, smaller research labs
- You're exactly what they're looking for
- Research Engineer / ML Engineer roles

**Tier 4 (Backup):** Academic labs, research intern positions
- Easy to get with this background
- Can be stepping stone to industry

### The Interview Process

**What to expect:**

**1. Initial screen (recruiter or engineer)**
- "Tell me about your voice conversion project"
- "What was the hardest technical challenge?"
- "Why do you want to work here?"

**2. Technical deep-dive**
- "Walk me through your architecture"
- "Why did you choose approach X over Y?"
- "Show me your ablation studies"
- "What didn't work and why?"

**3. Coding (sometimes)**
- Implement a simple ML component
- Debug some code
- System design question

**4. Research fit / culture**
- "Tell me about a paper you read recently"
- "How do you approach ambiguous problems?"
- "How would you collaborate with a team?"

**How your portfolio helps:**
- ✅ Technical deep-dive: Just walk through your project (you're an expert)
- ✅ Coding: You've written thousands of lines of ML code
- ✅ Research fit: Your preprint shows research thinking
- ✅ Culture: Your open-source engagement shows collaboration

**You're interviewing from a position of strength** - you've proven you can do the job.

### If You Don't Get Offers Immediately

**Don't panic.** Adjust:

**Option 1: Keep building**
- Work on v2 of your model
- Collaborate with others
- Contribute to other projects
- Reapply in 6 months with more work

**Option 2: Pivot to related roles**
- ML Engineer (not researcher) at startups
- Developer Relations at AI companies
- Research Engineer at academic labs
- Use these as stepping stones

**Option 3: Consulting/contract**
- Freelance ML work
- Build portfolio while getting paid
- Network with potential employers

**The work you did is never wasted** - it builds your skills and credibility regardless.

---

## Final Thoughts

### The AI Age Changes Everything

**Old model:**
- Knowledge = power
- Credentials = gatekeeping
- Solo genius in ivory tower

**New model:**
- Judgment = power (knowledge is commoditized via AI)
- Demonstrated ability = currency (credentials are secondary)
- Collaborative building in public

**You're living in the best time in history to do research without a PhD.**

### What Matters Now

**Not:**
- ❌ Where you went to school
- ❌ Who your advisor is
- ❌ How many papers you've published in top venues
- ❌ How much math you've memorized

**But:**
- ✅ Can you identify important problems?
- ✅ Can you build things that work?
- ✅ Can you evaluate rigorously?
- ✅ Can you communicate clearly?
- ✅ Can you collaborate effectively?

**All of these are learnable through doing.**

### Your Advantages

As a builder coming from product/SaaS:

✅ **You know how to ship** (most researchers don't)
✅ **You're user-focused** (you think about who will use this)
✅ **You iterate quickly** (you're comfortable with uncertainty)
✅ **You're practical** (you optimize for working, not perfect)
✅ **You use AI effectively** (younger researchers haven't adapted yet)

**These are advantages, not weaknesses.**

### The Real Challenge

It's not technical - you can learn the ML.

It's **persistence through uncertainty:**
- Month 2: "Is this even working?"
- Month 5: "Why is my model worse than baselines?"
- Month 8: "Will anyone care about this?"
- Month 11: "Am I good enough to get hired?"

**This is normal.** Everyone feels this.

**The difference:** You keep building anyway.

### Success Looks Like

**12 months from now:**
- You deeply understand one area of ML (voice conversion)
- You've shipped a real project (open-source model)
- You've proven research ability (preprint + experiments)
- You have options (job offers, or sustainable side revenue, or both)
- You're confident you can do this again (transferable skills)

**Even if the specific project doesn't "succeed"** (doesn't get cited, doesn't make money), you've de-risked your career by proving you can do hard technical work.

### Your Next Step

**Don't overthink it. Just start.**

**This week:**
1. Set up your development environment
2. Download VCTK dataset
3. Implement a simple mel-spectrogram extractor
4. Listen to the spectrograms

**That's it. You're doing research.**

The rest is just iteration.

---

## Resources

### Learning Resources

**Courses (Optional):**
- [Fast.ai Practical Deep Learning](https://course.fast.ai/)
- [Stanford CS224S: Speech Processing](http://web.stanford.edu/class/cs224s/)
- [Hugging Face Audio Course](https://huggingface.co/learn/audio-course/)

**Blogs to Follow:**
- [Distill.pub](https://distill.pub) (excellent explanations)
- [The Gradient](https://thegradient.pub)
- [Sebastian Raschka's blog](https://sebastianraschka.com/blog/)

**Twitter Accounts (ML/Speech):**
- @ylecun (Yann LeCun)
- @karpathy (Andrej Karpathy)
- @hardmaru (David Ha)
- Follow people who cite your target papers

**Discord/Slack:**
- HuggingFace Discord
- EleutherAI Discord
- Papers We Love

### Tools

**Training:**
- PyTorch (framework)
- Weights & Biases / TensorBoard (logging)
- Hydra (config management)

**Audio:**
- librosa (audio processing)
- soundfile (I/O)
- pyworld / CREPE (pitch extraction)

**Deployment:**
- FastAPI (API framework)
- Modal / Replicate (serverless GPU)
- Docker (containerization)

**Writing:**
- Overleaf (LaTeX for papers)
- Notion / Obsidian (notes)
- Grammarly (proofreading)

### Communities

**Ask questions:**
- r/MachineLearning
- r/LanguageTechnology
- Stack Overflow
- Cross Validated (stats)

**Share work:**
- Twitter
- Reddit
- Hacker News
- Papers with Code

**Collaborate:**
- HuggingFace Forums
- Discord servers
- GitHub Discussions

---

## Conclusion

**Research isn't magic. It's just building + documentation + honesty.**

You already know how to build (you shipped a SaaS).

Now you'll learn to:
- Build with ML (new domain, same skills)
- Document like a researcher (papers, not product specs)
- Evaluate rigorously (metrics, not user feedback)

**12 months from now, you'll be employable at AI labs.**

Not because you got a PhD.

Because you **proved** you can do the work.

Now go build something.

---

*This guide was written for builders who want to do research in the age of AI. Feel free to share, remix, and improve. Good luck.*

