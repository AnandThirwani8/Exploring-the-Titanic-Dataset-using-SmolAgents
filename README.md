# EDA and ML with SmolAgents

## Overview
This repository demonstrates how to use HuggingFace SmolAgents for automating exploratory data analysis (EDA) and machine learning. SmolAgents is a lightweight yet powerful library that leverages AI agents to simplify complex workflows.

## Prerequisites
To run this repository, ensure you have the following:
- Conda 
- A`.env` file in the root directory that includes your Google API key
```bash
env GOOGLE_API_KEY=your-google-api-key-here
```

## Setup
```bash
git clone https://github.com/AnandThirwani8/Exploring-the-Titanic-Dataset-using-SmolAgents.git
cd Exploring-the-Titanic-Dataset-using-SmolAgents
conda create --name smolagents101 python=3.10
conda activate smolagents101
pip install -r requirements.txt
python DataAgent.py
```
