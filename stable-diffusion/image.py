from diffusers import StableDiffusionPipeline
import torch

model_id = "sd-legacy/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("mps")  # Using MPS backend for Mac

prompt = "a majestic golden retriever pilot wearing mirror aviator sunglasses and a leather flight jacket, sitting in the cockpit of an F-16 fighter jet, dramatic sunset lighting, dynamic angle, high detail, professional photography, dramatic sky background, volumetric lighting, 4k, highly detailed"
image = pipe(prompt).images[0]

image.save("dog-in-air.png")