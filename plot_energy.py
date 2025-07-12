import matplotlib.pyplot as plt

x = list(range(1,61))

y = [
0.0000,
0.0137,
0.0695,
0.1408,
0.2300,
0.3423,
0.4472,
0.5973,
0.7731,
0.9685,
1.1804,
1.4095,
1.6700,
2.0046,
2.4133,
2.8524,
3.3428,
3.8724,
4.3856,
4.9412,
5.5809,
6.2613,
6.9505,
7.6232,
8.2603,
8.8471,
9.3664,
9.8096,
10.1676,
10.4305,
10.5936,
10.6533,
10.6230,
10.4973,
10.2752,
9.9723,
9.5873,
9.1372,
8.6325,
8.0887,
7.5111,
6.9432,
6.4256,
6.0430,
5.5782,
5.1453,
4.7794,
4.4555,
4.2411,
4.0243,
3.8094,
3.6557,
3.5131,
3.4194,
3.3246,
3.2395,
3.1765,
3.1294,
3.0986,
3.0967
]

plt.figure(figsize=(8,5))
plt.plot(x,y,marker='o', linestyle='-',color="purple")
plt.xlabel("Indexed Reaction Coordinate", fontsize=16)
plt.ylabel("QM/MM Energy (kcal/mol)",fontsize=16)
plt.xticks(range(1, 66, 5))     
plt.yticks(range(0, 13, 2))
plt.title("QM/MM Energy Profile")
plt.tight_layout()
plt.savefig("QMMM_Energy_Profile.png", dpi=300)
plt.show()

