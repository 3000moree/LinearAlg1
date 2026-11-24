import numpy as np

# 두 벡터
u = np.array([2, -4])
v = np.array([4, 2])

#내적 계산
dot_uv = np.dot(u,v)
print("u dot v =", dot_uv)

#직교 여부 판단
if np.allclose(0, dot_uv):
    print("두 벡터는 서로 직교")
else:
    print("두 벡터는 서로 직교하지 않음")

#사이각 계산
norm_product = np.linalg.norm(u) * np.linalg.norm(v)

if norm_product > 0:
    cos_theta = dot_uv / norm_product
    theta = np.degrees(
        np.arccos(np.clip(cos_theta, -1, 1))
    )
    print(f"두 벡터 사이각 = {theta:.6f}도")

else:
    print("0벡터가 포함되면 사이각은 정의되지 않음")
    