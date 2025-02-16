

def calculate_loss(leverage, drop_percentage):
    """
    레버리지와 코인 가격 하락률을 입력받아 손실율을 계산하는 함수입니다.
    
    매개변수:
    - leverage: 레버리지 배수 (예: 20)
    - drop_percentage: 코인이 하락한 퍼센트 (예: 0.5는 0.5% 하락)
    
    반환:
    - loss_percentage: 계산된 실제 손실율 (%)
    """
    # 손실율 계산: 레버리지 배수 * 코인 가격 하락률
    loss_percentage = leverage * drop_percentage
    return loss_percentage

# 예시: 레버리지 20배, 코인이 0.5% 하락하는 경우
leverage = 20
drop_percentage = 0.5  # 0.5% 하락

# 함수 호출하여 손실율 계산
loss = calculate_loss(leverage, drop_percentage)

# 결과 출력 (소수점 없이 %로 표시)
print(f"코인이 {drop_percentage}% 하락할 때, {leverage}배 레버리지로 인한 손실율은 약 {loss}% 입니다.")
