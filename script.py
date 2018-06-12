city_name = "Istanbul, Turkey"
pop_1927 = 691000
pop_2017 = 15029231 
pop_change = pop_2017 - pop_1927
percentage_gr = (pop_change/pop_1927)*100
annual_gr = percentage_gr/90
def population_growth(year_one,year_two,population_one,population_two):
    growth_rate = (((pop_two-pop_one)/pop_one) * 100)/(year_two-year_one)     
    return growth_rate 
pop_one = 691000
pop_two = 15029231
year_two = 2017
year_one = 1927
print (annual_gr)
set_one = population_growth(year_one,year_two,pop_one,pop_two)
print (set_one)
year_one_one = 1950
year_two_two = 2000
set_two = population_growth(year_one_one,year_two_two,pop_one,pop_two)
print(set_two)
report  = "The annual population of Instambul for"+" " + str (year_one) + " "+ "and "+ " " + str(year_two)+" "+ "were"+" "+ str(pop_one)+" "+"and "+ str(pop_two) +" "+ "respectively."+" "+"The annual growth rate for these time period was"+" "+ str(set_one)+"."+"This compares less to the higher population growth rate of " +" "+ str(set_two)+ " "+"for the years" +" "+ str (year_one_one)+ " " +"and" +" "+ str(year_two_two)+"."
print (report)