# zizeon 지전 (摯錢, 祉田)
ssafy 11기 비전공 파이썬반 1학기 최종 관통프로젝트 - 4반 자치호에 팀 입니다

### ✨개요

- 진행기간 : 2024. 05. 16(목) - 2024. 05. 24(금) 8:55am
- 팀명 : 자치호에(JACHIHOE)
- 서비스명 : ***지전***
- 주제 : 예적금 상품 조회 및 맞춤형 상품 추천 서비스 (지전 짱 좋은 서비스)

### 🌱 지전 - 돈을 움켜쥐는, 복이 넘치는 밭

- 서울 4반 반장과 CA로 구성된 팀이기에 팀명을 '자치회'의 영어로 하려고 하니 제대로된 로마자 표기가 'JACHIHOE'여서 자치호에가 됨
- 'HOE'가 호미라는 뜻이 있어 '밭'이라는 컨셉을 생각해냈고, 한자 동음이의어를 이용한 '지전' 이라는 서비스명을 결정함

### 🌱 팀원

| 이름   | 담당 영역                       | Github                       |
| ------ | ------------------------------- | ---------------------------- |
| 이하림 | 프론트엔드(Vue), Git 관리, 기획 구체화, 디자인       | https://github.com/haaazz |
| 이승주 | 백엔드(Django), 프론트엔드(Vue), 추천 알고리즘 작성 | https://github.com/KristaLEE |

### 🌱 필수 요구사항 구현 정도

| No.  | 구분                    | 기능                                                         | 구현 정도|
| --- | ----------------------- | ------------------------------------------------------------ | --------------------------------- |
| 1   | 메인 페이지             | HomeView 구성                                                | 기능 구현 및  css 완료              |
| 2   | 회원 기능               | 로그인/로그아웃 및 회원가입                                  | 기능 구현 및 css 완료             |
| 3   | 금융상품조회            | 정기예금/정기적금 키워드 별 데이터 조회                      | 기능 구현 및 css 완료                |
| 4   | 환율 계산기             | 당일 환율 데이터 조회 및 환율 변환 계산기 구현               | 기능 구현 및 css 완료               |
| 5   | 근처 은행 검색          | 카카오 맵 API를 활용하여 은행 위치 검색                         | 기능 구현 및 css 완료              |
| 6   | 게시판                 | 게시글 및 댓글 CRUD                         | 기능 구현 및 css 완료              |
| 7   | 프로필                  | 회원 정보, 관심상품 등록 리스트, 금리 비교 그래프 | 기능 구현 완료 및 css 완료 |
| 8   | 금융 상품 추천 알고리즘 | 금융상품 추천 알고리즘                                | 기능 구현 및 css 완료               |

### 🌱 서비스 화면
깃허브 이슈로 추후 업데이트 예정입니다

### 🌱 주요 기능

- 메인페이지
    - 깔끔하게 작업하면서도 서비스의 주 목적을 작성해둠
    - 각 핵심 페이지로 이동할 수 있는 네비게이션 바 제공
    - UX적으로 사용자에게 서비스 이용 효용감을 주기 위하여 로그인시 메인페이지에 사용자의 닉네임을 작성하도록 함
- 금융 퀴즈
    - 원래는 경험치바까지 구현하려했으나 시간과 능력상 포기하게되어 간단한 문제를 랜덤으로 제공하도록 설계함
    - 비로그인 사용자도 사용 가능하도록 하여 어려운 분야인 금융에 대해 모두가 잘 알 수 있도록 설계함
- 예적금 상품 조회
    - 예금과 적금을 나누어 한 눈에 볼 수 있도록 표 형태로 제작
- 예적금 추천 상품 조회
    - 예금과 적금을 나누어 한 눈에 볼 수 있도록 표 형태로 제작
    - 개인 맞춤 추천이 아닌 가입자 수를 기반으로 비로그인 사용자도 볼 수 있는 추천 페이지 별도 제작
- 환율 계산
    - 매일 오전 10시 초기화되는 API 데이터를 반영해 외화 <-> 원화 환율 계산을 해줌
    - 전체 환율 정보는 아래쪽에 표 형태로 확인할 수 있게끔 해둠
- 근처 은행 지도
- 커뮤니티
    - 게시글 작성, 삭제, 조회, 수정 가능
    - 댓글 작성, 삭제, 조회, 수정 가능
- 회원 / 마이페이지
    - 회원 가입을 통해 개인 정보를 등록하고, 로그인을 통해 상품 가입-해지 가능, 게시글-댓글 작성 및 수정 기능 접근 가능
    - 맞춤 상품 추천을 위해서는 로그인 필수
    - 회원 정보 수정 기능 포함

### 🌱 사용 개발 툴
#### BE
![Django](https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=django&logoColor=white)&nbsp;
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)&nbsp;
![sqlite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=nodedotjs&logoColor=white)&nbsp;
#### FE
![Vue.js](https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)&nbsp;
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)&nbsp;
#### DevOps
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)&nbsp;
![Github](https://img.shields.io/badge/Github-000000?style=for-the-badge&logo=github&logoColor=white)&nbsp;
#### TOOLS
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)&nbsp;
![VS code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)&nbsp;
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)&nbsp;
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)&nbsp;

### 🌱 데이터베이스 모델링 (ERD)
![zz](https://github.com/haaazz/zizeon/assets/90473086/8927029c-1de5-4f40-8ad7-4219c4adbc89)

### 🌱 IA
<img width="2452" alt="IA" src="https://github.com/haaazz/zizeon/assets/90473086/3ea266bf-eb51-46e4-b481-5f01122a7e29">

### 🌱 기획 당시 작성한 컴포넌트 구조도
<img width="2274" alt="vue_component_architecture" src="https://github.com/haaazz/zizeon/assets/90473086/f149d06a-973c-4d94-b37e-69b6488b0865">

### 🌱 금융 상품 추천 알고리즘

머신러닝 사용
- KNN (K-Nearest Neighbors)
    - 분류 및 예측 시 사용되는 가장 기본적인 머신러닝 알고리즘 중 하나
    - columns 개수만큼의 차원에서 각 데이터의 위치를 정하고, 지정된 거리 계산식을 통해 가장 가까운 K개의 데이터를 활용하여 범주를 예측하여 해당 범주로 분류
    - 이 서비스의 경우, 현재 로그인한 회원과 가장 가까운 10명의 회원 데이터(소득, 성별, 나이, 가입한 상품 목록 등)를 활용하여 KNN 모델을 학습, 해당 회원의 데이터를 적합하여 상위 3개의 상품을 추천
- 여담
    - 원래 다른 것들도 해서 같이 하려고 함.. (KNN + XGBoost + LightGBM + CatBoost ⇒ Soft Voting)
    - 일단 데이터 가져오고 추천 시스템 구현하는 게 생각보다 시간 걸림
    - 막상 저거 다 섞어놓으니까 추천 상품 목록 데이터 생성하는 게 오래 걸려서 페이지 들어가도 로딩에 시간이 좀 걸림.. (약 3초)
    - **결론**: 가장 간단한 KNN만 남김

### 🌱 작업 내역 💙하림💜승주🖤함께

## 5월 16일(목)

- 🖤 서비스의 컨셉, 방향성 설정
- 💙 노션, 깃허브 등 협업을 위한 툴 설정
- 💙 IA 작성
- 💙 컴포넌트 구성도 작성
- 💜 ERD 작성
- 🖤 스케쥴 분담

---  

## 5월 17일(금)

- 💜 ERD 구성도 수정
- 💜 데이터셋 확인
- 💜 django 모델 작성
- 💙 와이어프레임 작성
- 💙 API 키 발급

---

## 5월 18일(토)

---

## 5월 19일(일)

---

## 5월 20일(월)

- 💜 user custom model 작성, user dummy data 생성
- 💜 환율 계산기 vue 작성
- 💙 근처 은행 지도 마무리, 타 vue 페이지 전부 작성
- 💙 커뮤니티 게시글 cr 구현
- 💙 전체 데이터 조회 페이지 작성
- 💙 랜덤 금융퀴즈 페이지 작성

---

## 5월 21일(화)

- 💜 로그인, 회원가입
- 💙 뒤로가기가 필요한 페이지 뒤로가기 구현
- 💙 게시글/적금/예금 목록 페이지네이션, 표로 제작
- 💙 로그인, 회원가입
- 💙 랜덤 금융퀴즈 문제 작성
- 🖤 예적금 금리 비교 페이지
- 🖤 상세 데이터 조회 페이지, 가입 기능

---

## 5월 22일(수)

- 💜 추천 알고리즘 작성
- 💜 금리 비교 그래프 Chart.js를 이용해 구현
- 💙 게시글 ud 구현
- 💙 회원 정보 수정 페이지 작성
- 💙 예적금 뷰 필터링 기능 추가, sort기능 추가, null값 '-'로 출력하도록 설정
- 💙 비로그인 사용자 접근 제한 페이지 설정
- 💙 새로고침시 로그인 풀리는 오류 수정
- 💙 axios 자체를 return함으로 상품 조회 페이지 속도 개선
- 💙 deposit 가입 / 마이페이지 조회 기능
- 💙 CSS 작업

---

## 5월 23일(목)

- 💙 CSS 작업
- 💙 회원 탈퇴 기능 작성
- 💙 게시글 댓글 기능 추가
- 💜 한 component로 묶여있던 금리 비교 그래프 separate 작업
- 💜 개인 맞춤형 추천 상품 목록 출력(KNN)
- 💜 댓글 기능 추가에 따른 백엔드 serializer 수정
- 💜 수정 후 댓글 작성자가 렌더링되도록 vue 수정
  
---

## 5월 24일(금)

- 💙 CSS 작업
- 💜 가입 여부에 따른 노출 버튼 설정


### 🌱 배운점 및 느낀점

#### 이하림
- 둘 다 GIT으로 하는 협업이 처음이라, 초기 세팅 및 충돌시 해결이 어려웠습니다.
- TailwindCSS를 처음 사용해봤습니다. 처음 사용하는 것이기도 했고, 아직 익숙하지 않은데다 시간이 부족해 TailwindCSS의 장점을 제대로 사용하지 못한 것 같아 아쉽습니다.
- CSS만 잘 하면 될 것이라 생각했는데, 데이터를 어떻게 받아오고 어떤 URL로 요청을 보내야 할지라는 백엔드적인 부분 지식이 없으니 너무 힘들었습니다.
- 기획 시에 있던 '경험치' 나 '출석체크' 등의 아이디어를 능력 부족으로 구현하지 못한게 아쉽고 분합니다.

#### 이승주
- 개발은 정말 어려운 것 같습니다.. 특히 jupyter에서 추천 알고리즘을 개발, 모델링한 걸 django view함수로 옮겨서 구현하려니 생각보다 어려웠습니다.
- user custom model이 복잡하고 어려웠습니다.
- 기획이나 생각으로는 간단해보이던 기능들이 막상 코드를 작성하고 나면 버그가 많이 생깁니다. 생각보다 버그 고치는게 정신적으로 힘들었으니 처음부터 일정을 잘 짜는게 좋을 것 같습니다
- 그럼에도 백엔드는 생각보다 막 어렵지 않았습니다. 창의력이 부족한 편이라 그런지 디자인하고 CSS 넣는 것도 모자라 보내놓은 데이터 처리 후 렌더링까지 하는 프론트엔드분들이 능력자라고 생각했습니다.

### 🌱 사용 API

- 금융감독원 API
- 한국수출입은행 환율정보
- 카카오맵
