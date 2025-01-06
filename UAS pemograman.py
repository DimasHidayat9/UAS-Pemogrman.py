# Class untuk data barang
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        else:
            return False

# Class untuk proses transaksi
class Transaction:
    def __init__(self):
        self.cart = []
        self.total_price = 0

    def add_to_cart(self, product, quantity):
        if product.reduce_stock(quantity):
            self.cart.append((product, quantity))
            self.total_price += product.price * quantity
        else:
            raise ValueError("Stok barang tidak mencukupi!")

    def print_receipt(self):
        print("\n--- Struk Pembelian ---")
        for item, quantity in self.cart:
            print(f"{item.name} x{quantity} - Rp{item.price * quantity}")
        print(f"Total: Rp{self.total_price}")
        print("-----------------------")

# Class untuk menampilkan menu
class View:
    @staticmethod
    def display_products(products):
        print("\nDaftar Barang Toko Elektronik:")
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product.name} - Rp{product.price} (Stok: {product.stock})")

    @staticmethod
    def get_user_input():
        try:
            product_choice = int(input("Pilih nomor barang: "))
            quantity = int(input("Jumlah barang: "))
            return product_choice, quantity
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            return None, None

# Main program
if __name__ == "__main__":
    # Data barang
    products = [
        Product("Laptop", 7000000, 15),
        Product("Smartphone", 3000000, 12),
        Product("Headset", 200000, 10),
        Product("Televisi", 3000000, 15),
        Product("Speaker", 500000, 6),
        Product("PlayStation 5", 12000000, 12)
    ]

    transaction = Transaction()

    while True:
        try:
            View.display_products(products)
            choice, quantity = View.get_user_input()

            if choice is None or quantity is None:
                continue

            if 1 <= choice <= len(products):
                selected_product = products[choice - 1]
                transaction.add_to_cart(selected_product, quantity)
                print(f"{selected_product.name} sebanyak {quantity} berhasil ditambahkan ke keranjang.")
            else:
                print("Pilihan barang tidak valid.")

            more = input("Tambah barang lagi? (y/n): ").lower()
            if more != 'y':
                break
        except ValueError as e:
            print(f"Error: {e}")

    # Menampilkan struk
    transaction.print_receipt()