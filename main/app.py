# 스트림릿 라이브러리를 사용하기 위한 임포트
import streamlit as st

# 웹 대시보드 개발 라이브러리인 스트림릿은,
# main 함수가 있어야 한다.

def main() :
    st.title('안녕하세요. Tiktok 대시보드 프로젝트')
    st.title('Hello')
    st.header('abc')
    st.subheader('this is subheader')


# col1,col2 = st.columns([2,3])
# # 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  

# with col1 :
#   # column 1 에 담을 내용
#   st.title('here is column1')
# with col2 :
#   # column 2 에 담을 내용
#   st.title('here is column2')
#   st.checkbox('this is checkbox1 in col2 ')


# # with 구문 말고 다르게 사용 가능 
# col1.subheader(' i am column1  subheader !! ')
# col2.checkbox('this is checkbox2 in col2 ') 
# #=>위에 with col2: 안의 내용과 같은 기능을합니다


# if __name__ == '__main__' :
#     main()