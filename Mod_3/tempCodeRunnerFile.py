# Part 2
L1 = [i for i in range(100)]
L2 = [i for i in range(200)]
L3 = [i for i in range(400)]
L4 = [i for i in range(600)]
L5 = [i for i in range(800)]

print("=================================================")  
print("n     t_const (ms)     t_lin (ms)     t_quad (ms)")
print("-------------------------------------------------")
print("100   {:.7f}          {:.7f}          {:.7f}".format(time_function(constant, L1) * 1000, time_function(linear, L1) * 1000, time_function(quadratic, L1) * 1000))
print("200   {:.7f}          {:.7f}          {:.7f}".format(time_function(constant, L2) * 1000, time_function(linear, L2) * 1000, time_function(quadratic, L2) * 1000))
print("400   {:.7f}          {:.7f}          {:.7f}".format(time_function(constant, L3) * 1000, time_function(linear, L3) * 1000, time_function(quadratic, L3) * 1000))
print("600   {:.7f}          {:.7f}          {:.7f}".format(time_function(constant, L4) * 1000, time_function(linear, L4) * 1000, time_function(quadratic, L4) * 1000))
print("800   {:.7f}          {:.7f}          {:.7f}".format(time_function(constant, L5) * 1000, time_function(linear, L5) * 1000, time_function(quadratic, L5) * 1000))
print("-------------------------------------------------")

# Part 3
def search(args):
    return 1 in args

def search_string(args):
    return "1" in args


# n = 1000
t_list = time_function(search, [i for i in range(10000)])
t_tup = time_function(search, (i for i in range(10000)))
t_string = time_function(search_string, "1"*(10000))
t_set = time_function(search, {i for i in range(10000)})

# n = 2000
t_list2 = time_function(search, [i for i in range(20000)])
t_tup2 = time_function(search, (i for i in range(20000)))
t_string2 = time_function(search_string, "1"*(20000))
t_set2 = time_function(search, {i for i in range(20000)})

# n = 4000
t_list3 = time_function(search, [i for i in range(40000)])
t_tup3 = time_function(search, (i for i in range(40000)))
t_string3 = time_function(search_string, "1"*(40000))
t_set3 = time_function(search, {i for i in range(40000)})

# n = 6000
t_list4 = time_function(search, [i for i in range(60000)])
t_tup4 = time_function(search, (i for i in range(60000)))
t_string4 = time_function(search_string, "1"*(60000))
t_set4 = time_function(search, {i for i in range(60000)})

# n = 8000
t_list5 = time_function(search, [i for i in range(80000)])
t_tup5 = time_function(search, (i for i in range(80000)))
t_string5 = time_function(search_string, "1"*(80000))
t_set5 = time_function(search, {i for i in range(80000)})


print("=================================================")  
print("             Contains (times in ms)              ")
print("-------------------------------------------------")
print("n      t_list       t_tup       t_str       t_set")    
print("-------------------------------------------------")   
print("100    {:.7f}   {:.7f}   {:.7f}   {:.7f}".format(t_list * 1000, t_tup * 1000, t_string * 1000, t_set * 1000))
print("100    {:.7f}   {:.7f}   {:.7f}   {:.7f}".format(t_list2 * 1000, t_tup2 * 1000, t_string2 * 1000, t_set2 * 1000)) 
print("100    {:.7f}   {:.7f}   {:.7f}   {:.7f}".format(t_list3 * 1000, t_tup3 * 1000, t_string3 * 1000, t_set3 * 1000)) 
print("100    {:.7f}   {:.7f}   {:.7f}   {:.7f}".format(t_list4 * 1000, t_tup4 * 1000, t_string4 * 1000, t_set4 * 1000)) 
print("100    {:.7f}   {:.7f}   {:.7f}   {:.7f}".format(t_list5 * 1000, t_tup5 * 1000, t_string5 * 1000, t_set5 * 1000))  
print("-------------------------------------------------")                          