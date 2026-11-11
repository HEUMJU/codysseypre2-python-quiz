
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
        try:
            with open(self.state_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            # JSON 데이터 구조 확인
            if not isinstance(data, dict):
                raise ValueError("JSON 데이터 형식이 올바르지 않습니다.")

            quiz_data = data.get("quizzes", [])
            best_score = data.get("best_score", 0)

            if not isinstance(quiz_data, list):
                raise ValueError("퀴즈 목록 형식이 올바르지 않습니다.")

            if type(best_score) is not int or best_score < 0:
                raise ValueError("최고 점수 형식이 올바르지 않습니다.")

            self.quizzes = [Quiz.from_dict(item) for item in quiz_data]
            self.best_score = best_score

            print("저장된 데이터를 불러왔습니다.")

        except FileNotFoundError:
            print("저장 파일이 없습니다. 새 데이터를 생성합니다.")
            self.save_data()

        except (json.JSONDecodeError, ValueError, KeyError, TypeError) as e:
            print(f"저장 파일의 데이터가 올바르지 않습니다: {e}")

        except OSError as e:
            print(f"파일을 읽는 중 오류가 발생했습니다: {e}")
        
    def save_data(self):
        """퀴즈와 점수를 JSON 파일에 저장하기"""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        try:
            with open(self.state_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("데이터를 저장했습니다.")

        except OSError as e:
            print(f"파일 저장 중 오류가 발생했습니다: {e}")

    def play_quiz(self):
        """퀴즈 진행 및 점수 계산"""
        print("\n========== 퀴즈 시작 ==========")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            print("먼저 퀴즈를 추가해 주세요.")
            return

        score = 0

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}/{len(self.quizzes)}번 문제]")

            quiz.display()

            user_answer = self.get_number(
                "정답 번호를 입력하세요: ",
                1,
                len(quiz.choices)
            )

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print("\n========== 퀴즈 결과 ==========")
        print(f"총 문제 수: {len(self.quizzes)}개")
        print(f"맞힌 문제 수: {score}개")
        print(f"틀린 문제 수: {len(self.quizzes) - score}개")

        if score > self.best_score:
            self.best_score = score
            print("축하합니다! 최고 점수를 갱신했습니다.")
            self.save_data()
        else:
            print(f"현재 최고 점수는 {self.best_score}점입니다.")

        print(f"최종 점수: {score}점")

    def add_quiz(self):
        """새로운 퀴즈 추가"""
        print("\n========== 퀴즈 추가 ==========")

        question = self.get_text("문제를 입력하세요: ")

        choices = []

        for i in range(4):
            choice = self.get_text(f"{i + 1}번 선택지를 입력하세요: ")
            choices.append(choice)

        answer = self.get_number("정답 번호를 입력하세요 (1~4): ", 1, 4)

        quiz = Quiz(question, choices, answer)

        self.quizzes.append(quiz)
        self.save_data()

        print("새로운 퀴즈가 추가되었습니다!")

    def show_quizzes(self):
        """등록된 퀴즈 목록 출력"""
        print("\n========== 퀴즈 목록 ==========")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{index}번 문제]")
            quiz.display()

        print("\n총 등록된 퀴즈:", len(self.quizzes), "개")

    def show_score(self):
        """최고 점수 출력"""
        print("\n========== 최고 점수 ==========")

        print(f"현재 최고 점수: {self.best_score}점")

        print("===============================")

    def get_number(self, prompt, min_value, max_value):
        """숫자 입력 및 범위 검증"""
        while True:
            try:
                value = input(prompt).strip()
                number = int(value)

                if min_value <= number <= max_value:
                    return number

                print(f"{min_value}부터 {max_value} 사이의 숫자를 입력하세요.")

            except ValueError:
                print("올바른 숫자를 입력하세요.")

    def get_text(self, prompt):
        """문자열 입력 및 빈 문자열 검증"""
        while True:
            value = input(prompt).strip()

            if value:
                return value

            print("빈 문자열은 입력할 수 없습니다.")

    def run(self):
        """게임 메인 실행"""
        pass
