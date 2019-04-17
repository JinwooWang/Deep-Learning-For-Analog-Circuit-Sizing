opamp GBW
*dgsb
.model NMOS NMOS VTO = 0.7 KP = 110U GAMMA = 0.4 LAMBDA = 0.04 PHI = 0.7
.model PMOS PMOS VTO = -0.7 KP = 50U GAMMA = 0.57 LAMBDA = 0.05 PHI = 0.8
m1 2 2 10 10 nmos w=4.5u l=1u
m2 4 4 1 1 pmos w=15u l=1u
m3 5 4 1 1 pmos w=15u l=1u
m4 4 8 3 3 nmos w=5u l=1u
m5 5 9 3 3 nmos w=5u l=1u
m6 3 2 10 10 nmos w=4.5u l=1u
m7 7 5 1 1 pmos w=94u l=1u
m8 7 2 10 10 nmos w=13u l=1u
r1 1 2 50k
r2 6 7 10k
cc 5 6 200f

vdd 1 0 dc 2.5
CL 7 0 10p
vm 8 0 dc 0.0
vp 9 0 dc 0.0 ac 1.0
vss 0 10 dc 2.5

.DC vdd 2.5 2.5 0.1
.print dc v(2)
.print dc v(3)
.print dc v(4)
.print dc v(5)
.print dc v(6)
.print dc v(7)
.print dc v(8)
.print dc v(9)
.print dc v(10)
*.ac dec 10 1 10000meg
*.plot ac vdb(7)
*.plot ac vp(7)

.end
