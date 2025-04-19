from diffusers import StableDiffusionPipeline
import torch

model_id = "sd-legacy/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("mps")  # Using MPS backend for Mac

prompt = "a golden retriver wearing aviator glasses flying a fighter jet "
image = pipe(prompt).images[0]

image.save("dog-in-air.png")