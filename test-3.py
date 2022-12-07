component = {'component': {'key': 'xss-checker-1', 'name': 'xss-checker-1', 'qualifier': 'TRK', 'measures': [{'metric': 'security_hotspots_reviewed_status', 'value': '10', 'bestValue': True}]}}
# component = {'component': {'key': 'xss-checker-1', 'name': 'xss-checker-1', 'qualifier': 'TRK', 'measures': [{'metric': 'quality_gate_details', 'value': '{"level":"OK","conditions":[{"metric":"bugs","op":"GT","error":"1","actual":"1","level":"OK"},{"metric":"new_code_smells","op":"GT","period":1,"error":"200","actual":"0","level":"OK"}],"ignoredConditions":false}'}]}}
# component = {'component': {'key': 'xss-checker-1', 'name': 'xss-checker-1', 'qualifier': 'TRK', 'measures': [{'metric': 'new_uncovered_conditions', 'periods': [{'index': 1, 'value': '0', 'bestValue': True}], 'period': {'index': 1, 'value': '0', 'bestValue': True}}]}}
measures = component['component']['measures'][0]
if 'value' in measures:
    try:
        value = measures['value']
    except (KeyError, IndexError, NameError) as error:
        value = None
elif 'periods' in measures:
    try:
        value = measures['periods'][0]['value']
    except (KeyError, IndexError, NameError) as error:
        value = None

print(type(value))