
class Quiz:
    """퀴즈 한 문제의 정보를 관리하는 클래스"""

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        """문제와 선택지를 출력한다."""
        print(f"\n{self.question}")

        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def check_answer(self, user_answer):
        """사용자의 답이 정답인지 확인한다."""
        return user_answer == self.answer

    def to_dict(self):
        """퀴즈 객체를 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        """딕셔너리를 Quiz 객체로 변환한다."""
        return cls(
            data["question"],
            data["choices"],
            data["answer"]
        )
