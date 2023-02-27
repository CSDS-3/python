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
        'fieldset':
            {
                'name':'Computers'
            },
        'fields':
            {
                'name':'OS',
                'element': 'text',
                'format' : 'ANY'
            }
        }

def main():
    manufacturers = snipe.manufacturers.update(infra.get('manufacturers'))    
    categories = snipe.categories.update(infra.get('categories'))  
    fields = snipe.fields.update(infra.get('fields'))
    fieldsets = snipe.fieldsets.update(infra.get('fieldsets'))
    snipe.fields.associate(fieldsets['id'])
    infra['models']['category_id'] = categories['id']
    infra['models']['manufacturer_id'] =manufacturers['id']
    infra['models']['fieldset_id'] = fieldsets['id']
    models = snipe.models.update(infra.get('models'))
    print(f'Completed: {manufacturers=} {categories=} {fields=} {fieldsets=} {models=}')
    

if __name__ == '__main__':
    main()
    print('Done')
