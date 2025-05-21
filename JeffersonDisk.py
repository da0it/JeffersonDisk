import random

class JeffersonCipher:
    def __init__(self, num_disks=36):
        self.num_disks = num_disks
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        # Создаем диски с уникальными перестановками алфавита
        self.disks = []
        for _ in range(num_disks):
            disk = self.alphabet.copy()
            random.shuffle(disk)
            self.disks.append(disk)
        
        # Сохраняем начальный порядок дисков как часть ключа
        self.disk_order = list(range(num_disks))
        random.shuffle(self.disk_order)
    
    def set_disk_order(self, order):
        if len(order) == self.num_disks:
            self.disk_order = order.copy()
    
    def get_key(self):
        return self.disk_order.copy()
    
    def encrypt(self, plaintext, key_row):
        plaintext = plaintext.upper()
        ciphertext = []
        
        for i, char in enumerate(plaintext):
            # Выбираем диск согласно порядку
            disk_idx = self.disk_order[i % self.num_disks]
            disk = self.disks[disk_idx]
            
            if char in disk:
                # Находим символ в выбранной строке (без сдвига!)
                cipher_char = disk[key_row % len(disk)]
            else:
                cipher_char = char
            
            ciphertext.append(cipher_char)
        
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext, key_row):
        return self.encrypt(ciphertext, key_row)
    
    def display_disks(self):
        print(f"\nJefferson Cipher Disks (Order: {self.disk_order})")
        print("="*50)
        for i in self.disk_order:
            print(f"Disk {i:2d}: {' '.join(self.disks[i])}")

# Пример использования
if __name__ == "__main__":
    # Инициализация с 6 дисками (как в оригинальном устройстве)
    cipher = JeffersonCipher(6)
    
    # Сохраняем ключ (порядок дисков) для последующего использования
    secret_key = cipher.get_key()
    
    print("Original Jefferson Cipher")
    cipher.display_disks()
    
    # Шифрование
    message = "HELLO WORLD"
    key_row = 5  # Выбираем строку для шифрования (0-25)
    encrypted = cipher.encrypt(message, key_row)
    
    print("\nOriginal:", message)
    print("Encrypted:", encrypted)
    
    # Дешифрование (требует тот же порядок дисков)
    cipher.set_disk_order(secret_key)  # Восстанавливаем порядок дисков
    decrypted = cipher.decrypt(encrypted, key_row)
    
    print("Decrypted:", decrypted)