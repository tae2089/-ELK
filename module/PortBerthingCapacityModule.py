

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import scipy.cluster.hierarchy as shc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.transform import factor_cmap, factor_mark
import numpy as np
class BerthingCapacity:
    def __init__(self):
            pass

    def test22():
        dd = BerthingCapacity()
        data = pd.read_csv(
            '/home/ubuntu/myflask/static/data/handling_capacity_test.csv', sep=',')

        # 데이터프레임 만들기
        df = pd.DataFrame(
            data, columns=['Cargo Handling Capacity', 'Load/Capacity'])

        # 스케일링
        scaler = MinMaxScaler()
        df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
        df_scaled.head()

        # 군집분석 수행
        clusters = shc.linkage(y=df_scaled, method='ward', metric='euclidean')
        cut_tree = shc.fcluster(clusters, t=0.55, criterion='distance')
        a = cut_tree.tolist()

        cut_tree1 = list(map(lambda x: str(x), a))

        # 기존 데이터프레임에 군집분석결과와 부두명 추가
        df_scaled['Port_dockname'] = data.Port_dockname
        df_scaled['cluster'] = cut_tree1
        # 기존 데이터프레임에 군집분석결과와 부두명 추가

        # 여기 아래부터 웹에 띄울것들
        # 보케 시각화 시각화
        tips = ColumnDataSource(df_scaled)
        clusters = ['1', '2', '3', '4']
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
        p = figure(title='Cargo Handling Capacity Analysis', x_axis_label='Cargo Handling Capacity ',
                    y_axis_label='Load/Capacity', plot_width=400, plot_height=400)
        p.scatter(x='Cargo Handling Capacity', y='Load/Capacity', source=tips,
                    color=factor_cmap('cluster', colors, clusters), legend_field='cluster')
        script, div = components(p)
        cluster_statistics = df_scaled.groupby('cluster')
        df1 = cluster_statistics.mean()
        a = []
        df1_column = list(df1.columns.values)
        for i in range(0, len(df1)):
            port_json = {
                "number": i,
                df1_column[0]: df1.iloc[i, 0],
                df1_column[1]: df1.iloc[i, 1],
            }

            a.append(port_json)


        cluster1 = df_scaled.loc[[13, 29], ['cluster', 'Port_dockname']]
        cluster2 = df_scaled.loc[[1, 15, 16, 17, 21, 22, 23, 31, 32, 33, 34, 35, 36], ['cluster', 'Port_dockname']]
        cluster3 = df_scaled.loc[[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14,18, 19, 20, 24, 25, 27, 28, 30, 37, 38], ['cluster', 'Port_dockname']]
        cluster4 = df_scaled.loc[[26], ['cluster', 'Port_dockname']]

        cluster1 = dd.makeList(cluster1)
        cluster2 = dd.makeList(cluster2)
        cluster3 = dd.makeList(cluster3)
        cluster4 = dd.makeList(cluster4)

        return script, div, a, cluster1,cluster2,cluster3,cluster4

    def makeList(data,c):
        print(c)
        df_column = list(c.columns.values)
        data_list = []
        for i in range(0,len(c)):
            data_json ={
                df_column[1]:c.iloc[i,1]
            }
            data_list.append(data_json)
        return data_list
        
