# paper-taste digest — 2026-10-31

Ranked by heuristic quality × recency (10-day half-life). Scores are a first pass from metadata and abstracts; see [TASTE.md](TASTE.md) for the rubric an agent applies on top, and [AGENTS.md](AGENTS.md) to get recommendations matched to your own repos.

## Papers (last 7 days, 1026 kept in the last 14)

1. **[Intrinsic Distribution Matching](https://arxiv.org/abs/2610.39633)** — quality 63  
   Deyuan Liu, Yansen Han, Kaiwen Zheng et al. · 2026-10-29  
   _why:_ ablations; variance / significance; code released; HF daily papers: 239 upvotes  
   > One-step and few-step text-to-image generation must accurately render the details specified in the prompt despite limited opportunities for refinement. Distribution matching distillation (DMD) uses score differences to bring the generated distribution closer to a reference…

2. **[Training Foundation Models with a Single Algorithm](https://arxiv.org/abs/2610.40564)** — quality 58  
   Yuda Song, Alvin Zhang, Fahim Tajwar et al. · 2026-10-29  
   _why:_ code released; 67 pages; HF daily papers: 5 upvotes; senior author (h-index 69); shared on X by 1 account  
   > Foundation models are typically trained in stages: pretraining, midtraining, supervised fine-tuning (SFT), and reinforcement learning (RL), with changes in both data and learning algorithms. We show that this algorithmic separation is not fundamental. By deriving suitable RL…

3. **[Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?](https://arxiv.org/abs/2610.37662)** — quality 62  
   Jialv Zou, Xiaotong Li, Zhengrong Yue et al. · 2026-10-27  
   _why:_ theory; code released; HF daily papers: 83 upvotes; senior author (h-index 86)  
   > Discrete visual tokens represent vision in a discrete form analogous to language, offering a native interface for multimodal modeling under a shared next-token prediction objective. However, quantization error is widely assumed to cause unavoidable semantic loss, fundamentally…

4. **[EmbeddingGemma 2: Unified and Efficient Multimodal Representations](https://arxiv.org/abs/2610.37364)** — quality 63  
   Henrique Schechter Vera, Sahil Dua, Jovan Andonov et al. · 2026-10-27  
   _why:_ ablations; weights/data released; 28 pages; HF daily papers: 29 upvotes; senior author (h-index 72); 73-author team  
   > We present EmbeddingGemma 2, an open multimodal embedding model which natively represents text, images, audio, video, and combinations thereof in a unified space. Our approach introduces improvements such as simplified per-layer embeddings and a multi-stage curriculum with…

5. **[AskStream: When and What to Ask Proactively under Uncertainty in Streaming Video Understanding](https://arxiv.org/abs/2610.38678)** — quality 57  
   Lu Wang, Zhuoran Jin, Longxiang Wang et al. · 2026-10-28  
   _why:_ negative results / limitations; code released; weights/data released; 42 pages; HF daily papers: 10 upvotes  
   > Recent advances in multimodal large language models have increased interest in interaction paradigms for video understanding. The evolution from offline to streaming and proactive interaction has gradually shifted models from passive responders toward more proactive agents that…

6. **[Proving and Improving the Platonic Representation Hypothesis with JEPAs](https://arxiv.org/abs/2610.39302)** — quality 53  
   Randall Balestriero, Yann LeCun · 2026-10-29  
   _why:_ model-scale sweep; theory; code released; HF daily papers: 55 upvotes ⚠ hype: remarkably  
   > Whether models trained on different modalities converge to the same representation of the world is central to AI. The Platonic Representation Hypothesis (PRH) conjectures that they do as they scale, but without a proof it offers neither a guarantee nor a recipe. We turn the…

7. **[Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers](https://arxiv.org/abs/2610.40647)** — quality 50  
   Jiongfan Yang, Weichen Fan, Haiwen Diao et al. · 2026-10-29  
   _why:_ code released; HF daily papers: 36 upvotes  
   > Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency…

8. **[L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](https://arxiv.org/abs/2610.40614)** — quality 50  
   Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al. · 2026-10-29  
   _why:_ strong baselines; code released; HF daily papers: 37 upvotes  
   > Interactive world models generate visual content conditioned on user actions, yet maintaining spatial consistency over long-horizon exploration in real time remains challenging. Existing approaches rely on either temporal context or explicit 3D memory, both of which scale poorly…

9. **[S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning](https://arxiv.org/abs/2610.35518)** — quality 62  
   Shuo Shen, Guangran Cheng, Chengqi Lyu et al. · 2026-10-26  
   _why:_ strong baselines; model-scale sweep; negative results / limitations; code released; HF daily papers: 33 upvotes  
   > Critic-free methods are widely used in reinforcement learning with verifiable rewards (RLVR) for long chain-of-thought (CoT) reasoning, avoiding difficult and costly critic training. Common alternatives lack token-level credit assignment and typically rely on grouped rollouts to…

10. **[Hy-Nomas: Towards Free-form Interactive World Generation](https://arxiv.org/abs/2610.36729)** — quality 58  
   Qiaoling Chen, Jiaxiang Cheng, Xueqing Deng et al. · 2026-10-27  
   _why:_ human evaluation; weights/data released; code released; HF daily papers: 126 upvotes; 38-author team  
   > Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences. We present Hy-Nomas, a video world model with an 8B diffusion backbone that supports free-form text instructions and continuous camera control…

11. **[AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers](https://arxiv.org/abs/2610.39663)** — quality 49  
   Bin Xu, Mo Zhang, Zhengfeiyang Zhang et al. · 2026-10-29  
   _why:_ strong baselines; negative results / limitations; code released; HF daily papers: 5 upvotes  
   > Video diffusion transformers generate high-quality videos, but the quadratic cost of 3D full attention dominates their inference. Dynamic block-sparse attention reduces this cost by computing exact attention only on key/value blocks selected from current activations. However,…

12. **[M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents](https://arxiv.org/abs/2610.37459)** — quality 55  
   Hannes Ill, Rafi Al Attrach, Rajna Fani et al. · 2026-10-27  
   _why:_ strong baselines; reproduction / replication; code released; weights/data released; accepted: NeurIPS; 33 pages  
   > Clinical research over electronic health records depends on derived variables whose definitions sit outside the schema, in item codes, time windows, missingness rules, and output-grain choices that change cohorts and downstream conclusions. We introduce M4Bench, 28 clinical…

13. **[The Quine Test: How Much of a Model's Self Survives Its Own Description?](https://arxiv.org/abs/2610.38726)** — quality 49  
   Bibin Babu, Ivan P. Yamshchikov, Aleksei Shpilman · 2026-10-28  
   _why:_ strong baselines; theory; reproduction / replication; code released; weights/data released; 32 pages  
   > Frontier language models express coherent preferences, but behavioral evidence alone cannot say whether these belong to the model or to a character it portrays. Following Hofstadter's view of the self as a self-description, we ask whether a model's description of itself works as…

14. **[Is It the Curriculum or Just the Easy Start? Benchmarking Unsupervised Environment Design on Quadrupeds](https://arxiv.org/abs/2610.40364)** — quality 46  
   Jakub Gilewicz, Dominik Galus, Piotr Wojdas · 2026-10-29  
   _why:_ strong baselines; variance / significance; mechanistic / causal analysis; contamination check; code released  
   > Unsupervised environment design (UED) methods such as PLR, ACCEL, SFL and PAIRED are compared mostly on 2D mazes, grid worlds and BipedalWalker, while terrain curricula for legged robots are hand-designed and evaluated against a few baselines. We present a benchmark that runs…

15. **[Online Dense Reinforcement Learning with Planning-Grounding Agent for UI Navigation on Live IOS Apps](https://arxiv.org/abs/2610.39264)** — quality 48  
   Peitong Duan, Khashayar Gatmiry, Jeffrey Nichols et al. · 2026-10-29  
   _why:_ strong baselines; negative results / limitations; HF daily papers: 7 upvotes; senior author (h-index 93)  
   > While frontier vision-language models demonstrate strong capabilities in user interface (UI) navigation, their high inference costs prohibit everyday use. Conversely, smaller models trained via supervised fine-tuning (SFT) or offline reinforcement learning often memorize static…

16. **[NEOPIC: A Neural Operator Framework for Particle-based Kinetic Plasma Simulations](https://arxiv.org/abs/2610.40528)** — quality 46  
   Sriramkrishnan Muralikrishnan, Chelsea Maria John, Jeffrey Kelling et al. · 2026-10-29  
   _why:_ theory; code released; 84 pages  
   > We introduce NEOPIC, a framework for learning the field operator in particle-based methods applied to kinetic plasma simulations. Its key novelty is a neural operator that acts directly on the empirical measure of the particles, rather than on a grid, and is evaluated at the…

17. **[OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images](https://arxiv.org/abs/2610.35684)** — quality 57  
   Junyeong Ahn, Geonwoo Kim, Kinam Kim et al. · 2026-10-26  
   _why:_ negative results / limitations; contamination check; code released; 25 pages; HF daily papers: 50 upvotes  
   > Generating videos of a specific subject from a few reference images remains challenging when the camera reveals surfaces that are not visible in the input. Early subject-to-video (S2V) methods condition on a single reference image and must therefore infer the subject's unseen…

18. **[MUSE: Multi-Level Memory with Selective Runtime Injection for Scientific Coding Agents](https://arxiv.org/abs/2610.38332)** — quality 50  
   Haoran Jin, Defu Lian, Xiting Wang et al. · 2026-10-28  
   _why:_ ablations; strong baselines; code released; senior author (h-index 56)  
   > Historical experience can guide scientific coding at multiple levels, but task-level retrieval may miss implementation lessons that become relevant during execution. We introduce MUSE, a memory management framework combining multi-level memory with selective runtime injection…

19. **[A-RSI: Adaptive Task Refresh for Zero-Data Multimodal Self-Improvement](https://arxiv.org/abs/2610.38568)** — quality 50  
   Yu Liu, Youxing Li, Yuedong Tan et al. · 2026-10-28  
   _why:_ HF daily papers: 151 upvotes; senior author (h-index 106); 20-author team  
   > Recursive self-improvement requires models not only to acquire useful training experience, but also to decide when their current experience has ceased to be useful. Existing methods often focus on what experience to generate next, while paying less attention to when fresh…

20. **[HairDeck: Animation-Ready Stylized Hair Cards from a Single Image](https://arxiv.org/abs/2610.40599)** — quality 45  
   Yuze He, Yixiang Wei, Wang Zhao et al. · 2026-10-29  
   _why:_ code released; 27 pages; HF daily papers: 18 upvotes  
   > The hair of stylized characters in games and avatars is built from hair cards: artist-placed ribbons whose geometry is the visible hair, animated by spring bones. Existing image-based methods produce realistic hair or a single fused mesh, while CHARM, the only generator of…

21. **[Multi-Token Prediction Done Right](https://arxiv.org/abs/2610.38331)** — quality 50  
   Jayden Teoh · 2026-10-28  
   _why:_ model-scale sweep; code released; HF daily papers: 11 upvotes; Reddit: 1 submission  
   > Multi-Token Prediction (MTP) is now a common ingredient in language-model pre-training, as it improves downstream performance and enables faster inference through speculative decoding. We identify a flaw in standard MTP training, in which a residual component of the MTP gradient…

22. **[Timestral](https://arxiv.org/abs/2610.37585)** — quality 51  
   Adrien Petralia, Alexandre Gavaudan, Artjom Joosen et al. · 2026-10-27  
   _why:_ code released; weights/data released; HF daily papers: 13 upvotes; senior author (h-index 56); 356-author team  
   > We introduce Timestral, a family of four time series foundation models for probabilistic forecasting, with 5M, 28M, 123M, and 209M parameters. Timestral sets a new state of the art on GIFT-Eval, TIME, and fev-bench, where Timestral-209M and Timestral-123M take the top two places…

23. **[LLM-Assisted Optimization for Simulation-Based Redesign](https://arxiv.org/abs/2610.39275)** — quality 46  
   Chan-Eui Song, Jeremy J. Michalek, Christopher McComb · 2026-10-29  
   _why:_ strong baselines; code released; weights/data released  
   > Engineering design frequently involves redesigning a prior solution to adapt to changes in context, such as material prices or system requirements. Redesign often leverages simulators too complex and/or computationally intensive for traditional numerical solvers, which lack…

24. **[Glance: The Generator Is Its Own Reranker](https://arxiv.org/abs/2610.40454)** — quality 44  
   Adilet Metinov, Chingiz Arziev · 2026-10-29  
   _why:_ variance / significance; weights/data released; HF daily papers: 10 upvotes  
   > Retrieval-augmented generation commonly serves separate models for reranking and answering, duplicating model residency and passage processing. We introduce Glance, which equips the generator with a lightweight decision adapter and pointer head to score candidate passages from a…

25. **[Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception](https://arxiv.org/abs/2610.37037)** — quality 52  
   Lai Wei, Yatai Li, Liangbo He et al. · 2026-10-27  
   _why:_ ablations; code released; HF daily papers: 28 upvotes  
   > Multimodal perception forms the foundation of multimodal intelligence. In particular, spatial perception and multimodal long-context understanding are two pivotal tasks that underpin embodied AI and multimodal agents. However, synthesizing targeted, high-quality training data…


## Blog posts & lab write-ups (last 14 days)

1. **[Automated Subtle Emergent Misalignment Research](https://alignment.anthropic.com/2026/automated-em-search/)** — quality 75  
   Anthropic Alignment Science · 2026-10-31  
   _why:_ strong baselines; variance / significance; mechanistic / causal analysis; negative results / limitations; contamination check; long-form (37k chars)  
   > Automated Subtle Emergent Misalignment Research Alignment Science Blog Automated Subtle Emergent Misalignment Research Oscar Balcells Obeso October 2026 Richard Qi, Monte MacDiarmid, Evan Hubinger tl;dr Red-teaming by humans is a vital part of model safety testing, but it may…

2. **[Open-weight AI models can exploit the patch gap](https://epoch.ai/publications/open-weight-models-patch-gap)** — quality 71  
   Epoch AI (Publications) · 2026-10-29  
   _why:_ mechanistic / causal analysis; reproduction / replication; negative results / limitations; code released; source tier 1; shared on X by 1 account  
   > GLM 5.3 turned published-but-unshipped Firefox security fixes into working one-click exploits for six releases, at roughly $1,000 each.

3. **[Anthropic Residency: applications open for established technical leaders](https://alignment.anthropic.com/2026/anthropic-residency/)** — quality 54  
   Anthropic Alignment Science · 2026-11-22  
   _why:_ mechanistic / causal analysis; source tier 1  
   > Anthropic Residency: applications open for established technical leaders Alignment Science Blog Anthropic Residency: applications open for established technical leaders Today we are opening applications for the Anthropic Residency, our paid, fixed-term research program with…

4. **[DeepSeek-V4.1-Flash: Run Locally Guide](https://unsloth.ai/docs/models/deepseek-v4.1-flash)** — quality 56  
   unsloth.ai · 2026-10-30  
   _why:_ strong baselines; reproduction / replication; contamination check; weights/data released; source tier 3; shared on X by 2 accounts  
   > Run DeepSeek-V4.1-Flash-1017 locally with Unsloth GGUFs and Engram n-gram offloading.

5. **[How AI agents shape experts’ judgment calls](https://www.anthropic.com/research/agents-judgment-calls)** — quality 70  
   Anthropic Research · 2026-10-27  
   _why:_ variance / significance; mechanistic / causal analysis; controlled experiments; negative results / limitations; source tier 1; in newsletters: Ben's Bites  
   > In a randomized trial, professional analysts working with an AI coding agent went with the option the agent was randomly assigned to favor 86% of the time. We look at what this means for human oversight of AI-assisted work.

6. **[From Tokens to Bytes I: Scaling Hierarchical Networks](https://cartesia.ai/blog/from-tokens-to-bytes-part-1)** — quality 65  
   Cartesia · 2026-10-28  
   _why:_ strong baselines; model-scale sweep; reproduction / replication; negative results / limitations; contamination check; long-form (52k chars)  
   > A newer generation of H-Nets learns directly from raw bytes, and matches an open-source 3B Transformer with 10x less compute and data.

7. **[Le Chonk: Built for Coders, Trusted by Defenders.](https://mistral.ai/news/mistral-large-4-oss/)** — quality 56  
   Mistral AI · 2026-10-29  
   _why:_ reproduction / replication; human evaluation; weights/data released; source tier 3; shared on X by 1 account; Hacker News: 1 submission, 1694 points  
   > The weights of Mistral Large 4 (Le Chonk) are now open. A 1T parameter multimodal model, and best open-weight model for coding, trained in Europe.

8. **[Frontiers in Making up People](https://www.argmin.net/p/frontiers-in-making-up-people)** — quality 55  
   Ben Recht (arg min) · 2026-10-29  
   _why:_ theory; source tier 1  
   > Trying (and failing) to make sense of the buzzy weird world of silicon sampling.

9. **[Galactus the Devourer](https://www.argmin.net/p/galactus-the-devourer)** — quality 51  
   Ben Recht (arg min) · 2026-10-30  
   _why:_ theory; source tier 1 ⚠ hype: incredibly  
   > On efficient algorithms, the exponential time hypothesis, and losing the plot.

10. **[Circuits Updates](https://transformer-circuits.pub/2026/october-update/index.html)** — quality 51  
   Transformer Circuits · 2026-10-30  
   _why:_ mechanistic / causal analysis; source tier 1  
   > A short update on an extension to the Jacobian lens.

11. **[CS 2881 Fall 26: Lecture 3: Modern LLM Training and Inference](https://windowsontheory.org/2026/10/28/cs-2881-fall-26-lecture-3-modern-llm-training-and-inference/)** — quality 57  
   Windows On Theory (Boaz Barak) · 2026-10-28  
   _why:_ strong baselines; model-scale sweep; mechanistic / causal analysis; reproduction / replication; negative results / limitations; human evaluation  
   > September 17, 2026 · Boaz Barak · Scribe notes by Daniel Schwartz, Dev Desai, and Ed Gerrard Lecture Video: https://youtu.be/Lp_e8Ts5-nE Slides: Presentation slides Authors’ Intro Daniel Schwartz: I’m a second-year MS/MBA student. I worked as a PM at multiple early-stage…

12. **[Day 0 support for Mistral Large 4 on vLLM](https://vllm.ai/blog/2026-10-29-mistral-large-4)** — quality 54  
   vLLM · 2026-10-29  
   _why:_ model-scale sweep; variance / significance; reproduction / replication; long-form (33k chars); source tier 2  
   > Day-0 vLLM support for Mistral Large 4 with sparse MLA, cross-layer KV sharing, DSpark speculative decoding, DCP/PCP long context and NIXL P/D on NVIDIA Blackwe


## Shared on X, in newsletters & on HN/Reddit (last 14 days)

1. **[Automated Subtle Emergent Misalignment Research](https://alignment.anthropic.com/2026/automated-em-search/)** — quality 75  
   Anthropic Alignment Science · 2026-10-31  
   _why:_ strong baselines; variance / significance; mechanistic / causal analysis; negative results / limitations; contamination check; long-form (37k chars)  
   > Automated Subtle Emergent Misalignment Research Alignment Science Blog Automated Subtle Emergent Misalignment Research Oscar Balcells Obeso October 2026 Richard Qi, Monte MacDiarmid, Evan Hubinger tl;dr Red-teaming by humans is a vital part of model safety testing, but it may…

2. **[Open-weight AI models can exploit the patch gap](https://epoch.ai/publications/open-weight-models-patch-gap)** — quality 71  
   Epoch AI (Publications) · 2026-10-29  
   _why:_ mechanistic / causal analysis; reproduction / replication; negative results / limitations; code released; source tier 1; shared on X by 1 account  
   > GLM 5.3 turned published-but-unshipped Firefox security fixes into working one-click exploits for six releases, at roughly $1,000 each.

3. **[DeepSeek-V4.1-Flash: Run Locally Guide](https://unsloth.ai/docs/models/deepseek-v4.1-flash)** — quality 56  
   unsloth.ai · 2026-10-30  
   _why:_ strong baselines; reproduction / replication; contamination check; weights/data released; source tier 3; shared on X by 2 accounts  
   > Run DeepSeek-V4.1-Flash-1017 locally with Unsloth GGUFs and Engram n-gram offloading.

4. **[Training Foundation Models with a Single Algorithm](https://arxiv.org/abs/2610.40564)** — quality 58  
   Yuda Song, Alvin Zhang, Fahim Tajwar et al. · 2026-10-29  
   _why:_ code released; 67 pages; HF daily papers: 5 upvotes; senior author (h-index 69); shared on X by 1 account  
   > Foundation models are typically trained in stages: pretraining, midtraining, supervised fine-tuning (SFT), and reinforcement learning (RL), with changes in both data and learning algorithms. We show that this algorithmic separation is not fundamental. By deriving suitable RL…

5. **[How AI agents shape experts’ judgment calls](https://www.anthropic.com/research/agents-judgment-calls)** — quality 70  
   Anthropic Research · 2026-10-27  
   _why:_ variance / significance; mechanistic / causal analysis; controlled experiments; negative results / limitations; source tier 1; in newsletters: Ben's Bites  
   > In a randomized trial, professional analysts working with an AI coding agent went with the option the agent was randomly assigned to favor 86% of the time. We look at what this means for human oversight of AI-assisted work.

6. **[From Tokens to Bytes I: Scaling Hierarchical Networks](https://cartesia.ai/blog/from-tokens-to-bytes-part-1)** — quality 65  
   Cartesia · 2026-10-28  
   _why:_ strong baselines; model-scale sweep; reproduction / replication; negative results / limitations; contamination check; long-form (52k chars)  
   > A newer generation of H-Nets learns directly from raw bytes, and matches an open-source 3B Transformer with 10x less compute and data.

7. **[Le Chonk: Built for Coders, Trusted by Defenders.](https://mistral.ai/news/mistral-large-4-oss/)** — quality 56  
   Mistral AI · 2026-10-29  
   _why:_ reproduction / replication; human evaluation; weights/data released; source tier 3; shared on X by 1 account; Hacker News: 1 submission, 1694 points  
   > The weights of Mistral Large 4 (Le Chonk) are now open. A 1T parameter multimodal model, and best open-weight model for coding, trained in Europe.

8. **[EmbeddingGemma 2: Unified and Efficient Multimodal Representations](https://arxiv.org/abs/2610.37364)** — quality 63  
   Henrique Schechter Vera, Sahil Dua, Jovan Andonov et al. · 2026-10-27  
   _why:_ ablations; weights/data released; 28 pages; HF daily papers: 29 upvotes; senior author (h-index 72); 73-author team  
   > We present EmbeddingGemma 2, an open multimodal embedding model which natively represents text, images, audio, video, and combinations thereof in a unified space. Our approach introduces improvements such as simplified per-layer embeddings and a multi-stage curriculum with…

9. **[The sleep framework: A new way for LLMs to retain knowledge in continual learning](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)** — quality 59  
   Google Research · 2026-10-27  
   _why:_ strong baselines; mechanistic / causal analysis; source tier 2; shared on X by 1 account; Hacker News: 1 submission, 224 points  
   > Education Innovation

10. **[Artificial Analysis v5 and the benchmarker's dilemma](https://www.interconnects.ai/p/artificial-analysis-v5-and-the-benchmarkers)** — quality 52  
   Interconnects (Nathan Lambert) · 2026-10-28  
   _why:_ strong baselines; multiple benchmarks; source tier 2; Hacker News: 1 submission, 70 points ⚠ hype: incredibly  
   > A sort of review of the benchmarking industry and what's missing.

11. **[Introducing LFM3: Every Modality for Specialized Intelligence](https://www.liquid.ai/blog/lfm3)** — quality 56  
   Liquid AI · 2026-10-27  
   _why:_ multiple benchmarks; long-form (31k chars); source tier 2; Hacker News: 1 submission, 171 points  
   > LFM3 is Liquid AI’s new open-weight model family: 2B-class text, vision, audio, omni, and decision models built to fine-tune and run fast on any device.

12. **[Concerning behavior from a popular open-weight AI model](http://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model)** — quality 57  
   cohere.com · 2026-10-26  
   _why:_ mechanistic / causal analysis; reproduction / replication; weights/data released; source tier 3; shared on X by 5 accounts  
   > Discover how untrusted open-weight AI models can potentially leak data, even when self-hosted. Learn the security risks and how to protect your enterprise.
