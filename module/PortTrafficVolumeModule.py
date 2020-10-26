import scipy.cluster.hierarchy as shc
import seaborn as sns
import pandas as pd
import plotly.io as pio
from fbprophet.plot import plot_plotly
from fbprophet import Prophet

class TrafficVolume:
    def __init__(self):
        pass

    def test23():
        data = pd.read_csv(
            '/home/ubuntu/myflask/static/data/car.csv')
        df = pd.DataFrame({'ds': data['Month'], 'y': data['Monthly volume of car']})
        # 예측 model 생성
        m = Prophet(interval_width=0.90, changepoint_prior_scale=4)
        m.fit(df)
        # 예측할 2020 데이터프레임 만들기
        future = m.make_future_dataframe(periods=5, freq='MS')
        # 여기 아래부터 웹에 띄울 것들
        # 2020 8월 ~ 12월 예측 결과 표
        forecast = m.predict(future)
        # 예측 그래프 plotly로 그리기
        fig = plot_plotly(m, forecast, figsize=(480,500 ))
        json_data = fig.to_json()
        df1 = forecast[['ds', 'yhat_lower', 'yhat', 'yhat_upper']].tail()
        df1_column = list(df1.columns.values)
        a = []
        for i in range(0, len(df1)):
            port_json = {
                df1_column[0]: df1.iloc[i, 0],
                df1_column[1]: df1.iloc[i, 1],
                df1_column[2]: df1.iloc[i, 2],
                df1_column[3]: df1.iloc[i, 3]
            }
            a.append(port_json)
        return json_data,a

    def test24():
        data = pd.read_csv(
            '/home/ubuntu/myflask/static/data/chemical.csv')
        df = pd.DataFrame(
            {'ds': data['Month'], 'y': data['Monthly volume of chemical product']})
        # 예측 model 생성
        m = Prophet(interval_width=0.90, changepoint_prior_scale=0.08)
        m.fit(df)
        # 예측할 미래 데이터프레임 만들기
        future = m.make_future_dataframe(periods=5, freq='MS')
        # 여기 아래부터 웹에 띄울 것들
        # 2020 8월 ~ 12월 예측 결과 표
        forecast = m.predict(future)
        df1 = forecast[['ds', 'yhat_lower', 'yhat', 'yhat_upper']].tail()
        # 예측 그래프 plotly로 그리기
        fig = plot_plotly(m, forecast, figsize=(480, 500))
        json_data = fig.to_json()
        a = []
        df1_column = list(df1.columns.values)
        for i in range(0, len(df1)):
            port_json = {
                df1_column[0]: df1.iloc[i, 0],
                df1_column[1]: df1.iloc[i, 1],
                df1_column[2]: df1.iloc[i, 2],
                df1_column[3]: df1.iloc[i, 3]
            }
            a.append(port_json)
        return json_data, a

    def test25():
        # 원유 데이터 가져오기 & dataframe 생성
        data = pd.read_csv(
            '/home/ubuntu/myflask/static/data/oil.csv')
        df = pd.DataFrame({'ds': data['Month'], 'y': data['Monthly volume of oil']})
        # 예측 model 생성
        m = Prophet(interval_width=0.90, changepoint_prior_scale=5,
                    yearly_seasonality=15)
        m.fit(df)
        # 예측할 미래 데이터프레임 만들기
        future = m.make_future_dataframe(periods=5, freq='MS')
        # 여기 아래부터 웹에 띄울 것들
        # 2020 8월 ~ 12월 예측 결과 표
        forecast = m.predict(future)
        df1 = forecast[['ds', 'yhat_lower', 'yhat', 'yhat_upper']].tail()
        # 예측 그래프 plotly로 그리기
        fig = plot_plotly(m, forecast, figsize=(480, 500))
        json_data = fig.to_json()
        a = []
        df1_column = list(df1.columns.values)
        for i in range(0, len(df1)):
            port_json = {
                df1_column[0]: df1.iloc[i, 0],
                df1_column[1]: df1.iloc[i, 1],
                df1_column[2]: df1.iloc[i, 2],
                df1_column[3]: df1.iloc[i, 3]
            }
            a.append(port_json)
        return json_data, a
