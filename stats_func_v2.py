import numpy as np
from scipy import stats 

def calculate_statistics(array: np.array) -> np.array:
    """Вычисляет среднее, медиану, стандартное отклонение, моду и размах
    
    Параметры
    array(np.array): Входной массив
    
    Возвращает:
    dict: Возвращает словарь со статистическими показателями
    """
    mean_value=np.mean(array)
    median_value=np.median(array)
    std_dev=np.std(array)
    mode_val=stats.mode(array)[0] #Возвращает моду и количество
    range_val=np.ptp(array)
    
    return {'mean': mean_value, 
            'median': median_value,
            'std_dev': std_dev,
            'mode': mode_val,
            'range': range_val}            
def filter_greater_then_mean(array):
    """Фильтрует элементы массива, которые больше среднего.
    Параметры:
    array(np.array): Входной массив
    ВозвращаетЖ
    np.array Отфильтрованный массив 
    """
    
    mean_val=np.mean(array)
    filtered_array=array[array>mean_val]
    return filtered_array
    
if __name__ =='_main_'
 #Создаем массив чисел
data = np.array([1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10])
#Вызываем функцию для вычисления статистики
stats_result=calculate_statistics(data)
#Вызываем функцию для фильтрации
filtered_data = filter_greater_then_mean(data)
#Печатаем результат
print('Статистические результаты:')
for key, value in stats_result.items():
    print(f"{key.capitalize()}: {value}")
    
print('Отфильтрованный массив:', filtered_data)
    
    
