# Week 1 — GenAI Foundations

## Overview

This week focused on understanding the basic workflow behind Generative AI and Large Language Models (LLMs).

I worked through a practical GenAI demonstration that breaks the text generation process into several stages, from tokenization to autoregressive text generation.

## Topics Covered

* Tokenization
* Token IDs and decoding
* Embeddings
* Next-token prediction
* Logits and probabilities
* Autoregressive text generation
* Token sampling
* Hugging Face high-level APIs

## Practical Work

### 1. Tokenization

Explored how text is converted into tokens and token IDs, and how token IDs can be decoded back into text.

### 2. Embeddings

Examined how token IDs are mapped to numerical vectors using an embedding layer.

### 3. Next-Token Prediction

Explored how a pretrained language model assigns probabilities to possible next tokens and selects a likely continuation.

### 4. Text Generation

Studied autoregressive generation, where the model predicts and appends one token at a time until the generation limit is reached.

### 5. High-Level Generation API

Used the Hugging Face `pipeline()` API to perform text generation and compared it with the lower-level generation process.

## Personal Experiments

To reinforce the concepts covered during the training, I modified the original inputs and prompts and ran additional experiments:

* Tested GPT-2 tokenization with Arabic text and observed how Arabic is split into multiple tokens.
* Examined the resulting token IDs and embedding vectors for Arabic text.
* Tested next-token prediction using the prompt `Artificial intelligence is`.
* Tested autoregressive text generation using the prompt `Artificial intelligence will`.
* Used the Hugging Face `pipeline()` API with an AI-related prompt to generate text.
* Compared the different stages of prediction and generation to understand how the model processes and generates text token by token.

These experiments helped me connect the theoretical concepts with actual model behavior and better understand the difference between next-token prediction and autoregressive text generation.

## Key Learning

The main workflow explored during this week was:

```text
Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Embeddings
 ↓
Neural Network / Transformer
 ↓
Logits
 ↓
Probabilities
 ↓
Next-Token Selection
 ↓
Generated Text
```

## Tools & Technologies

* Python
* PyTorch
* Hugging Face Transformers
* GPT-2
* uv
* VS Code

## Training Materials

The practical exercises were completed as part of the AI Operations Specialist training. The repository contains my work and notes from the exercises I practiced during the training.

## Outcome

By the end of this week, I developed a practical understanding of how a language model processes text through tokenization, embeddings, prediction, and autoregressive generation.

I also gained hands-on experience experimenting with Arabic and AI-related prompts and using both low-level model operations and the Hugging Face `pipeline()` API.

