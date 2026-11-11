# codysseypre2-python-quiz
대전 코디세이 연수 2주차 파이썬 퀴즈

# IT 기초 지식 퀴즈 게임

## 1. 프로젝트 개요

Python을 활용하여 개발하는 콘솔 기반 객관식 퀴즈 게임입니다.

사용자는 IT 기초 지식에 관한 퀴즈를 풀거나 새로운 퀴즈를 등록할 수 있으며, 최고 점수를 확인할 수 있습니다.

퀴즈 데이터와 최고 점수는 JSON 파일을 이용하여 저장합니다.

## 2. 퀴즈 주제 및 선정 이유

**주제: IT 기초 지식**

Python, Linux, Docker, Git, 네트워크 등 IT 분야의 기초 지식을 퀴즈로 구성합니다.

프로젝트를 개발하면서 기존에 학습한 IT 지식을 복습하고 Python의 객체지향 프로그래밍과 파일 입출력 기능을 익히기 위해 선정하였습니다.

## 3. 실행 방법

Python 3.10 이상이 필요합니다.

프로젝트 루트 디렉터리에서 다음 명령어를 실행합니다.

```bash
python main.py
```

## 4. 주요 기능

- 퀴즈 풀기
- 퀴즈 랜덤 출제
- 새로운 퀴즈 등록
- 전체 퀴즈 목록 조회
- 최고 점수 확인
- JSON 파일을 이용한 데이터 저장 및 불러오기
- 잘못된 입력 및 예외 상황 처리

## 5. 파일 구조

```text
codysseypre2-python-quiz/
├── main.py
├── quiz.py
├── quiz_game.py
├── state.json
├── README.md
└── .gitignore
```

## 6. 데이터 파일 설명

**state.json**

프로젝트 루트에 위치하며 퀴즈 데이터와 최고 점수를 저장합니다.

- quizzes: 퀴즈 목록
- question: 문제 내용
- choices: 4개의 선택지
- answer: 정답 번호
- best_score: 최고 점수

파일 인코딩은 UTF-8을 사용하며 JSON 형식으로 데이터를 관리합니다.

## 7. 개발 환경

- Python 3.10 이상
- Visual Studio Code
- Git / GitHub
- Python 표준 라이브러리