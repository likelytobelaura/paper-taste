# paper-taste digest — 2026-11-13

Ranked by heuristic quality × recency (10-day half-life). Scores are a first pass from metadata and abstracts; see [TASTE.md](TASTE.md) for the rubric an agent applies on top, and [AGENTS.md](AGENTS.md) to get recommendations matched to your own repos.

## Papers (last 7 days, 2552 kept in the last 14)

1. **[TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models](https://arxiv.org/abs/2611.17331)** — quality 62  
   Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe et al. · 2026-11-12  
   _why:_ multiple benchmarks; code released; accepted: NeurIPS; HF daily papers: 18 upvotes  
   > Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We…

2. **[SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models](https://arxiv.org/abs/2611.15777)** — quality 64  
   Lichen Li, Ziping Dong, Sicheng Feng et al. · 2026-11-11  
   _why:_ multiple benchmarks; negative results / limitations; code released; 32 pages; HF daily papers: 46 upvotes  
   > System One models promise fast, general-purpose decision-making without lengthy token generation. However, understanding their capability spectrum and decision reliability requires more than aggregate performance on current benchmarks. Existing evaluations often provide limited…

3. **[Factored One-sided Adam-Moment for Practical and Scalable SOAP](https://arxiv.org/abs/2611.16905)** — quality 56  
   Jaemyung Yu, Byeongho Heo, Sangdoo Yun et al. · 2026-11-12  
   _why:_ strong baselines; model-scale sweep; code released; HF daily papers: 11 upvotes  
   > Second-order optimizers (e.g., Shampoo, SOAP) have emerged as compelling alternatives to Adam/AdamW and promise faster per-step convergence than AdamW in transformer training. However, they still remain costly in practice, and even SOAP still pays substantial optimizer-state…

4. **[Verifier Choice is a Benchmark Design Variable: Auditing Structural Counting Evaluation in Text-to-Image Models](https://arxiv.org/abs/2611.15433)** — quality 57  
   Shurun Li, Michael Hua Wang, Haibo Zeng et al. · 2026-11-11  
   _why:_ strong baselines; controlled experiments; code released; weights/data released; accepted: NeurIPS  
   > Automatic evaluation is now central to text-to-image benchmarking, but the verifier that converts generated images into scores is often treated as an implementation detail. We argue that this is unsafe: an automatic benchmark score is a property of the image generator, prompt…

5. **[Open Vision Banana: A Fully Open Recipe for Generative Visual Perception](https://arxiv.org/abs/2611.15844)** — quality 56  
   Arpit Jadon, Valentinos Pariza, Jona Ruthardt et al. · 2026-11-11  
   _why:_ ablations; weights/data released; code released; HF daily papers: 12 upvotes  
   > Recent work suggests that pretrained image generators encode real-world understanding beyond image synthesis. Vision Banana exploits this by framing vision tasks as conditional image editing. However, its data, weights, code, and implementation details are not public. We present…

6. **[Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors](https://arxiv.org/abs/2611.17060)** — quality 52  
   Hao Li, Fangzhou Hong, Zhaoxi Chen et al. · 2026-11-12  
   _why:_ model-scale sweep; code released; HF daily papers: 15 upvotes; 21-author team  
   > Large foundation models such as GPT-6 Astra and Claude Fable 5.1 have recently been shown to control robots directly from visual observations. They nevertheless remain brittle on long-horizon, contact-rich tasks in real-world environments. Further progress depends on two…

7. **[PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](https://arxiv.org/abs/2611.16748)** — quality 50  
   Yuxuan Chen, Xiaojie Li, Hao Chen et al. · 2026-11-12  
   _why:_ weights/data released; code released; HF daily papers: 30 upvotes  
   > Video generation models produce visually realistic videos but still struggle with physical dynamics and causal consistency. Learning from generated videos requires fine-grained physical supervision, yet reliable quality judgments, correction pairs, and controlled variations are…

8. **[Detection Is Not Early Warning: Evaluating Token-Level Alarms on Language Model Failures](https://arxiv.org/abs/2611.16803)** — quality 50  
   Marco De Negri, Luca Sartori, Lorenzo Baggi et al. · 2026-11-12  
   _why:_ strong baselines; mechanistic / causal analysis; code released; weights/data released; accepted: NeurIPS workshop; 30 pages  
   > Many failures of language models begin at a specific token, the onset. A monitor that reads the model during generation can classify the finished response, detect the failure once it is under way, or warn before it begins, and only a warning leaves time to stop or steer the…

9. **[MoE Pretraining:Parallelism Layout Changes the Model, Not Quality](https://arxiv.org/abs/2611.15271)** — quality 54  
   Esther Xin · 2026-11-11  
   _why:_ ablations; model-scale sweep; code released; weights/data released  
   > Large Mixture-of-Experts (MoE) models are trained across many machines, and the way the work is split, the parallelism layout, often changes between runs: a job resumes on a different GPU count, a cluster is resized, or an ablation runs on a new setup. In exact arithmetic the…

10. **[SWAM: Scaling World Action Models with Cross-Modal Alignment](https://arxiv.org/abs/2611.12870)** — quality 60  
   Yu Zhou, Xinyuan Xia, Xuankun Yang et al. · 2026-11-09  
   _why:_ strong baselines; mechanistic / causal analysis; controlled experiments; code released; weights/data released; HF daily papers: 22 upvotes  
   > World action models jointly predict video and actions conditioned on language. Existing studies focus primarily on architectures and training mechanisms, typically treating language-video alignment acquired through video pretraining as an established foundation. However,…

11. **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320)** — quality 56  
   Yukyeong Lee, Yumin Choi, Jinheon Baek et al. · 2026-11-10  
   _why:_ strong baselines; code released; HF daily papers: 65 upvotes; shared on X by 1 account  
   > External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it…

12. **[CADET: Construction of PCB Routing Instances with Executable Demonstrations](https://arxiv.org/abs/2611.16913)** — quality 48  
   Hyungseok Song, Won-Seok Choi, Seohui Bae et al. · 2026-11-12  
   _why:_ strong baselines; mechanistic / causal analysis; code released; weights/data released; 28 pages  
   > Printed circuit board (PCB) routing is the stage of physical layout that finds paths connecting the placed pads of each net. Public datasets in this domain are few, and most contain only the final states of routed boards, not demonstrations of the electronic design automation…

13. **[Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery](https://arxiv.org/abs/2611.12762)** — quality 59  
   Weida Wang, Benteng Chen, Yigeng Jiang et al. · 2026-11-09  
   _why:_ strong baselines; code released; 38 pages; HF daily papers: 57 upvotes; 90-author team  
   > We introduce Sage-Taiyi, a metacognition-inspired architecture that uses accumulated scientific understanding to guide what to investigate next and how to investigate it. Through explicit monitoring and control, the system revises its understanding of evidence, assumptions, and…

14. **[Maximizing Capacity Utilization of LoRA Adapters for Mitigating the Learning-Forgetting Trade-off](https://arxiv.org/abs/2611.17191)** — quality 47  
   Tomohiro Sawada, Kartik Goyal · 2026-11-12  
   _why:_ variance / significance; mechanistic / causal analysis; negative results / limitations; code released  
   > Low-Rank Adaptation (LoRA) often underperforms full fine-tuning, especially in heterogeneous and continual-learning settings in which substantial forgetting occurs. In general, it suffers from an undesirable learning-forgetting trade-off across diverse fine-tuning settings. We…

15. **[Kezek: Splitting Mono Two-Person Conversations into Per-Speaker Tracks for Full-Duplex Dialogue Data](https://arxiv.org/abs/2611.16933)** — quality 47  
   Bagzhan Karl, Alizhan Karl · 2026-11-12  
   _why:_ negative results / limitations; contamination check; code released; weights/data released  
   > Full-duplex spoken dialogue models learn turn-taking, overlaps and backchannels from conversations recorded with one channel per speaker, but most available conversational audio is a single mono mix. We present Kezek, a model that turns a mono recording of exactly two people…

16. **[Discovering Effective Agent Memory Designs through Program Evolution](https://arxiv.org/abs/2611.17068)** — quality 47  
   Xinheng Ding, Seyyed Saeid Cheshmi, Ziyang Zhang et al. · 2026-11-12  
   _why:_ ablations; strong baselines; code released  
   > Program evolution provides a promising approach to discover agent memory designs and study the choices underlying their effectiveness. We introduce MAPE, a framework that evolves whole memory programs from minimal seeds through a standardized lifecycle interface and an iterative…

17. **[FLEX-LBP: Learning Local Binary Patterns with Exact Binary Inference for Texture Classification](https://arxiv.org/abs/2611.17302)** — quality 47  
   Mohamed Alimoussa, Amal El Kaid · 2026-11-12  
   _why:_ ablations; mechanistic / causal analysis; code released  
   > Local Binary Patterns (LBP) remain among the most widely used texture descriptors, from industrial inspection to medical imaging. Yet their radius, sampling angles, color transform and thresholds are fixed by hand for each dataset. We present FLEX-LBP, which learns these…

18. **[From Link Prediction to Linear Community Detection: A Finite-Sample Guarantee for Graph Pretraining](https://arxiv.org/abs/2611.15778)** — quality 50  
   Ying Chen, Zhangyang Wang, Yixuan He · 2026-11-11  
   _why:_ theory; contamination check; code released; accepted: NeurIPS; 47 pages  
   > Link prediction (LP) is a standard pretraining objective for graph neural networks (GNNs): hide edges, train an encoder-decoder to predict them, and reuse the node embeddings for downstream node tasks. Despite its empirical success, there is little quantitative theory explaining…

19. **[Bellman Contraction under MMD: A Unified Framework](https://arxiv.org/abs/2611.17116)** — quality 47  
   Baptiste Debes, Tinne Tuytelaars · 2026-11-12  
   _why:_ theory; code released; accepted: NeurIPS; 88 pages  
   > We introduce a mathematical framework for studying contraction of the distributional Bellman operator under Maximum Mean Discrepancy (MMD). We show that contraction reduces to conditional positive definiteness of an associated kernel constructed from the base kernel, which we…

20. **[GA-HEL: A Knowledge-Driven Expert System for Open-Set, Granularity-Aware Hierarchical Event Linking in Social Media](https://arxiv.org/abs/2611.16194)** — quality 48  
   Shengqi Zhou, Zhigang Liu, Wenxiang Zhu et al. · 2026-11-12  
   _why:_ ablations; mechanistic / causal analysis; contamination check; code released  
   > Social-media event intelligence requires a system to determine whether a post belongs to a registered event space, identify the supported hierarchy path, and stop at the deepest level warranted by the evidence. We formulate this requirement as open-set hierarchical event linking…

21. **[Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://arxiv.org/abs/2611.14210)** — quality 53  
   Hadi Salloum, Ammar Ali · 2026-11-10  
   _why:_ variance / significance; code released; HF daily papers: 66 upvotes  
   > Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million…

22. **[WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory Learning](https://arxiv.org/abs/2611.12527)** — quality 57  
   Sang-Hoon Lee, Ha-Yeong Choi · 2026-11-09  
   _why:_ model-scale sweep; code released; accepted: NeurIPS; HF daily papers: 17 upvotes  
   > This work proposes WaveGen, a fully end-to-end diffusion-based text-to-waveform framework based on Spectral Forcing, which jointly learns an internal spectral trajectory and the target waveform trajectory within a single model, enabling direct end-to-end text-to-waveform…

23. **[WorldDraft: If Code Builds the World, Can Video Models Just Render It?](https://arxiv.org/abs/2611.16217)** — quality 48  
   Zhiyu Hou, Wen-Jie Shu, Harold Haodong Chen et al. · 2026-11-12  
   _why:_ contamination check; code released; HF daily papers: 13 upvotes  
   > Multimodal coding agents decouple 4D world construction from visual generation, repurposing video models from world generators toward generative renderers. This division of labor raises a fundamental question: if code builds the world, can video models just render it? A reliable…

24. **[Parsed, Plausible, Wrong: Output Format Controls Silent Errors in Small-Model Semantic Parsing](https://arxiv.org/abs/2611.17169)** — quality 46  
   Umar Ahmed, Maxim Dunaev, Mohammad Nour Al Awad et al. · 2026-11-12  
   _why:_ variance / significance; contamination check; code released  
   > A small fine-tuned parser that emits a well-formed but wrong tree fails silently: nothing downstream can tell. We ask whether the output format, a free design choice, controls how often this happens. On the PIZZA ordering benchmark we fine-tune two sub-billion models…

25. **[ORCA:Orthogonal Residual Consensus Alignment for Multi-View Clustering](https://arxiv.org/abs/2611.16749)** — quality 46  
   Xiaojian Ding, Xian Li, Xiaoying Zhu et al. · 2026-11-12  
   _why:_ ablations; strong baselines; code released  
   > Deep multi-view clustering often suffers from redundant information accumulation during fusion and indiscriminate alignment across representation levels. We propose Orthogonal Residual Consensus Alignment (ORCA) to address these challenges. Its semantic incremental recurrent…


## Blog posts & lab write-ups (last 14 days)

1. **[Anthropic Residency: applications open for established technical leaders](https://alignment.anthropic.com/2026/anthropic-residency/)** — quality 54  
   Anthropic Alignment Science · 2026-11-22  
   _why:_ mechanistic / causal analysis; source tier 1  
   > Anthropic Residency: applications open for established technical leaders Alignment Science Blog Anthropic Residency: applications open for established technical leaders Today we are opening applications for the Anthropic Residency, our paid, fixed-term research program with…

2. **[Neurons as an Interpretable Basis](https://www.goodfire.ai/research/neurons-as-an-interpretable-basis)** — quality 68  
   Goodfire Research · 2026-11-10  
   _why:_ ablations; strong baselines; mechanistic / causal analysis; contamination check; long-form (425k chars); source tier 1  
   > Neural networks have long been regarded as opaque black boxes, in part because their neurons seemed inscrutable. This article makes the case that language model neurons—the hidden units of MLPs—are interpretable units of computation.

3. **[Worse Together: How Performance Breaks Down in Multi-User Multi-Agent Teams](https://alignment.anthropic.com/2026/worse-together/)** — quality 61  
   Anthropic Alignment Science · 2026-11-11  
   _why:_ variance / significance; negative results / limitations; source tier 1  
   > Anthropic Fellows Blog: When several users each delegate to their own agent and those agents share a resource, group outcomes are worse than when one agent serves everyone, and the agents show problematic behaviors that vary by model and environment.

4. **[Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs](http://unemploymentlabs.com/checkpoint-forensics)** — quality 57  
   unemploymentlabs.com · 2026-11-12  
   _why:_ reproduction / replication; negative results / limitations; weights/data released; long-form (38k chars); source tier 3; shared on X by 3 accounts  
   > Our forensic analysis of publicly released AI models finds evidence that DeepSeek, Moonshot AI, MiniMax and Ant Group have gained access to NVIDIA’s Blackwell GPUs, despite restrictions on exporting these chips to China, and are using that hardware to create their AI models.

5. **[Claude can design electronic prototypes from start to finish](https://www.anthropic.com/research/claude-electronics-design)** — quality 66  
   Anthropic Research · 2026-11-09  
   _why:_ mechanistic / causal analysis; negative results / limitations; source tier 1; Hacker News: 1 submission, 35 points  
   > We asked Claude to design three electronic devices: a speakerphone, a voice-assistant hub, and a handheld virtual pet. The prototypes worked without any fixes to their circuitry.

6. **[The fall of “what you can do” and the rise of “who you know”](https://www.jasonwei.net/blog/the-fall-of-what-you-can-do-and-the-rise-of-who-you-know)** — quality 53  
   Jason Wei · 2026-11-11  
   _why:_ mechanistic / causal analysis; source tier 1  
   > Traditionally, many of us believe in a world where how hard you work is more important than who you know. I used to subscribe to this idea as both a scientist, who believed that facts about our world are agnostic to who says them, and as an American, who grew up believing that…

7. **[Using wearables to enable cardiovascular-kidney-metabolic (CKM) risk profiling for personalized coaching](https://research.google/blog/using-wearables-to-enable-cardiovascular-kidney-metabolic-ckm-risk-profiling-for-personalized-coaching/)** — quality 52  
   Google Research · 2026-11-11  
   _why:_ strong baselines; mechanistic / causal analysis; human evaluation; source tier 2  
   > Health & Bioscience

8. **[SynthDeception: Realistic, Multi-Domain Agentic Scenarios for Studying Falsehood Detection Probes | FAR.AI](https://www.far.ai/blog/synthdeception)** — quality 58  
   FAR.AI · 2026-11-10  
   _why:_ mechanistic / causal analysis; source tier 1  
   > Nov 09, 2026 SynthDeception is a fully synthetic dataset of realistic, multi-domain agentic scenarios. We test how well probes trained on it detect deception and sabotage, and how FIBS probes perform on it as models scale.

9. **[A few lines of text bypass Kimi K3.1 Pro's safeguards | FAR.AI](https://www.far.ai/blog/security-stress-test-kimi-k3-1-pro-safeguards)** — quality 57  
   FAR.AI · 2026-11-10  
   _why:_ mechanistic / causal analysis; source tier 1  
   > Nov 09, 2026 Ask Kimi K3.1 Pro directly for help with a chemical, biological or cyber attack, and it almost always says no. Write the opening of its answer for it, using the same short piece of text every time, and it gives harmful help on up to 99.4% of requests, across every…

10. **[No One Buys Corn in the Corn Market](https://www.argmin.net/p/no-one-buys-corn-in-the-corn-market)** — quality 54  
   Ben Recht (arg min) · 2026-11-10  
   _why:_ mechanistic / causal analysis; source tier 1  
   > Prediction markets are for gambling. But what part of finance isn’t gambling?

11. **[Encoder Disaggregation in vLLM: Scaling Multimodal Serving with EPD](https://vllm.ai/blog/2026-11-11-encoder-disaggregation-epd)** — quality 52  
   vLLM · 2026-11-11  
   _why:_ strong baselines; mechanistic / causal analysis; source tier 2  
   > Recent advances in vLLM encoder disaggregation: metadata-only multimodal requests, dedicated encoder execution, remote embedding transfer, cross-encoder caching

12. **[Diluting Poisoned Fine-Tuning Data Can Strengthen Its Effect](https://alignment.anthropic.com/2026/homeopathic-learning/)** — quality 54  
   Anthropic Alignment Science · 2026-11-10  
   _why:_ controlled experiments; reproduction / replication; negative results / limitations; source tier 1  
   > Diluting Poisoned Fine-Tuning Data Can Strengthen Its Effect Alignment Science Blog Diluting Poisoned Fine-Tuning Data Can Strengthen Its Effect Matt Clarke*¹, Jan Dubiński*² ³ ⁴, James Chua¹† November 10, 2026 Simon Schrodi⁵ ⁶†, Owain Evans² ⁷, Alex Cloud¹ ¹ Anthropic; ²…


## Shared on X, in newsletters & on HN/Reddit (last 14 days)

1. **[Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs](http://unemploymentlabs.com/checkpoint-forensics)** — quality 57  
   unemploymentlabs.com · 2026-11-12  
   _why:_ reproduction / replication; negative results / limitations; weights/data released; long-form (38k chars); source tier 3; shared on X by 3 accounts  
   > Our forensic analysis of publicly released AI models finds evidence that DeepSeek, Moonshot AI, MiniMax and Ant Group have gained access to NVIDIA’s Blackwell GPUs, despite restrictions on exporting these chips to China, and are using that hardware to create their AI models.

2. **[Claude can design electronic prototypes from start to finish](https://www.anthropic.com/research/claude-electronics-design)** — quality 66  
   Anthropic Research · 2026-11-09  
   _why:_ mechanistic / causal analysis; negative results / limitations; source tier 1; Hacker News: 1 submission, 35 points  
   > We asked Claude to design three electronic devices: a speakerphone, a voice-assistant hub, and a handheld virtual pet. The prototypes worked without any fixes to their circuitry.

3. **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320)** — quality 56  
   Yukyeong Lee, Yumin Choi, Jinheon Baek et al. · 2026-11-10  
   _why:_ strong baselines; code released; HF daily papers: 65 upvotes; shared on X by 1 account  
   > External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it…

4. **[Introducing Gemini 4 Hydrogen for Agentic Workflows](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)** — quality 47  
   blog.google · 2026-11-12  
   _why:_ source tier 3; shared on X by 2 accounts; Hacker News: 1 submission, 533 points; in newsletters: The Rundown AI  
   > Google introduces Gemini 4 Hydrogen, a fast, cost-efficient model built for reliable agentic workflows and everyday tasks. Get the details.

5. **[Inkling 2 Small on vLLM: Day-0 Support](https://vllm.ai/blog/2026-11-12-inkling2-small)** — quality 47  
   vLLM · 2026-11-12  
   _why:_ source tier 2; shared on X by 1 account  
   > vLLM supports Thinking Machines' Inkling 2 Small from day 0: attention residuals, a new decode kernel for relative-bias attention, all-reduce fused with the ops

6. **[Teaching AI to build scientific models](https://www.anthropic.com/research/teaching-ai-to-build-scientific-models)** — quality 70  
   Anthropic Research · 2026-11-06  
   _why:_ mechanistic / causal analysis; reproduction / replication; negative results / limitations; source tier 1; shared on X by 1 account  
   > AI for Science grantees Jakob Macke, Daniel Gedon, and Stefan Wahl on how AI is starting to change how scientific models are built and interpreted.

7. **[Introducing Claude Fable 5.2 and Claude Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2)** — quality 56  
   anthropic.com · 2026-11-09  
   _why:_ theory; mechanistic / causal analysis; reproduction / replication; long-form (41k chars); source tier 3; Hacker News: 2 submissions, 1626 points ⚠ hype: astonishing  
   > Claude Fable 5.2 and Claude Mythos 5.2, our new models for the hardest technical challenges. Fable 5.2 sets a new bar in coding, finance, and the sciences.

8. **[The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory)** — quality 69  
   Anthropic Research · 2026-11-06  
   _why:_ strong baselines; source tier 1; shared on X by 1 account; Hacker News: 1 submission, 188 points; in newsletters: Ben's Bites, The Rundown AI  
   > For Claude to learn from experience, it has to decide what’s worth remembering before it knows what’s next. Here’s how “dreaming” helps it organize memory and correct mistakes.

9. **[InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure](https://arxiv.org/abs/2611.11558)** — quality 55  
   InfraRSI Team, Yuchuan Tian, Haocheng Mei et al. · 2026-11-08  
   _why:_ strong baselines; code released; HF daily papers: 33 upvotes; shared on X by 1 account  
   > While Recursive Self-Improvement (RSI) accelerates isolated algorithm and kernel synthesis, distributed LLM training depends on tightly coupled launch settings, operator kernels, and communication schedules, where single edits often hit out-of-memory (OOM) boundaries, compiler…

10. **[Gemini Decisions API: Fast multimodal decisions](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)** — quality 46  
   blog.google · 2026-11-11  
   _why:_ source tier 3; shared on X by 1 account; Hacker News: 1 submission, 448 points; in newsletters: AINews, The Rundown AI  
   > The Gemini Decisions API provides fast, calibrated multimodal decisions for Google apps. Evaluate 1,000 questions in one pass. Get the details.

11. **[Can LLM Agents Organize Their Own Memory?](https://arxiv.org/abs/2611.11929)** — quality 49  
   Zichuan Fu, Junjia Qi, Wenlin Zhang et al. · 2026-11-09  
   _why:_ strong baselines; code released; shared on X by 1 account  
   > In most LLM agents, weights are fixed after deployment, so new information must be retained in external memory. Existing approaches often rely on predefined records and fixed organizational rules, which cannot readily accommodate evolving tasks and interactions. This raises the…

12. **[Independent Assessment of AI R&D Acceleration at Anthropic in October 2026](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/)** — quality 64  
   METR · 2026-11-05  
   _why:_ variance / significance; negative results / limitations; long-form (75k chars); source tier 1; Hacker News: 1 submission, 47 points; Reddit: 2 submissions ⚠ hype: remarkable, unprecedented  
   > Redaction summary: As part of this assessment, Anthropic had rights to redact any non-public information in this post. Per our approach to transparency , we had the right to disclose if Anthropic exercised redaction rights, and whether or not any of our findings depended…
