import pandas as pd


def nav_trading_gain_loss_to_airtable(df_nav_trading_gain_loss, report_date, fund_code):
    
    df_trading_gain_loss = pd.DataFrame({

        "Fund Code": fund_code,
        "Value Date": report_date,
        "Identifier": df_nav_trading_gain_loss["IsinNo"],
        "Identifier 2": df_nav_trading_gain_loss["Ticker"],
        "Description": df_nav_trading_gain_loss["IssuerName"],
        "Currency": df_nav_trading_gain_loss["CurrName"],
        "MTD PNL": df_nav_trading_gain_loss["MtdNetPNL"]

    })

    return df_trading_gain_loss

def nav_unrealized_tax_lot_to_airtable(df_nav_unrealized_tax_lot, report_date, fund_code):
    
    df_unrealized_market_value = pd.DataFrame({

        "Fund Code": fund_code,
        "Value Date": report_date,
        "Identifier": df_nav_unrealized_tax_lot["ISIN"],
        "Identifier 2": df_nav_unrealized_tax_lot["Ticker"],
        "Description": df_nav_unrealized_tax_lot["IssuerName"],
        "Currency": df_nav_unrealized_tax_lot["Currency"],
        "Qty": df_nav_unrealized_tax_lot["OpenQuantity"],
        "Market Value (Base)": df_nav_unrealized_tax_lot["MarketValueBase"]
 

    })

    df_unrealized_market_value_grouped = (
        df_unrealized_market_value
        .groupby(["Fund Code"],["Value Date"],["Identifier"],["Indentifier 2"],["Description"],["Currency"])
        .agg(**{
            "Qty": ("Qty", "sum"),
            "Market Value (Base)": ("Market Value (Base)", "sum")
        })


    )

    return df_unrealized_market_value_grouped