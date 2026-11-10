
import json
from pathlib import Path

from quiz import Quiz


class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self):
        self.quizzes = []
        self.best_score = 0

        # 현재 파일이 위치한 폴더를 기준으로 state.json 경로 설정
        self.state_path = Path(__file__).parent / "state.json"

        self.load_data()

    def show_menu(self):
        """게임 메뉴 출력"""
        print("\n========== IT 기초 퀴즈 게임 ==========")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")
        print("======================================")

    def load_data(self):
        """JSON 파일에서 퀴즈와 점수 불러오기"""
        pass

    def save_data(self):
        """퀴즈와 점수를 JSON 파일에 저장하기"""
        pass

    def play_quiz(self):
        """퀴즈 진행"""
        pass

    def add_quiz(self):
        """새로운 퀴즈 추가"""
        pass

    def show_quizzes(self):
        """등록된 퀴즈 목록 출력"""
        pass

    def show_score(self):
        """최고 점수 출력"""
        pass

    def get_number(self, prompt, min_value, max_value):
        """숫자 입력 및 범위 검증"""
        pass

    def get_text(self, prompt):
        """문자열 입력 및 빈 문자열 검증"""
        pass

    def run(self):
        """게임 메인 실행"""
        pass
