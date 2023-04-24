import streamlit as st
import pandas as pd
from  sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import altair as alt
import datetime

st.title('随机森林相关展示')
def random_feature():
    max_depth = st.sidebar.slider('max_depth',5,100,6)
    n_estimators = st.sidebar.slider('n_estimators',100,1000,100)
    feature_dict = {'max_depth':max_depth,
                    'n_estimators':n_estimators
                    }
    return feature_dict
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length, 'sepal_width': sepal_width,
            'petal_length': petal_length, 'petal_width': petal_width}
    st.sidebar.write(data)
    features = pd.DataFrame(data, index=[0])
    st.markdown(':red[这里是数据特征]')
    st.header(':red[这里是数据特征]')
    st.caption(':red[这里是数据特征]')
    st.write(features)
    return features

code = '''
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length, 'sepal_width': sepal_width,
            'petal_length': petal_length, 'petal_width': petal_width}
    st.sidebar.write(data)
    features = pd.DataFrame(data, index=[0])
    st.markdown(':red[这里是数据特征]')
    st.header(':red[这里是数据特征]')
    st.caption(':red[这里是数据特征]')
    st.write(features)
    return features
'''
st.code(code,language='python')

st.write('这里是显示latex公式')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

df = user_input_features()
random_feature = random_feature()
# 加载Iris并训练模型
iris = datasets.load_iris()
st.header('iris数据')
st.dataframe(pd.DataFrame(iris['data'],columns=iris['feature_names']))
st.table(pd.DataFrame(iris['data'][:5],columns=iris['feature_names']))

col1,col2,col3,col4 = st.columns(4)
col1.metric(label="sepal_length", value=df['sepal_length'])
col2.metric(label="sepal_width", value=df['sepal_width'])
col3.metric(label="petal_length", value=df['petal_length'])
col4.metric(label="petal_width", value=df['petal_width'])

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

st.header('显示交互式图像')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.header('面积图')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.area_chart(chart_data)

st.header('bar')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])
st.bar_chart(chart_data)

st.header('显示alt散点图')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.altair_chart(c, use_container_width=True)

st.header('将显示Vega-Lite内容，支持交互式信息展示，但不支持放大和缩小。')
chart_data = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.vega_lite_chart(chart_data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

st.header('可以点击的按钮')
# 如果按钮点击，则展示hello there
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.header('下载图片')
st.image('hello.gif')
with open("hello.gif", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="hello.gif",
            mime="image/png"
          )

st.header('checkbox')
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

st.header('radio')
genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

st.header('下拉菜单')
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.write('You selected:', option)

st.header('下拉多选')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
)
st.write('You selected:', options)


st.header('选择滚动条')
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

st.header('输入文字')
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.header('多行文字输入')
txt = st.text_area('Text to input')
st.write('Your input:', txt)

st.header('输入日期')
d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

st.header('输入时间')
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)

st.header('上传文件')
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

st.header('摄像头拍照')
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)

st.header('颜色选择')
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.header('音频展示')
audio_file = open('one.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='one.mp3')

st.header('视频展示')
video_file = open('two.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.header('分栏展示')
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

st.header('分列展示')
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")


st.header('折叠内容')
with st.expander("See explanation"):
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})
    st.write('''The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.''')
    st.image("https://static.streamlit.io/examples/dice.jpg")

st.header('其他')
st.image('./Snipaste_2023-04-25_03-30-29.png')
st.image('./Snipaste_2023-04-25_03-31-15.png')


X = iris.data
Y = iris.target
clf = RandomForestClassifier(**random_feature)
clf.fit(X, Y)

# 对输入数据进行分类，并进行展示
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)


st.header(':red[转载自https://zhuanlan.zhihu.com/p/603791519]')
st.header(':red[图片和视频均来自于无版权网站(除了动图)]')
