import marimo

__generated_with = "0.5.2"
app = marimo.App()


@app.cell
def __():
    import json

    import matplotlib.pyplot as plt
    import mplfinance as mpf
    import yfinance as yf
    import marimo as mo
    return json, mo, mpf, plt, yf


@app.cell
def __(mo):
    mo.md("""
    # Quick overview of CD Projekt Red
    """)
    return


@app.cell
def __(json, yf):
    ticker_name = "CDR.WA"
    yf_ticker = yf.Ticker(ticker_name)
    json.dumps(yf_ticker.info, indent=2)
    return ticker_name, yf_ticker


@app.cell
def __(yf_ticker):
    period = "3mo"
    interval = "1d"
    historical_data = yf_ticker.history(
        period=period,
        interval=interval,
    )
    historical_data.tail(10)
    return historical_data, interval, period


@app.cell
def __(historical_data, mo, mpf, yf_ticker):
    plot = mpf.plot(
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
    return plot,


if __name__ == "__main__":
    app.run()
