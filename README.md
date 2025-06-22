# AI Experiments & Research Lab

This repository serves as my personal laboratory for exploring and experimenting with various cutting-edge AI technologies, focusing on areas like Generative AI, Agentic AI, and Model Context Protocol (MCP).

## 🗂 Project Catalog

### 1. Machine Learning Basics
- **[ML Hello World](./ml-hello-world/README.md)**
  - Simple linear regression example using TensorFlow
  - Demonstrates basic neural network concepts
  - Example: Predicting values using y = 5x + 5 relationship

### 2. Generative AI
- **[Stable Diffusion Implementation](./stable-diffusion/README.md)**
  - Text-to-image generation optimized for Apple Silicon
  - Uses Metal Performance Shaders (MPS) for hardware acceleration
  - Example: Generating creative images from text prompts

### 3. Agentic AI (Planned)
- Autonomous AI agents that can:
  - Perform complex tasks through decomposition
  - Interact with their environment
  - Make decisions and learn from outcomes
- Implementation examples:
  - Task planning and execution
  - Multi-agent collaboration
  - Environment interaction

### 4. Model Context Protocol (MCP)
- **[Weather MCP Server](./mcp-server-weather/README.md)**
  - Integrates with Open-Meteo API for weather data
  - Demonstrates async API handling in MCP
  - Example: Getting current weather conditions by coordinates

- **[GitHub Models Helper](./gh-models-helper/README.md)**
  - Interacts with GitHub's AI models
  - Compare responses from different models
  - Features model listing, metadata, and response comparison
  - Example: Comparing GPT-4, Claude, and other models' responses

## 🎯 Goals

1. **Experimentation**: Test and validate different AI approaches and technologies
2. **Learning**: Document insights and learnings from each implementation
3. **Innovation**: Combine different technologies to create novel solutions
4. **Sharing**: Provide clear documentation and examples for others to learn from

## 📚 Project Structure

```
.
├── README.md                 # Main documentation
├── inference-example/       # ML model inference example
│   ├── inference.py        # Inference script
│   ├── training.py         # Model training script
│   └── README.md          # Documentation
├── ml-hello-world/         # Basic ML experiments
│   ├── hello-model.py      # Linear regression implementation
│   └── README.md          # ML-specific documentation
├── stable-diffusion/       # Stable Diffusion experiments
│   ├── image.py           # Image generation implementation
│   └── README.md          # SD-specific documentation
├── mcp-server-weather/     # Weather MCP server
│   ├── server.py          # Weather API integration
│   └── README.md          # Documentation
├── gh-models-helper/       # GitHub Models MCP server
│   ├── src/               # TypeScript source files
│   └── README.md          # Documentation
└── agentic-ai/            # (Planned) Agentic AI experiments
```

## 🛠 Technologies Used

- Python 3.9+
- TensorFlow
- PyTorch
- Hugging Face Transformers
- Diffusers
- More to be added as experiments grow

## 🚀 Getting Started

Each project directory contains its own README with specific setup instructions and requirements. Navigate to the specific project you're interested in to get started.

## 📝 Documentation Standards

Each experiment/project includes:
1. Clear explanation of concepts
2. Implementation details
3. Setup instructions
4. Usage examples
5. Results and observations

## 🤝 Contributing

Feel free to:
- Open issues for discussion
- Submit pull requests with improvements
- Share your own experiments
- Suggest new areas of exploration

## 📄 License

This repository is MIT licensed unless otherwise specified in individual project directories.

---

> 🔬 This is an active research repository, and new experiments are added regularly. Check back often for updates!