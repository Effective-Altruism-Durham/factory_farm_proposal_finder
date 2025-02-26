# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="open-paws/effect_on_animals_prediction")
result = pipe("I am starting a veterinary practice.")
print(result)
