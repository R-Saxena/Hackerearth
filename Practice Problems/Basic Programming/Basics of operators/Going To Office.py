N = int(input())
Oc, Of, Od = list(map(int, input().split()))
Cs, Cb, Cm, Cd = list(map(int, input().split()))

Online = Oc + (N-Of)*Od
classic = Cb + int(N/Cs)*Cm + Cd*N
if Online > classic:
    print('Classic Taxi')
else:
    print('Online Taxi')