import humanize
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf

# Set the page configuration for Streamlit
st.set_page_config(
    layout='wide',
    page_title='FinSight',
    page_icon=':bar_chart:',
    initial_sidebar_state='expanded',
)

@st.cache_data()
def get_ticker(ticker_name: str) -> yf.Ticker:
    return yf.Ticker(ticker_name)


ticker_name = st.text_input(
    'Input ticker name', 
    value='GOOG', 
    help='Input the ticker name of the company you want to analyze. For example, "GOOG" for Alphabet Inc.'
)

ticker = yf.Ticker(ticker_name)

with st.sidebar:
    with st.container():
        st.header('Day Losers')
        resp = yf.screen('day_losers', count=5)
        for t in resp['quotes']:
            st.metric(
                label=t['symbol'] + ' - ' + t['shortName'],
                value=f'{humanize.intcomma(t["regularMarketPrice"], 2)} ({t["regularMarketChangePercent"]:.2f}%)',
                delta=f"{t['regularMarketChangePercent']:.2f}%",
                delta_color='normal',
                border=True
            )

    st.header('Notices')
    news = ticker.news
    for n in news:
        n = n['content']
        with st.container(border=True):
            column_a, column_b = st.columns([1, 3])
            column_a.image(n['thumbnail']['originalUrl'])
            column_b.markdown(f"[{n['title']}]({n['canonicalUrl']['url']})")


fast_info = ticker.fast_info
info = ticker.info

st.subheader(info['longName'])

with st.container():
    st.subheader('Ticker Information')
    a, b, c, d = st.columns(4)
    a.metric(label='Last Price', value=humanize.intcomma(fast_info['lastPrice'], 2))
    b.metric(label='Year High', value=humanize.intcomma(fast_info['yearHigh'], 2))
    c.metric(label='Year Low', value=humanize.intcomma(fast_info['yearLow'], 2))
    d.metric(label='Dividend Yield', value=f'{info['dividendYield']:.2f}%')


with st.container():
    st.subheader('Historic Prices')
    fig = px.line(
        history:=ticker.history(period='max'),
        x=history.index,
        y='Close',
        title=f'{ticker_name} - Historic Prices',
    )

    fig.update_xaxes(
        rangeselector=dict(
            buttons=list([
                dict(label='5 Days', count=5, step='day', stepmode='backward'),
                dict(label='1 Month', count=1, step='month', stepmode='backward'),
                dict(label='6 Months', count=6, step='month', stepmode='backward'),
                dict(label='This Year', count=1, step='year', stepmode='todate'),
                dict(label='1 Year', count=1, step='year', stepmode='backward'),
                dict(label='2 Years', count=2, step='year', stepmode='backward'),
                dict(label='5 Years', count=5, step='year', stepmode='backward'),
                dict(label='All', step='all')
            ])
        )
    )
    st.plotly_chart(fig)

    st.subheader('Earnings and Dividends')
    div = ticker.dividends
    earn_h = ticker.get_earnings_history()['epsActual']
    div.index = pd.to_datetime(div.index).tz_convert('UTC')
    earn_h.index = pd.to_datetime(earn_h.index).tz_localize('UTC')

    div = pd.concat([div, earn_h], axis=1)
    div.rename({'epsActual': 'Earnings'}, axis=1, inplace=True)
    div.index = div.index

    filters, div_chart = st.columns([0.25, 1])
    period = filters.radio(
        'Select period',
        options=['M', 'Y'],
        index=1,
        format_func=lambda x: 'Month' if x == 'M' else 'Year'
    )
    fig = px.bar(
        data:=div.groupby(div.index.to_period(period).astype(str)).sum().reset_index(),
        x='index',
        y=['Dividends', 'Earnings'],
        title=f'Earnings and Dividends - {ticker_name}',
        text_auto=True
    )
    div_chart.plotly_chart(fig)


a, b, c, d = st.columns(4)
a.metric('Enterprice Value', value=humanize.intword(ticker.info['enterpriseValue']))
b.metric('Market Cap', value=humanize.intword(ticker.info['marketCap']))
c.metric(label='Operational Margins', value=f'{info['operatingMargins']*100:.2f}%')
d.metric(label='Return on Assets', value=f'{info['returnOnAssets']*100:.2f}%')


with st.container():
    st.subheader('Quarterly Income Statement')
    qis: pd.DataFrame = ticker.quarterly_income_stmt
    qis: pd.DataFrame = qis.transpose()
    qis.index = pd.to_datetime(qis.index)
    fig = go.Figure(
        data=[
            go.Bar(x=qis.index, y=qis['Total Revenue'], marker_color='#00CC96', name='Revenue'),
            go.Bar(x=qis.index, y=(qis['Total Revenue'] - qis['Net Income']) * -1, name='Expenses', marker_color='#EF553B'),
            go.Line(x=qis.index, y=qis['Net Income'], marker_color='blue', name='Net Income', line=dict(width=2, dash='dash')),
        ]
    )
    fig.update_layout(barmode='overlay')
    st.plotly_chart(fig)


