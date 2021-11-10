
Nx = 4
Ny = 3

# for j in range(1,4):
#   for i in range(1,5):
#       eq_ij = "\\frac{1}{\\Delta t} (u^{n+1}_{%d,%d}-u^{n}_{%d,%d}) + \\sigma\\left[\\frac{2}{\\Delta x^2+\\Delta y^2} u^{n}_{%d,%d} - \\frac{1}{\\Delta x^2} u^{n}_{%d,%d} -  \\frac{1}{\\Delta x^2} u^{n}_{%d,%d} +  \\frac{1}{\\Delta y^2} u^{n}_{%d,%d} +  \\frac{1}{\\Delta y^2} u^{n}_{%d,%d}\\right] = f^{n}_{%d,%d} \\\\ " % (i, j, i, j, i, j, i+1, j, i-1, j, i, j+1, i, j-1, i, j)
#       print(eq_ij)


# for j in range(1,4):
#   for i in range(1,5):
#       print "u^{n+1}_{%d,%d}\\\\" %(i, j)

# for j in range(1,4):
#   for i in range(1,5):
#       print "u^{n}_{%d,%d}\\\\" %(i, j)

# for j in range(1,4):
#     for i in range(1,5):
#         u = ["0"] * 12
#         I = (j-1)*Nx+ i-1
#         u[I] = "\\frac{2}{\\Delta x^2}+\\frac{2}{\\Delta y^2}"
#         if i > 1 :
#             u[I-1] = "\\frac{-1}{\\Delta x^2}"
#         if i < Nx :
#             u[I+1] = "\\frac{-1}{\\Delta x^2}"
#         if j > 1 :
#             u[I-Nx] = "\\frac{-1}{\\Delta y^2}"
#         if j < Ny :
#                u[I+Nx] = "\\frac{-1}{\\Delta y^2}"
#         line = "%s & %s & %s & %s & %s & %s & %s & %s & %s & %s & %s & %s \\\\" % (u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], u[10], u[11])
#         print(line)



# for j in range(1,4):
#     for i in range(1,5):
#         u = ["0"] * 12
#         I = (j-1)*Nx+ i-1
#         u[I] = "\\alpha"
#         if i > 1 :
#             u[I-1] = "\\beta"
#         if i < Nx :
#             u[I+1] = "\\beta"
#         if j > 1 :
#             u[I-Nx] = "\\gamma"
#         if j < Ny :
#                u[I+Nx] = "\\gamma"
#         line = "%s & %s & %s & %s & %s & %s & %s & %s & %s & %s & %s & %s \\\\" % (u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7], u[8], u[9], u[10], u[11])
#         print(line)


# for j in range(1,4):
#     for i in range(1,5):
#         greenip1j = greenip1jf = greenim1j = greenim1jf = greenijp1 = greenijp1f = greenijm1 = greenijm1f = ""
#         if i == 1 :
#             greenim1j = "{\\color{green}"
#             greenim1jf = "}"
#         if i == Nx :
#             greenip1j = "{\\color{green}"
#             greenip1jf = "}"
#         if j == 1 :
#             greenijm1 = "{\\color{green}"
#             greenijm1f = "}"
#         if j == Ny :
#             greenijp1 = "{\\color{green}"
#             greenijp1f = "}"
#         eq_ij = "(u^{n+1}_{%d,%d}-u^{n}_{%d,%d}) + \\sigma\\Delta t\\left(\\alpha u^{n}_{%d,%d} + \\beta %su^{n}_{%d,%d}%s +  \\beta %su^{n}_{%d,%d}%s +  \\gamma %su^{n}_{%d,%d}%s +  \\gamma %su^{n}_{%d,%d}%s\\right) = f^{n}_{%d,%d} \\\\ " % (i, j, i, j, i, j, greenip1j ,i+1, j, greenip1jf, greenim1j, i-1, j, greenim1jf, greenijp1, i, j+1, greenijp1f, greenijm1, i, j-1, greenijm1f, i, j)
#         print(eq_ij)

for I in range(Nx*Ny):
    print "u^{n+1}_{%d}\\\\" %(I)

for I in range(Nx*Ny):
    print "u^{n}_{%d}\\\\" %(I)

for I in range(Nx*Ny):
    print "f^{n}_{%d}\\\\" %(I)