import json

import marimo as mo
import matplotlib.pyplot as plt
import mplfinance as mpf
import yfinance as yf

__generated_with = "0.5.2"
app = mo.App()


@app.cell
def __(mo):
    mo.md(
        """
        # Quick overview of CD Projekt Red
        """
    )
    ticker_name = "CDR.WA"
    yf_ticker = yf.Ticker(ticker_name)

    mo.md(
        f"""
        {json.dumps(yf_ticker.info, indent=2)}    
        """
    )

    period = "3mo"
    interval = "1d"
    historical_data = yf_ticker.history(
        period=period,
        interval=interval,
    )
    historical_data.tail(10)
    plot = mpf.figure(
        historical_data,
        type="candle",
        mav=(4, 30),
        volume=True,
        style="yahoo",
        figratio=(3, 2),
        figscale=1.0,
        show_nontrading=False,
        title=yf_ticker.info["longName"],
        tight_layout=True,
        warn_too_much_data=10_000,
    )

    mo.md(
        f"""
        {mo.as_html(plot)}
        """
    )


if __name__ == "__main__":
    app.run()
