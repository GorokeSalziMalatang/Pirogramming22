import time
import random
from dataclasses import dataclass

@dataclass(frozen=True)
class Character:
    """
    등장인물 클래스
    """
    name: str
    hair: str
    clothes: str
    shoes: str


class DetectiveGame:
    """
    탐정 게임 클래스
    """
    
    def __init__(self):
        self.characters = [
            Character("최OO", "장발이야", "운동복을 입었어", "나이키를 신었어"),
            Character("김OO", "파란 모자를 썼어", "양복을 입었어", "구두를 신었어"),
            Character("이O희", "파마를 했어", "무스탕을 입었어", "아무것도 안 신고 있었어"),
            Character("손OO", "스님 머리야", "셔츠를 입었어", "슬리퍼 신었어"),
            Character("장OO", "단발머리야", "치마를 입었어", "부츠를 신었어"),
            Character("안OO", "투블럭을 했어", "반팔티를 입었어", "크록스를 신었어"),
            Character("이O현", "허리까지 머리카락이 있어", "원피스를 입었어", "힐을 신었어")
        ]
        self.character_attr = {"hair":"머리스타일", 
                               "clothes":"옷", 
                               "shoes":"신발"}
        self.murderer = None
        self.victim = None
        self.suspect = None
        self.dying_message = ""
        self.detective_name = ""
        self.lives = 2

    def show_intro(self):
        """
        게임 인트로

        1. 탐정 이름 설정
        2. 랜덤 희생자 선정
        3. 랜덤 범인 선정
        4. 다잉메시지 생성
        
        """
        print("탐정 게임에 오신 것을 환영합니다.")
        time.sleep(1)

        # 탐정 이름 설정
        self.detective_name = input("\n탐정님의 성함을 입력해주세요: ")
        print(f"\n{self.detective_name} 탐정님 어서 오십시오. 피로그래밍 22기의 해커톤을 즐겨주시기 바랍니다.")
        
        # 랜덤 희생자 선정
        self.select_victim()

        # 랜덤 범인 선정
        self.murderer = random.choice(self.characters)
        
        # 다잉메시지 생성
        self.write_dying_message()


        # -----
        print(f"""
########################################

            ~평화로운 해커톤~
                         
########################################
        """)

        time.sleep(1.5)


        print(f"\n코딩에 몰두하던 {self.detective_name}, 눈이 피로해지기 시작한다. 해커톤의 열기가 고조될수록, 정신은 점점 흐릿해진다.")
        time.sleep(1)
        print(f"\n🕵 {self.detective_name}: 이 해커톤, 너무 평화롭기만 하군... 뭔가 재밌는 사건이라도 터져야 할 텐데. 뭐, 코드가 몽땅 날아가는 일이라든지.")
        time.sleep(1)
        print(f"😀 {self.victim.name}: 하하, 탐정님! 그런 무서운 말씀은 제발 그만하세요. 상상만 해도 아찔하네요... 그런 일은 절대로 일어나지 않을 거예요.")
        time.sleep(1)
        print(f"🕵 {self.detective_name}: 뭐, 그렇긴 하겠지. 아, 참고로 나는 명탐정 {self.detective_name}! 사건이 터지면 언제든 나를 찾아.")
        time.sleep(1)
        print(f"😀 {self.victim.name}: 하하, 명탐정님! 알겠습니다. 그런데 요즘 제 노트북을 자꾸 누가 훔쳐보는 것 같아서 신경 쓰이긴 해요. 집 앞 카페에서 코딩하다 보면 말이죠...")
        time.sleep(1)
        print(f"그렇게 둘은 헤어졌고, 그로부터 10분 후 갑자기 정전이 일어나게 되는데..\n")
        time.sleep(1)

        print(f"""
########################################

               사건 발생
                         
########################################
        """)
        time.sleep(1)

        print(f"갑자기 날카로운 비명 소리가 울려 퍼졌다. {self.victim.name} 씨의 노트북 화면이 순식간에 블루스크린으로 바뀌었다.")
        time.sleep(1)
        print(f"그 충격에 {self.victim.name} 씨는 정신을 잃고 그대로 쓰러졌다...")
        time.sleep(1)

        print(f"\n현장은 순식간에 혼란에 빠졌고, 바닥에는 {self.victim.name} 씨의 메시지가 남겨져 있었다.")
        time.sleep(1)
        
        print(f"""\n
================사망하지는 않았지만 이게 다잉메시지?!================
                {self.dying_message}
==================================================================
        """)
        time.sleep(1)

        print(f"문제의 노트북 주위에 있는 사람은 {len(self.characters)}명입니다.")
        time.sleep(1)
        print("그 중, 범인은 바로 이 자리에 있을 것입니다...")
        time.sleep(1)
        print(f"{self.detective_name} 님의 임무는 범인을 찾아내는 것입니다. 진실을 밝혀내세요. 기회는 {self.lives}번입니다.")
        time.sleep(1)

        print(f"""
########################################

               추리 시작
                         
########################################
        """)
        time.sleep(1)
        
    def select_victim(self):
        """
        랜덤 희생자 선정
        """
        self.victim = random.choice(self.characters)
        self.characters.remove(self.victim)
    
    def write_dying_message(self):
        """
        다잉메시지 생성
        """
        dying_message_type = random.choice(list(self.character_attr.keys()))
        self.dying_message = f"{self.character_attr[dying_message_type]}은 {getattr(self.murderer, dying_message_type)} 윽..☠️"        
    
    def investigate(self):
        """
        용의자 조사
        """

        # 용의자 리스트 출력
        print("\n용의자와 대화를 나누고 인상착의를 수집하세요...\n")
        for index, char in enumerate(self.characters, 1):
            print(f"{index}. {char.name}")

        # 조사할 용의자 선택
        choice_name = input("\n누구를 조사하시겠습니까? 이름을 입력하세요: ").strip()

        # 유효성 검사 후, 용의자 정보 출력
        for char in self.characters:
            if char.name == choice_name:
                self.display_clues(char) # 용의자 정보 출력
                return

        # 유효하지 않은 입력일 때
        print("잘못된 입력입니다! 시간이 얼마 남지 않았습니다, 다시 시도해주세요!")
        print("범인은 아직도 우리 곁에 있어요. 서둘러 진실을 밝혀내야 합니다!")
        print(f"🕵 {self.detective_name}: 좋아, 이번엔 잘 선택해보자.\n")
        self.investigate();
      
    def display_clues(self, choice):
        """
        용의자 정보 출력
        """
        print(f"\n{choice.name}의 인상착의를 봅니다.")
        for attr_name, kor in self.character_attr.items():
            print(f"- {kor}: {getattr(choice, attr_name)}")

    def prompt_choice(self, prompt):
         while True:
            choice = input(prompt).strip().lower()
            if choice in ['네', '아니오']:
                return choice
            print("잘못된 입력입니다. 네 또는 아니오만 입력해 주세요.")

    def accuse(self):
        """
        범인 색출
        """

        # 용의자 리스트 출력
        print("\n범인을 지목할 시간입니다.")
        for index, char in enumerate(self.characters, 1):
            print(f"{index}. {char.name}")

        # 범인 지목
        choice_name = input("\n누구를 범인으로 지목하시겠습니까? 이름을 입력하세요: ").strip()
        print(f"🕵 {self.detective_name}: 범인은 바로 {choice_name} 씨야")

        # 범인이 맞는지 확인
        for char in self.characters:
            if char.name == choice_name:
                self.suspect = char
                self.check_outcome()
                return

        # 지목한 사람이 용의자 리스트에 없는 사람일 때 범인 색출 재시작
        print("탐정님, 그건 잘못된 선택입니다! 시간이 얼마 남지 않았습니다, 다시 시도해주세요!")
        print("범인은 아직도 우리 곁에 있어요. 서둘러 진실을 밝혀내야 합니다!")
        print(f"🕵 {self.detective_name}: 좋아, 이번엔 잘 선택해보자.\n")
        time.sleep(1)
        self.accuse()

    def match_dying_message(self, character) -> bool:
        if self.dying_message == f"머리스타일은 {character.hair} 윽..☠️" or \
                self.dying_message == f"옷은 {character.clothes} 윽..☠️" or \
                self.dying_message == f"신발은 {character.shoes} 윽..☠️":
            return True
        return False

    def check_outcome(self):
        """
        범인 색출 성공 확인

        1. 맞으면 -> 성공 메시지 + 게임 재시작 여부
        2. 틀리면 -> 기회 1만큼 차감
            1) 기회 남은 경우 -> 재조사 or 재지목
            2) 기회 없는 경우 -> 실패 메시지 + 게임 재시작 여부
        """
        if self.match_dying_message(self.suspect):
            print("""
----------------------------------------------------------------------------------


     ██████╗  █████╗ ███╗   ███╗███████╗    ██╗    ██╗██╗███╗   ██╗
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║    ██║██║████╗  ██║
    ██║  ███╗███████║██╔████╔██║█████╗      ██║ █╗ ██║██║██╔██╗ ██║
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║███╗██║██║██║╚██╗██║
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚███╔███╔╝██║██║ ╚████║
     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝


----------------------------------------------------------------------------------""")
            time.sleep(1)
            print(f"""
########################################

           당신은 역시 명탐정!! 
                         
########################################
        """)
            time.sleep(1)
            print(f"\n정답입니다! 범인은 바로 {self.suspect.name} 씨였습니다!")
            time.sleep(1)
            print(f"당신의 추리는 완벽했습니다, 역시 명탐정 {self.detective_name}답군요.")
            time.sleep(1)
            print(f"\n🕵 {self.detective_name}: 왜 노트북을 망가뜨렸습니까?? {self.victim.name} 씨의 노트북을 왜 그렇게 했죠?")
            time.sleep(1)
            print(f"🥹 {self.suspect.name}: 그게 사실... {self.victim.name} 씨의 팀이 해커톤 우승을 못하게 하려고... 그래서 홧김에... 죄송합니다🥹")
            time.sleep(1)
            print(f"\n{self.suspect.name} 씨는 끝내 자신의 범행을 인정했고, 피로그래밍 22기 해커톤에서 퇴출당했습니다.")
            time.sleep(1)
            print(f"사건은 해결되었고, 모든 사람들이 안도의 한숨을 내쉬었습니다. 당신의 활약 덕분입니다.")
            time.sleep(1)
            self.ask_restart()

        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"\n😡 {self.suspect.name}: 무슨 소리야? 내 인상착의를 봐... 당신 명탐정 맞아? 💢💢💢")
                print(f"\n틀렸습니다... {self.suspect.name} 씨는 범인이 아닙니다. 남은 기회는 {self.lives}번입니다.")
                print(f"시간이 얼마 남지 않았어요. 신중하게 선택해주세요.")
                time.sleep(1)

                choice = self.prompt_choice("\n용의자들의 인상착의를 다시 보겠습니까? (네/아니오): ")
                if choice == '네':
                    print(f"🕵 {self.detective_name}: 좋았어... 다시 차근차근 보자\n")
                    time.sleep(1)
                    self.main_flow()  
                else:
                    self.accuse()  # 다시 지목할 기회를 줌
            else:
                print(
                    """
----------------------------------------------------------------------------------


    ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝


----------------------------------------------------------------------------------"""
                )
                time.sleep(1)
                print(f"""
########################################

            추리 실패...... 
                         
########################################
        """)
                time.sleep(1)
                print(f"\n🤪 {self.murderer.name}: 명탐정 별거 없네~~~ 해커톤 우승은 내꺼다!!!")
                time.sleep(1)
                print(f"\n안타깝습니다... 범인은 {self.murderer.name} 씨였습니다. 모든 기회를 다 써버렸습니다.")
                time.sleep(1)
                print(f"추리는 실패했습니다. {self.detective_name} 탐정님, 이번 사건은 당신에게 큰 상처로 남게 될 것입니다.")
                time.sleep(1)
                print(f"당신은 이 미스터리를 풀 기회를 잃었습니다...")
                time.sleep(1)
                print(f"하지만, 진정한 탐정은 실패에서도 배웁니다. 다음엔 꼭 진실을 밝혀내세요.")
                time.sleep(1)
                self.ask_restart()
        
    def ask_restart(self):
        """
        게임 재시작 여부 확인 -> 재시작 or 종료
        """
        choice = self.prompt_choice("\n게임을 다시 시작하시겠습니까? (네/아니오): ")
        if choice == '네':
            print()
            self.reset_game()
            self.play()
        else:
            print("게임을 종료합니다. 감사합니다!")

    def reset_game(self):
        """
        게임 재시작 시, 리셋
        """
        self.characters.append(self.victim)
        self.lives = 2
        self.victim = None
        self.murderer = None
        self.suspect = None
    
    def main_flow(self):
        """
        범인 찾기

        1. 용의자 조사
        2. 범인 지목
        """
        # 조사 단계 (인상착의를 수집, 무제한)
        while True:
            self.investigate()
            if self.prompt_choice("\n계속 조사하시겠습니까? (네/아니오): ") == '아니오':
                break

        # 범인 지목
        self.accuse()

    def play(self):
        """
        게임 실행

        1. 인트로
        2. 범인 찾기
        """
        self.show_intro()
        self.main_flow()


# 게임 실행
if __name__ == "__main__":
    game = DetectiveGame()
    game.play()