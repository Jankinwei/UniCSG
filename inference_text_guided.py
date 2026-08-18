import torch
from PIL import Image
from diffsynth.pipelines.qwen_image import QwenImagePipeline, ModelConfig
import os

pipe = QwenImagePipeline.from_pretrained(
    torch_dtype=torch.bfloat16,
    device="cuda",
    model_configs=[
        ModelConfig(
            model_id="Qwen/Qwen-Image-Edit-2509",
            download_source='huggingface',
            origin_file_pattern="transformer/diffusion_pytorch_model*.safetensors"
        ),
        ModelConfig(
            model_id="Qwen/Qwen-Image-Edit-2509",
            download_source='huggingface',
            origin_file_pattern="text_encoder/model*.safetensors"
        ),
        ModelConfig(
            model_id="Qwen/Qwen-Image-Edit-2509",
            download_source='huggingface',
            origin_file_pattern="vae/diffusion_pytorch_model.safetensors"
        ),
    ],
    tokenizer_config=None,
    processor_config=ModelConfig(
        model_id="Qwen/Qwen-Image-Edit-2509",
        download_source='huggingface',
        origin_file_pattern="processor/"
    ),
)

# load lora
qwen_image_style_transfer_lora_model = './Qwen-Image-Edit-2509-unicsg.safetensors'
qwen_image_speedup_lora_model = './Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors'
pipe.load_lora(pipe.dit, qwen_image_style_transfer_lora_model)
pipe.load_lora(pipe.dit, qwen_image_speedup_lora_model)


content_ref = "./test_content.jpg"  
prompt = "Transform the image into 3D Chibi style."

w, h = Image.open(content_ref).convert("RGB").size
minedge = 1024
if w > h:
    r = w / h
    h = minedge
    w = int(h * r) - int(h * r) % 16
else:
    r = h / w
    w = minedge
    h = int(w * r) - int(w * r) % 16

content_img = Image.open(content_ref).convert("RGB").resize((w, h))

# text‑guided
image = pipe(
    prompt,
    edit_image=[content_img],
    seed=123,
    num_inference_steps=4,
    height=h,
    width=w,
    edit_image_auto_resize=False,
    cfg_scale=1.0
)

save_dir = './output/'
os.makedirs(save_dir, exist_ok=True)
prefix = content_ref.split('/')[-1].split('.')[0]
out_path = os.path.join(save_dir, f'{prefix}_text_result.png')
image.save(out_path)
print(f"saved to {out_path}")
