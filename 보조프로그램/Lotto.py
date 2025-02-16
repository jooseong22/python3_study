import random

def generate_lotto_numbers_with_fixed(fixed_numbers, exclude_numbers, games=5):
    # 고정 번호와 제외 번호 중복 체크
    if any(num in exclude_numbers for num in fixed_numbers):
        raise ValueError("고정 번호와 제외 번호가 중복됩니다!")
    
    # 고정 번호가 6개를 초과하는지 체크
    if len(fixed_numbers) > 6:
        raise ValueError("고정 번호가 6개를 초과할 수 없습니다!")
    
    lotto_games = []
    for _ in range(games):
        # 고정 번호로 시작
        lotto = fixed_numbers.copy()
        
        # 나머지 번호 추가
        while len(lotto) < 6:
            num = random.randint(1, 45)
            if num not in lotto and num not in exclude_numbers:
                lotto.append(num)
        lotto_games.append(sorted(lotto))
    return lotto_games

# 사용 예시
fixed = []  # 원하는 만큼의 고정 번호 설정
excluded = [1,30,31,34,39,41,45,7]  # 제외할 번호 설정
lotto_results = generate_lotto_numbers_with_fixed(fixed, excluded)

# 결과 출력
print(f"고정 번호: {fixed}")
print(f"제외 번호: {excluded}")
print("-" * 40)
for i, numbers in enumerate(lotto_results, 1):
    print(f"{i}번째 게임: {numbers}")
