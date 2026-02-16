import statistics
class TemperatureMap:
    def __init__(self, temp, ui):
        self.temp = temp
        self.ui = ui
        
    def add_5C(ui):
        result = ui + 5
        
        return(result)
        
    temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19)]
    def create_alt_temps(self.ui):
        array_temps = []
        for ui in self.ui:
            inp = add_5c(ui)
            array_temps.append(inp)
        return(array_temps)
    
    def c_to_f(data[0], data[1]):
        conversion = (9/5) * data[1] + 32
        return(data[0], conversion)
    lambda data: (data[0], (9/5)*data[1]+32)
    
    def conv_city_temp_C(c_to_f, temps):
        list_mapped_values = list(map(c_to_f, temps))
        return(list_mapped_values)
    
    data_fuel_temps = [1.3,2.7,.8,4.3,4.1,-.1]
    def get_avg_fuel_temps(data_fuel_temps):
        avg_fuel_arr = statistics.mean(data_fuel_temps)
        return avg_fuel_arr
    def get_filtered_avg_fuel_temps(self.ui):
        result = 0
        for temp in range(len(data_fuel_temps)):
            result = filter(get_avg_fuel_temps, data_fuel_temps)
        return result
    def remove_missing_data(data):
        cleaned_data = list(filter(None, data))
        return cleaned_data
    
    if __name__ == "__main__":
        try:
            user_input = int(input("Please input a celsius temperature: "))
            obj_instance = TemperatureMap()
            result_final = obj_instance.c_to_f(34,52)
        except ValueError:
            return("This is not a number, either int or double, try again.")
        
        