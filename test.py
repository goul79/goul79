import pyupbit

access = "ZSxO3kI91FSbxCymUxWryOBEHxm9eAwuWUQOLfgi"          # 본인 값으로 변경
secret = "FIRscki8kFupDX8wFeJSZIcOPGLtX58MLHYYOGAu"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-DOGE"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
