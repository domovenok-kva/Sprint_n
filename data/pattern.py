import re
class Pattern:
    price_pattern_for_route_pg = r'~\s*(\d+)\s*руб\.'
    time_pattern_for_route_pg = r'в пути\s*(\d+)\s*мин\.?'
    price_pattern_for_taxi_pg = r'~\s*(\d+)\s*₽\.'