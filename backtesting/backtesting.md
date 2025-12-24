## Model Selection for Final Evaluation

During qualitative analysis of the benchmark outputs, we observed clear differences in how models grounded their technical reasoning in the provided inputs.

Only **Gemini** and **Gemma** consistently referenced **correct and meaningful price levels**, accurately extracting them from both:
- the OHLCV tabular data, and
- the accompanying chart images.

Other models generally produced **generic or weakly grounded technical explanations**, often failing to align stated support/resistance levels, trend structure, or price action commentary with the actual market data shown.

As a result, **only Gemini and Gemma are retained for the final performance evaluation phase**.

## Final Evaluation Methodology

In the final step of the benchmark, the model-generated signals from Gemini and Gemma will be **cumulatively aggregated** over time to form directional trading series.

These aggregated signals will then be evaluated using **post-hoc quantitative performance metrics**, including:

- Sharpe Ratio  
- Sortino Ratio  
- Maximum Drawdown  
- Win Rate  
- Total Return  
- Additional risk-adjusted performance measures

This evaluation is intended to assess **signal consistency and directional coherence**, not to present a deployable trading strategy.

## Status

The cumulative signal backtesting and quantitative evaluation are currently in progress.  
This section will be updated once the final backtesting results are completed.
