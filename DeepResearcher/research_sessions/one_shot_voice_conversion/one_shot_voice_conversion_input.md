# Prompt for AI Voice Conversion Research Agent

You are an expert AI research assistant in **voice conversion** and **speech processing**. Your goal is to help design a **cutting-edge single-shot voice conversion model** (targeting performance beyond RVC-level systems) using only publicly available datasets and tools. Specifically, craft a comprehensive research plan and analysis covering the following points:

- **Background and Scope:** Explain what one-shot voice conversion entails (converting any source speaker’s speech to an arbitrary target speaker’s voice using only one reference utterance of that target). Emphasize the need for **state-of-the-art quality** in naturalness and speaker similarity. Highlight why single-shot (or zero-shot) is challenging and important, and how it differs from multi-shot systems (like the original RVC) that use many samples per speaker. 

- **Literature Survey:** Perform an in-depth review of recent and relevant research (last ~5 years) on one-shot/zero-shot voice conversion. Summarize key methods and architectures, such as:
  - **Disentanglement and Autoencoding:** e.g., VAE-based systems (AutoVC), instance normalization methods (AdaIN-VC), etc.
  - **Attention & Transformer-based:** e.g., StyleTTS-VC, Pureformer-VC, Zipformer-based decoders, Triplet-loss training.
  - **ASR/PPG-based:** systems using phonetic posteriorgrams or bottleneck ASR features to separate content from speaker (e.g., HiFi-VC, other PPG-VC approaches).
  - **Self-supervised/SSL features:** using models like WavLM, HuBERT as content encoders (e.g., FreeVC, other recent work).
  - **TTS and Cloning methods:** techniques borrowing from text-to-speech voice cloning (e.g., VITS-based, VALL-E/YourTTS style approaches).
  - **Flow/Diffusion models:** any diffusion transformer approaches or normalizing flow methods applied to voice conversion (e.g., DiffusionVC, Seed-VC).
  - **Prosody and expressiveness:** systems that also convert prosody and emotion (e.g., integrated prosody conversion like prosody encoder).
  - Cite and contrast the top contenders: RVC (Retrieval-based Voice Conversion), **OpenVoice**, **FreeVC**, **TriAAN-VC**, **Pureformer-VC**, **Phoneme Hallucinator**, **StyleTTS-VC**, **ALO-VC**, **Seed-VC**, **VITS/AUTOVC-based clones**, etc. Identify which are open-source and under what licenses, and note their strengths and weaknesses. 

- **Competitor Analysis:** Identify existing **open-source voice conversion projects** (especially one-shot/zero-shot) as benchmarks. Include:
  - RVC (multi-shot baseline we aim to surpass).
  - Any recent released models (e.g., Seed-VC, OpenVoice, CosyVoice, yourTTS, etc.).
  - Voice Conversion Challenge entries (if code is available).
  - Evaluate publicly known performance metrics of these models (MOS scores, speaker similarity, F0 correlation, etc.).
  - Determine what the current **best-in-class** values are for key tasks (naturalness MOS, similarity MOS, intelligibility).
  - Discuss limitations or gaps in these systems (e.g., artifacts, limited prosody handling, language coverage, inference speed).

- **Evaluation Framework:** Define how to **evaluate and compare** models:
  - **Subjective Metrics:** Plan listening tests (MOS or MUSHRA) for naturalness and voice similarity. Consider ABX tests for speaker identity.
  - **Objective Metrics:** Use speaker verification scores/EER to measure identity match, F0/RMF0 correlation for pitch accuracy, Mel-Cepstral Distortion (MCD) for spectral fidelity, ASR word error rate for content preservation. Mention standard benchmarks like VCC tests. 
  - **Tools and Protocols:** Suggest using open tools (ASR models, speaker encoders) for automatic evaluation. Emphasize reproducibility: use standard splits, hold-out speakers, etc. 
  - **Baseline Comparison:** Plan to compare against RVC (as baseline) and any other top approaches you found. Specify test scenarios (same-language vs cross-language conversion, same gender vs cross-gender, emotional speech, singing).

- **Data Strategy:** Choose and justify open-source datasets for training and evaluation:
  - Candidate datasets: e.g., **VCTK** (multi-speaker English), **LibriSpeech/LibriTTS**, **AISHELL-3** (multi-speaker Mandarin), **CommonVoice**, **M4Singer** (for singing VOX), or other multilingual corpora. 
  - Explain how to preprocess data (e.g., voice activity detection, normalization). Plan to split archives so target reference utterance is excluded from training.
  - If needed, propose using publicly available speaker datasets for indexing (like a large pool to find reference speakers) but ensuring single-shot conditions.
  - Ensure license compliance and highlight any dataset used is compatible with open-source (avoid proprietary or bumper-limited ones).
  - Consider data augmentation or unsupervised data sources (e.g., TTS-generated data for augmentation) to improve robustness.

- **Model Design and Innovation:** Outline a blueprint for the new model, focusing on improvements over competitors:
  - **Architecture:** Suggest a modern neural architecture (e.g., encoder-decoder with Conformer/Transformer blocks, flow-based decoder, diffusion, etc.). Consider using *Siamese* or dual encoders for source and target as seen in MAIN-VC or TriAAN-VC. 
  - **Content Representation:** Propose leveraging self-supervised features (WavLM or HuBERT) or ASR bottleneck features to represent content without speaker info. Possibly use an information bottleneck or adversarial loss to remove speaker identity.
  - **Speaker/Style Encoding:** For the one-shot reference, decide on using a speaker encoder (x-vector, d-vector) or learn style tokens. Alternatively, use quantized style codes or the Phoneme Hallucinator set-expansion idea. 
  - **Losses and Training:** Incorporate a mixture of reconstruction (VITS-style), adversarial, cyclic, and/or contrastive losses. Consider using triplet loss or GE2E loss to improve speaker separation. If text/alignment is available, maybe a joint ASR/VC training.
  - **Vocoder and End-to-End:** Use or adapt a high-quality neural vocoder (Parallel WaveGAN, HiFiGAN, or VITS end-to-end) for waveform generation. Integrate vocoder training if needed.
  - **Efficiency and Deployment:** Aim for a lightweight but fast model. Consider low-latency inference for real-time use. Use knowledge from MobileNets or similar if needed. 
  - **Novel Ideas:** Encourage creativity – e.g., multi-scale prosody modeling, unsupervised contrastive learning, integrated pitch encoder, or chaining with singing conversion techniques. If trending, look at using diffusion transformers or large checkpoint bit like Conda's approach (in-context learning).
  - **Benchmark Goals:** Define target improvements (e.g., +X% speaker similarity, or MOS above current best) and articulate how design choices help reach them.

- **Challenges & Solutions:** Discuss potential obstacles (speaker leakage, overfitting to one-shot, content distortion, prosody mismatch) and mitigation strategies (data augmentation, disentanglement losses, multistage training).

- **Implementation Plan:** Lay out the steps to actually build the model:
  - Data acquisition and preprocessing.
  - Model prototyping (blocks, embedding extractors).
  - Training (loss schedule, hardware considerations).
  - Iterative evaluation against baselines (RVC, others).
  - Fine-tuning strategies (targeted on particular languages or speaking styles if needed).
  - Open-sourcing: packaging code, writing documentation, complying with Apache license rules (e.g., acknowledging any incorporated third-party code or models).
  - Timeline (if relevant): set realistic milestones (proof of concept, alpha version, benchmarking, final model).

- **Milestones and Deliverables:** Define clear deliverables like: a technical report, code repositories, trained model checkpoints, evaluation results. Emphasize reproducibility (share config and scripts).

Use clear headings and subheadings, bullet points or numbered lists to structure your plan. Your answer should read like a detailed project brief for an AI researcher, identifying concrete tasks, references to methods/datasets, and measurable goals.