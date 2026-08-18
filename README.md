<div align="center">
<h2>UniCSG: Unified High‑Fidelity Content‑Constrained Style‑Driven Generation via Staged Semantic and Frequency Disentanglement</h2>

Jingwei Yang<sup>1</sup>, Ruoxi Wu<sup>2,*</sup>, Wei Shen<sup>2</sup>, Meng Li<sup>2</sup>, Yulong Liu<sup>2</sup>, Huimin She<sup>2</sup>, Lunxi Yuan<sup>2</sup>

<sup>1</sup> China University of Mining and Technology, Beijing, China
<br>
<sup>2</sup> OPPO Artificial Intelligence Center, Beijing, China
<br>
<sup>*</sup> Corresponding Author
</div>

<br>

## 📖 Introduction
![UniCSG Overview](./assets/teaser_figure.jpg)
Style transfer must match a target style while preserving content semantics. DiT-based diffusion models often suffer from content–style entanglement, leading to reference-content leakage and unstable generation. We present UniCSG, a uniffed framework for content-constrained, style-driven generation in both text-guided and reference-guided settings. UniCSG employs staged training: (i) a latent-space semantic disentanglement stage that combines low-frequency preprocessing with conditioning corruption to encourage content–style separation, and (ii) a latent-space frequency-aware detail reconstruction stage that reffnes details via multiscale frequency supervision. We further incorporate pixel-space reward learning to align latent objectives with perceptual quality after decoding. Experiments demonstrate improved content faithfulness, style alignment, and robustness in both settings.

## 🚀 Quick Start
### 1. Environment Setup
```bash
# Clone DiffSynth base repo
git clone https://github.com/modelscope/DiffSynth‑Studio.git
cd DiffSynth‑Studio
pip install -e .
```

### 2. Model Base & Resource Info
- Backbone Base Model: [Qwen‑Image‑Edit‑2509](https://huggingface.co/Qwen/Qwen-Image-Edit-2509)
- Acceleration LoRA: [Qwen‑Image‑Lightning](https://huggingface.co/lightx2v/Qwen-Image-Lightning)
- UniCSG task‑specific LoRAs: coming soon
- Dataset: Built on [OmniConsistency](https://github.com/showlab/OmniConsistency) & [OmniStyle](https://github.com/StyleX-Research/OmniStyle)
- Evaluation Benchmark: CSG‑Bench

### 3. Inference
```bash
# Text-Guided Image Style Transfer
CUDA_VISIBLE_DEVICES=0 python inference_text_guided.py

# Reference-Guided Image Style Transfer
CUDA_VISIBLE_DEVICES=0 python inference_reference_guided.py
```

## 📅 Release Schedule
- Full training code: Coming soon
- UniCSG task‑specific LoRAs: Coming soon

## 📌 Citation
If our work is helpful to your research, please cite our paper:
```bibtex
@misc{yang2026unicsgunifiedhighfidelitycontentconstrained,
      title={UniCSG: Unified High-Fidelity Content-Constrained Style-Driven Generation via Staged Semantic and Frequency Disentanglement}, 
      author={Jingwei Yang and Ruoxi Wu and Wei Shen and Meng Li and Yulong Liu and Huimin She and Lunxi Yuan},
      year={2026},
      eprint={2604.17850},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2604.17850}, 
}
