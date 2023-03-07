from pysnipeit import SnipeIT
snipe = SnipeIT()

infra = {
        'manufacturers':         
            {
                'name': 'AWS',
            },
        'categories':
            {
                'name': 'Cloud',
                'category_type': 'asset',
                
            },
        'models':
            {
                'name': 'AWS EC2',
                
            },
        'fieldsets':
            {
                'name':'Computers'
            },
        'fields':
            [{
                'name':'OS',
                'element': 'text',
                'format' : 'ANY'
            },
            {
                'name':'ip',
                'element': 'text',
                'format' : 'IP'
            },
            {
                'name':'software',
                'element': 'text',
                'format' : 'ANY'
            },
            {
                'name':'aws_ami_id',
                'element': 'text',
                'format' : 'ANY'
            },
             {
                'name':'aws_vpc_id',
                'element': 'text',
                'format' : 'ANY'
            },
            {
                'name':'mac_address',
                'element': 'text',
                'format' : 'ANY'
            },
            {
                'name':'sources',
                'element': 'text',
                'format' : 'ANY'
            },
            ]
        }


def add_field(data):
    fields = [snipe.fields.update(field) for field in data]
    fieldsets = next(i for i in snipe.fieldsets.list() if i['name'] == infra['fieldsets']['name'])
    for field in fields:
        snipe.fields.associate(field_id=field['id'], fieldset_id=fieldsets['id'])
    

def main():
    manufacturers = snipe.manufacturers.update(infra.get('manufacturers'))    
    categories = snipe.categories.update(infra.get('categories'))  
    fields = [snipe.fields.update(field) for field in infra.get('fields')]
    fieldsets = snipe.fieldsets.update(infra.get('fieldsets'))
    for field in fields:
        snipe.fields.associate(field_id=field['id'], fieldset_id=fieldsets['id'])
    infra['models']['category_id'] = categories['id']
    infra['models']['manufacturer_id'] =manufacturers['id']
    infra['models']['fieldset_id'] = fieldsets['id']
    models = snipe.models.update(infra.get('models'))
    print(f'Completed: {manufacturers=} {categories=} {fields=} {fieldsets=} {models=}')
    

if __name__ == '__main__':
    main()
    print('Done')
