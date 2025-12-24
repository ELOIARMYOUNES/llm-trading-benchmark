# Multimodal LLM Trading Analysis Benchmark

An experimental benchmark for evaluating **Large Language Models (LLMs)** as **professional market analysts**, combining **OHLCV time-series data** and **price chart images**, with evaluation based on **rolling backtests and risk-adjusted quantitative metrics**.

---

## Overview

This benchmark assesses whether modern LLMs can go beyond generic financial commentary and instead:

- Interpret **numerical market data**
- Extract **price-relevant information from charts**
- Produce **grounded technical reasoning**
- Generate **consistent trading signals** that survive backtesting

Rather than focusing on single-step prediction accuracy, the benchmark emphasizes **cumulative performance, drawdown control, and risk-adjusted returns**.

---

## Task Definition

For each task, an LLM is provided with:

- **OHLCV time-series data**
- A **corresponding price chart image**

The model must generate:

1. **Trading Signal**  
   - Directional or scaled (e.g., long / short / neutral, or continuous range)

2. **Confidence Score**  
   - A normalized confidence level associated with the signal

3. **Technical Confirmations (Natural Language)**  
   - Grounded explanations such as:
     - Trend structure
     - Momentum
     - Volatility
     - Support and resistance levels

---

## Benchmark Design

### Multimodal Reasoning
The benchmark explicitly tests whether models can **cross-reference tabular data and visual price charts**, rather than relying on generic financial templates.

### Rolling Backtesting Framework
- **Start date:** 2025-01-01  
- **Initial window:** ~60 trading days  
- **Planned extension:** 180 trading days  
- Signals are generated **sequentially and cumulatively applied**, simulating real-time decision-making.

---

## Models Evaluated

The benchmark currently evaluates **9 LLMs**, including:

- DeepSeek
- Gemini
- Gemma
- Qwen
- Claude Haiku  
- (others may be added)

At a surface level, most models complete the task.  
However, deeper qualitative analysis shows that **only Gemini and Gemma consistently extract and reference correct price levels** from both chart images and OHLCV data.

As a result, only these models advance to the **final quantitative backtesting stage**.

---

## Evaluation Metrics

Final strategy performance is evaluated using **advanced quantitative finance metrics**, including:

- **Sharpe Ratio**
- **Sortino Ratio**
- **Maximum Drawdown**
- **Win Rate**
- **Total Return**
- Additional volatility- and downside-risk–adjusted measures

This ensures models are assessed on **risk-adjusted consistency**, not just raw returns.

---

## Key Findings (Preliminary)

- Passing a task syntactically does **not** imply usable trading reasoning.
- Many LLMs produce fluent but **weakly grounded technical confirmations**.
- **Gemini and Gemma** demonstrate superior multimodal grounding by:
  - Correctly identifying price levels
  - Aligning explanations with observed chart structure
  - Maintaining internal consistency between signal and reasoning

Final performance metrics will be reported after cumulative backtesting is completed.

---

## Limitations

- This benchmark is **not a trading system** and makes no claims of profitability.
- Results are sensitive to:
  - Prompt design
  - Signal schema
  - Backtesting assumptions
- Market regime coverage is currently limited and will expand with longer horizons.

---

## Future Work

- Extend backtesting to **180+ trading days**
- Add regime-specific analysis (trending vs ranging markets)
- Introduce signal calibration and ensemble aggregation
- Expand model coverage and prompt robustness testing

---

## Disclaimer

This project is for **research and benchmarking purposes only**.  
It does **not constitute financial advice** or a recommendation to trade real capital.

---

## Links

- Kaggle Benchmark Tasks: [https://www.kaggle.com/benchmarks/youneseloiarm/es-trading-professional-analysis/leaderboard]
- Discussion / Analysis: [ADD LINK]
- Author: Younes Eloiarm

---

## License

MIT License

---

## Tags

`LLMs` · `Multimodal AI` · `Quantitative Finance` · `Trading Benchmarks` · `OHLCV` · `Time Series`

