# paper-taste digest — 2026-11-14

Ranked by heuristic quality × recency (10-day half-life). Scores are a first pass from metadata and abstracts; see [TASTE.md](TASTE.md) for the rubric an agent applies on top, and [AGENTS.md](AGENTS.md) to get recommendations matched to your own repos.

## Papers (last 7 days, 2356 kept in the last 14)

1. **[TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models](https://arxiv.org/abs/2611.17331)** — quality 58  
   Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe et al. · 2026-11-12  
   _why:_ multiple benchmarks; code released; accepted: NeurIPS; HF daily papers: 21 upvotes  
   > Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We…

2. **[SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models](https://arxiv.org/abs/2611.15777)** — quality 60  
   Lichen Li, Ziping Dong, Sicheng Feng et al. · 2026-11-11  
   _why:_ multiple benchmarks; negative results / limitations; code released; 32 pages; HF daily papers: 83 upvotes  
   > System One models promise fast, general-purpose decision-making without lengthy token generation. However, understanding their capability spectrum and decision reliability requires more than aggregate performance on current benchmarks. Existing evaluations often provide limited…

3. **[Bellman Contraction under MMD: A Unified Framework](https://arxiv.org/abs/2611.17116)** — quality 52  
   Baptiste Debes, Tinne Tuytelaars · 2026-11-12  
   _why:_ theory; code released; accepted: NeurIPS; 88 pages; senior author (h-index 78)  
   > We introduce a mathematical framework for studying contraction of the distributional Bellman operator under Maximum Mean Discrepancy (MMD). We show that contraction reduces to conditional positive definiteness of an associated kernel constructed from the base kernel, which we…

4. **[Open Vision Banana: A Fully Open Recipe for Generative Visual Perception](https://arxiv.org/abs/2611.15844)** — quality 54  
   Arpit Jadon, Valentinos Pariza, Jona Ruthardt et al. · 2026-11-11  
   _why:_ ablations; weights/data released; code released; HF daily papers: 32 upvotes  
   > Recent work suggests that pretrained image generators encode real-world understanding beyond image synthesis. Vision Banana exploits this by framing vision tasks as conditional image editing. However, its data, weights, code, and implementation details are not public. We present…

5. **[Factored One-sided Adam-Moment for Practical and Scalable SOAP](https://arxiv.org/abs/2611.16905)** — quality 51  
   Jaemyung Yu, Byeongho Heo, Sangdoo Yun et al. · 2026-11-12  
   _why:_ strong baselines; model-scale sweep; code released; HF daily papers: 12 upvotes  
   > Second-order optimizers (e.g., Shampoo, SOAP) have emerged as compelling alternatives to Adam/AdamW and promise faster per-step convergence than AdamW in transformer training. However, they still remain costly in practice, and even SOAP still pays substantial optimizer-state…

6. **[Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors](https://arxiv.org/abs/2611.17060)** — quality 50  
   Hao Li, Fangzhou Hong, Zhaoxi Chen et al. · 2026-11-12  
   _why:_ model-scale sweep; code released; HF daily papers: 26 upvotes; 21-author team  
   > Large foundation models such as GPT-6 Astra and Claude Fable 5.1 have recently been shown to control robots directly from visual observations. They nevertheless remain brittle on long-horizon, contact-rich tasks in real-world environments. Further progress depends on two…

7. **[Unbundling Multimodal Vision Encoding](https://arxiv.org/abs/2611.17334)** — quality 49  
   Ellis Brown, Chris Hoang, Shengyi Qian et al. · 2026-11-12  
   _why:_ controlled experiments; HF daily papers: 13 upvotes; senior author (h-index 40); shared on X by 1 account  
   > How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design…

8. **[Detection Is Not Early Warning: Evaluating Token-Level Alarms on Language Model Failures](https://arxiv.org/abs/2611.16803)** — quality 49  
   Marco De Negri, Luca Sartori, Lorenzo Baggi et al. · 2026-11-12  
   _why:_ strong baselines; mechanistic / causal analysis; code released; weights/data released; accepted: NeurIPS workshop; 30 pages  
   > Many failures of language models begin at a specific token, the onset. A monitor that reads the model during generation can classify the finished response, detect the failure once it is under way, or warn before it begins, and only a warning leaves time to stop or steer the…

9. **[SWAM: Scaling World Action Models with Cross-Modal Alignment](https://arxiv.org/abs/2611.12870)** — quality 60  
   Yu Zhou, Xinyuan Xia, Xuankun Yang et al. · 2026-11-09  
   _why:_ strong baselines; mechanistic / causal analysis; controlled experiments; code released; weights/data released; HF daily papers: 22 upvotes  
   > World action models jointly predict video and actions conditioned on language. Existing studies focus primarily on architectures and training mechanisms, typically treating language-video alignment acquired through video pretraining as an established foundation. However,…

10. **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320)** — quality 56  
   Yukyeong Lee, Yumin Choi, Jinheon Baek et al. · 2026-11-10  
   _why:_ strong baselines; code released; HF daily papers: 66 upvotes; shared on X by 1 account  
   > External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it…

11. **[Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery](https://arxiv.org/abs/2611.12762)** — quality 59  
   Weida Wang, Benteng Chen, Yigeng Jiang et al. · 2026-11-09  
   _why:_ strong baselines; code released; 38 pages; HF daily papers: 57 upvotes; 90-author team  
   > We introduce Sage-Taiyi, a metacognition-inspired architecture that uses accumulated scientific understanding to guide what to investigate next and how to investigate it. Through explicit monitoring and control, the system revises its understanding of evidence, assumptions, and…

12. **[Verifier Choice is a Benchmark Design Variable: Auditing Structural Counting Evaluation in Text-to-Image Models](https://arxiv.org/abs/2611.15433)** — quality 51  
   Shurun Li, Michael Hua Wang, Haibo Zeng et al. · 2026-11-11  
   _why:_ strong baselines; controlled experiments; code released; weights/data released; accepted: NeurIPS  
   > Automatic evaluation is now central to text-to-image benchmarking, but the verifier that converts generated images into scores is often treated as an implementation detail. We argue that this is unsafe: an automatic benchmark score is a property of the image generator, prompt…

13. **[Consensus Capture in Reference-Based UAV Video Stabilization: A Benchmark on Dynamic Urban Scenes](https://arxiv.org/abs/2611.17190)** — quality 46  
   Robert Fonod, Nikolas Geroliminis · 2026-11-12  
   _why:_ code released; 50 pages; HF daily papers: 3 upvotes; senior author (h-index 49)  
   > Reference-frame stabilization registers every frame of a hovering-drone video onto one reference frame, keeping object positions comparable. The registration pipelines it relies on are selected on feature-matching benchmarks in which only the camera moves. Over a busy…

14. **[PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](https://arxiv.org/abs/2611.16748)** — quality 47  
   Yuxuan Chen, Xiaojie Li, Hao Chen et al. · 2026-11-12  
   _why:_ weights/data released; code released; HF daily papers: 44 upvotes  
   > Video generation models produce visually realistic videos but still struggle with physical dynamics and causal consistency. Learning from generated videos requires fine-grained physical supervision, yet reliable quality judgments, correction pairs, and controlled variations are…

15. **[WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory Learning](https://arxiv.org/abs/2611.12527)** — quality 57  
   Sang-Hoon Lee, Ha-Yeong Choi · 2026-11-09  
   _why:_ model-scale sweep; code released; accepted: NeurIPS; HF daily papers: 17 upvotes  
   > This work proposes WaveGen, a fully end-to-end diffusion-based text-to-waveform framework based on Spectral Forcing, which jointly learns an internal spectral trajectory and the target waveform trajectory within a single model, enabling direct end-to-end text-to-waveform…

16. **[Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://arxiv.org/abs/2611.12304)** — quality 57  
   Hao Kang, Weili Xu, Ziyang Li et al. · 2026-11-09  
   _why:_ negative results / limitations; code released; weights/data released; HF daily papers: 12 upvotes; senior author (h-index 45)  
   > Agentic workloads are a major source of LLM inference demand. Existing prefill--decode (PD) disaggregated serving systems offer limited flexibility for runtime adaptation of compute allocation and KV cache management, and rely on coarse signals that only partly capture the…

17. **[Are Dense Rewards Worth Their Tokens in GRPO?](https://arxiv.org/abs/2611.13560)** — quality 54  
   Vikash Singh, Weicong Chen, Debargha Ganguly et al. · 2026-11-10  
   _why:_ reproduction / replication; code released; 59 pages; HF daily papers: 5 upvotes; 19-author team  
   > RLVR trains language models to reason by rewarding correct final answers. A widely used algorithm, group-relative policy optimization (GRPO), gives every token of a solution the same credit, so dense process rewards have been proposed to credit intermediate steps, for example…

18. **[Predicting the Needle in a Petabyte Scale Haystack: Open-Vocabulary Event Anticipation in Satellite Imagery](https://arxiv.org/abs/2611.16000)** — quality 48  
   Shreelekha Revankar, Mikhail Klassen, Creon Levit et al. · 2026-11-11  
   _why:_ strong baselines; code released; accepted: NeurIPS; 29 pages  
   > Satellite constellations now image the Earth daily, capturing the lifecycle of events from deforestation to urban construction. Anticipating these events before completion enables timely intervention, yet existing systems cannot jointly identify where a change occurs, what it…

19. **[RipBench: A Unified Benchmark for Multi-Level Rip Current Detection, Classification and Segmentation](https://arxiv.org/abs/2611.15574)** — quality 48  
   Andrei Dumitriu, Aakash Ralhan, Florin Miron et al. · 2026-11-11  
   _why:_ strong baselines; variance / significance; accepted: NeurIPS; 47 pages; senior author (h-index 107)  
   > Rip currents are a serious and often under-addressed threat to beach safety and the leading cause of coastal drownings worldwide. They are difficult to detect due to their amorphous structure, similarity to the background, and large variability in viewpoints and environments.…

20. **[Market-Conditioned JEPA: Learning from Unpredictable Market Shocks](https://arxiv.org/abs/2611.13572)** — quality 53  
   Yuqi Wang, Fengyuan Liu, Mukai Li et al. · 2026-11-10  
   _why:_ ablations; strong baselines; variance / significance; code released; HF daily papers: 5 upvotes  
   > Much of the variation in financial time series is driven by market-wide shocks that cannot be predicted from an asset's own history. Per-asset self-supervised learning treats this variation as irreducible noise. Under a latent factor model, we show that conditioning prediction…

21. **[Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://arxiv.org/abs/2611.14210)** — quality 52  
   Hadi Salloum, Ammar Ali · 2026-11-10  
   _why:_ variance / significance; code released; HF daily papers: 45 upvotes  
   > Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million…

22. **[JustRUA: A Controlled Study of GPT-6 Robot-Use Agents](https://arxiv.org/abs/2611.16009)** — quality 47  
   Zefan Wang, Yufan Dang, Xuanwei Shi et al. · 2026-11-11  
   _why:_ controlled experiments; code released; 30 pages; HF daily papers: 4 upvotes  
   > GPT-6 Astra can drive a robot arm directly through a fixed harness, and scores of such robot-use agents on RoboDojo have risen quickly since. Reported systems differ in harness and test subset and often change several designs at once, so it is hard to tell which choices produce…

23. **[Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents](https://arxiv.org/abs/2611.17167)** — quality 44  
   Haochen Liu, Qianhao Zhu, Zixuan Wang et al. · 2026-11-12  
   _why:_ code released; HF daily papers: 30 upvotes; shared on X by 1 account  
   > Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has…

24. **[MoE Pretraining:Parallelism Layout Changes the Model, Not Quality](https://arxiv.org/abs/2611.15271)** — quality 48  
   Esther Xin · 2026-11-11  
   _why:_ ablations; model-scale sweep; code released; weights/data released  
   > Large Mixture-of-Experts (MoE) models are trained across many machines, and the way the work is split, the parallelism layout, often changes between runs: a job resumes on a different GPU count, a cluster is resized, or an ablation runs on a new setup. In exact arithmetic the…

25. **[EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming](https://arxiv.org/abs/2611.16728)** — quality 44  
   Yaru Niu, Binghong Chen, Changwei Yao et al. · 2026-11-12  
   _why:_ ablations; code released; HF daily papers: 1 upvotes; 22-author team  
   > Generalist manipulation policies can benefit from the complementary experience of humans, real robots, and simulated agents. However, differences in morphology, sensing, and control interfaces make it difficult to learn effectively from their combined demonstrations. We…


## Blog posts & lab write-ups (last 14 days)

1. **[End‑to‑End 4‑Bit Training](https://thinkingmachines.ai/blog/end-to-end-4-bit-training/)** — quality 75  
   Thinking Machines · 2026-11-13  
   _why:_ model-scale sweep; controlled experiments; negative results / limitations; long-form (26k chars); source tier 1; shared on X by 3 accounts  
   > Training large language models involves calculating and storing a lot of numbers. Using fewer bits for each value reduces memory usage and allows GPUs to perform calculations faster. However, there is a tradeoff: fewer bits also mean fewer representable numbers, leading to more…

2. **[Building strong safety evaluations](https://www.anthropic.com/research/building-strong-safety-evaluations)** — quality 73  
   Anthropic Research · 2026-11-13  
   _why:_ strong baselines; variance / significance; reproduction / replication; contamination check; long-form (30k chars); source tier 1  
   > Recommendations for designing, running, and reporting safety evaluations, based on our own experiences.

3. **[Advancing science & engineering with Antigravity’s /teamwork](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/)** — quality 59  
   Google Research · 2026-11-13  
   _why:_ theory; mechanistic / causal analysis; source tier 2; shared on X by 1 account  
   > Education Innovation

4. **[AI agents attempted exploits on our website](https://epoch.ai/publications/incident-report-ai-agents-attempted-exploits-on-our-website)** — quality 62  
   Epoch AI (Publications) · 2026-11-13  
   _why:_ reproduction / replication; source tier 1; shared on X by 1 account  
   > Three October 2026 events involving Trajectory Labs, PBC, in which agents probed our site and impersonated staff. No private data was accessed.

5. **[Anthropic Residency: applications open for established technical leaders](https://alignment.anthropic.com/2026/anthropic-residency/)** — quality 54  
   Anthropic Alignment Science · 2026-11-22  
   _why:_ mechanistic / causal analysis; source tier 1  
   > Anthropic Residency: applications open for established technical leaders Alignment Science Blog Anthropic Residency: applications open for established technical leaders Today we are opening applications for the Anthropic Residency, our paid, fixed-term research program with…

6. **[Neurons as an Interpretable Basis](https://www.goodfire.ai/research/neurons-as-an-interpretable-basis)** — quality 68  
   Goodfire Research · 2026-11-10  
   _why:_ ablations; strong baselines; mechanistic / causal analysis; contamination check; long-form (425k chars); source tier 1  
   > Neural networks have long been regarded as opaque black boxes, in part because their neurons seemed inscrutable. This article makes the case that language model neurons—the hidden units of MLPs—are interpretable units of computation.

7. **[Worse Together: How Performance Breaks Down in Multi-User Multi-Agent Teams](https://alignment.anthropic.com/2026/worse-together/)** — quality 61  
   Anthropic Alignment Science · 2026-11-11  
   _why:_ variance / significance; negative results / limitations; source tier 1  
   > Anthropic Fellows Blog: When several users each delegate to their own agent and those agents share a resource, group outcomes are worse than when one agent serves everyone, and the agents show problematic behaviors that vary by model and environment.

8. **[Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs](http://unemploymentlabs.com/checkpoint-forensics)** — quality 57  
   unemploymentlabs.com · 2026-11-12  
   _why:_ reproduction / replication; negative results / limitations; weights/data released; long-form (38k chars); source tier 3; shared on X by 3 accounts  
   > Our forensic analysis of publicly released AI models finds evidence that DeepSeek, Moonshot AI, MiniMax and Ant Group have gained access to NVIDIA’s Blackwell GPUs, despite restrictions on exporting these chips to China, and are using that hardware to create their AI models.

9. **[Claude can design electronic prototypes from start to finish](https://www.anthropic.com/research/claude-electronics-design)** — quality 66  
   Anthropic Research · 2026-11-09  
   _why:_ mechanistic / causal analysis; negative results / limitations; source tier 1; Hacker News: 1 submission, 35 points  
   > We asked Claude to design three electronic devices: a speakerphone, a voice-assistant hub, and a handheld virtual pet. The prototypes worked without any fixes to their circuitry.

10. **[The fall of “what you can do” and the rise of “who you know”](https://www.jasonwei.net/blog/the-fall-of-what-you-can-do-and-the-rise-of-who-you-know)** — quality 53  
   Jason Wei · 2026-11-11  
   _why:_ mechanistic / causal analysis; source tier 1  
   > Traditionally, many of us believe in a world where how hard you work is more important than who you know. I used to subscribe to this idea as both a scientist, who believed that facts about our world are agnostic to who says them, and as an American, who grew up believing that…

11. **[Using wearables to enable cardiovascular-kidney-metabolic (CKM) risk profiling for personalized coaching](https://research.google/blog/using-wearables-to-enable-cardiovascular-kidney-metabolic-ckm-risk-profiling-for-personalized-coaching/)** — quality 52  
   Google Research · 2026-11-11  
   _why:_ strong baselines; mechanistic / causal analysis; human evaluation; source tier 2  
   > Health & Bioscience

12. **[Faster Scientific Simulations with New FP64 Algorithms in NVIDIA cuBLAS](https://developer.nvidia.com/blog/faster-scientific-simulations-with-new-fp64-algorithms-in-nvidia-cublas/)** — quality 45  
   NVIDIA Technical Blog · 2026-11-13  
   _why:_ model-scale sweep; theory; source tier 3  
   > Many scientific simulations, from molecular chemistry to materials science, spend the majority of their execution time computing high-precision dense general...


## Shared on X, in newsletters & on HN/Reddit (last 14 days)

1. **[End‑to‑End 4‑Bit Training](https://thinkingmachines.ai/blog/end-to-end-4-bit-training/)** — quality 75  
   Thinking Machines · 2026-11-13  
   _why:_ model-scale sweep; controlled experiments; negative results / limitations; long-form (26k chars); source tier 1; shared on X by 3 accounts  
   > Training large language models involves calculating and storing a lot of numbers. Using fewer bits for each value reduces memory usage and allows GPUs to perform calculations faster. However, there is a tradeoff: fewer bits also mean fewer representable numbers, leading to more…

2. **[Building strong safety evaluations](https://www.anthropic.com/research/building-strong-safety-evaluations)** — quality 73  
   Anthropic Research · 2026-11-13  
   _why:_ strong baselines; variance / significance; reproduction / replication; contamination check; long-form (30k chars); source tier 1  
   > Recommendations for designing, running, and reporting safety evaluations, based on our own experiences.

3. **[Advancing science & engineering with Antigravity’s /teamwork](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/)** — quality 59  
   Google Research · 2026-11-13  
   _why:_ theory; mechanistic / causal analysis; source tier 2; shared on X by 1 account  
   > Education Innovation

4. **[AI agents attempted exploits on our website](https://epoch.ai/publications/incident-report-ai-agents-attempted-exploits-on-our-website)** — quality 62  
   Epoch AI (Publications) · 2026-11-13  
   _why:_ reproduction / replication; source tier 1; shared on X by 1 account  
   > Three October 2026 events involving Trajectory Labs, PBC, in which agents probed our site and impersonated staff. No private data was accessed.

5. **[Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs](http://unemploymentlabs.com/checkpoint-forensics)** — quality 57  
   unemploymentlabs.com · 2026-11-12  
   _why:_ reproduction / replication; negative results / limitations; weights/data released; long-form (38k chars); source tier 3; shared on X by 3 accounts  
   > Our forensic analysis of publicly released AI models finds evidence that DeepSeek, Moonshot AI, MiniMax and Ant Group have gained access to NVIDIA’s Blackwell GPUs, despite restrictions on exporting these chips to China, and are using that hardware to create their AI models.

6. **[Claude can design electronic prototypes from start to finish](https://www.anthropic.com/research/claude-electronics-design)** — quality 66  
   Anthropic Research · 2026-11-09  
   _why:_ mechanistic / causal analysis; negative results / limitations; source tier 1; Hacker News: 1 submission, 35 points  
   > We asked Claude to design three electronic devices: a speakerphone, a voice-assistant hub, and a handheld virtual pet. The prototypes worked without any fixes to their circuitry.

7. **[Unbundling Multimodal Vision Encoding](https://arxiv.org/abs/2611.17334)** — quality 49  
   Ellis Brown, Chris Hoang, Shengyi Qian et al. · 2026-11-12  
   _why:_ controlled experiments; HF daily papers: 13 upvotes; senior author (h-index 40); shared on X by 1 account  
   > How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design…

8. **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320)** — quality 56  
   Yukyeong Lee, Yumin Choi, Jinheon Baek et al. · 2026-11-10  
   _why:_ strong baselines; code released; HF daily papers: 66 upvotes; shared on X by 1 account  
   > External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it…

9. **[AlphaGenome 2: Deciphering how cells read DNA to better understand disease](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)** — quality 51  
   Google DeepMind · 2026-11-11  
   _why:_ source tier 2; shared on X by 1 account; in newsletters: The Rundown AI  
   > Predicting how DNA sequences and their variations impact specific human cell types and disease.

10. **[Training a 1T-Parameter MoE on EU public infrastructure with PyTorch and TorchTitan](https://pytorch.org/blog/training-a-1t-parameter-moe-on-eu-public-infrastructure-with-pytorch-and-torchtitan/)** — quality 47  
   PyTorch · 2026-11-12  
   _why:_ strong baselines; reproduction / replication; source tier 3; Reddit: 2 submissions  
   > TL;DR Scaling pretraining for a ~1-trillion-parameter Mixture-of-Experts (MoE) model on shared, public infrastructure was previously considered unfeasible due to unique architectural and interconnect bottlenecks. However, by leveraging the fine-grained flexibility... The post…

11. **[Qwen3.8](https://unsloth.ai/docs/models/qwen3.8#exllama-v3-considerations)** — quality 49  
   unsloth.ai · 2026-11-11  
   _why:_ source tier 3; shared on X by 1 account; Hacker News: 1 submission, 149 points; Reddit: 1 submission; in newsletters: AINews  
   > Guide to running Qwen3.8 quants including Qwen3.8-27B on your local setup.

12. **[Introducing Gemini 4 Hydrogen for Agentic Workflows](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)** — quality 47  
   blog.google · 2026-11-12  
   _why:_ source tier 3; shared on X by 2 accounts; Hacker News: 1 submission, 533 points; in newsletters: The Rundown AI  
   > Google introduces Gemini 4 Hydrogen, a fast, cost-efficient model built for reliable agentic workflows and everyday tasks. Get the details.
