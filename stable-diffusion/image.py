from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe = pipe.to("mps")

prompt = "a golden retriver wearing aviator glasses flying a fighter jet "
image = pipe(prompt).images[0]

image.save("dog-in-air.png")