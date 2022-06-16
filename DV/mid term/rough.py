import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sb 
import matplotlib.pyplot as plt 
import pandas_profiling
from wordcloud import WordCloud
import plotly.express as px
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
plt.style.use('dark_background') ; 
st.set_option('deprecation.showPyplotGlobalUse', False)
components.html(
    """
    <div class="college" style="border: 2px solid black; background-color: rgb(5, 5, 5);color: aliceblue;text-align: center;border-radius: 10px;font-family:Trebuchet MS,Garamond;font-size: 14px"> 
        <h1><span>Presidency University, Bangalore</span></h1>
        <h3>Department of Computer Science & Engineering</h3>
        <h2>Data Visualization Project | 7 - CSE - 10 | CSE 367 </h2>
    </div>
    <br>
    <div class="intro" style="border: 2px solid black; border-radius: 25px; background-color: cornflowerblue;font-family:Trebuchet MS,Garamond ;font-size: 18px;text-align: center; ">
        <h1 style="margin: 0.25;"><strong>AutoPlot</strong></h1>
        <h2 style="margin: 0.25;">A Web-App that aims to automate plotting...</h2>
    </div>
    
    """,
    height=350,
)

st.cache(allow_output_mutation=True)
def main():
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    st.write(" Choose your activity from the sidebar.  ")
    st.sidebar.write("""<strong style="font-size:22px">About :</strong><br>This is a WebApp built using streamlit that can be used to simplify basic EDA and visualizations.<br> Made by Sai Ram.K """,unsafe_allow_html=True)
    st.sidebar.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/am-ram/dv/main/AutoPlot.py&label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')

    activities = ["EDA" , "PLOT","In-Depth Report","Interactive-Mode","ML"]
    st.sidebar.write("""<strong style="font-size:18px">Select Activity To Perform : </strong>""",unsafe_allow_html=True)
    choice = st.sidebar.radio(" " ,activities)
    st.sidebar.write('**<strong style="font-size:22px">FAQs**</strong>',unsafe_allow_html=True)
    st.sidebar.markdown('**What happens to my data?**')
    st.sidebar.markdown('The data you upload is not saved anywhere on this site or any 3rd party site i.e, not in any storage like DB/FileSystem/Logs.')   
    st.sidebar.markdown('**To Suggest changes & improvements do reach on LinkedIn. **')
    st.sidebar.markdown('[![Sairam](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=whit)](https://www.linkedin.com/in/am-ram/ )')
    

    
    if choice == "EDA":
        st.subheader("|  Exploratory Data Analysis  |")
        st.write(""" <strong><p style="font-size: 42px">Upload Your Dataset Here</p></strong> """,unsafe_allow_html=True)
        
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])   
        
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)
            if st.checkbox("SHOW SHAPE"):
                st.write(df.shape)
            if st.checkbox("SHOW SIZE"):
                st.write(df.size)
            if st.checkbox("SHOW COLUMN "):
                st.write(df.columns)
            if st.checkbox("SELECT COLUMN NAME"):
                select_columns = st.multiselect("Select Column" , df.columns)
                new_df = df[select_columns]
                st.dataframe(new_df)
            if st.checkbox("SHOW MISSING VALUES"):
                st.write(df.isna().sum())
            if st.checkbox("SHOW VALUE COUNTS"):
                column = st.selectbox("Select Columns" , df.columns)
                st.write(df[column].value_counts())
            if st.checkbox("SHOW SUMMARY"):
                st.write(df.describe())
            if st.checkbox("SHOW COLUMN TYPES"):
                column = st.selectbox("Select Columns" , df.columns,key="1")
                st.write(df[column].dtype)    
               

    elif choice == "PLOT":
        st.subheader("|  Data Visualization  |")
        st.write(""" <strong><p style="font-size: 42px">Upload Your Dataset Here</p></strong> """,unsafe_allow_html=True)
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])
        
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)

            if st.checkbox("CORRELATION"):
                try:
                    st.write(sb.heatmap(df.corr() , annot = True,cmap="Blues"))
                    st.pyplot()
                except (ValueError,TypeError):
                    st.error("This Column does not correspond to a valid input data. Please Select a valid Column.") 
            if st.checkbox("Bar Graph"):
                try:
                    x_axis = st.selectbox("Select x axis:" , df.columns)
                    x_axis = df[x_axis]
                    y_axis = st.selectbox("Select y axis:" , df.columns)
                    y_axis = df[y_axis]
                    st.write(sb.barplot(x_axis , y_axis,palette=['cyan','deeppink','cornflowerblue','coral']))
                    st.pyplot()
                    plt.xticks(rotation = 90)
                    plt.legend()
                    plt.grid()
                except (ValueError,TypeError):
                    st.error("This Column does not correspond to a valid input data. Please Select a valid Column.") 
            
            if st.checkbox("Count Plot"):
                try:
                    c = st.selectbox("Select  axis:" , df.columns)
                    c_main = df[c]
                    st.write(sb.countplot(c_main,palette=['cyan','deeppink','cornflowerblue','coral','violet','crimson','yellow','lightcoral']))
                    st.pyplot()
                    plt.grid()
                    plt.xticks(rotation = 90)
                    plt.legend()
                except (ValueError,TypeError):
                    st.error("This Column does not correspond to a valid input data. Please Select a valid Column.") 


            if st.checkbox("Pie Chart"):
                try:
                    col = st.selectbox("Select 1 column" , df.columns)
                    pie = df[col].value_counts().plot.pie(autopct = "%1.1f%%",colors=['cyan','deeppink','cornflowerblue','coral'])
                    st.write(pie)
                    st.pyplot()
                except (ValueError,TypeError):
                    st.error("This Column does not correspond to a valid input data. Please Select a valid Column.") 
            if st.checkbox("Box Plot"):
                try:
                    col1 = st.selectbox("Select X column" , df.columns)
                    col2 = st.selectbox("Select Y column", df.columns)
                    box=sb.boxplot(x = col1, y = col2, data = df,notch=True,boxprops=dict(facecolor='r', color='cyan'), capprops=dict(color='yellow'),flierprops=dict(color='g', markeredgecolor='r'),medianprops=dict(color='black'))
                    st.write(box)
                    st.pyplot()
                except (ValueError,TypeError):
                     st.error("These Columns do not correspond to a valid input data. Please Select a valid Column.") 
            
            if st.checkbox("Violin Plot"):
                try:
                    col = st.selectbox("Select 1 column" , df.columns,key="3")
                    vio=sb.violinplot( y = df[col] )
                    st.write(vio)
                    st.pyplot() 
                except (ValueError,TypeError):
                    st.error("This Column does not correspond to a valid input data. Please Select a valid Column.")   
                    
            if st.checkbox("Word Cloud"):
                try:
                    col = st.selectbox("Select 1 column" , df.columns,key="4")
                    wordcloud = WordCloud().generate(str(df[col].values))
                    plt.imshow(wordcloud, interpolation='bilinear')
                    plt.axis("off")
                    plt.show()
                    st.pyplot()
                except (ValueError,TypeError):
                    st.error("This Column Accepts only text data and not numeric data. Please Select a valid Column.")   
           
            if st.checkbox("Time Series"):
                try:
                    col1 = st.selectbox("Select 1 column" , df.columns, key="2")
                    fig1 = px.line(df, x=df.index, y = df[col1])
                    fig1.update_layout(template="plotly_dark")
                    #fig.show()
                    #st.pyplot()
                    st.plotly_chart(fig1)
                except (ValueError,TypeError):
                    st.error("The selected column is not in a time series format. Please Select a valid Column.")   

    if choice =="In-Depth Report":
            st.subheader("|  In - Depth Report  |")
            st.write(""" <strong><p style="font-size: 42px">Upload Your Dataset Here</p></strong> """,unsafe_allow_html=True)
            dataset = st.file_uploader("" ,type = ["csv","txt","xls"])
            
            if dataset is not None:
                df = pd.read_csv(dataset , delimiter = ",")
                st.dataframe(df)
                pr = df.profile_report()
                st_profile_report(pr)       
                export=pr.to_html()
                st.download_button(label="Download Full Report", data=export, file_name='Report.html')
    
    if choice =="Interactive-Mode":
            st.subheader("|  Interactive Visualization  |")
            st.write(""" <strong><p style="font-size: 42px">Upload Your Dataset Here</p></strong> """,unsafe_allow_html=True)
            dataset = st.file_uploader("" ,type = ["csv","txt","xls"])
            
            if dataset is not None:
                df = pd.read_csv(dataset , delimiter = ",")
                st.dataframe(df)
                if st.checkbox("Time Series"):
                    try:
                        col1 = st.selectbox("Select 1 column" , df.columns, key="2")
                        fig1 = px.line(df, x=df.index, y = df[col1])
                        fig1.update_layout(template="plotly_dark")
                        st.plotly_chart(fig1)
                    except (ValueError,TypeError):
                        st.error("The selected column is not in a time series format. Please Select a valid Column.")
                
                if st.checkbox("Histogram"):
                    try:
                        column= st.selectbox("Select 1 column " , df.columns, key="6")
                        his=px.histogram(df, x=column,title=column, height=400,color_discrete_sequence=['#03DAC5'])
                        his.update_layout(margin=dict(t=100, b=0, l=70, r=40),hovermode="x unified",xaxis_tickangle=360,xaxis_title=' ', yaxis_title=" ",plot_bgcolor='#2d3035', paper_bgcolor='#2d3035',\
                        title_font=dict(size=40, color='#a5a7ab', family="Muli, sans-serif"),font=dict(color='#FFFFFF',size=25),legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
                        st.write(his)
                    except (ValueError,TypeError):
                        st.error("The selected column is not in a valid format. Please Select a valid Column.")
                
                if st.checkbox("Map Co-Ordinates"):
                    try:
                        lat= st.selectbox("Select Latitudes column " , df.columns, key="8")
                        long=st.selectbox("Select Longitudes column " , df.columns, key="9")
                        lat=df[lat]
                        long=df[long]
                        d={"lat":lat,"lon":long}
                        temp=pd.DataFrame(d,columns=['lat', 'lon'])
                        st.map(temp)
                    except (ValueError,TypeError):
                        st.error("The selected column is not in a Co-Ordinates format. Please Select a valid Column.")
    if choice == "ML":
        st.subheader("|  Machine Learning  |")
        st.write(""" <strong><p style="font-size: 42px">Upload Your Dataset Here</p></strong> """,unsafe_allow_html=True)
        dataset = st.file_uploader("" ,type = ["csv","txt","xls"])
        if dataset is not None:
            df = pd.read_csv(dataset , delimiter = ",")
            st.dataframe(df)      
            try:
                if st.checkbox("Linear Regression"):
                    features = st.multiselect("Select Feature Columns" , df.columns)
                    target = st.selectbox("Select a target column",df.columns)       
                    left_column, right_column = st.columns(2)
                    # test size
                    test_size = left_column.number_input('Validation-dataset size (rate: 0.0-1.0):',min_value=0.0,max_value=1.0,value=0.2,step=0.1,)
                    # random_seed
                    random_seed = right_column.number_input('Set random seed (0-):',value=0, step=1,min_value=0)
                    
                    # split the dataset
                    X_train, X_val, Y_train, Y_val = train_test_split(df[features], df[target],test_size=test_size,random_state=random_seed)
                    st.write('Split success',X_train.shape)
                    regressor = LinearRegression()
                    regressor.fit(X_train, Y_train)
                    Y_pred_train = regressor.predict(X_train)
                    Y_pred_val = regressor.predict(X_val)
                    R2 = metrics.r2_score(Y_val, Y_pred_val)
                    st.write(f'R2 score: {R2:.2f}')
                    left_column, right_column = st.columns(2)
                    show_train = left_column.radio('Show the training dataset:', ('Yes','No'))
                    show_val = right_column.radio('Show the validation dataset:', ('Yes','No'))
                    
                    # default axis range
                    y_max_train = max([max(Y_train), max(Y_pred_train)])
                    y_max_val = max([max(Y_val), max(Y_pred_val)])
                    y_max = int(max([y_max_train, y_max_val])) 
                    
                    # interactive axis range
                    left_column, right_column = st.columns(2)
                    x_min = left_column.number_input('x_min:',value=0,step=1)
                    x_max = right_column.number_input('x_max:',value=y_max,step=1)
                    left_column, right_column = st.columns(2)
                    y_min = left_column.number_input('y_min:',value=0,step=1)
                    y_max = right_column.number_input('y_max:',value=y_max,step=1)
                    
                    
                    fig = plt.figure(figsize=(3, 3))
                    if show_train == 'Yes':
                    	plt.scatter(Y_train, Y_pred_train,lw=0.1,color="r",label="training data")
                    if show_val == 'Yes':
                    	plt.scatter(Y_val, Y_pred_val,lw=0.1,color="b",label="validation data")
                    plt.xlabel("Actual",fontsize=8)
                    plt.ylabel("Predicted",fontsize=8)
                    plt.xlim(int(x_min), int(x_max)+5)
                    plt.ylim(int(y_min), int(y_max)+5)
                    plt.legend(fontsize=6)
                    plt.tick_params(labelsize=6)
                    st.pyplot(fig)
            except ValueError: st.error("Only Numeric Columns accepted")
    else:
        st.write(""" <strong><p style="font-size: 42px">Thank You For Using This WebApp.</p></strong> """,unsafe_allow_html=True)

       
if __name__ == "__main__":
    main()