# 초기값과 최종값
initial_value = 97873
final_value = 97363

# 변동률 계산
percentage_movement = ((initial_value - final_value) / initial_value) * 100
print(f"가격 변동률: {percentage_movement:.3f}%")

# 레버리지 설정
leverage = 20

# 레버리지 적용 후 최대 변동 계산
max_value_with_leverage = percentage_movement * leverage
print(f"레버리지 적용 최대 변동: {max_value_with_leverage:.3f}%")
