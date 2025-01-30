# # Connections Game AI Solver

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

An AI-powered solution to the New York Times Connections puzzle, leveraging language model fine-tuning and semantic similarity approaches.

## Project Overview
This repository contains two distinct AI approaches to solve the Connections game:
1. **Word2Vec-based Solution**: Utilizes pretrained word embeddings fine-tuned on game-specific data
2. **LLM Fine-tuning Approach**: Implements a fine-tuned GPT-2 model with custom prompt engineering

Our methodology focuses on adapting general-purpose language models to the specific constraints and patterns of the Connections puzzle through targeted fine-tuning.

## Features
- Dual-model architecture for category prediction
- Custom fine-tuning pipeline for word embeddings
- Prompt-engineered GPT-2 model for contextual understanding
- Adaptive thresholding for category similarity detection
- Game-specific data preprocessing and augmentation

## Approach

### Word2Vec Fine-tuning
- Initialized with pretrained embeddings
- Domain adaptation using limited training games
- Similarity-based clustering with game constraints
- Dynamic category boundary detection

### GPT-2 Fine-tuning
- Custom prompt template for game context
- Few-shot learning architecture
- Output constrained to valid game categories
- Context-aware prediction refinement

## Dataset
- Curated set of Connections game instances
- Augmented with semantically similar terms
- Structured as (category, words) pairs
- Includes negative samples for contrastive learning

## Installation

```bash 
git clone https://github.com/yourusername/connections-ai-solver.git
cd connections-ai-solver
pip install -r requirements.txt
```

## Usage
```python
# Word2Vec approach
from word2vec_solver import solve_connections
solution = solve_connections(word_list)

# GPT-2 approach
from gpt_solver import GPTConnectionsSolver
solver = GPTConnectionsSolver()
solution = solver.solve(word_list)
```

## Results
Initial experiments show:
- 68% accuracy on seen categories (Word2Vec)
- 72% accuracy on novel categories (GPT-2)
- 85% precision in category boundary detection