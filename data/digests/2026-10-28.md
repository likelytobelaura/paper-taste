# paper-taste digest — 2026-10-28

Ranked by heuristic quality × recency (10-day half-life). Scores are a first pass from metadata and abstracts; see [TASTE.md](TASTE.md) for the rubric an agent applies on top, and [AGENTS.md](AGENTS.md) to get recommendations matched to your own repos.

## Papers (last 7 days, 560 kept in the last 14)

1. **[S3AC: Stabilized, Selective, and Scalable Actor-Critic for LLM Reasoning](https://arxiv.org/abs/2610.35518)** — quality 64  
   Shuo Shen, Guangran Cheng, Chengqi Lyu et al. · 2026-10-26  
   _why:_ strong baselines; model-scale sweep; negative results / limitations; code released; HF daily papers: 30 upvotes  
   > Critic-free methods are widely used in reinforcement learning with verifiable rewards (RLVR) for long chain-of-thought (CoT) reasoning, avoiding difficult and costly critic training. Common alternatives lack token-level credit assignment and typically rely on grouped rollouts to…

2. **[Hy-Nomas: Towards Free-form Interactive World Generation](https://arxiv.org/abs/2610.36729)** — quality 61  
   Qiaoling Chen, Jiaxiang Cheng, Xueqing Deng et al. · 2026-10-27  
   _why:_ human evaluation; weights/data released; code released; HF daily papers: 104 upvotes; 38-author team  
   > Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences. We present Hy-Nomas, a video world model with an 8B diffusion backbone that supports free-form text instructions and continuous camera control…

3. **[Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?](https://arxiv.org/abs/2610.37662)** — quality 58  
   Jialv Zou, Xiaotong Li, Zhengrong Yue et al. · 2026-10-27  
   _why:_ theory; code released; HF daily papers: 81 upvotes  
   > Discrete visual tokens represent vision in a discrete form analogous to language, offering a native interface for multimodal modeling under a shared next-token prediction objective. However, quantization error is widely assumed to cause unavoidable semantic loss, fundamentally…

4. **[OBB-PBD: Extending Parallel Box Decoding to Oriented Bounding Boxes for Referring Expression Grounding in Aerial Imagery](https://arxiv.org/abs/2610.35450)** — quality 60  
   Chang Woo Song, Yeong Jun Koh · 2026-10-26  
   _why:_ strong baselines; variance / significance; contamination check; code released; weights/data released; HF daily papers: 9 upvotes  
   > Referring expression grounding in overhead imagery requires oriented bounding boxes rather than horizontal ones, since aerial objects appear at arbitrary orientations. Most grounding models emit box coordinates sequentially; Parallel Box Decoding (PBD) instead predicts all…

5. **[DynaFlow: Learning Free-Form Multi-Agent Orchestration](https://arxiv.org/abs/2610.34467)** — quality 62  
   Ruhao Liu, Qi Li, Shizun Wang et al. · 2026-10-25  
   _why:_ strong baselines; code released; HF daily papers: 203 upvotes  
   > Multi-agent systems often rely on predefined collaboration structures, limiting their ability to adapt to diverse task requirements. We introduce DynaFlow, a framework that integrates free-form executable workflow synthesis into the action space of the main agent. The agent…

6. **[M4Bench: Evaluating Procedural Specification for Clinical EHR Derivation Agents](https://arxiv.org/abs/2610.37459)** — quality 54  
   Hannes Ill, Rafi Al Attrach, Rajna Fani et al. · 2026-10-27  
   _why:_ strong baselines; reproduction / replication; code released; weights/data released; accepted: NeurIPS; 33 pages  
   > Clinical research over electronic health records depends on derived variables whose definitions sit outside the schema, in item codes, time windows, missingness rules, and output-grain choices that change cohorts and downstream conclusions. We introduce M4Bench, 28 clinical…

7. **[Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception](https://arxiv.org/abs/2610.37037)** — quality 54  
   Lai Wei, Yatai Li, Liangbo He et al. · 2026-10-27  
   _why:_ ablations; code released; HF daily papers: 21 upvotes  
   > Multimodal perception forms the foundation of multimodal intelligence. In particular, spatial perception and multimodal long-context understanding are two pivotal tasks that underpin embodied AI and multimodal agents. However, synthesizing targeted, high-quality training data…

8. **[PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381)** — quality 53  
   Hanqing Wang, Zhaotian Cai, Ruichuan An et al. · 2026-10-27  
   _why:_ ablations; HF daily papers: 135 upvotes; 15-author team  
   > Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited. Video world models can capture scene dynamics, yet generating future videos introduces high latency into…

9. **[StreamVibe: Proactive Video Agents for Evolving User Intent](https://arxiv.org/abs/2610.34662)** — quality 57  
   Chengzhi Liu, Yuxiang Lai, Yuzhe Yang et al. · 2026-10-26  
   _why:_ strong baselines; negative results / limitations; 43 pages; HF daily papers: 257 upvotes; 16-author team  
   > Vision-language models are shifting from offline passive understanding toward online proactive interaction. However, prevailing methods largely rely on explicit requests while miss the implicit user intent (e.g., "where should I click next?" while a user navigate a website),…

10. **[Channel Selection for Mixture-of-Experts Decoding Needs No Calibration Data](https://arxiv.org/abs/2610.37386)** — quality 51  
   Geunhyoung Kim, Sung Ju Hwang · 2026-10-27  
   _why:_ code released; 37 pages; HF daily papers: 11 upvotes  
   > Mixture-of-Experts (MoE) models are bottlenecked by loading routed-expert weights from memory during interactive decoding at small batch sizes. Because most intermediate channels in a routed expert contribute little to any single token, channel selectors predict which channels…

11. **[Memory Tax: Dissecting the Net Value of Agent Memory](https://arxiv.org/abs/2610.34073)** — quality 60  
   Xuan He, Sining Zhoubian, Ruozhen Yang et al. · 2026-10-25  
   _why:_ multiple benchmarks; code released; HF daily papers: 99 upvotes; shared on X by 1 account  
   > Memory is increasingly used in long-horizon agents, yet the net value of building memory over direct retrieval from raw history remains largely unclear. Through a large-scale evaluation across multiple benchmarks and model backbones, we find many dedicated memory systems…

12. **[EmbeddingGemma 2: Unified and Efficient Multimodal Representations](https://arxiv.org/abs/2610.37364)** — quality 51  
   Henrique Schechter Vera, Sahil Dua, Jovan Andonov et al. · 2026-10-27  
   _why:_ ablations; weights/data released; 28 pages; HF daily papers: 11 upvotes; 73-author team  
   > We present EmbeddingGemma 2, an open multimodal embedding model which natively represents text, images, audio, video, and combinations thereof in a unified space. Our approach introduces improvements such as simplified per-layer embeddings and a multi-stage curriculum with…

13. **[SearchHorizonBench: A Benchmark for Search Value in AI Agents](https://arxiv.org/abs/2610.34714)** — quality 56  
   Jingjie Ning, Xueqi Li, Yibo Kong · 2026-10-26  
   _why:_ strong baselines; variance / significance; contamination check; code released; HF daily papers: 6 upvotes  
   > AI agents must decide when another search is worth its cost. Answer-success probabilities capture question difficulty, while this decision requires estimating the additional benefit of search. We introduce SearchHorizonBench, a benchmark for learning and evaluating search value…

14. **[Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion](https://arxiv.org/abs/2610.34415)** — quality 57  
   Kam Man Wu, Yu Zhang, Pengjun Fang et al. · 2026-10-25  
   _why:_ strong baselines; code released; 28 pages; HF daily papers: 56 upvotes  
   > Spatial audio authoring coordinates source decisions with soundfield synthesis. For editing, plans specify what to change and retain, while reference audio supplies further acoustic detail. We present AMBIT, a unified framework for native First-Order Ambisonics (FOA) generation…

15. **[$Δτ$-Bench: Pushing Agents Toward a Moving Capability](https://arxiv.org/abs/2610.34238)** — quality 58  
   Shuofei Qiao, Xuanguang Pan, Yijun Chen et al. · 2026-10-25  
   _why:_ multiple benchmarks; negative results / limitations; code released; HF daily papers: 26 upvotes  
   > In this paper, we introduce $Δτ$-Bench, an executable agent benchmark that models the structural evolution of large tool ecosystems. In $Δτ$-Bench, independently evolving services continually reshape how tasks can be accomplished: familiar tools may disappear or be replaced,…

16. **[MatAnyone-E: Sparse Memory Propagation for Efficient High-Resolution Video Matting](https://arxiv.org/abs/2610.35724)** — quality 53  
   Shuyun Wang, Shangchen Zhou, Peiqing Yang et al. · 2026-10-26  
   _why:_ reproduction / replication; code released; HF daily papers: 17 upvotes  
   > High-resolution video matting requires preserving fine details, such as hair strands and soft transparency, while maintaining consistency across frames. Memory-based methods achieve strong matting quality by matching current-frame features with information stored from earlier…

17. **[Cross-modal Steering Vectors Exist Across Both Image and Text Generation](https://arxiv.org/abs/2610.36269)** — quality 52  
   Donghao Zeng, Nishant Subramani, Tamar Rott Shaham et al. · 2026-10-26  
   _why:_ mechanistic / causal analysis; code released; weights/data released; HF daily papers: 8 upvotes  
   > Are concepts and mechanisms unified across modalities in current AI models, or instead implemented separately for each one? We operationalize this broad question of modality unification by studying cross-modal steering: 1) finding vectors that successfully steer generation on…

18. **[The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents](https://arxiv.org/abs/2610.36077)** — quality 52  
   Weidong Tang, Ruiheng Wang, Jingxuan Zhang et al. · 2026-10-26  
   _why:_ code released; HF daily papers: 311 upvotes; 20-author team  
   > Multimodal intelligence can be viewed as human-guided co-evolution between worlds and agents through interaction. However, scaling this process faces two bottlenecks: constructing heterogeneous, verifiable environments is costly, and manual Harness iteration cannot keep pace…

19. **[ParetoRSI-Gym: Can AI Agents Improve Language Models Across Multiple Domains?](https://arxiv.org/abs/2610.34386)** — quality 56  
   Haojin Wang, Yangzhen Wu, Zeyi Chen et al. · 2026-10-25  
   _why:_ multiple benchmarks; variance / significance; code released; HF daily papers: 13 upvotes  
   > Recursive self-improvement (RSI) requires an agentic system to design, train, and evaluate its own successor. Data-driven post-training is a central part of that loop, yet existing evaluations measure it on a single benchmark, where an agent selects from a static pool or…

20. **[Work Agents: Systems, Capabilities, and Optimization](https://arxiv.org/abs/2610.35845)** — quality 52  
   Zishan Xu, Enjun Du, Mingqi Gao et al. · 2026-10-26  
   _why:_ code released; HF daily papers: 117 upvotes; 16-author team  
   > As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish…

21. **[More Memory, Better Videos? A Controlled Study of Visual Memory in Long-Video Generation](https://arxiv.org/abs/2610.35001)** — quality 53  
   Yuzhuo Chen, Huafeng Shi, Xinyu Wang et al. · 2026-10-26  
   _why:_ controlled experiments; code released; HF daily papers: 22 upvotes  
   > Long-video generators increasingly retrieve past visual observations to prevent identity drift. The intuition is compelling: more access to history should make future video more consistent. But an image can be faithful to the past and wrong for the present. Does visual memory…

22. **[HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning](https://arxiv.org/abs/2610.36374)** — quality 50  
   Fanqi Yu, Matteo Tiezzi, Cigdem Beyan et al. · 2026-10-26  
   _why:_ strong baselines; mechanistic / causal analysis; code released; accepted: NeurIPS  
   > Robotic agents operating in real-world environments must adapt continuously from a stream of multimodal demonstrations, often under constraints that preclude storing or revisiting past data. In this replay-free, single-pass lifelong imitation learning setting, sequential updates…

23. **[RynnVLA-Latent: Scaling Robotic Manipulation Foundation Models with 3D-Grounded Latent Actions](https://arxiv.org/abs/2610.34356)** — quality 54  
   Haoyu Zhao, Xingyue Zhao, Zhian Su et al. · 2026-10-25  
   _why:_ ablations; code released; HF daily papers: 28 upvotes  
   > Scaling vision-language-action (VLA) models is constrained by scarce action-labeled demonstrations and incompatible control spaces across robot embodiments. We present RynnVLA-Latent, a framework that turns heterogeneous interaction videos into scalable supervision for robot…

24. **[CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments](https://arxiv.org/abs/2610.36484)** — quality 49  
   Kianté Fernandez, Caitlin Chen, Jialu Zhou et al. · 2026-10-27  
   _why:_ reproduction / replication; contamination check; code released; accepted: NeurIPS; 28 pages  
   > Claims about the cognitive capabilities of large language models are typically tested by translating behavioral paradigms into text prompts, bypassing the visual interfaces and time pressure through which human participants actually engage with experiments. At the same time, AI…

25. **[VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation](https://arxiv.org/abs/2610.35864)** — quality 50  
   Muxi Diao, Wenbin Xu, Lele Yang et al. · 2026-10-26  
   _why:_ human evaluation; HF daily papers: 169 upvotes; 24-author team  
   > Diffusion video models produce striking clips, but they cannot reliably render an exact formula, a correct chart, a rule-consistent game or narration synchronized to on-screen events. A different route is emerging: multimodal agents that write code to render every frame and…


## Blog posts & lab write-ups (last 14 days)

1. **[How AI agents shape experts’ judgment calls](https://www.anthropic.com/research/agents-judgment-calls)** — quality 66  
   Anthropic Research · 2026-10-27  
   _why:_ variance / significance; mechanistic / causal analysis; controlled experiments; negative results / limitations; source tier 1  
   > In a randomized trial, professional analysts working with an AI coding agent went with the option the agent was randomly assigned to favor 86% of the time. We look at what this means for human oversight of AI-assisted work.

2. **[CS 2881 Fall 26: Lecture 3: Modern LLM Training and Inference](https://windowsontheory.org/2026/10/28/cs-2881-fall-26-lecture-3-modern-llm-training-and-inference/)** — quality 57  
   Windows On Theory (Boaz Barak) · 2026-10-28  
   _why:_ strong baselines; model-scale sweep; mechanistic / causal analysis; reproduction / replication; negative results / limitations; human evaluation  
   > September 17, 2026 · Boaz Barak · Scribe notes by Daniel Schwartz, Dev Desai, and Ed Gerrard Lecture Video: https://youtu.be/Lp_e8Ts5-nE Slides: Presentation slides Authors’ Intro Daniel Schwartz: I’m a second-year MS/MBA student. I worked as a PM at multiple early-stage…

3. **[The sleep framework: A new way for LLMs to retain knowledge in continual learning](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)** — quality 57  
   Google Research · 2026-10-27  
   _why:_ strong baselines; mechanistic / causal analysis; source tier 2; shared on X by 1 account  
   > Education Innovation

4. **[Concerning behavior from a popular open-weight AI model](http://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model)** — quality 57  
   cohere.com · 2026-10-26  
   _why:_ mechanistic / causal analysis; reproduction / replication; weights/data released; source tier 3; shared on X by 5 accounts  
   > Discover how untrusted open-weight AI models can potentially leak data, even when self-hosted. Learn the security risks and how to protect your enterprise.

5. **[NVIDIA Nemotron 3.5 Transcribe and Granary v2: Intelligent Multilingual Transcription You Can Prompt and Adapt](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary)** — quality 46  
   Hugging Face · 2026-10-28  
   _why:_ strong baselines; multiple benchmarks; reproduction / replication; contamination check; source tier 3  
   > 

6. **[Artificial Analysis v5 and the benchmarker's dilemma](https://www.interconnects.ai/p/artificial-analysis-v5-and-the-benchmarkers)** — quality 46  
   Interconnects (Nathan Lambert) · 2026-10-28  
   _why:_ strong baselines; multiple benchmarks; source tier 2 ⚠ hype: incredibly  
   > A sort of review of the benchmarking industry and what's missing.

7. **[Genie 4: A new generation of world simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)** — quality 48  
   Google DeepMind · 2026-10-27  
   _why:_ weights/data released; source tier 2; shared on X by 3 accounts ⚠ hype: agi, unprecedented  
   > Genie 4: our new world model unlocking unprecedented realism in real-time simulation.

8. **[Gemini 4 Carbon: Our next frontier model](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)** — quality 44  
   Google DeepMind · 2026-10-28  
   _why:_ source tier 2  
   > 

9. **[PyTorch 2.15 Release Blog](https://pytorch.org/blog/pytorch-2-15-release-blog/)** — quality 44  
   PyTorch · 2026-10-28  
   _why:_ variance / significance; reproduction / replication; source tier 3  
   > We are excited to announce the release of PyTorch® 2.15 (release notes)! The PyTorch 2.15 release features the following changes: Rewritten NCCL backend becomes the default, with a flight recorder... The post PyTorch 2.15 Release Blog appeared first on PyTorch .

10. **[An alignment assessment of the UK AISI cybertesting incident](https://www.anthropic.com/research/alignment-assessment-ukaisi)** — quality 65  
   Anthropic Research · 2026-10-23  
   _why:_ mechanistic / causal analysis; reproduction / replication; negative results / limitations; long-form (55k chars); source tier 1  
   > In a UK AISI evaluation, Mythos 5 took unsanctioned actions that impacted real people and organizations. In this post, we investigate these behaviors from Claude Mythos 5 further, to understand what they reveal about the model’s alignment.

11. **[Working with academic communities to build scientific understanding](https://openai.com/index/building-scientific-understanding-with-academic-communities)** — quality 48  
   OpenAI · 2026-10-26  
   _why:_ theory; mechanistic / causal analysis; source tier 3; shared on X by 2 accounts ⚠ hype: groundbreaking  
   > OpenAI shares model results on the Kakeya conjecture, Exponential Time Hypothesis, and quantum chromodynamics—and how researchers can verify and build on them.

12. **[Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents](https://alignment.anthropic.com/2026/red-teaming-auto-mode/)** — quality 65  
   Anthropic Alignment Science · 2026-10-22  
   _why:_ ablations; variance / significance; negative results / limitations; source tier 1  
   > Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents Alignment Science Blog Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents Alex Remedios 1* , Simon Storf 1* October 22, 2026 Fabien Roger 2 , John Hughes 2 1…


## Shared on X (last 14 days: AI-Twitter recaps, plus your timeline if configured)

1. **[The sleep framework: A new way for LLMs to retain knowledge in continual learning](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)** — quality 57  
   Google Research · 2026-10-27  
   _why:_ strong baselines; mechanistic / causal analysis; source tier 2; shared on X by 1 account  
   > Education Innovation

2. **[Concerning behavior from a popular open-weight AI model](http://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model)** — quality 57  
   cohere.com · 2026-10-26  
   _why:_ mechanistic / causal analysis; reproduction / replication; weights/data released; source tier 3; shared on X by 5 accounts  
   > Discover how untrusted open-weight AI models can potentially leak data, even when self-hosted. Learn the security risks and how to protect your enterprise.

3. **[Memory Tax: Dissecting the Net Value of Agent Memory](https://arxiv.org/abs/2610.34073)** — quality 60  
   Xuan He, Sining Zhoubian, Ruozhen Yang et al. · 2026-10-25  
   _why:_ multiple benchmarks; code released; HF daily papers: 99 upvotes; shared on X by 1 account  
   > Memory is increasingly used in long-horizon agents, yet the net value of building memory over direct retrieval from raw history remains largely unclear. Through a large-scale evaluation across multiple benchmarks and model backbones, we find many dedicated memory systems…

4. **[Genie 4: A new generation of world simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)** — quality 48  
   Google DeepMind · 2026-10-27  
   _why:_ weights/data released; source tier 2; shared on X by 3 accounts ⚠ hype: agi, unprecedented  
   > Genie 4: our new world model unlocking unprecedented realism in real-time simulation.

5. **[Rethinking Verification in Agent Harnesses](https://arxiv.org/abs/2610.34577)** — quality 51  
   Zhengxin Zhang, Erkang Zhu, Yin Lin et al. · 2026-10-25  
   _why:_ strong baselines; 65 pages; HF daily papers: 9 upvotes; shared on X by 1 account  
   > Agent harnesses enable large language models to act through tools, observe the results, and iteratively work toward a task goal. Verification checks and revises agents' work to improve output quality. Yet there is limited guidance on how harnesses should organize this effort. We…

6. **[Working with academic communities to build scientific understanding](https://openai.com/index/building-scientific-understanding-with-academic-communities)** — quality 48  
   OpenAI · 2026-10-26  
   _why:_ theory; mechanistic / causal analysis; source tier 3; shared on X by 2 accounts ⚠ hype: groundbreaking  
   > OpenAI shares model results on the Kakeya conjecture, Exponential Time Hypothesis, and quantum chromodynamics—and how researchers can verify and build on them.

7. **[Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance](https://arxiv.org/abs/2610.32555)** — quality 50  
   Antonio Ken Iannillo, Joshua Segun Owotogbe, Roberto Natella et al. · 2026-10-23  
   _why:_ code released; accepted: NeurIPS; shared on X by 1 account  
   > LLM agents increasingly rely on external tools exposed via the Model Context Protocol (MCP), yet current benchmarks assume tools respond correctly and on time, leaving agent resilience to realistic tool failures untested. We introduce MCP-Injector, a drop-in, protocol-aware…

8. **[Serving DeepSeek-V4.1-Flash at Scale: vLLM Matches DeepInfer and Scales to GB300 NVL72](https://vllm.ai/blog/2026-10-23-deepseek-v41-flash-pd-wide-ep)** — quality 46  
   vllm.ai · 2026-10-23  
   _why:_ source tier 3; shared on X by 2 accounts  
   > With P/D disaggregation and Wide-EP on a GB300 NVL72 rack, vLLM serves DeepSeek-V4.1-Flash on SemiAnalysis AgentX at 954K tokens/s per GPU at a P90 of 196 token

9. **[How Depth Growth and Looping Shape In-Context Learning in Language Models](https://arxiv.org/abs/2610.31421)** — quality 46  
   Ferdinand Kapl, Kaitlin Maile, Stefan Bauer et al. · 2026-10-22  
   _why:_ ablations; mechanistic / causal analysis; shared on X by 1 account  
   > Looped and depth-grown language models reuse computations across depth and have attracted interest for their reasoning capabilities. Building on prior suggestive evidence of improved in-context-learning (ICL), we investigate how such reuse favors ICL, including how it shapes the…

10. **[HarnessMM: Recursive Self-Improvement for Harness Token Efficiency](https://arxiv.org/abs/2610.32813)** — quality 42  
   Yuhua Jiang, Chang Xu, Feifei Gao et al. · 2026-10-23  
   _why:_ ablations; shared on X by 1 account  
   > Agent harnesses repeatedly invoke reasoning after tool feedback, even when an earlier call has already fixed the next action. We introduce HarnessMM (Harness Minus Minus), a method for improving harness token efficiency through guarded decision reuse and recursive…

11. **[TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning](https://arxiv.org/abs/2610.26754)** — quality 50  
   Liana Patel, Rishabh Ranjan, Ion Stoica et al. · 2026-10-19  
   _why:_ multiple benchmarks; mechanistic / causal analysis; code released; shared on X by 1 account  
   > Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters. On the other hand, language models process all input tokens through each model layer, resulting in significant processing costs for long-context…

12. **[BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing](https://arxiv.org/abs/2610.31633)** — quality 40  
   Hayden Prairie, Jacob M. Ryan, Taylor Berg-Kirkpatrick et al. · 2026-10-22  
   _why:_ mechanistic / causal analysis; shared on X by 1 account  
   > Looped architectures scale quality while keeping parameter count fixed by repeatedly passing activations through the same block of layers. During inference, each recurrence generates independent KV-caches, causing memory to grow linearly. To address this challenge, prior work…
