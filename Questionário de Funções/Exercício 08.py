s1, s2, s3 = input().split()

def duplica(f):
    return f+f
def duplica_o_duplicado(f):
    print(duplica(f)+duplica(f))

def imprime_parte_linha1(s1,s2):
    return (" "+s1+s2+" ")
    
def imprime_parte_linha1_fim():
    return  "\n"
    
def imprime_parte_linha2(s1,s2,s3):
    return s1+2*s3+s2
    
def imprime_parte_linha2_fim():
    return " \n"
      
def imprime_linha1(s1,s2,s3):
    duplica_o_duplicado((imprime_parte_linha1(s1,s2)))
    duplica_o_duplicado((imprime_parte_linha2(s1,s2,s3)))

def imprime_linha2(s1,s2,s3):
    duplica_o_duplicado((imprime_parte_linha1(s1,s2)))
    duplica_o_duplicado((imprime_parte_linha2(s1,s2,s3)))
    
def imprime_parte_padrão(s1,s2,s3):
    imprime_linha1(s1,s2,s3)
    imprime_linha2(s1,s2,s3)

def imprime_padrão(s1,s2,s3):
    imprime_parte_padrão(s1,s2,s3)
    imprime_parte_padrão(s1,s2,s3)
    
imprime_padrão(s1,s2,s3)