def transform(legacy_data):
    #create a new dict 

    new_points = {}

    #cycle through legacy data 
    for point, letter in legacy_data.items():
        #cycle through each letter in the list 
        for l in letter:
            new_points[l.lower()] = point 
    print(new_points)
    
    sorted_points=dict(sorted(new_points.items()))
    print(sorted_points)
    
    
# legacy_data = {1: ['A', 'E', 'I', 'O', 'U']}
legacy_data = {
            1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
            2: ["D", "G"],
            3: ["B", "C", "M", "P"],
            4: ["F", "H", "V", "W", "Y"],
            5: ["K"],
            8: ["J", "X"],
            10: ["Q", "Z"],
        }
transform(legacy_data)