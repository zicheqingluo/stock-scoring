#! /usr/bin/env python
# *_*coding:utf-8*_*

import akshare as ak


def historyDayK(symbol, sd, ed):
    stock_zh_a_hist_df = ak.stock_zh_a_hist(
        symbol=symbol,
        period="daily",
        start_date=sd,
        end_date=ed,
        adjust="",
    )
    print(stock_zh_a_hist_df)


def lhb(date):
    lhbData = ak.stock_lhb_stock_statistic_em(
        symbol=date)
    print(lhbData.loc[lhbData['名称']=='平安电工'])
    


if __name__ == "__main__":
    # historyDayK()
    lhb("近一月")
