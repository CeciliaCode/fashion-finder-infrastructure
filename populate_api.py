USERS = [
    {"email": "swearsweepfilter@gmail.com", "password": "password123", "name": "John Doe", "role": "user", "image": "https://www.cameo.com/cdn-cgi/image/fit=cover,format=auto,width=500,height=500/https://cdn.cameo.com/resizer/EB2otn6YJ_avatar-1687038155759.jpg"},
    {"email": "mpb74513@lasallebajio.edu.mx", "password": "password123", "name": "Miguel Gómez", "role": "user", "image": "https://i1.rgstatic.net/ii/profile.image/1092300918792198-1637436241940_Q512/Miguel-Gomez-Diaz.jpg"},
    {"email": "cecilia.pena.software@gmail.com", "password": "adminpassword", "name": "Admin", "role": "admin", "image": "https://images.generated.photos/821-VtXMXirBLBtKIs89jvVIeumCf_FkCzv2S0ImS1E/rs:fit:256:256/czM6Ly9pY29uczgu/Z3Bob3Rvcy1wcm9k/LnBob3Rvcy92M18w/MTg4MzMwLmpwZw.jpg"}
]

CATEGORIES = [
    {"name": "Moda rápida", "description": "Moda accesible en tendencia. ", "image":"https://www.thegreensideofpink.com/wp-content/uploads/2024/09/shein-fast-fashion.jpg"},
    {"name": "Moda de lujo", "description": "Marcas de diseñador de alta gama.", "image": "https://chiclymag.com/wp-content/uploads/2024/09/luxury-fashion-brands-1024x585.png"},
    {"name": "Moda deportiva", "description": "Vestimenta atlética y casual.", "image": "https://youraverageguystyle.com/wp-content/uploads/2023/12/5-Ways-To-Mix-Sportswear-And-Fashion-1.jpg"}
]

STORES = [
    {"name": "H&M", "description": "Ropa en tendencia.", "category_id": "675a02d082c4433d9f9cf55b", "main_address": "Plaza Mayor, León, Gto.", "main_phone": "800-040-8555", "website": "https://www2.hm.com/es_mx/", "image": "https://media.fashionnetwork.com/cdn-cgi/image/format=auto/m/3119/9a5d/6f3d/f577/4a55/e329/ad41/7f26/a7be/c2de/c2de.png"},
    {"name": "Versace", "description": "Ropa lujosa.", "category_id": "675a02e982c4433d9f9cf55d", "main_address": "Centro Max, León, Gto.", "main_phone": "477-771-7361", "website": "https://www.versace.com/mx/es/", "image": "https://www.versace.com/dw/image/v2/BGWN_PRD/on/demandware.static/-/Library-Sites-ver-library/default/dw90f21a1e/images/world-of-versace/sustainability/wovclp-sustainability-art4-01-01-img_240418-mob.jpg"},
    {"name": "Adidas", "description": "Atuendo para el ejercicio.", "category_id": "675a02fa82c4433d9f9cf55f", "main_address": "Altacia, León, Gto.", "main_phone": "669-915-5300", "website": "https://www.adidas.mx/", "image": "https://sucursales.net/wp-content/uploads/2022/01/adidas-Leon.jpg"}
]

BRANCHES = [
   {
        "store_id": "675a045482c4433d9f9cf56c",
        "name": "H&M Sucursal Plaza Mayor",
        "category_id": "675a02d082c4433d9f9cf55b", 
        "address": "Blvd. Juan Alonso de Torres 2002-Local 136, Centro Comercial, 37150 León de los Aldama, Gto.",
        "latitude": 21.162817087255277,
        "longitude": -101.69400990548503,
        "services": ["Ropa", "Accessorios"],
        "schedule": {  
            "monday": {"open": "11:00", "close": "21:00"},
            "tuesday": {"open": "11:00", "close": "21:00"},
            "wednesday": {"open": "11:00", "close": "21:00"},
            "thursday": {"open": "11:00", "close": "21:00"},
            "friday": {"open": "11:00", "close": "21:00"},
            "saturday": {"open": "11:00", "close": "21:00"},
            "sunday": {"open": "11:00", "close": "21:00"}
        }
    },
    {
        "store_id": "675a045482c4433d9f9cf56c",
        "name": "H&M Sucursal Aeropuerto",
        "category_id": "675a02d082c4433d9f9cf55b", 
        "address": "Blvd. Aeropuerto #104 Local L-1002, 37545 León de los Aldama, Gto.",
        "latitude": 21.096527387122183,
        "longitude": -101.62397206390762,
        "services": ["Ropa", "Accessorios"],
        "schedule": {  
            "monday": {"open": "11:00", "close": "21:00"},
            "tuesday": {"open": "11:00", "close": "21:00"},
            "wednesday": {"open": "11:00", "close": "21:00"},
            "thursday": {"open": "11:00", "close": "21:00"},
            "friday": {"open": "11:00", "close": "21:00"},
            "saturday": {"open": "11:00", "close": "21:00"},
            "sunday": {"open": "11:00", "close": "21:00"}
        }
    },
    {
        "store_id": "675a04b782c4433d9f9cf56e",
        "name": "Versace Sucursal Centro Max",
        "category_id": "675a02e982c4433d9f9cf55d",  
        "address": "Blvd. Adolfo López Mateos 2518, Jardines de Jerez, 37530 León de los Aldama, Gto.",
        "latitude": 21.100178206458992,
        "longitude": -101.63575481398323,
        "services": ["Ropa de diseñador", "Accesorios de lujo"],
        "schedule": {  
            "monday": {"open": "10:00", "close": "21:00"},
            "tuesday": {"open": "10:00", "close": "21:00"},
            "wednesday": {"open": "10:00", "close": "21:00"},
            "thursday": {"open": "10:00", "close": "21:00"},
            "friday": {"open": "10:00", "close": "21:00"},
            "saturday": {"open": "10:00", "close": "21:00"},
            "sunday": {"open": "10:00", "close": "21:00"}
        }
    },
      {
        "store_id": "675a04b782c4433d9f9cf56e",
        "name": "Versace Sucursal Palacio de Hierro",
        "category_id": "675a02e982c4433d9f9cf55d",  
        "address": "Cerro Gordo, Blvd. Casa de Piedra esquina, Centro Comercial, 37150 León de los Aldama, Gto.",
        "latitude": 21.15730465952265,
        "longitude": -101.69709943323541,
        "services": ["Ropa de diseñador", "Accesorios de lujo"],
        "schedule": {  
            "monday": {"open": "11:00", "close": "21:00"},
            "tuesday": {"open": "11:00", "close": "21:00"},
            "wednesday": {"open": "11:00", "close": "21:00"},
            "thursday": {"open": "11:00", "close": "21:00"},
            "friday": {"open": "11:00", "close": "21:00"},
            "saturday": {"open": "11:00", "close": "21:00"},
            "sunday": {"open": "11:00", "close": "21:00"}
        }
    },
    {
        "store_id": "675a04d682c4433d9f9cf570",
        "name": "Adidas Sucursal Altacia",
        "category_id": "675a02fa82c4433d9f9cf55f",  
        "address": "Blvd. Aeropuerto 104, Cerrito de Jerez, 37545 León de los Aldama, Gto.",
        "latitude": 21.092893510408114,
        "longitude": -101.62607016233643,
        "services": ["Ropa deportiva", "Zapatos"],
        "schedule": {  
            "monday": {"open": "11:00", "close": "20:00"},
            "tuesday": {"open": "11:00", "close": "20:00"},
            "wednesday": {"open": "11:00", "close": "20:00"},
            "thursday": {"open": "11:00", "close": "20:00"},
            "friday": {"open": "11:00", "close": "20:00"},
            "saturday": {"open": "11:00", "close": "20:00"},
            "sunday": {"open": "11:00", "close": "20:00"}
        }
    },
    {
        "store_id": "675a04d682c4433d9f9cf570",
        "name": "Adidas Sucursal Plaza Mayor",
        "category_id": "675a02fa82c4433d9f9cf55f",  
        "address": "Plaza Mayor, Blvd. Juan Alonso de Torres Pte. 2002, Centro Comercial, 37150 León de los Aldama, Gto.",
        "latitude":  21.158922066146232,
        "longitude": -101.69613149264613,
        "services": ["Ropa deportiva", "Zapatos"],
        "schedule": {  
            "monday": {"open": "11:00", "close": "21:00"},
            "tuesday": {"open": "11:00", "close": "21:00"},
            "wednesday": {"open": "11:00", "close": "21:00"},
            "thursday": {"open": "11:00", "close": "21:00"},
            "friday": {"open": "11:00", "close": "21:00"},
            "saturday": {"open": "11:00", "close": "21:00"},
            "sunday": {"open": "11:00", "close": "21:00"}
        }
    }
]

PRODUCTS = [
    {"store_id": "675a045482c4433d9f9cf56c", "name": "Playera halter", "description": "Top cropped de algodón.", "price": 199.99, "image": "https://media.karousell.com/media/photos/products/2021/9/1/hm_black_halter_top_1630467916_1896eb0e_progressive.jpg"},
    {"store_id": "675a04b782c4433d9f9cf56e", "name": "Lentes Versace", "description": "Gafas de sol.", "price": 3999.99, "image": "https://images-cdn.ubuy.co.in/650b26e0d03c3858c744d7e9-versace-ve-4361-plastic-unisex-geometric.jpg"},
    {"store_id": "675a04d682c4433d9f9cf570", "name": "Sneakers", "description": "Calzado para correr.", "price": 899.99, "image": "https://m.media-amazon.com/images/I/31I+ORmDcDL._AC_.jpg"}
]