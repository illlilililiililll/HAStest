import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm

path = 'fonts/font.ttf'
fm.fontManager.addfont(path)
plt.rc('font', family=fm.FontProperties(fname=path).get_name())

wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
colors=['#AC6869', '#ECA4A4', '#F7E2E1', '#DCEBEB', '#92DAD9']

semester = st.sidebar.selectbox('학기', ['1학기', '2학기'])
type = st.sidebar.selectbox('분류', ['중간고사', '기말고사'])
grade = st.sidebar.selectbox('학년', ['1학년', '2학년', '3학년'])

s = 1 if semester == '1학기' else 2 if semester == '2학기' else None
t = 1 if type == '중간고사' else 2 if type == '기말고사' else None
g = 1 if grade == '1학년' else 2 if grade == '2학년' else 3 if grade == '3학년' else None

try:
    df = pd.read_csv(f'result/{s}-{t}-{g}.csv')
except FileNotFoundError:
    df = None

st.title('2023 하나고등학교 시험 통계분석')
tab1, tab2, tab3 = st.tabs(['Count', 'Score', 'Data'])
with tab1:
    if not df:
        st.error('해당 데이터가 존재하지 않습니다')
    else:
        def make_autopct(values, total):
            def my_autopct(pct):
                val = int(round(pct*total/100.0))
                return '{v:d}문제 ({p:.2f}%)'.format(p=pct, v=val)
            return my_autopct

        def explode(lists):
            return [0.07 if v == max(lists) else 0 for i, v in enumerate(lists)]

        st.title(f'{semester} {type} {grade} 통계')
        if grade == '1':
            plt.figure(figsize=(20, 20))
        else:
            plt.figure(figsize=(20, 54))

        # 전체 차트 제목 설정

        # subplot 개수 결정
        if len(df) % 3 == 0:
            plotnum = len(df)//3
        else:
            plotnum = len(df)//3 + 1

        # 위 예시들과 동일
        for i in range(len(df)):
            plt.subplot(plotnum, 3, i+1)
            title = df.loc[i, 'Subject']
            total = int(df.loc[i, 'Total'])
            data = []
            for j in range(1, 6):
                num = df.loc[i, str(j)]
                data.append(int(num[:num.index('(')].strip()))
        plt.pie(data, labels=[str(k)+'번' for k in range(1, 6)], wedgeprops=wedgeprops, colors=colors, autopct=make_autopct(data, total), explode=explode(data))
        plt.title(title + f'\t{total}문제')
        plt.subplots_adjust(top=0.9) # 전체 제목 아래에서부터 시작하도록 시작점 조정     
        
        st.pyplot(plt)

with tab2:
    if not df:
        st.error('해당 데이터가 존재하지 않습니다')
    else:
        def make_autopct_score(values):
            def my_autopct(pct):
                total = sum(values)
                val = pct*total/100.0
                return '{v:.1f}점 ({p:.2f}%)'.format(p=pct, v=val)
            return my_autopct

        def explode_score(lists):
            return [0.07 if v == max(lists) else 0 for i, v in enumerate(lists)]

        st.title(f'{semester} {type} {grade} 점수 통계')
        if grade == '1':
            plt.figure(figsize=(20, 20))
        else:
            plt.figure(figsize=(20, 54))

        if len(df) % 3 == 0:
            plotnum = len(df)//3
        else:
            plotnum = len(df)//3 + 1

        # 위와 동일
        for i in range(len(df)):
            plt.subplot(plotnum, 3, i+1)
            title = df.loc[i, 'Subject']
            data = []
            for j in range(1, 6):
                data.append(float(df.loc[i, 'Score'+str(j)]))
        plt.pie(data, labels=[str(k)+'번' for k in range(1, 6)], wedgeprops=wedgeprops, colors=colors, autopct=make_autopct_score(data), explode=explode_score(data))
        plt.title(title + f'\t{total}문제')
        plt.subplots_adjust(top=0.9)

        st.pyplot(plt)

with tab3:
    st.title('Dataset')
    st.subheader()
    if st.button('1학기'):
        if st.button('중간고사'):
            if st.button('1학년'):
                st.dataframe(pd.read_csv('result/1-1-1.csv'))
                st.download_button('Download', 'result/1-1-1.csv')
            elif st.button('2학년'):
                st.dataframe(pd.read_csv('result/1-1-2.csv'))
                st.download_button('Download', 'result/1-1-2.csv')
            elif st.button('3학년'):
                st.dataframe(pd.read_csv('result/1-1-3.csv'))
                st.download_button('Download', 'result/1-1-3.csv')
        elif st.button('기말고사'):
            if st.button('1학년'):
                st.dataframe(pd.read_csv('result/1-2-1.csv'))
                st.download_button('Download', 'result/1-2-1.csv')
            elif st.button('2학년'):
                st.dataframe(pd.read_csv('result/1-2-2.csv'))
                st.download_button('Download', 'result/1-2-2.csv')
            elif st.button('3학년'):
                st.dataframe(pd.read_csv('result/1-2-3.csv'))
                st.download_button('Download', 'result/1-2-3.csv')
    elif st.button('2학기'):
        if st.button('중간고사'):
            if st.button('1학년'):
                st.dataframe(pd.read_csv('result/2-1-1.csv'))
                st.download_button('Download', 'result/2-1-1.csv')
            elif st.button('2학년'):
                st.dataframe(pd.read_csv('result/2-1-2.csv'))
                st.download_button('Download', 'result/2-1-2.csv')
            elif st.button('3학년'):
                st.dataframe(pd.read_csv('result/2-1-3.csv'))
                st.download_button('Download', 'result/2-1-3.csv')
    st.subheader()
    if st.button('데이터 통계분석'):
        st.download_button('Download', 'testSort_csv.py')
        st.download_button('1st Final', 'testSort_final.py')