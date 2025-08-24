print('                                               Student Enrollment For Streams                                                                    ')





ai_stream = {'Nibras' ,'Anas' ,'Sofia' ,'Akash'}
cs_stream = {'Nibras' ,'Rahul' ,'Hasan' ,'Drake' ,'Akash'}


print("Students in both streams: ", ai_stream & cs_stream)
print("Students only in AI stream: ", ai_stream - cs_stream)
print("All Students: ", ai_stream | cs_stream)