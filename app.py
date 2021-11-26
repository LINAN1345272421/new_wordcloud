from flask import Flask, render_template, jsonify, request

import test
import until

app = Flask(__name__)
#页面跳转
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/word')
def word():
    return render_template("word.html")


#柱状图
@app.route('/bar')
def bar():
    data=test.class_text_num()
    data_values=[]
    data_name = []
    for num,class_name in data:
        data_values.append(num)
        data_name.append(class_name)
    print( data_values)
    print(data_name)
    return jsonify({"name":data_name,"values":data_values})

#返回树形结构
@app.route('/tree')
def tree():
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    h=[]
    i=[]
    j=[]
    k=[]
    a=test.deep_2("体育")
    b=test.deep_2("综合体育最新")
    c=test.deep_2("军事")
    d=test.deep_2("娱乐")
    e=test.deep_2("体育焦点")
    f=test.deep_2("房产")
    g=test.deep_2("教育")
    h=test.deep_2("汽车")
    i=test.deep_2("游戏")
    j=test.deep_2("科技")
    k=test.deep_2("财经")
    print(i)
    return jsonify({"a": a, "b": b,"c":c,"d":d,"e":e,"f":f,"g":g,"h":h,"i":i,"j":j,"k":k})
    pass

#详情数据展示包括云图
@app.route("/tree_details")
def tree_details():
    title_name = request.values.get("title")
    values=test.find_content_by_title(title_name)
    return render_template("details.html",values=values[0],title=title_name)
#词云图数据单个文章
@app.route("/word_cloud_date")
def word_cloud_date():
    title_name = request.values.get("title")
    values = test.find_content_by_title(title_name)
    word_top=until.word_top_string(values[0][0])
    print(word_top)
    word_cloud_num=[]
    flag=0;
    for i in word_top:
        word_cloud_num.append({"name":i[0],"value":i[1]})
        flag=flag+1;
        if(flag>30):
            break
    return jsonify({"data":word_cloud_num})




#词云图通过type区别
@app.route("/word_cloud_data_type")
def word_cloud_data_type():
    type = request.values.get("type")
    print(type)
    articlelist=until.find_word_bySql(type)
    word_cloud_num=[]
    flag=0
    for i in articlelist:
        word_cloud_num.append({"name":i[0],"value":i[1]})
        flag=flag+1;
        if(flag>100):
            break
    return jsonify({"data":word_cloud_num})
    pass


if __name__ == '__main__':
    app.run()
