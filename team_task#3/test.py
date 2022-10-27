import random

POPULATION_SIZE = 5		# 개체 집단의 크기
MUTATION_RATE = 0.1			# 돌연 변이 확률
SIZE = 8				# 하나의 염색체에서 유전자 개수		

# 염색체를 클래스로 정의한다. 
class Chromosome:
    def __init__(self, g):
        self.genes = g		# 유전자는 리스트로 구현된다. 
        self.fitness = 0		# 적합도
        if self.genes.__len__()==0:	# 염색체가 초기 상태이면 초기화한다. 
            temp_list = ['0','1','2','3','4','5','6','7']    
            random.shuffle(temp_list)
            self.genes = "".join(temp_list)
        
    
    def cal_fitness(self):		# 적합도를 계산한다. 
        self.fitness = 0
        value = 0
        for i in range(SIZE):
            value += self.genes[i]*pow(2,SIZE-1-i)
        self.fitness = value
        return self.fitness

    def __str__(self):
        return self.genes.__str__()

# 돌연변이 연산
def mutate(c):
    for i in range(SIZE):
        if random.random() < 0.1:
            c.genes = c.genes[: i] + str(random.randint(0,7)) + c.genes[i+1:]

temp_c = Chromosome("")
print(temp_c)
mutate(temp_c)
print(temp_c)

# temp_str = "0123456"
# print(temp_str[:3] + "4" + temp_str[4:])