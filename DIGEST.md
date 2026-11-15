# paper-taste digest — 2026-11-15

Ranked by heuristic quality × recency (10-day half-life). Scores are a first pass from metadata and abstracts; see [TASTE.md](TASTE.md) for the rubric an agent applies on top, and [AGENTS.md](AGENTS.md) to get recommendations matched to your own repos.

## Papers (last 7 days, 2221 kept in the last 14)

1. **[SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models](https://arxiv.org/abs/2611.15777)** — quality 64  
   Lichen Li, Ziping Dong, Sicheng Feng et al. · 2026-11-11  
   _why:_ multiple benchmarks; negative results / limitations; code released; 32 pages; HF daily papers: 136 upvotes  
   > System One models promise fast, general-purpose decision-making without lengthy token generation. However, understanding their capability spectrum and decision reliability requires more than aggregate performance on current benchmarks. Existing evaluations often provide limited…

2. **[TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models](https://arxiv.org/abs/2611.17331)** — quality 59  
   Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe et al. · 2026-11-12  
   _why:_ multiple benchmarks; code released; accepted: NeurIPS; HF daily papers: 23 upvotes  
   > Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We…

3. **[Factored One-sided Adam-Moment for Practical and Scalable SOAP](https://arxiv.org/abs/2611.16905)** — quality 56  
   Jaemyung Yu, Byeongho Heo, Sangdoo Yun et al. · 2026-11-12  
   _why:_ strong baselines; model-scale sweep; code released; HF daily papers: 14 upvotes  
   > Second-order optimizers (e.g., Shampoo, SOAP) have emerged as compelling alternatives to Adam/AdamW and promise faster per-step convergence than AdamW in transformer training. However, they still remain costly in practice, and even SOAP still pays substantial optimizer-state…

4. **[Open Vision Banana: A Fully Open Recipe for Generative Visual Perception](https://arxiv.org/abs/2611.15844)** — quality 58  
   Arpit Jadon, Valentinos Pariza, Jona Ruthardt et al. · 2026-11-11  
   _why:_ ablations; weights/data released; code released; HF daily papers: 36 upvotes  
   > Recent work suggests that pretrained image generators encode real-world understanding beyond image synthesis. Vision Banana exploits this by framing vision tasks as conditional image editing. However, its data, weights, code, and implementation details are not public. We present…

5. **[Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors](https://arxiv.org/abs/2611.17060)** — quality 53  
   Hao Li, Fangzhou Hong, Zhaoxi Chen et al. · 2026-11-12  
   _why:_ model-scale sweep; code released; HF daily papers: 27 upvotes; 21-author team  
   > Large foundation models such as GPT-6 Astra and Claude Fable 5.1 have recently been shown to control robots directly from visual observations. They nevertheless remain brittle on long-horizon, contact-rich tasks in real-world environments. Further progress depends on two…

6. **[Bellman Contraction under MMD: A Unified Framework](https://arxiv.org/abs/2611.17116)** — quality 52  
   Baptiste Debes, Tinne Tuytelaars · 2026-11-12  
   _why:_ theory; code released; accepted: NeurIPS; 88 pages; senior author (h-index 78)  
   > We introduce a mathematical framework for studying contraction of the distributional Bellman operator under Maximum Mean Discrepancy (MMD). We show that contraction reduces to conditional positive definiteness of an associated kernel constructed from the base kernel, which we…

7. **[WorldDraft: If Code Builds the World, Can Video Models Just Render It?](https://arxiv.org/abs/2611.16217)** — quality 52  
   Zhiyu Hou, Wen-Jie Shu, Harold Haodong Chen et al. · 2026-11-12  
   _why:_ contamination check; code released; HF daily papers: 16 upvotes; senior author (h-index 51)  
   > Multimodal coding agents decouple 4D world construction from visual generation, repurposing video models from world generators toward generative renderers. This division of labor raises a fundamental question: if code builds the world, can video models just render it? A reliable…

8. **[Unbundling Multimodal Vision Encoding](https://arxiv.org/abs/2611.17334)** — quality 50  
   Ellis Brown, Chris Hoang, Shengyi Qian et al. · 2026-11-12  
   _why:_ controlled experiments; HF daily papers: 15 upvotes; senior author (h-index 40); shared on X by 1 account  
   > How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design…

9. **[Detection Is Not Early Warning: Evaluating Token-Level Alarms on Language Model Failures](https://arxiv.org/abs/2611.16803)** — quality 49  
   Marco De Negri, Luca Sartori, Lorenzo Baggi et al. · 2026-11-12  
   _why:_ strong baselines; mechanistic / causal analysis; code released; weights/data released; accepted: NeurIPS workshop; 30 pages  
   > Many failures of language models begin at a specific token, the onset. A monitor that reads the model during generation can classify the finished response, detect the failure once it is under way, or warn before it begins, and only a warning leaves time to stop or steer the…

10. **[SWAM: Scaling World Action Models with Cross-Modal Alignment](https://arxiv.org/abs/2611.12870)** — quality 60  
   Yu Zhou, Xinyuan Xia, Xuankun Yang et al. · 2026-11-09  
   _why:_ strong baselines; mechanistic / causal analysis; controlled experiments; code released; weights/data released; HF daily papers: 22 upvotes  
   > World action models jointly predict video and actions conditioned on language. Existing studies focus primarily on architectures and training mechanisms, typically treating language-video alignment acquired through video pretraining as an established foundation. However,…

11. **[PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](https://arxiv.org/abs/2611.16748)** — quality 49  
   Yuxuan Chen, Xiaojie Li, Hao Chen et al. · 2026-11-12  
   _why:_ weights/data released; code released; HF daily papers: 46 upvotes  
   > Video generation models produce visually realistic videos but still struggle with physical dynamics and causal consistency. Learning from generated videos requires fine-grained physical supervision, yet reliable quality judgments, correction pairs, and controlled variations are…

12. **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320)** — quality 56  
   Yukyeong Lee, Yumin Choi, Jinheon Baek et al. · 2026-11-10  
   _why:_ strong baselines; code released; HF daily papers: 66 upvotes; shared on X by 1 account  
   > External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it…

13. **[Sage-Taiyi: A Metacognitive Architecture for Scientific Discovery](https://arxiv.org/abs/2611.12762)** — quality 59  
   Weida Wang, Benteng Chen, Yigeng Jiang et al. · 2026-11-09  
   _why:_ strong baselines; code released; 38 pages; HF daily papers: 57 upvotes; 90-author team  
   > We introduce Sage-Taiyi, a metacognition-inspired architecture that uses accumulated scientific understanding to guide what to investigate next and how to investigate it. Through explicit monitoring and control, the system revises its understanding of evidence, assumptions, and…

14. **[Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents](https://arxiv.org/abs/2611.17167)** — quality 47  
   Haochen Liu, Qianhao Zhu, Zixuan Wang et al. · 2026-11-12  
   _why:_ code released; HF daily papers: 34 upvotes; shared on X by 1 account  
   > Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has…

15. **[Verifier Choice is a Benchmark Design Variable: Auditing Structural Counting Evaluation in Text-to-Image Models](https://arxiv.org/abs/2611.15433)** — quality 51  
   Shurun Li, Michael Hua Wang, Haibo Zeng et al. · 2026-11-11  
   _why:_ strong baselines; controlled experiments; code released; weights/data released; accepted: NeurIPS  
   > Automatic evaluation is now central to text-to-image benchmarking, but the verifier that converts generated images into scores is often treated as an implementation detail. We argue that this is unsafe: an automatic benchmark score is a property of the image generator, prompt…

16. **[Consensus Capture in Reference-Based UAV Video Stabilization: A Benchmark on Dynamic Urban Scenes](https://arxiv.org/abs/2611.17190)** — quality 47  
   Robert Fonod, Nikolas Geroliminis · 2026-11-12  
   _why:_ code released; 50 pages; HF daily papers: 4 upvotes; senior author (h-index 49)  
   > Reference-frame stabilization registers every frame of a hovering-drone video onto one reference frame, keeping object positions comparable. The registration pipelines it relies on are selected on feature-matching benchmarks in which only the camera moves. Over a busy…

17. **[Split-and-scale Latent 3D Representations](https://arxiv.org/abs/2611.16126)** — quality 49  
   Dorian Chan, Muhammed Kocabas, Xiaoming Zhao et al. · 2026-11-12  
   _why:_ ablations; strong baselines; negative results / limitations; accepted: NeurIPS; senior author (h-index 48)  
   > Latent 3D representations have significantly expanded the capabilities of modern shape modeling, enabling compact encoding of 3D scenes and supporting powerful 3D generative models. Despite this progress, current representations struggle to capture the fine details of complex…

18. **[WaveGen: Truly End-to-End Waveform Generation via Internal Spectral Trajectory Learning](https://arxiv.org/abs/2611.12527)** — quality 57  
   Sang-Hoon Lee, Ha-Yeong Choi · 2026-11-09  
   _why:_ model-scale sweep; code released; accepted: NeurIPS; HF daily papers: 17 upvotes  
   > This work proposes WaveGen, a fully end-to-end diffusion-based text-to-waveform framework based on Spectral Forcing, which jointly learns an internal spectral trajectory and the target waveform trajectory within a single model, enabling direct end-to-end text-to-waveform…

19. **[Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://arxiv.org/abs/2611.12304)** — quality 57  
   Hao Kang, Weili Xu, Ziyang Li et al. · 2026-11-09  
   _why:_ negative results / limitations; code released; weights/data released; HF daily papers: 12 upvotes; senior author (h-index 45)  
   > Agentic workloads are a major source of LLM inference demand. Existing prefill--decode (PD) disaggregated serving systems offer limited flexibility for runtime adaptation of compute allocation and KV cache management, and rely on coarse signals that only partly capture the…

20. **[JustRUA: A Controlled Study of GPT-6 Robot-Use Agents](https://arxiv.org/abs/2611.16009)** — quality 48  
   Zefan Wang, Yufan Dang, Xuanwei Shi et al. · 2026-11-11  
   _why:_ controlled experiments; code released; 30 pages; HF daily papers: 5 upvotes  
   > GPT-6 Astra can drive a robot arm directly through a fixed harness, and scores of such robot-use agents on RoboDojo have risen quickly since. Reported systems differ in harness and test subset and often change several designs at once, so it is hard to tell which choices produce…

21. **[Are Dense Rewards Worth Their Tokens in GRPO?](https://arxiv.org/abs/2611.13560)** — quality 54  
   Vikash Singh, Weicong Chen, Debargha Ganguly et al. · 2026-11-10  
   _why:_ reproduction / replication; code released; 59 pages; HF daily papers: 5 upvotes; 19-author team  
   > RLVR trains language models to reason by rewarding correct final answers. A widely used algorithm, group-relative policy optimization (GRPO), gives every token of a solution the same credit, so dense process rewards have been proposed to credit intermediate steps, for example…

22. **[Predicting the Needle in a Petabyte Scale Haystack: Open-Vocabulary Event Anticipation in Satellite Imagery](https://arxiv.org/abs/2611.16000)** — quality 48  
   Shreelekha Revankar, Mikhail Klassen, Creon Levit et al. · 2026-11-11  
   _why:_ strong baselines; code released; accepted: NeurIPS; 29 pages  
   > Satellite constellations now image the Earth daily, capturing the lifecycle of events from deforestation to urban construction. Anticipating these events before completion enables timely intervention, yet existing systems cannot jointly identify where a change occurs, what it…

23. **[RipBench: A Unified Benchmark for Multi-Level Rip Current Detection, Classification and Segmentation](https://arxiv.org/abs/2611.15574)** — quality 48  
   Andrei Dumitriu, Aakash Ralhan, Florin Miron et al. · 2026-11-11  
   _why:_ strong baselines; variance / significance; accepted: NeurIPS; 47 pages; senior author (h-index 107)  
   > Rip currents are a serious and often under-addressed threat to beach safety and the leading cause of coastal drownings worldwide. They are difficult to detect due to their amorphous structure, similarity to the background, and large variability in viewpoints and environments.…

24. **[Market-Conditioned JEPA: Learning from Unpredictable Market Shocks](https://arxiv.org/abs/2611.13572)** — quality 53  
   Yuqi Wang, Fengyuan Liu, Mukai Li et al. · 2026-11-10  
   _why:_ ablations; strong baselines; variance / significance; code released; HF daily papers: 5 upvotes  
   > Much of the variation in financial time series is driven by market-wide shocks that cannot be predicted from an asset's own history. Per-asset self-supervised learning treats this variation as irreducible noise. Under a latent factor model, we show that conditioning prediction…

25. **[EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming](https://arxiv.org/abs/2611.16728)** — quality 45  
   Yaru Niu, Binghong Chen, Changwei Yao et al. · 2026-11-12  
   _why:_ ablations; code released; HF daily papers: 1 upvotes; 22-author team  
   > Generalist manipulation policies can benefit from the complementary experience of humans, real robots, and simulated agents. However, differences in morphology, sensing, and control interfaces make it difficult to learn effectively from their combined demonstrations. We…


## Blog posts & lab write-ups (last 14 days)

1. **[End‑to‑End 4‑Bit Training](https://thinkingmachines.ai/blog/end-to-end-4-bit-training/)** — quality 76  
   Thinking Machines · 2026-11-13  
   _why:_ model-scale sweep; controlled experiments; negative results / limitations; long-form (26k chars); source tier 1; shared on X by 3 accounts  
   > Training large language models involves calculating and storing a lot of numbers. Using fewer bits for each value reduces memory usage and allows GPUs to perform calculations faster. However, there is a tradeoff: fewer bits also mean fewer representable numbers, leading to more…

2. **[Building strong safety evaluations](https://www.anthropic.com/research/building-strong-safety-evaluations)** — quality 73  
   Anthropic Research · 2026-11-13  
   _why:_ strong baselines; variance / significance; reproduction / replication; contamination check; long-form (30k chars); source tier 1  
   > Recommendations for designing, running, and reporting safety evaluations, based on our own experiences.

3. **[Anthropic Residency: applications open for established technical leaders](https://alignment.anthropic.com/2026/anthropic-residency/)** — quality 58  
   Anthropic Alignment Science · 2026-11-22  
   _why:_ mechanistic / causal analysis; source tier 1; in newsletters: Don't Worry About the Vase (Zvi)  
   > Anthropic Residency: applications open for established technical leaders Alignment Science Blog Anthropic Residency: applications open for established technical leaders Today we are opening applications for the Anthropic Residency, our paid, fixed-term research program with…

4. **[Advancing science & engineering with Antigravity’s /teamwork](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/)** — quality 59  
   Google Research · 2026-11-13  
   _why:_ theory; mechanistic / causal analysis; source tier 2; shared on X by 1 account  
   > Education Innovation

5. **[AI agents attempted exploits on our website](https://epoch.ai/publications/incident-report-ai-agents-attempted-exploits-on-our-website)** — quality 62  
   Epoch AI (Publications) · 2026-11-13  
   _why:_ reproduction / replication; source tier 1; shared on X by 1 account  
   > Three October 2026 events involving Trajectory Labs, PBC, in which agents probed our site and impersonated staff. No private data was accessed.

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

11. **[When One GPU Isn’t Enough: Serving GLM-5.3 Across Two NVIDIA DGX Stations with vLLM](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/)** — quality 46  
   NVIDIA Technical Blog · 2026-11-13  
   _why:_ strong baselines; source tier 3; Hacker News: 1 submission, 138 points  
   > Running a frontier-scale model locally means keeping all its weights in GPU memory; the largest models no longer fit on one machine. Two NVIDIA DGX Stations...

12. **[Open-source AI without Jensen](https://www.interconnects.ai/p/open-source-ai-without-jensen)** — quality 43  
   Interconnects (Nathan Lambert) · 2026-11-14  
   _why:_ source tier 2; Hacker News: 1 submission, 26 points ⚠ hype: incredible  
   > A decapitation. It’s time to rebuild.


## Shared on X, in newsletters & on HN/Reddit (last 14 days)

1. **[End‑to‑End 4‑Bit Training](https://thinkingmachines.ai/blog/end-to-end-4-bit-training/)** — quality 76  
   Thinking Machines · 2026-11-13  
   _why:_ model-scale sweep; controlled experiments; negative results / limitations; long-form (26k chars); source tier 1; shared on X by 3 accounts  
   > Training large language models involves calculating and storing a lot of numbers. Using fewer bits for each value reduces memory usage and allows GPUs to perform calculations faster. However, there is a tradeoff: fewer bits also mean fewer representable numbers, leading to more…

2. **[Building strong safety evaluations](https://www.anthropic.com/research/building-strong-safety-evaluations)** — quality 73  
   Anthropic Research · 2026-11-13  
   _why:_ strong baselines; variance / significance; reproduction / replication; contamination check; long-form (30k chars); source tier 1  
   > Recommendations for designing, running, and reporting safety evaluations, based on our own experiences.

3. **[Anthropic Residency: applications open for established technical leaders](https://alignment.anthropic.com/2026/anthropic-residency/)** — quality 58  
   Anthropic Alignment Science · 2026-11-22  
   _why:_ mechanistic / causal analysis; source tier 1; in newsletters: Don't Worry About the Vase (Zvi)  
   > Anthropic Residency: applications open for established technical leaders Alignment Science Blog Anthropic Residency: applications open for established technical leaders Today we are opening applications for the Anthropic Residency, our paid, fixed-term research program with…

4. **[Advancing science & engineering with Antigravity’s /teamwork](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/)** — quality 59  
   Google Research · 2026-11-13  
   _why:_ theory; mechanistic / causal analysis; source tier 2; shared on X by 1 account  
   > Education Innovation

5. **[AI agents attempted exploits on our website](https://epoch.ai/publications/incident-report-ai-agents-attempted-exploits-on-our-website)** — quality 62  
   Epoch AI (Publications) · 2026-11-13  
   _why:_ reproduction / replication; source tier 1; shared on X by 1 account  
   > Three October 2026 events involving Trajectory Labs, PBC, in which agents probed our site and impersonated staff. No private data was accessed.

6. **[Top Chinese Frontier AI Models Carry the Fingerprint of Export-Controlled NVIDIA Blackwell GPUs](http://unemploymentlabs.com/checkpoint-forensics)** — quality 57  
   unemploymentlabs.com · 2026-11-12  
   _why:_ reproduction / replication; negative results / limitations; weights/data released; long-form (38k chars); source tier 3; shared on X by 3 accounts  
   > Our forensic analysis of publicly released AI models finds evidence that DeepSeek, Moonshot AI, MiniMax and Ant Group have gained access to NVIDIA’s Blackwell GPUs, despite restrictions on exporting these chips to China, and are using that hardware to create their AI models.

7. **[Claude can design electronic prototypes from start to finish](https://www.anthropic.com/research/claude-electronics-design)** — quality 66  
   Anthropic Research · 2026-11-09  
   _why:_ mechanistic / causal analysis; negative results / limitations; source tier 1; Hacker News: 1 submission, 35 points  
   > We asked Claude to design three electronic devices: a speakerphone, a voice-assistant hub, and a handheld virtual pet. The prototypes worked without any fixes to their circuitry.

8. **[Unbundling Multimodal Vision Encoding](https://arxiv.org/abs/2611.17334)** — quality 50  
   Ellis Brown, Chris Hoang, Shengyi Qian et al. · 2026-11-12  
   _why:_ controlled experiments; HF daily papers: 15 upvotes; senior author (h-index 40); shared on X by 1 account  
   > How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design…

9. **[When One GPU Isn’t Enough: Serving GLM-5.3 Across Two NVIDIA DGX Stations with vLLM](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/)** — quality 46  
   NVIDIA Technical Blog · 2026-11-13  
   _why:_ strong baselines; source tier 3; Hacker News: 1 submission, 138 points  
   > Running a frontier-scale model locally means keeping all its weights in GPU memory; the largest models no longer fit on one machine. Two NVIDIA DGX Stations...

10. **[Open-source AI without Jensen](https://www.interconnects.ai/p/open-source-ai-without-jensen)** — quality 43  
   Interconnects (Nathan Lambert) · 2026-11-14  
   _why:_ source tier 2; Hacker News: 1 submission, 26 points ⚠ hype: incredible  
   > A decapitation. It’s time to rebuild.

11. **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://arxiv.org/abs/2611.14320)** — quality 56  
   Yukyeong Lee, Yumin Choi, Jinheon Baek et al. · 2026-11-10  
   _why:_ strong baselines; code released; HF daily papers: 66 upvotes; shared on X by 1 account  
   > External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it…

12. **[AlphaGenome 2: Deciphering how cells read DNA to better understand disease](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)** — quality 51  
   Google DeepMind · 2026-11-11  
   _why:_ source tier 2; shared on X by 1 account; in newsletters: The Rundown AI  
   > Predicting how DNA sequences and their variations impact specific human cell types and disease.
