
import memory_profiler as mem_profile
import random
import time

names=["Johnson","David","Rox","Newton","Albeta","Emily","Joy"]
majors=["Math","English","French","Economics","Computer sci.","Business"]

print("memory before {} MB".format(mem_profile.memory_usage()))
def people_list(num_people):
    result=[]
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person={
            'id':i,
            'name':random.choice(names),
            'major':random.choice(majors)
        }

        yield person

t1=time.time()
# people=people_list(10000000)
# people= people_generator(10000000)
t2=time.time()

#
#
#
# for i in people:
#     print(i)
#
# print("Memory after {} MB".format(mem_profile.memory_usage()))
# print("Totel execution time is {}".format(t2-t1))

t=[1,1,2,1,3,4,5]
t.insert(0,1)
print(t)



