import torch
import torch.nn as nn

# Определение простой нейросети
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(3, 10)
        self.fc2 = nn.Linear(10, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Создание экземпляра нейросети
model = SimpleNN()

# Определение входных данных
input_data = torch.tensor([1.0, 2.0, 3.0])

# Подача данных через нейросеть
output = model(input_data)

# Вывод результата
print("Результат:", output)
