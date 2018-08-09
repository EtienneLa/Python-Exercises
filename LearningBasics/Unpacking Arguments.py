def health_caculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - cigs_smoked
    print(answer)


max_data = [25, 5, 25]

health_caculator(max_data[0], max_data[1], max_data[2])
health_caculator(*max_data)
