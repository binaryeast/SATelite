내가 쓸 수능 관리 프로그램.
=========================


그래서, 어떻게 할 거야?

일단 가상환경은 안 잡을래. 귀찮아.

그래서 그냥 빠르게 exe로 빼고 NSIS로 묶어서 배포. 끝.

모듈화를 해 말아?

하지 마. 귀찮아.

좋아. 예상 시간은?

대략 8시?

알았어. 시작하자.


일단 제일 먼저는 데이터 구조부터 생각해야 하는 거야.

내가 있어야 하는 정보들.

1. 모의고사 성적
2. 하루 일과
3. 믿음(멘탈)
4. 

과목
날짜
시간
점수
분량
상태(컨디션)
분야(활동분야)
내용
일기


아오 이제 뭘 어떻게 해야 하지?

일단 여기에 구조 복붙 해 놓고, 틀부터 만들고 해야겠지.

이번엔 전체화면에 페이지도 할 수 있으면 좋겠다.

1.	Date
    A.	Date_id
    B.	Date – text
2.	Study
    A.	_id
    B.	Date
    C.	Sub-id
    D.	Time(hour)
3.	Subject
    A.	_id
    B.	Sub_name
4.	Task
    A.	_id
    B.	Task_name
    C.	Difficulty
    D.	Body_or_brain
    E.	Holy
    F.	Weight
    G.	Factor_id
5.	Test
    A.	_id
    B.	Sub_id
    C.	Test_time
    D.	Grade
    E.	score
6.	Diary
    A.	_id
    B.	Date
    C.	text
7.	Think_factor
    A.	_id
    B.	factor


# 기본 테이블

1.  Date
3.	Subject
7.	Think_factor

# 중간 테이블

6.	Diary
2.	Study

# 심화 테이블

4.	Task
5.	Test


# 앞으로 해야 하는 일

이제 내가 추가로 구현하면 좋을 것들 이 아래에 기록해놀 것.
1. 구글 캘린더 API
2. 메일이나 문자로 알림 주기.
3. 서버 통신으로 백업이랑 자동화 하기.
4. 아침 체조 틀어주기

그래서 코리아 체조에 좋은 뽕짝 하나 붙여야 한다는 소리네.

폰트 트라이 문으로 짜서 할 것.

또 뭐 트라이로 하려 했는데 까먹었다.