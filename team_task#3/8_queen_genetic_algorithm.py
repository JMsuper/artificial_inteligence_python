import random

POPULATION_SIZE = 8	# 개체 집단의 크기
MUTATION_RATE = 0.2	# 돌연 변이 확률
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
            i_row_idx = int(self.genes[i])
            i_col_idx = i
            for j in range(i+1,SIZE):
                j_row_idx = int(self.genes[j])
                j_col_idx = j
                if i_row_idx == j_row_idx or i_col_idx == j_col_idx or abs(i_row_idx - j_row_idx) == abs(i_col_idx - j_col_idx):
                    value += 1

        self.fitness = 28 - value
        return self.fitness

    def __str__(self):
        return self.genes.__str__()

# 염색체와 적합도를 출력한다. 
def print_p(pop):
    i = 0
    for x in pop:
        print("염색체 #", i, "=", x, "적합도=", x.cal_fitness())
        i += 1
    print("")

# 선택 연산
def select(pop):
    max_value  = sum([c.cal_fitness() for c in population])
    pick    = random.uniform(0, max_value)
    current = 0
    
    # 룰렛휠에서 어떤 조각에 속하는지를 알아내는 루프
    for c in pop:
        current += c.cal_fitness()
        if current > pick:
            return c

# 교차 연산
def crossover(pop):
    father = select(pop)
    mother = select(pop)
    index = random.randint(1, SIZE - 1)
    child1 = father.genes[:index] + mother.genes[index:] 
    child2 = mother.genes[:index] + father.genes[index:] 
    return (child1, child2)
    
# 돌연변이 연산
def mutate(c):
    global count
    for i in range(SIZE):
        if random.random() < MUTATION_RATE:
            c.genes = c.genes[: i] + str(random.randint(0,7)) + c.genes[i+1:]

# 메인 프로그램
population = []
i=0

# 초기 염색체를 생성하여 객체 집단에 추가한다. 
while i<POPULATION_SIZE:
    population.append(Chromosome(""))
    i += 1

count=0
population.sort(key=lambda x: x.cal_fitness(), reverse=True)
print("세대 번호=", count)
print_p(population)
count=1

while population[0].fitness < 28:
    new_pop = []

    # 선택과 교차 연산
    for _ in range(POPULATION_SIZE//2):
        c1, c2 = crossover(population)
        new_pop.append(Chromosome(c1))
        new_pop.append(Chromosome(c2))

    # 자식 세대가 부모 세대를 대체한다. 
    # 깊은 복사를 수행한다. 
    population = new_pop.copy()
    
    # 돌연변이 연산
    for c in population: mutate(c)

    # 출력을 위한 정렬
    population.sort(key=lambda x: x.cal_fitness(), reverse=True)
    print("세대 번호=", count)
    print_p(population)
    count += 1


    # if population[0].fitness == 28:
    #     print("세대 번호=", count)
    #     print_p(population)
    # else:
    #     print("세대 번호=", count)
    #     count += 1
    if count > 1000000 : break