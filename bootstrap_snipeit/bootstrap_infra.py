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
    infra['models']['category_id'] = categories['id']
    infra['models']['manufacturer_id'] =manufacturers['id']
    models = snipe.models.update(infra.get('models'))
    fields = snipe.fields.update(infra.get('fields'))
    fieldsets = snipe.fieldsets.update(infra.get('fieldsets'))
    snipe.fields.associate(fieldsets['id'])
    print(f'Completed: {manufacturers=} {categories=} {models=}')
    

if __name__ == '__main__':
    main()
    print('Done')
