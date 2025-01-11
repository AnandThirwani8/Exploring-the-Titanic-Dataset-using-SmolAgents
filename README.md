# EDA and ML with SmolAgents

## Overview
This repository demonstrates how to use HuggingFace SmolAgents for automating exploratory data analysis (EDA) and machine learning. SmolAgents is a lightweight yet powerful library that leverages AI agents to simplify complex workflows.

## Prerequisites
To run this repository, ensure you have the following:
- Conda 
- A `.env` file in the root directory that includes your Google API key

## Setup
```bash
git clone https://github.com/AnandThirwani8/Exploring-the-Titanic-Dataset-using-SmolAgents.git
cd Exploring-the-Titanic-Dataset-using-SmolAgents

conda create --name smolagents101 python=3.10
conda activate smolagents101
pip install -r requirements.txt

python DataAgent.py
```

After running the script, you will see the message like the following:
```bash
Running on local URL: http://127.0.0.1:7860
```
Open this URL in your browser to start interacting with the application.
