# Task Definition — ES Professional Trading Analysis

## Overview
This benchmark evaluates how well Large Language Models (LLMs) can generate
**professional discretionary trading analysis** using **both tabular market data
and chart images**.

The task simulates a real-world futures trading desk workflow rather than a
purely numeric prediction problem.

---

## Market Context
- **Instrument**: E-mini S&P 500 Futures (ES)
- **Frequency**: Daily
- **Prediction Horizon**: Next trading day
- **Date Example**: 2025-01-01

---

## Inputs Provided to the Model

Each model receives:

1. **Recent OHLCV data**
   - Open, High, Low, Close, Volume
   - Recent window (e.g., last 10 trading days)

2. **Price Chart Image**
   - Visual candlestick or price chart
   - Intended to test visual reasoning and pattern recognition

---

## Model Task

The model must generate a **professional trading assessment**, written in
natural language, exactly as a discretionary futures trader would prepare a
daily trading plan.

This is **not** a numeric-only benchmark.

---

## Required Output Components

The analysis **must include all of the following**:

### 1. Directional Signal
- A numeric signal between **-1 and +1**
- Indicates bearish to bullish bias

### 2. Trade Bias
- One of:
  - **Buy**
  - **Sell**
  - **Wait**

### 3. Confidence Level
- A numeric confidence score between **0 and 1**

### 4. Technical Confirmation
Qualitative justification including:
- Trend assessment
- Key support and resistance levels
- Chart pattern or price action signal
- Momentum and/or volume confirmation

---

## Style Requirements

- Professional trading desk tone
- Clear and concise
- Natural language only
- **No JSON**
- **No structured key-value outputs**
- Avoid excessive bullet points
- Human-like discretionary reasoning

---

## Evaluation Philosophy

This benchmark focuses on **qualitative reasoning quality**, including:
- Market coherence
- Consistency between signal, bias, and explanation
- Use of both numerical and visual inputs
- Realism of professional trading logic

There is no single “correct” answer.
Models are evaluated comparatively based on reasoning depth,
clarity, and professional plausibility.

---

## Non-Goals

- This is **not** a price forecasting benchmark
- This is **not** a classification or regression task
- Exact numeric accuracy is not the primary objective
