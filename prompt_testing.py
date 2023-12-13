from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

device = "cuda:0"
tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-3b-4e1t")
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/stablelm-3b-4e1t",
  trust_remote_code=True,
  torch_dtype=torch.float16,
)
model.to(device)

inputs = tokenizer("The weather is always wonderful", return_tensors="pt").to(device)
tokens = model.generate(
  **inputs,
  max_new_tokens=64,
  temperature=0.75,
  top_p=0.95,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
