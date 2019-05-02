
import nlp
List_of_insults = [None]*10

List_of_insults[0] = 'A most notable coward, an infinite and endless liar, an hourly promise breaker, the owner of no one good quality.'
#All’s Well That Ends Well (Act 3, Scene 6)

List_of_insults[1]= 'Away, you starvelling, you elf-skin, you dried neat’s-tongue, bull’s-pizzle, you stock-fish!'
#Henry IV Part I (Act 2, Scene 4)

List_of_insults[2]= 'Away, you three-inch fool! '
#The Taming of the Shrew (Act 3, Scene 3)

List_of_insults[3]= 'Come, come, you froward and unable worms!'
#The Taming Of The Shrew (Act 5, Scene 2)

List_of_insults[4]= 'Go, prick thy face, and over-red thy fear, Thou lily-liver’d boy.'
#Macbeth (Act 5, Scene 3)

List_of_insults[5]= 'His wit’s as thick as a Tewkesbury mustard.'
#Henry IV Part 2 (Act 2, Scene 4)

List_of_insults[6]= 'I am pigeon-liver’d and lack gall.'
#Hamlet (Act 2, Scene 2)

List_of_insults[7]= 'I am sick when I do look on thee '
#A Midsummer Night’s Dream (Act 2, Scene 1)

List_of_insults[8]= 'I must tell you friendly in your ear, sell when you can, you are not for all markets.'
#As You Like It (Act 3 Scene 5)

List_of_insults[9]= 'If thou wilt needs marry, marry a fool; for wise men know well enough what monsters you make of them.'
#Hamlet (Act 3, Scene 1)


count = 0
insults_with_scores = []
while count < len(List_of_insults):
    fittness_score = 100*round(nlp.analyze(List_of_insults[count]), 7)
    string = (str(List_of_insults[count])+ '| Fittness Score: '+ str(fittness_score))
    insults_with_scores.append(string)
    count += 1
print('\n')
print('\n'.join(map(str, insults_with_scores)))
