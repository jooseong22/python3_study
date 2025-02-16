import math

# 초기 투자 금액 (1000달러)
initial_investment = 1000

# 주간 수익률 (42.4% -> 0.424)
weekly_rate = 0.1
weekly_multiplier = 1 + weekly_rate  # 한 주 후 배수 (1.424)

# 각 기간을 일수로 정의 (가정)
days_in_week = 7       # 1주일 = 7일
days_in_month = 30     # 1개월 = 30일
days_in_quarter = 90   # 1분기 = 90일
days_in_6months = 180  # 6개월 = 180일
days_in_year = 365     # 1년 = 365일

# [1] 주간 수익률을 바탕으로 '일일 복리'를 계산
# 1주일에 1.424배가 되므로, 하루마다 매일 곱해지는 배수는 (1.424)^(1/7)
daily_multiplier = weekly_multiplier ** (1/days_in_week)
daily_rate = daily_multiplier - 1  # 일일 수익률

# [2] 특정 일수 후의 누적 배수를 계산하는 함수 (복리 효과)
def cumulative_multiplier(days):
    # 예: days일 후 배수 = weekly_multiplier^(days/7)
    return weekly_multiplier ** (days / days_in_week)

# [3] 각 기간에 대한 누적 배수 계산
multiplier_daily    = cumulative_multiplier(1)               # 1일 후
multiplier_weekly   = cumulative_multiplier(days_in_week)      # 7일 후
multiplier_monthly  = cumulative_multiplier(days_in_month)     # 30일 후
multiplier_quarterly= cumulative_multiplier(days_in_quarter)   # 90일 후
multiplier_6months  = cumulative_multiplier(days_in_6months)   # 180일 후
multiplier_yearly   = cumulative_multiplier(days_in_year)      # 365일 후

# [4] 초기 투자금에 배수를 곱하여 최종 누적 투자금 계산
final_daily    = initial_investment * multiplier_daily
final_weekly   = initial_investment * multiplier_weekly
final_monthly  = initial_investment * multiplier_monthly
final_quarterly= initial_investment * multiplier_quarterly
final_6months  = initial_investment * multiplier_6months
final_yearly   = initial_investment * multiplier_yearly

# [5] 각 기간별 수익률(%)는 최종 배수에서 1을 뺀 후 100을 곱함
rate_daily_percent     = daily_rate * 100
rate_weekly_percent    = weekly_rate * 100
rate_monthly_percent   = (multiplier_monthly - 1) * 100
rate_quarterly_percent = (multiplier_quarterly - 1) * 100
rate_6months_percent   = (multiplier_6months - 1) * 100
rate_yearly_percent    = (multiplier_yearly - 1) * 100

# 결과 출력
print("기간별 수익률:")
print(f"1일 수익률: 약 {rate_daily_percent:.2f}%")
print(f"1주일 수익률: 약 {rate_weekly_percent:.2f}%")
print(f"1개월 수익률: 약 {rate_monthly_percent:.2f}%")
print(f"1분기 수익률: 약 {rate_quarterly_percent:.2f}%")
print(f"6개월 수익률: 약 {rate_6months_percent:.2f}%")
print(f"1년 수익률: 약 {rate_yearly_percent:.2f}%\n")

print("투자금 1000불 기준 최종 누적액:")
print(f"1일 후: ${final_daily:.2f}")
print(f"1주일 후: ${final_weekly:.2f}")
print(f"1개월 후: ${final_monthly:.2f}")
print(f"1분기 후: ${final_quarterly:.2f}")
print(f"6개월 후: ${final_6months:.2f}")
print(f"1년 후: ${final_yearly:.2f}")
