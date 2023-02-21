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
                
            }
        }

def main():
    manufacturers = snipe.manufacturers.update(infra.get('manufacturers'))    
    categories = snipe.categories.update(infra.get('categories'))  
    infra['models']['category_id'] = categories['id']
    infra['models']['manufacturer_id'] =manufacturers['id']
    models = snipe.models.update(infra.get('models'))
    

if __name__ == '__main__':
    main()
    print('Done')
