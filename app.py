from bokeh.resources import INLINE
from flask import Flask,render_template

from module.PortTrafficVolumeModule import TrafficVolume
from module.PortLabourCapacityModule import LabourCapacity
from module.PortBerthingCapacityModule import BerthingCapacity

app = Flask(__name__)

@app.route('/')
def hello():
   return render_template("intro.html")

@app.route('/test1')
def hello1():
   return render_template("RealTimeVessl.html")

@app.route('/test2')
def hello2():
   return render_template("RealTimePort.html")

@app.route('/test3')
def hello3():
    script, div, df,c1,c2,c3,c4 = BerthingCapacity.test22()
    #건드리면 안되는 거
    print(c1)
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    html = render_template(
        'PortBerthingCapacity.html',
        script=script,
        div=div,
        df1 = df,
        c1 = c1,
        c2 = c2,
        c3 = c3,
        c4 = c4,
        js_resources=js_resources,
        css_resources=css_resources
    )
    return html


@app.route('/test4')
def hello4():
        bar, df,c1,c2,c3,c4 = LabourCapacity.test22()
        #건드리면 안되는 거
        js_resources = INLINE.render_js()
        css_resources = INLINE.render_css()
        html = render_template(
            'PortLabourCapacity.html',
            plot=bar,
            df= df,
            c1 = c1,
            c2 = c2,
            c3 = c3,
            c4 = c4,
            js_resources=js_resources,
            css_resources=css_resources
        )
        return html


@app.route('/test5')
def hello5():
    bar,df1 = TrafficVolume.test25()
    bar2,df2 = TrafficVolume.test24()
    bar3 ,df3 = TrafficVolume.test23()
    #건드리면 안되는 거
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    html = render_template(
        "PortTrafficVolume.html",
        plot1=bar,
        plot2=bar2,
        plot3 = bar3,
        df1=df1,
        df2=df2,
        df3=df3,
        js_resources=js_resources,
        css_resources=css_resources
    )
    return html

@app.route('/test6')
def test():
   return render_template('intro1.html')



   #return '<iframe src="http://3.35.113.255:5602/goto/6df42ddbceccea7038b68b52e2e0799b" height="600" width="800"></iframe>'
#if __name__ == "__main__":
#    app.run(host='0.0.0.0')
