

# ! matplotlib = Mathmetical Plot Library

###
# 파이썬에서 그래프를 그릴 수 있게 하는 라이브러리
# 꺾은선 그래프, 막대 그래프 등을 모두 지원
###


# basic example
# 아래는 서울시 월별 평균 미세먼지의 양을 나타낸다. (ug/m^3)
# 아래의 자료를 이용하여 막대 그래프를 그려보자
months = [1,2,3,4,5,6,7,8,9,10,11,12]
fine_dust = [66,57,69,41,53,29,26,25,21,33,41,42]

# matplotlib 라이브러리를 불러온다
import matplotlib.pyplot as plt

def draw_finedust_graph()
    # 막대 그래프의 막대 위치를 결정하는 pos를 선언한다
    # pos값은 그래프에서 x축 상의 그래프 갯수를 나타낸다.
    pos = range(len(months))
    
    # 높이가 fine_dust인 막대그래프를 그립니다. 각 막대를 가운데 정렬합니다.
    # 막대그래프를 그리기 위한 plt.bar()의 사용법은 아래와 같다
    # plt.bar(x축의 그래프 갯수, 막대그래프의 수치 기점, option?)
    plt.bar(pos, fine_dust, align='center')

    # 각 막대에 해당되는 연도를 표기합니다.
    # x축의 각 pos 위치의 명칭을 정합니다.
    plt.xticks(pos, years)

    # 실제 그림을 표시하는 함수인 plt.show()를 통해서 그래프를 출력합니다.
    plt.show()



# 막대 그래프 대신에 두 개의 칼럼이 있는 경우 인라인 그래프로 표기할 수 있다.
def draw_finedust_inline_graph()
    plt.plot(months, fine_dust)
    plt.show()

