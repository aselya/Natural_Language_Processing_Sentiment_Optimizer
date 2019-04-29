#needed imports
import data_setup as data_S
import hashMap
import nlp
import random
import numpy as np

#class variables
GENERATIONS = 20
POPULATION_OF_PHRASES = []
IDEAL_POPULATION_SIZE = 20
IDEAL_PHRASE_LENGTH = 3
MUTATION_RATE = 0.05
NUMBER_OF_PARENTS = 4
HASHMAP = hashMap.HashMap()

class Chromosomes:
    #creates and sets the insult string value for the chromosome
    #uses the correct a or an article
    def set_insult_string(chrom):
        while chrom.genes_that_contain_phrases[0][:1] not in ['a','e','i','o', 'u']:
            insult_string =("Thou art a " + ' '.join(chrom.genes_that_contain_phrases) + "     |fitness score:" + str(chrom.fittness_score))
            chrom.insult_string = insult_string
            return  insult_string
        else:
            insult_string = ("Thou art an " + ' '.join(chrom.genes_that_contain_phrases)+ "     |fitness score:" + str(chrom.fittness_score))
            chrom.insult_string = insult_string
            return  insult_string
    #sets the fittness score
    #first checks hashmap then calls google api
    def set_fittness_score(chrom):
        #random_score = random.randint(-10, 10)
        #chrom.fittness_score = random_score
        if(str(HASHMAP.get(chrom.insult_string)== None)):
            chrom.fittness_score = nlp.analyze(chrom.set_insult_string())
            print("google API used")
        else:
            chrom.fittness_score = HASHMAP.get(chrom.insult_string())
            print("hashMap used")
        return chrom

    #sets initial structure for chromosome
    def __init__(self, length):
        self.genes_that_contain_phrases = []
        self.fittness_score = 0
        self.current_length = 0
        self.insult_string = ""
        #fills the chromsome with genes
        while len(self.genes_that_contain_phrases) < length:
            new_gene = data_S.get_random_term(self.current_length)
            self.current_length += 1
            self.genes_that_contain_phrases.append(new_gene)
        self.set_insult_string()
        self.set_fittness_score()
 #end class chromosomes


def sort_pop_by_fittness_score (pop):
    return pop.sort(key=lambda x: x.fittness_score)

#returns a population only containing parents
def isolate_parents (pop, number_of_parents):
    sort_pop_by_fittness_score(pop)
    if number_of_parents < len(pop):
        new_pop = pop[:number_of_parents]
        pop = new_pop
        print("######PARENTS SELECTED#######")
        print_population(pop)
        return pop
    else:
        print("Need larger population or less parents")


def print_population(pop):
    for chrom in pop:
        print(chrom.set_insult_string())



#makes a new population of the correct size
def build_initial_population():
    while len(POPULATION_OF_PHRASES) < IDEAL_POPULATION_SIZE:
        new_chrom = Chromosomes( IDEAL_PHRASE_LENGTH)
        POPULATION_OF_PHRASES.append(new_chrom)

    print_population(POPULATION_OF_PHRASES)
    return POPULATION_OF_PHRASES

#checks for duplicate terms in any chromosome
def check_for_duplicates(chrom, new_phrase):
    if len(chrom.genes_that_contain_phrases)==0:
        return new_phrase
    count = 0
    for gene in chrom.genes_that_contain_phrases:
        if str(chrom.genes_that_contain_phrases[count]) == str(new_phrase):
            print("Duplicate occured fixing now")
            check_for_duplicates(chrom, data_S.get_random_term(count))
            count +=1
    print("no Duplicates")
    return new_phrase


#determines if a gene is to be mutated
def mutation(chrom):
    count = 0
    for genes in chrom.genes_that_contain_phrases:
        rand = random.random()
        if rand <= MUTATION_RATE:
            print("MUTATION HAS OCCURED")
            chrom.genes_that_contain_phrases[count] = check_for_duplicates(chrom,data_S.get_random_term(count) )
            #chrom.genes_that_contain_phrases[count] = data_S.get_random_term(count)
            chrom.set_insult_string()
        count += 1


#uses a selection of 2 parent chromosomes to initiate crossbreeding
def crossbreed (parent1, parent2):
    length = len(parent1.genes_that_contain_phrases)
    child_chrom = Chromosomes(length)
    for i in range(length):
        if i % 2 == 0:
            child_chrom.genes_that_contain_phrases[i] = parent1.genes_that_contain_phrases[i]
        else:
            child_chrom.genes_that_contain_phrases[i] = parent2.genes_that_contain_phrases[i]
    mutation(child_chrom)
    return child_chrom



#selects a random parent from the parent population
#initiates crossbreeding
def select_random_parents_and_crossbreed(pop, number_of_parents):

    sort_pop_by_fittness_score (pop)

    while len(pop) < IDEAL_POPULATION_SIZE:

        parent1index = random.randint(0, number_of_parents-1)
        parent2index = random.randint(0, number_of_parents-1)
        while parent2index == parent1index:
            parent2index = random.randint(0, number_of_parents-1)
        parent1 = pop[parent1index]
        parent2 = pop[parent2index]

        pop.append(crossbreed (parent1, parent2))

#main GA loop
pop = build_initial_population()
count = 0
best_from_each_generation=[]
while count < GENERATIONS:
    pop = isolate_parents (pop, NUMBER_OF_PARENTS)
    best_from_each_generation.append(pop[0])
    select_random_parents_and_crossbreed(pop, NUMBER_OF_PARENTS)
    print("############ GENERATION: " + str(count+1))
    print_population(pop)

    count += 1

print("############ FINAL GENERATION: " + str(count+1))
sort_pop_by_fittness_score(pop)
print_population(pop)

print("############ BEST FROM EACH GENERATION: " + str(count+1))
print_population(best_from_each_generation)
