@kbench.task(
    name="ES_Trading_Professional_Analysis",
    description=(
        "Generate professional trader-style analysis including signal, "
        "confidence, and technical confirmations using OHLCV data and chart image."
    )
)
def predict_es_professional_analysis(
    llm,
    tabular_data: pd.DataFrame,
    chart_image_path: str,
    prediction_date: str,
) -> None:
    """
    SDK-compliant:
    - Generates rich TEXT analysis
    - DOES NOT return dict / JSON
    - Output is printed/logged only
    """

    # --------------------------------------------------------------------------
    # A. TABULAR SUMMARY
    # --------------------------------------------------------------------------
    recent = tabular_data.tail(10)

    data_summary = f"""
RECENT 10-DAY OHLCV DATA:
{recent[['date', 'open', 'high', 'low', 'close', 'volume']].to_string(index=False)}

STATS:
- Last Close: {recent.iloc[-1]['close']:.2f}
- 10D High: {recent['high'].max():.2f}
- 10D Low: {recent['low'].min():.2f}
- Avg Volume: {recent['volume'].mean():.0f}
- Trend Direction: {"UP" if recent.iloc[-1]['close'] > recent.iloc[0]['close'] else "DOWN"}
"""

    # --------------------------------------------------------------------------
    # B. LOAD IMAGE → BASE64 → SEND
    # --------------------------------------------------------------------------
    chart_path = Path(chart_image_path)
    if not chart_path.exists():
        kbench.assertions.fail(f"Chart not found: {chart_image_path}")

    with open(chart_path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    image = images.from_base64(image_base64)
    kbench.user.send(image)

    # --------------------------------------------------------------------------
    # C. PROMPT (PROFESSIONAL TRADER STYLE)
    # --------------------------------------------------------------------------
    response = llm.prompt(
        f"""
You are a professional futures trader preparing a daily trading plan.

Market: ES Futures
Date: {prediction_date}

You are provided with:
1) Recent OHLCV data
2) A price chart image

YOUR TASK:
Write a professional trading assessment exactly like a discretionary trader would.

Your analysis MUST include:

1. **Directional Signal**:
   - A numeric signal between -1 and +1

2. **Trade Bias**:
   - Buy / Sell / Wait

3. **Confidence Level**:
   - A numeric confidence between 0 and 1

4. **Technical Confirmation**:
   - Trend assessment
   - Key support & resistance levels
   - Chart pattern or price action signal
   - Momentum or volume confirmation

STYLE REQUIREMENTS:
- Clear
- Concise
- Professional trading desk tone
- No JSON
- No bullet overload
- Natural language

This is NOT a numeric benchmark task.
Write a full professional trading note.
"""
    ).strip()

    # --------------------------------------------------------------------------
    # D. BASIC SANITY ASSERTIONS (TEXT EXISTS)
    # --------------------------------------------------------------------------
    kbench.assertions.assert_not_empty(
        response,
        expectation="Model must produce a professional trading analysis",
    )

    # Optional: ensure signal & confidence appear in text
    kbench.assertions.assert_contains_regex(
        r"[-+]?(0(\.\d+)?|1(\.0+)?)",
        response,
        expectation="Analysis should contain a numeric signal or confidence",
    )

    # --------------------------------------------------------------------------
    # E. LOG OUTPUT (VISIBLE IN NOTEBOOK)
    # --------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print(f"ES PROFESSIONAL TRADING ANALYSIS — {prediction_date}")
    print("=" * 80)
    print(response)
    print("=" * 80)
