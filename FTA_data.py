# FTA - data file



# product name

specie_list = ['Poultry',
               'Swine',
               'Ruminants',
               'Silage',
               'Other',
               ]



product_list = ['Gallipro',
                'Gallipro Tect',
                'Gallipro MS',
                'Gallipro FIT',
                'Bioplus',
                'Solpreme',
                'Everest',
                'Bovacilus',
                'Bovacilus 2',
                'Bovacilus 3',
                'Silage 0',
                'Silage 1',
                'Silage 2',
                'Silage 3',
                'Silage 4',
                ]

product_segment_dict = {
     'Gallipro': ['broiler', 'layers', 'breeders'],
     'Gallipro Tect': ['broiler', 'layers', 'breeders'],
     'Gallipro MS':  ['broiler', 'layers', 'breeders', 'Turkeys'],
     'Gallipro FIT':  ['broiler', 'layers', 'breeders', 'Turkeys'],
     'Bioplus':  ['broiler', 'layers', 'breeders', 'Turkeys'],

               }



def take_product(option):
    if option == 1:
        product = [product_list[0],
                   product_list[1],
                   product_list[2],
                   product_list[3],
                   ]

    elif option == 2:
        product = [product_list[4],
                   product_list[5],
        ]

    elif option == 3:
        product = [product_list[4],
                   product_list[5],
                   product_list[6],
                   ]

    elif option == 4:
        product = [product_list[7],
                   product_list[8],
                   product_list[9],
                   ]
    elif option == 5:
        product = [product_list[10],
                   product_list[11],
                   product_list[12],
                   product_list[13],
                   ]

    return product



a = product_list[2]

print(product_segment_dict[a])