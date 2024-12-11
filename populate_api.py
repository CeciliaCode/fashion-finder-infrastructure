import requests
import time

# Base API URL
BASE_URL = "http://fashionfinder.ddns.net"

# Delay in seconds between requests
DELAY = 2

# Sample data for users, categories, stores, branches, and products
USERS = [
    {"email": "user1@example.com", "password": "password123", "name": "User One", "role": "client", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/800px-User_icon_2.svg.png"},
    {"email": "user2@example.com", "password": "password123", "name": "User Two", "role": "client", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/800px-User_icon_2.svg.png"},
    {"email": "admin@example.com", "password": "adminpassword", "name": "Admin User", "role": "admin", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/800px-User_icon_2.svg.png"}
]

CATEGORIES = [
    {"name": "Fast Fashion", "description": "Affordable, trendy fashion.", "image": "https://www.thegreensideofpink.com/wp-content/uploads/2024/09/shein-fast-fashion.jpg"},
    {"name": "Luxury Fashion", "description": "High-end designer brands.", "image": "https://chiclymag.com/wp-content/uploads/2024/09/luxury-fashion-brands-1024x585.png"},
    {"name": "Sportswear", "description": "Casual and athletic wear.", "image": "https://youraverageguystyle.com/wp-content/uploads/2023/12/5-Ways-To-Mix-Sportswear-And-Fashion-1.jpg"}
]

STORES = [
    {"name": "H&M", "description": "Trendy and affordable clothing.", "category_id": None, "main_address": "Plaza Mayor, León, Gto.", "main_phone": "477-123-4567", "website": "https://hm.com", "image": "https://cdn.milenio.com/uploads/media/2021/02/26/apertura-tiendas-camino-facil-mejores_0_26_978_608.jpg"},
    {"name": "Versace", "description": "Luxury designer fashion.", "category_id": None, "main_address": "Centro Max, León, Gto.", "main_phone": "477-987-6543", "website": "https://versace.com", "image": "https://www.versace.com/dw/image/v2/BGWN_PRD/on/demandware.static/-/Library-Sites-ver-library/default/dw90f21a1e/images/world-of-versace/sustainability/wovclp-sustainability-art4-01-01-img_240418-mob.jpg"},
    {"name": "Adidas", "description": "Premium sportswear and casual clothing.", "category_id": None, "main_address": "Altacia, León, Gto.", "main_phone": "477-555-1234", "website": "https://adidas.com", "image": "https://www.palco23.com/thumb/eyJ0IjoiZCIsInciOjEyMDAsImgiOjY3NSwibSI6MSwidiI6IjEuMS43MSJ9/files/2020/19_redaccion/equipamiento/adidas/adidas-outlet-948.jpg"}
]

BRANCHES = [
    {"store_id": None, "name": "H&M Plaza Mayor", "address": "Blvd. Juan Alonso de Torres Pte. 2002, León, Gto.", "latitude": 21.133775, "longitude": -101.685872, "services": ["Clothing", "Accessories"], "schedules": {"monday": {"open": "10:00", "close": "21:00"}}, "image": "https://zonafranca.mx/wp-content/uploads/2024/10/IMG_20241003_191322_060.jpg"},
    {"store_id": None, "name": "Versace Centro Max", "address": "Blvd. Adolfo López Mateos 2510, León, Gto.", "latitude": 21.134169, "longitude": -101.696785, "services": ["Designer Clothing", "Luxury Accessories"], "schedules": {"monday": {"open": "11:00", "close": "20:00"}}, "image": "https://lasillarota.com/u/fotografias/m/2023/8/1/f850x638-471955_549444_5050.jpg"},
    {"store_id": None, "name": "Adidas Altacia", "address": "Blvd. Aeropuerto 104, León, Gto.", "latitude": 21.108588, "longitude": -101.648671, "services": ["Sportswear", "Shoes"], "schedules": {"monday": {"open": "10:00", "close": "21:00"}}, "image": "https://www.aryba.com.mx/newWeb/wp-content/uploads/2014/10/5bAltacia.jpg"}
]

PRODUCTS = [
    {"store_id": None, "name": "T-Shirt", "description": "Trendy cotton t-shirt.", "price": 299.99, "image": "https://media.karousell.com/media/photos/products/2021/9/1/hm_black_halter_top_1630467916_1896eb0e_progressive.jpg"},
    {"store_id": None, "name": "Versace Sunglasses", "description": "Luxury designer sunglasses.", "price": 3999.99, "image": "https://images-cdn.ubuy.co.in/650b26e0d03c3858c744d7e9-versace-ve-4361-plastic-unisex-geometric.jpg"},
    {"store_id": None, "name": "Adidas Sneakers", "description": "Comfortable running shoes.", "price": 899.99, "image": "https://m.media-amazon.com/images/I/31I+ORmDcDL._AC_.jpg"}
]

# Helper function to send POST requests with retries
def post_data(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.post(url, json=data, headers=HEADERS)
        response.raise_for_status()
        print(f"Success: {data}")
        return response.json()
    except requests.RequestException as e:
        print(f"Error posting to {url}: {e}")
        return None

# Populate the API with sample data
def populate_data():
    # Add users
    for user in USERS:
        post_data("/users/register", user)
        time.sleep(DELAY)

    # Add categories
    category_ids = []
    for category in CATEGORIES:
        response = post_data("/categories/", category)
        if response:
            category_ids.append(response["_id"])
        time.sleep(DELAY)

    # Add stores
    store_ids = []
    for i, store in enumerate(STORES):
        store["category_id"] = category_ids[i]
        response = post_data("/stores/", store)
        if response:
            store_ids.append(response["_id"])
        time.sleep(DELAY)

    # Add branches
    for i, branch in enumerate(BRANCHES):
        branch["store_id"] = store_ids[i]
        post_data("/branches/", branch)
        time.sleep(DELAY)

    # Add products
    for i, product in enumerate(PRODUCTS):
        product["store_id"] = store_ids[i]
        post_data("/products/", product)
        time.sleep(DELAY)

if __name__ == "__main__":
    populate_data()
