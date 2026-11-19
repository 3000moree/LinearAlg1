import numpy as np

u = np.array([1, 2], dtype = float)
v = np.array([6, -3], dtype = float)

dot_product = np.dot(u, v)
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

print(f"내젹 = {dot_product:.6f}")

if norm_u == 0 or norm_v == 0:
    print("직교")
    print("영벡터 포함, 각도 정의 못함")
else:
    cos_theta = dot_product / (norm_v*norm_u)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    theta_deg = np.degrees(np.arccos(cos_theta))
    is_orthogonal = np.isclose(
        cos_theta, 0.0, atol=1e-10, rtol=0.0
    )

    print(f"cos(theta) = {cos_theta:6f}")
    print(f"각도 = {theta_deg:.6f}")
    print("직교" if is_orthogonal else "직교 안함")