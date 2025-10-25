#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Setup Django
django.setup()

from listings.models import Product

def create_test_products():
    try:
        print("Creating test products...")
        
        # Create a few test products
        products_data = [
            {
                'name': 'iPhone 15 Pro',
                'description': 'Latest Apple iPhone with advanced camera system',
                'tags': ['electronics', 'smartphone', 'apple'],
                'price': 999.99,
                'rating': 4.5,
                'store': 'Apple Store'
            },
            {
                'name': 'Nike Air Max 90',
                'description': 'Classic sneakers with Air Max cushioning',
                'tags': ['shoes', 'nike', 'sneakers'],
                'price': 120.00,
                'rating': 4.2,
                'store': 'Nike'
            },
            {
                'name': 'MacBook Air M3',
                'description': 'Lightweight laptop with M3 chip',
                'tags': ['laptop', 'apple', 'computer'],
                'price': 1199.99,
                'rating': 4.7,
                'store': 'Apple Store'
            }
        ]
        
        created_products = []
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                print(f"✓ Created: {product.name}")
            else:
                print(f"- Already exists: {product.name}")
            created_products.append(product)
        
        # Show all products
        all_products = Product.objects.all()
        print(f"\n📦 Total products in database: {all_products.count()}")
        for product in all_products:
            print(f"  - {product.name} (${product.price}) - {product.store}")
            
        print(f"\n🎉 Test data created! Check your Supabase Table Editor now!")
        print(f"   Look for the 'listings_product' table in Supabase dashboard")
        
    except Exception as e:
        print(f"❌ Error creating test data: {e}")
        return False
        
    return True

if __name__ == "__main__":
    create_test_products()