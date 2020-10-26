
import pandas as pd
import scipy.cluster.hierarchy as shc
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class LabourCapacity:
    def __init__(self):
            pass

        
    def test22():
            # 데이터 불러오기
        dd = LabourCapacity()
        data = pd.read_csv(
            '/home/ubuntu/myflask/static/data/berth_capacity_test.csv', sep=',')

        # 데이터프레임 만들기
        df = pd.DataFrame(data, columns=['Number of vessel used/Space Capacity', 'Long wait vessel Ratio', 'Average berth Time'])

        # 스케일링
        scaler = MinMaxScaler()
        df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

        # 군집분석 수행
        clusters = shc.linkage(y=df_scaled, method='ward', metric='euclidean')
        cut_tree = shc.fcluster(clusters, t=4, criterion='maxclust')
        cut_tree
        a = cut_tree.tolist()

        cut_tree1 = list(map(lambda x: str(x), a))

        # 기존 데이터프레임에 군집분석결과와 부두명 추가
        df_scaled['Port_dockname'] = data.Port_dockname
        df_scaled['cluster'] = cut_tree1
        fig = px.scatter_3d(df_scaled, x='Number of vessel used/Space Capacity', y='Long wait vessel Ratio', z='Average berth Time',
                            color='cluster', title="Berth Capacity Analysis", width=430, height=500)
        json_data = fig.to_json()
        cluster_statistics = df_scaled.groupby('cluster')
        df1 = cluster_statistics.mean()
        a = []
        df1_column = list(df1.columns.values)
        for i in range(0, len(df1)):
            port_json = {
                "number":i,
                df1_column[0]: df1.iloc[i, 0],
                df1_column[1]: df1.iloc[i, 1],
                df1_column[2]: df1.iloc[i, 2]
            }
            
            a.append(port_json)
        cluster1 = df_scaled.loc[[9, 17], ['cluster', 'Port_dockname']]
        cluster2 = df_scaled.loc[[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 18, 20, 21, 22, 23,
                                24, 25, 26, 28, 29, 30, 31, 32, 35, 36, 37, 38, 39, 41, 43, 44], ['cluster', 'Port_dockname']]
        cluster3 = df_scaled.loc[[27, 40, 42], ['cluster', 'Port_dockname']]
        cluster4 = df_scaled.loc[[15, 16, 19, 33, 34], ['cluster', 'Port_dockname']]

        cluster1 = dd.makeList(cluster1)
        cluster2 = dd.makeList(cluster2)
        cluster3 = dd.makeList(cluster3)
        cluster4 = dd.makeList(cluster4)

        return json_data,a,cluster1,cluster2,cluster3,cluster4

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

    def test():
        # Create some data.
        x = np.linspace(0, 2*np.pi, 20)
        y = np.sin(x)
        # Create a new plot with a title and axis labels
        p = figure(title="Simple Line Plot in Bokeh",x_axis_label='x', y_axis_label='y')
        # Add a line renderer with legend and line thickness
        p.line(x, y, legend="Value", line_width=3)
        script,div = components(p)
        return script,div
