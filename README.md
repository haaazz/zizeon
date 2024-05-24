# zizeon 지전 (摯錢, 祉田)
ssafy 11기 비전공 파이썬반 1학기 최종 관통프로젝트 - 4반 자치호에 팀 입니다

### ✨개요
프로젝트 기간 | 2024. 05. 16(목) - 2024. 05. 24(금) 8:55am
팀명         | 자치호에(JACHIHOE)
서비스명     | 지전
주제         | 예적금 상품 조회 및 맞춤형 상품 추천 서비스 (지전 짱 좋은 서비스)

### 🌱 지전 - 돈을 움켜쥐는, 복이 넘치는 밭

- 서울 4반 반장과 CA로 구성된 팀이기에 팀명을 '자치회'의 영어로 하려고 하니 제대로된 로마자 표기가 'JACHIHOE'여서 자치호에가 되었습니다.
- 'HOE'가 호미라는 뜻이 있어 '밭'이라는 컨셉을 생각해냈고, 한자 동음이의어를 이용한 '지전' 이라는 서비스명을 결정했습니다.

### 팀원

| 이름   | 담당 영역                       | Github                       |
| ------ | ------------------------------- | ---------------------------- |
| 이하림 | 프론트엔드(Vue), Git 관리       | https://github.com/haaazz |
| 이승주 | 백엔드(Django), 프론트엔드(Vue) | https://github.com/KristaLEE |

### 필수 요구사항 구현 정도

| No.  | 구분                    | 기능                                                         | 구현 정도|
| --- | ----------------------- | ------------------------------------------------------------ | --------------------------------- |
| 1   | 메인 페이지             | HomeView 구성                                                | 기능 구현 및  css 완료              |
| 2   | 회원 기능               | 로그인/로그아웃 및 회원가입                                  | 기능 구현 및 css 완료             |
| 3   | 금융상품조회            | 정기예금/정기적금 키워드 별 데이터 조회                      | 기능 구현 및 css 완료                |
| 4   | 환율 계산기             | 당일 환율 데이터 조회 및 환율 변환 계산기 구현               | 기능 구현 및 css 완료               |
| 5   | 근처 은행 검색          | 카카오 맵 API를 활용하여 은행 위치 검색                         | 기능 구현 및 css 완료              |
| 6   | 게시판                 | 게시글 및 댓글 CRUD                         | 기능 구현 및 css 완료              |
| 7   | 프로필                  | - 회원 정보, 관심상품 등록 리스트, 금리 비교 그래프 | 기능 구현 완료 및 css 완료 |
| 8   | 금융 상품 추천 알고리즘 | 금융상품 추천 알고리즘                                | 기능 구현 및 css 완료               |

### 서비스 화면

### 주요 기능

### 사용 개발 툴
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

### 데이터베이스 모델링 (ERD)
![zz](https://github.com/haaazz/zizeon/assets/90473086/8927029c-1de5-4f40-8ad7-4219c4adbc89)

### IA
<img width="2452" alt="IA" src="https://github.com/haaazz/zizeon/assets/90473086/3ea266bf-eb51-46e4-b481-5f01122a7e29">

### 기획 당시 작성한 컴포넌트 구조도
<img width="2274" alt="vue_component_architecture" src="https://github.com/haaazz/zizeon/assets/90473086/f149d06a-973c-4d94-b37e-69b6488b0865">

### 금융 상품 추천 알고리즘

### 작업 내역

### 배운점 및 느낀점

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

### 사용 API

- 금융감독원 API
- 한국수출입은행 환율정보
- 카카오맵
