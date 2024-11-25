import json
l=[]
s=[]
with open("C:/zta-automation/zero-analytics-automation/AnalyticsBackend/resources/result/pcs/l2_l4_application_overlay_filter.json", "r") as f:
    a=f.read()
    res = json.loads(a)
    # print(res.keys())
    for i in res.keys():
        if 'top_vdi_apps' in i and 'table'   in i:
            l.append(i)
print(l)
# top_sessions= ['pcs_connected_users_in_last_one_hour_top_sessions', 'pcs_connected_users_in_last_one_hour_top_sessions_table', 'pcs_connected_users_in_more_than_one_day_top_sessions', 'pcs_connected_users_in_more_than_one_day_top_sessions_table', 'pcs_non_compliance_users_top_sessions', 'pcs_non_compliance_users_top_sessions_table', 'pcs_users_from_most_busy_gateway_top_sessions', 'pcs_users_from_most_busy_gateway_top_sessions_table', 'pcs_users_from_least_busy_gateway_top_sessions', 'pcs_users_from_least_busy_gateway_top_sessions_table']
# for i in l:
#     if 'table'   in i and 'pre_auth' not in i:
#         s.append(i)
# print(s)

