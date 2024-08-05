cisco = [1,2,3]
juniper = [3,4,5]
ivanti = [6,7,8]

new_dict={}
new_dict["cisco_mon"] = cisco[0]
new_dict["juniper_mon"] =  juniper[0]
new_dict["ivanti_mon"] =  ivanti[0]

# week_days = ['mon', 'tues', 'wed']
# comp = ['cisco', 'juniper', 'ivanti']
#
# for i in week_days:
#     for j in comp:
#         new_dict[week_days[i]] = comp[i]

print(new_dict)
final_dict = {}
sorted_value = sorted(new_dict.values())
sorted_value_rev = sorted_value[-1]
for j in new_dict.keys():
    if new_dict[j] == sorted_value_rev:
        final_dict[j] = sorted_value_rev
print(final_dict)

