import os
from random import choice
import time
from .models import Cake
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s - %(message)s',
)

logs = []

def get_random_cake_instance():

    all_cake_names = Cake.objects.values_list('name', flat=True)

    num_choices = 1000

    counts = {cake: 0 for cake in all_cake_names}

    for i in range(num_choices):
        chosen_cake = choice(all_cake_names)
        logs.append(f'{time.asctime()} - {os.path.basename(__file__)} - J Bakers Chose: {chosen_cake}')
        counts[chosen_cake] += 1

    selected_cake = max(counts.keys())

    result = []

    for cake, count in counts.items():
        result.append(f'{cake} was selected: {count} times')

    random_cake_instance = Cake.objects.get(name=selected_cake)

    return random_cake_instance, result, str(max(counts.values())), logs