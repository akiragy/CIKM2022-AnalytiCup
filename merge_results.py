path_all = 'prediction.csv'
path_group1_task6 = 'exp/group1/gcflplus_gin_on_cikmcup_lr0.1_lstep1_/prediction3000.csv'
path_group1_task7 = 'exp/group1/gcflplus_gin_on_cikmcup_lr0.1_lstep1_/prediction4220.csv'
path_group1_task8 = 'exp/group1/gcflplus_gin_on_cikmcup_lr0.1_lstep1_/prediction3900.csv'
path_group1_task11 = 'exp/group1/gcflplus_gin_on_cikmcup_lr0.1_lstep1_/prediction1020.csv'
path_group1_task12 = 'exp/group1/gcflplus_gin_on_cikmcup_lr0.1_lstep1_/prediction4940.csv'
path_group2 = 'exp/group2/FedAvg_gin_on_cikmcup_lr0.1_lstep1_/prediction440.csv'
path_group3 = 'exp/group3/gcflplus_gin_on_cikmcup_lr0.1_lstep1_/prediction.csv'


with open(path_all, 'w') as f_all:
    pass

with open(path_all, 'a') as f_all:
    # task 1.2.3.4.5
    with open(path_group3) as f:
        for line in f:
            f_all.write(line)
    # task 6
    with open(path_group1_task6) as f:
        for line in f:
            if line.split(',')[0] == '6':
                f_all.write(line)
    # task 7
    with open(path_group1_task7) as f:
        for line in f:
            if line.split(',')[0] == '7':
                f_all.write(line)
    # task 8
    with open(path_group1_task8) as f:
        for line in f:
            if line.split(',')[0] == '8':
                f_all.write(line)
    # task 9.10
    with open(path_group2) as f:
        for line in f:
            if line.split(',')[0] == '1':
                line_new = '9,' + ','.join(line.split(',')[1:])
                f_all.write(line_new)
            elif line.split(',')[0] == '2':
                line_new = '10,' +','.join(line.split(',')[1:])
                f_all.write(line_new)
    # task 11
    with open(path_group1_task11) as f:
        for line in f:
            if line.split(',')[0] == '9':
                line_new = '11,' + ','.join(line.split(',')[1:])
                f_all.write(line_new)
    # task 12
    with open(path_group1_task12) as f:
        for line in f:
            if line.split(',')[0] == '10':
                line_new = '12,' + ','.join(line.split(',')[1:])
                f_all.write(line_new)
    # task 13
    with open(path_group2) as f:
        for line in f:
            if line.split(',')[0] == '3':
                line_new = '13,' + ','.join(line.split(',')[1:])
                f_all.write(line_new)


