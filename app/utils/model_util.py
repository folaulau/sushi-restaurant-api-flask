from re import sub

def to_dic_dto(model):
    dic = model.to_dict()
    return convert_dict_keys_to_camel_case(dic)

def to_dic_dto_list(models):
    dicts = []
    for model in models:
        dicts.append(to_dic_dto(model))
    return dicts

def camel_case(s):
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])

def convert_dict_keys_to_camel_case(dic):
    return dict((camel_case(k), v) for k, v in dic.items())