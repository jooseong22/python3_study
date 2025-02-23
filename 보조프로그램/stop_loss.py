# 진입가격을 변수에 저장합니다.
entry_price = 96251.81  # 진입가격 (USDT)

# 대표님께서 단기 평균 변동폭(ATR 5)을 위험폭으로 사용한다고 가정합니다.
risk = 112.1  # 위험폭 (USDT)

# 숏 포지션에서 손절가(SL)는 진입가격에 위험폭을 더합니다.
stop_loss = entry_price + risk  # SL = 진입가격 + 위험폭

# 숏 포지션에서 익절가(TP)는 진입가격에서 위험폭의 2배를 뺍니다.
take_profit = entry_price - 2 * risk  # TP = 진입가격 - 2×위험폭

# 기초 자산 기준 수익률(익절)과 위험률(손실) 계산
profit_percent = ((entry_price - take_profit) / entry_price) * 100  # 숏은 진입가에서 TP를 뺀 값이 이익
risk_percent = ((stop_loss - entry_price) / entry_price) * 100      # 손절은 SL과 진입가의 차

# 레버리지 20배 적용 (마진 기준)
leverage = 20
profit_margin_percent = profit_percent * leverage
risk_margin_percent = risk_percent * leverage

# 결과 출력
print("숏 손절가 (SL):", round(stop_loss, 2), "USDT")       # 손절가 출력
print("숏 익절가 (TP):", round(take_profit, 2), "USDT")      # 익절가 출력
print("기초 자산 기준 익절 수익률: {:.3f}%".format(profit_percent))
print("기초 자산 기준 위험(손실)률: {:.3f}%".format(risk_percent))
print("레버리지 20배 적용 익절 수익률:", round(profit_margin_percent, 2), "%")
print("레버리지 20배 적용 위험(손실)률:", round(risk_margin_percent, 2), "%")
