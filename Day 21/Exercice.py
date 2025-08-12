class Statistique:
    def __init__(self, data):
        self.data = sorted(data)
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum() / self.count()
    
    def median(self):
        n = self.count()
        if n % 2 == 1:
            return self.data[n//2]
        else:
            return (self.data[n//2 - 1] + self.data[n//2]) / 2
    
    def mode(self):
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
        
        max_count = max(frequency.values())
        modes = [(value, count) for value, count in frequency.items() if count == max_count]
        
        if len(modes) == 1:
            return modes[0]
        else:
            return modes
    
    def var(self):
        mean = self.mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]
        return sum(squared_diffs) / (self.count() - 1)  # Variance corrigée (n-1)
    
    def std(self):
        return self.var() ** 0.5
    
    def freq_dist(self):
        frequency = {}
        for value in self.data:
            frequency[value] = frequency.get(value, 0) + 1
        
        total = self.count()
        freq_dist = [(count/total * 100, value) for value, count in frequency.items()]
        return sorted(freq_dist, reverse=True)
    
    def describe(self):
        mode_result = self.mode()
        if isinstance(mode_result, tuple):
            mode_str = f"({mode_result[0]}, {mode_result[1]})"
        else:
            mode_str = str(mode_result)
        
        return f"""Count: {self.count()}
Sum: {self.sum()}
Min: {self.min()}
Max: {self.max()}
Range: {self.range()}
Mean: {self.mean():.1f}
Median: {self.median()}
Mode: {mode_str}
Variance: {self.var():.1f}
Standard Deviation: {self.std():.1f}
Frequency Distribution: {self.freq_dist()}"""


# Données d'exemple
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# Création de l'objet Statistique
data = Statistique(ages)

# Affichage des résultats
print('count:', data.count())          # 25
print('sum:', data.sum())              # 744
print('min:', data.min())              # 24
print('max:', data.max())              # 38
print('range:', data.range())          # 14
print('mean:', data.mean())            # 29.76
print('median:', data.median())        # 29
print('mode:', data.mode())            # (26, 5)
print('std:', data.std())              # 4.2
print('var:', data.var())              # 17.5
print('freq_dist:', data.freq_dist())  # [(20.0, 26), (16.0, 27), ...]

print("\nDescription complète:")
print(data.describe())