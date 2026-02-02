class TemperatureMap:
    def __init__(self, temps):
        temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19)]
    
    def c_to_f(data[0], data[1]):
        conversion = (9/5) * data[1] + 32
        return(data[0], conversion)
    lambda data: (data[0], (9/5)*data[1]+32)
    
    def conv_city_temp_C(c_to_f, temps):
        list_mapped_values = list(map(c_to_f, temps))
        return(list_mapped_values)