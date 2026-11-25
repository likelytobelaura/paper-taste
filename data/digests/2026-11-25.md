# paper-taste digest — 2026-11-25

Ranked by heuristic quality × recency (10-day half-life). Scores are a first pass from metadata and abstracts; see [TASTE.md](TASTE.md) for the rubric an agent applies on top, and [AGENTS.md](AGENTS.md) to get recommendations matched to your own repos.

## Papers (last 7 days, 2535 kept in the last 14)

1. **[Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness](https://arxiv.org/abs/2611.31201)** — quality 64  
   Xiao-Ming Wu, Kang Liao, Yuexiao Ma et al. · 2026-11-23  
   _why:_ strong baselines; controlled experiments; code released; HF daily papers: 101 upvotes; 15-author team  
   > Frontier multimodal models exhibit extraordinary generalization in generating robot actions from observations and instructions, enabling a new paradigm in which they serve directly as policies within closed-loop robotic harnesses. However, the design principles of such…

2. **[Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies](https://arxiv.org/abs/2611.33010)** — quality 59  
   Xuanchen Liu, Hejun Zhang, Boxuan Dong et al. · 2026-11-24  
   _why:_ strong baselines; negative results / limitations; code released; HF daily papers: 26 upvotes  
   > Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We…

3. **[ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds](https://arxiv.org/abs/2611.32649)** — quality 59  
   Qingle Liu, Jieming Li, Pei-lin Li et al. · 2026-11-24  
   _why:_ ablations; contamination check; code released; weights/data released; HF daily papers: 13 upvotes  
   > In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same frontier agents now operate both computers and robots, yet their ICL remains insufficiently assessed: existing benchmarks are largely offline,…

4. **[Rewirable Circuits in Transformers with Loom Attention](https://arxiv.org/abs/2611.30634)** — quality 58  
   Da Xiao, Qingye Meng, Shengping Li et al. · 2026-11-23  
   _why:_ strong baselines; mechanistic / causal analysis; code released; HF daily papers: 73 upvotes  
   > We propose loom attention, which allows a Transformer to dynamically rewire its circuits at every token by interweaving a head's vertical attention over the outputs of earlier heads (to obtain its query, key and value) with its horizontal attention over tokens. We instantiate…

5. **[OWE-Bench: A long-horizon benchmark for measuring real-world engineering](https://arxiv.org/abs/2611.30017)** — quality 59  
   Jacob Cole, Martin Dimakis, Victor Barres et al. · 2026-11-23  
   _why:_ negative results / limitations; code released; weights/data released; 35 pages; shared on X by 1 account  
   > We present OWE-Bench (OpenWorldEngineer-Bench), a benchmark of 26 long-horizon engineering tasks written by domain experts in software engineering, physical engineering, machine learning, and scientific computing. Tasks range from optimizing kernels and designing an aircraft, to…

6. **[RUIBench: What Makes a Good Robot-Use Interface?](https://arxiv.org/abs/2611.31115)** — quality 56  
   Yanzhe Chen, Zhijun Cao, Zechen Bai et al. · 2026-11-23  
   _why:_ controlled experiments; code released; HF daily papers: 22 upvotes; senior author (h-index 53)  
   > Foundation models can reason about complex physical tasks, yet translating this intelligence into reliable robot execution remains challenging. We argue that a critical, often overlooked factor is the robot-use interface (RUI), which determines how agents express and execute…

7. **[What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym](https://arxiv.org/abs/2611.30207)** — quality 56  
   Yikai Zhang, Mai Xu, Yunbei Zhang et al. · 2026-11-23  
   _why:_ controlled experiments; contamination check; code released; weights/data released; HF daily papers: 17 upvotes  
   > Reinforcement learning (RL) trains coding agents on software tasks whose hidden tests decide the reward, yet task collections check these tests only against the reference fix. We ask what makes a task good training data, focusing on the correctness of its reward labels. We audit…

8. **[Measuring Layer-wise Intrinsic Dimensionality of FFNs in LLMs via PCA](https://arxiv.org/abs/2611.32782)** — quality 51  
   Daehee Kim · 2026-11-24  
   _why:_ model-scale sweep; mechanistic / causal analysis; code released; accepted: NeurIPS  
   > Modern large language models (LLMs) keep the feed-forward network (FFN) intermediate width identical across every layer, a convention inherited from the original Transformer. Yet mechanistic work suggests layers at different depths do qualitatively different work, raising a…

9. **[Unlocking the Power of Loops in Pretrained LLMs with Loop Residuals](https://arxiv.org/abs/2611.31094)** — quality 54  
   Xuanlei Zhao, Hailun Xu, Kai Wang et al. · 2026-11-23  
   _why:_ strong baselines; model-scale sweep; code released; HF daily papers: 16 upvotes  
   > Looped Transformers iterate a shared block of layers to increase computation without adding parameters, offering stronger performance and test-time scaling. However, this power has so far required training from scratch and yielded only modest gains for LLMs. Finetuning existing…

10. **[MMMem: Self-Improving Agents with Task-Aware Multimodal Experience Consolidation](https://arxiv.org/abs/2611.30287)** — quality 54  
   Yuxuan Chen, Changwei Lv, Yunfei Li et al. · 2026-11-23  
   _why:_ ablations; strong baselines; mechanistic / causal analysis; code released; HF daily papers: 10 upvotes  
   > AI agents accumulate conversations, images, and documents through long-term interactions with users. Answering later questions often requires connecting evidence across these records, yet the resulting understanding is rarely retained, allowing mistakes to recur on related…

11. **[World Models as Native Latent Action Models](https://arxiv.org/abs/2611.30898)** — quality 52  
   Qinyue Li, Weijie Qiao, Qingyi Tao et al. · 2026-11-23  
   _why:_ strong baselines; weights/data released; HF daily papers: 28 upvotes  
   > Large and diverse video sources, such as egocentric human video and heterogeneous robot recordings, carry rich dynamics but come either without actions or without a shared action space. Latent action models (LAMs) can recover these dynamics, but they train their inverse- and…

12. **[Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with Verifiable Beliefs Teaches Them to Act on What They Believe](https://arxiv.org/abs/2611.32884)** — quality 48  
   Richmond Sin Jing Xuan, Peilin Feng, Wenbin Wang et al. · 2026-11-24  
   _why:_ code released; HF daily papers: 54 upvotes  
   > AI agents working on long tasks often commit to an answer before they have enough evidence, a behavior called laziness. In our evaluations, they frequently commit even while their stated belief still names several possible answers. An outcome reward at the end of the episode…

13. **[TrialAgentBench: Evaluating AI Agents for Clinical-Trial Analysis and Long-Horizon Drug-Development Decisions](https://arxiv.org/abs/2611.30916)** — quality 52  
   Bradley Segal, William Bolton, Philip Torr et al. · 2026-11-23  
   _why:_ variance / significance; weights/data released; accepted: NeurIPS; senior author (h-index 117)  
   > Clinical drug development is a long-horizon, high-stakes process requiring sequential decisions based on information that costs money and time to acquire. AI agents have demonstrated capabilities for scientific analysis, but there is no established way to evaluate them on these…

14. **[LeCellModel: Interpretable Density Estimation over the Gene Expression Manifold](https://arxiv.org/abs/2611.30955)** — quality 51  
   Gil Karin, Artemii Bakulin, Nir Yosef · 2026-11-23  
   _why:_ multiple benchmarks; theory; mechanistic / causal analysis; accepted: NeurIPS; senior author (h-index 75)  
   > Representation learning for single-cell RNA-seq has been evaluated by the identities representations capture -- cell types, lineages, perturbations -- rather than how faithfully they model the distribution of cell states on the gene expression manifold. As a result, density…

15. **[OmniEVIE: Evidence-Vector-Informed Embedding for Multi-modal Retrieval](https://arxiv.org/abs/2611.32203)** — quality 48  
   Zifei Wang, Wei Wen, Qiang Ji et al. · 2026-11-24  
   _why:_ strong baselines; code released; weights/data released; 28 pages  
   > Multimodal retrieval must match dense pages, fine-grained entities, ordered video, and agent tools and memory. Single-vector embeddings lose local evidence, cross-encoders reread every recalled item online, and uncompressed late interaction is too large to serve. We present…

16. **[XMind: Thinking Twice via Cross-Memory Reasoning for LLM-Based Autonomous Driving](https://arxiv.org/abs/2611.32209)** — quality 48  
   Zuyi Guo, Xianjie Dai, Lei Yang et al. · 2026-11-24  
   _why:_ ablations; strong baselines; negative results / limitations; code released  
   > Memory-augmented large language model (LLM) driving agents can reuse past experience, yet previously learned corrections often fail to transfer when traffic conditions change. A key limitation is that existing memories mainly record observed outcomes, providing little evidence…

17. **[WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce](https://arxiv.org/abs/2611.30662)** — quality 50  
   Binhui Xie, Jinmin Li, Haomiao Tang et al. · 2026-11-23  
   _why:_ code released; weights/data released; HF daily papers: 55 upvotes  
   > We present WeMM-Ecom, a family of multimodal large language models that deliver frontier e-commerce capabilities while achieving state-of-the-art general-purpose performance at their respective scales. The family spans five sizes, from a 0.8B dense model to a 35B…

18. **[Residual Guidance for Real-Time Interactive Video Generation](https://arxiv.org/abs/2611.32820)** — quality 46  
   NaHyeon Park, Kyeong-Hwan Moon, Youjin Jeon et al. · 2026-11-24  
   _why:_ mechanistic / causal analysis; code released; HF daily papers: 6 upvotes  
   > Real-time interactive video generation allows users to change the prompt during generation to steer the evolving video. However, existing streaming models, which generate videos chunk by chunk, often keep following the previous prompt after a switch. We trace this failure to…

19. **[SpecEngineeringBench: Evaluating Coding Agents as Autonomous Specification Engineers](https://arxiv.org/abs/2611.32973)** — quality 46  
   Xingjian Wang, Shijian Wang, Minghao Liu et al. · 2026-11-24  
   _why:_ code released; 31 pages; HF daily papers: 5 upvotes  
   > Autonomous specification engineering requires coding agents to translate functional requirements into executable tests and use the results to discover and validate defects. However, existing benchmarks evaluate coding agents on explicitly specified test generation tasks,…

20. **[Reliable and grounded reporting of any computed tomography scan with FORA](https://arxiv.org/abs/2611.32823)** — quality 46  
   Sezgin Er, Utku Turkbey, Alperen Gur et al. · 2026-11-24  
   _why:_ mechanistic / causal analysis; contamination check; code released; 58 pages; 24-author team  
   > Artificial intelligence systems for computed tomography (CT) remain largely restricted to specific anatomical regions, examination types or predefined abnormalities, limiting their ability to provide comprehensive and spatially grounded interpretations. Here we present FORA, a…

21. **[MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction](https://arxiv.org/abs/2611.32462)** — quality 46  
   Yifan Dai, Daili Hua, Bohan Zeng et al. · 2026-11-24  
   _why:_ negative results / limitations; HF daily papers: 12 upvotes; 18-author team  
   > Multi-reference image generation requires a model to preserve the appearance of selected subjects while arranging them according to an instruction. Despite recent progress in reference-based generation and compositional control, reliably organizing selected subjects into the…

22. **[Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control](https://arxiv.org/abs/2611.29897)** — quality 51  
   Yue Huang, Tianshan Zhang, Zeyu Zhang et al. · 2026-11-23  
   _why:_ code released; HF daily papers: 194 upvotes  
   > Long-horizon, real-time controllable motion generation is essential for interactive animation and humanoid robotics, where an agent must respond to changing instructions and spatial goals while moving. Existing autoregressive diffusion methods generate motion incrementally, but…

23. **[Single-Transformer Latent Diffusion](https://arxiv.org/abs/2611.29064)** — quality 55  
   Hao-Yu Hsu, Shenlong Wang, Alexander G. Schwing · 2026-11-21  
   _why:_ negative results / limitations; code released; HF daily papers: 16 upvotes; senior author (h-index 69)  
   > Latent generative models typically rely on three separate networks: an encoder that tokenizes pixels, a generator that models the latent distribution, and a decoder that maps latents back to pixels. UNITE recently merged the first two into a single generative encoder trained in…

24. **[C3H: Compression-to-Consensus Criteria Hijacking in Multimodal LLM Recommender Systems](https://arxiv.org/abs/2611.32780)** — quality 46  
   Guowei Guan, Yurong Hao, Jiaming Zhang et al. · 2026-11-24  
   _why:_ mechanistic / causal analysis; code released; accepted: NeurIPS  
   > Multimodal large language models (MLLMs) are transforming recommender systems into content-aware decision systems. In these systems, multimodal compression and cross-modal fusion are often viewed as robustness-enhancing mechanisms against content manipulation, as compression can…

25. **[PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement](https://arxiv.org/abs/2611.32554)** — quality 46  
   Yang Cao, Zhe Zhu, Yiheng Zhang et al. · 2026-11-24  
   _why:_ code released; HF daily papers: 31 upvotes  
   > Segmenting a 3D object into semantically meaningful parts requires joint reasoning about geometric structure and semantic context. Pretrained 3D experts provide spatially grounded region proposals, while 2D experts provide semantic cues for identifying object parts. The…


## Blog posts & lab write-ups (last 14 days)

1. **[Building stronger biological reasoning models](https://www.goodfire.ai/research/building-stronger-biological-reasoning-models)** — quality 66  
   Goodfire Research · 2026-11-24  
   _why:_ strong baselines; variance / significance; mechanistic / causal analysis; long-form (82k chars); source tier 1  
   > Working with NVIDIA and the Arc Institute, we used interpretability to improve how a multimodal biological reasoning model uses protein information and test the evidence behind its predictions.

2. **[Interpreting a recent acceleration in pretraining loss](https://metr.org/blog/2026-11-24-interpreting-a-recent-acceleration-in-pretraining-loss/)** — quality 57  
   METR · 2026-11-24  
   _why:_ model-scale sweep; contamination check; source tier 1  
   > OpenAI recently published the base-model log-perplexity of 13 models it has trained since GPT-3.5, measured on a fixed held-out dataset sourced from its own codebase. It shows a very striking acceleration in pretraining loss: since early 2026, it has been falling about seven…

3. **[AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure](https://metr.org/blog/2026-11-20-q4-2026-capability-update/)** — quality 75  
   METR · 2026-11-20  
   _why:_ strong baselines; variance / significance; reproduction / replication; negative results / limitations; contamination check; long-form (185k chars)  
   > Contents Overview 1 Background 2 Methodology 3 Results 4 Robustness Checks 5 Discussion 6 Acknowledgments Appendices A Difficulty Estimation and Baselining B Time Horizon Diagnostics C MCI Modelling Methodology D Limitations of IRT E MCI Robustness Checks F Estimating Lifecycle…

4. **[Supercharging transformer residual connections](https://research.google/blog/supercharging-transformer-residual-connections/)** — quality 59  
   Google Research · 2026-11-23  
   _why:_ strong baselines; mechanistic / causal analysis; negative results / limitations; source tier 2; shared on X by 1 account  
   > Algorithms & Theory

5. **[Pacing AI via Compute Reallocation](https://www.lesswrong.com/posts/dBEDh2WeZfhuiDnJ5/pacing-ai-via-compute-reallocation)** — quality 56  
   LessWrong (curated) · 2026-11-24  
   _why:_ strong baselines; mechanistic / causal analysis; reproduction / replication; negative results / limitations; long-form (33k chars); source tier 2  
   > This is a linkpost for pacing-ai.com . I encourage folks to read it via the site (which has interactive graphs and expandables), but we’ve copied the text here as well . We offer a concrete proposal for pacing the frontier. 1. Transparency: Verified Compute Allocation…

6. **[Plato’s Key](https://hazyresearch.stanford.edu/blog/2026-11-25-platos-key)** — quality 53  
   Hazy Research · 2026-11-25  
   _why:_ model-scale sweep; negative results / limitations; contamination check; source tier 2  
   > A rotation and one global scale, fit in closed form, let one LLM use another’s representations. We test the Platonic Representation Hypothesis on factual recall across 12 LLMs.

7. **[vLLM Day-0 Support for ERNIE 5.5 Flash Preview: Plugin Deployment and E2E Inference Acceleration](https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview)** — quality 56  
   vLLM · 2026-11-24  
   _why:_ reproduction / replication; code released; source tier 2; shared on X by 1 account  
   > vLLM supports Baidu's ERNIE 5.5 Flash Preview on day 0 through the vLLM-ERNIE plugin on the released vllm==0.32.0 wheel, with structure-aware kernel fusion, Fla

8. **[Sakana Namazu Small](/namazu-small/)** — quality 52  
   Sakana AI · 2026-11-24  
   _why:_ multiple benchmarks; weights/data released; source tier 1  
   > （English Announcement Below.） Sakana AIは本日、Sakana Namazu Smallを発表します。Sakana Namazu Smallは、NVIDIA®社のオープンモデルであるNVIDIA Nemotron™ 3 Nanoのベースモデル（事前学習モデル）に対して、継続事前学習から事後学習までを自社で行った、300億パラメータの大規模言語モデル（LLM）です。 Sakana Namazu…

9. **[Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections](https://alignment.anthropic.com/2026/neuron-basis-theory/)** — quality 58  
   Anthropic Alignment Science · 2026-11-23  
   _why:_ ablations; variance / significance; mechanistic / causal analysis; long-form (66k chars); source tier 1  
   > Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections Alignment Science Blog Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections Jasmine Shone 1,* , Lisa Dunlap 1 November 23, 2026 1 Anthropic * Work done as…

10. **[Skip the DRAM Tier: MoRI UMBP Runs the Agentic KV Cache on NVMe](https://vllm.ai/blog/2026-11-23-skip-the-dram-tier)** — quality 58  
   vLLM · 2026-11-23  
   _why:_ negative results / limitations; long-form (41k chars); source tier 2; shared on X by 1 account  
   > On AMD Instinct™ MI355X GPUs, a MoRI UMBP KV pool on NVMe matched a DRAM pool of the same size within 1% for Kimi-K3 on vLLM, and drives that hold a day of agen

11. **[GPT-6 models demonstrate intrinsic protein-design capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities)** — quality 50  
   OpenAI · 2026-11-24  
   _why:_ negative results / limitations; source tier 3; shared on X by 2 accounts; Hacker News: 1 submission, 295 points  
   > GPT-6 models design protein structures and sequences using reasoning and code. Lab tests found evidence of binding across five targets.

12. **[Comparing AI R&D compute caps and deployment lags](https://www.alignmentforum.org/posts/e758PJCpwAwyodvEj/comparing-ai-r-and-d-compute-caps-and-deployment-lags)** — quality 51  
   AI Alignment Forum · 2026-11-24  
   _why:_ strong baselines; mechanistic / causal analysis; source tier 2  
   > I’m publishing this a bit rougher than usual because it’s very pertinent to Evan Hubinger’s recent shortform , which advocates for blocking internal deployment as a pacing mechanism over compute reallocation (he mostly discusses it in the context of a risk-assessment-based…


## Shared on X, in newsletters & on HN/Reddit (last 14 days)

1. **[AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure](https://metr.org/blog/2026-11-20-q4-2026-capability-update/)** — quality 75  
   METR · 2026-11-20  
   _why:_ strong baselines; variance / significance; reproduction / replication; negative results / limitations; contamination check; long-form (185k chars)  
   > Contents Overview 1 Background 2 Methodology 3 Results 4 Robustness Checks 5 Discussion 6 Acknowledgments Appendices A Difficulty Estimation and Baselining B Time Horizon Diagnostics C MCI Modelling Methodology D Limitations of IRT E MCI Robustness Checks F Estimating Lifecycle…

2. **[Supercharging transformer residual connections](https://research.google/blog/supercharging-transformer-residual-connections/)** — quality 59  
   Google Research · 2026-11-23  
   _why:_ strong baselines; mechanistic / causal analysis; negative results / limitations; source tier 2; shared on X by 1 account  
   > Algorithms & Theory

3. **[vLLM Day-0 Support for ERNIE 5.5 Flash Preview: Plugin Deployment and E2E Inference Acceleration](https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview)** — quality 56  
   vLLM · 2026-11-24  
   _why:_ reproduction / replication; code released; source tier 2; shared on X by 1 account  
   > vLLM supports Baidu's ERNIE 5.5 Flash Preview on day 0 through the vLLM-ERNIE plugin on the released vllm==0.32.0 wheel, with structure-aware kernel fusion, Fla

4. **[OWE-Bench: A long-horizon benchmark for measuring real-world engineering](https://arxiv.org/abs/2611.30017)** — quality 59  
   Jacob Cole, Martin Dimakis, Victor Barres et al. · 2026-11-23  
   _why:_ negative results / limitations; code released; weights/data released; 35 pages; shared on X by 1 account  
   > We present OWE-Bench (OpenWorldEngineer-Bench), a benchmark of 26 long-horizon engineering tasks written by domain experts in software engineering, physical engineering, machine learning, and scientific computing. Tasks range from optimizing kernels and designing an aircraft, to…

5. **[Skip the DRAM Tier: MoRI UMBP Runs the Agentic KV Cache on NVMe](https://vllm.ai/blog/2026-11-23-skip-the-dram-tier)** — quality 58  
   vLLM · 2026-11-23  
   _why:_ negative results / limitations; long-form (41k chars); source tier 2; shared on X by 1 account  
   > On AMD Instinct™ MI355X GPUs, a MoRI UMBP KV pool on NVMe matched a DRAM pool of the same size within 1% for Kimi-K3 on vLLM, and drives that hold a day of agen

6. **[GPT-6 models demonstrate intrinsic protein-design capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities)** — quality 50  
   OpenAI · 2026-11-24  
   _why:_ negative results / limitations; source tier 3; shared on X by 2 accounts; Hacker News: 1 submission, 295 points  
   > GPT-6 models design protein structures and sequences using reasoning and code. Lab tests found evidence of binding across five targets.

7. **[Anthropic Residency: applications open for established technical leaders](https://alignment.anthropic.com/2026/anthropic-residency/)** — quality 58  
   Anthropic Alignment Science · 2026-11-22  
   _why:_ mechanistic / causal analysis; source tier 1; in newsletters: Don't Worry About the Vase (Zvi)  
   > Anthropic Residency: applications open for established technical leaders Alignment Science Blog Anthropic Residency: applications open for established technical leaders Today we are opening applications for the Anthropic Residency, our paid, fixed-term research program with…

8. **[The KL Divergence Is Never Negative, Except in PyTorch](https://arxiv.org/abs/2611.30835)** — quality 46  
   Zhen Yang, Wei Tang, Chu Chen et al. · 2026-11-23  
   _why:_ mechanistic / causal analysis; code released; Hacker News: 1 submission, 94 points  
   > A Kullback--Leibler (KL) divergence is never negative, yet PyTorch users have reported negative values for years, and the standard advice is to clamp them at zero. The sign is only the visible part of a silent failure. Many machine-learning applications compare nearby…

9. **[RoboUniverse-10K: Toward the Scaling Era of Agentic Robotics via Real-to-Sim Environments](https://arxiv.org/abs/2611.31002)** — quality 44  
   Jinkun Liu, Yingze Wang, Situ Wang et al. · 2026-11-23  
   _why:_ strong baselines; weights/data released; 24-author team; shared on X by 1 account  
   > Agentic Robotics, in which foundation models act as coding agents to control robots through executable programs, has emerged as a compelling paradigm for embodied intelligence. Yet unlike software engineering, where massive executable environments power post-training, robotics…

10. **[OpenAI and Cisco introduce Shirudo](https://openai.com/index/introducing-shirudo)** — quality 42  
   OpenAI · 2026-11-23  
   _why:_ source tier 3; shared on X by 1 account; Hacker News: 1 submission, 85 points; in newsletters: The Rundown AI  
   > OpenAI and Cisco introduce Shirudo, an open-source runtime for Linux. It helps teams protect running systems while they roll out patches.

11. **[Combatting adversarial distillation](https://openai.com/index/combatting-adversarial-distillation)** — quality 52  
   OpenAI · 2026-11-20  
   _why:_ strong baselines; reproduction / replication; source tier 3; shared on X by 1 account; Hacker News: 1 submission, 34 points; in newsletters: The Rundown AI  
   > OpenAI’s layered approach to adversarial distillation combines model training, safeguards, detection, and enforcement to protect against capability extraction.

12. **[Introducing Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/)** — quality 52  
   thinkingmachines.ai · 2026-11-20  
   _why:_ strong baselines; mechanistic / causal analysis; negative results / limitations; long-form (34k chars); source tier 3; shared on X by 9 accounts ⚠ hype: agi  
   > Inkling 2 Mini is an open-weights model small enough to run on your laptop. It loops its middle layers to reason more per token and reach answers in fewer tokens.
