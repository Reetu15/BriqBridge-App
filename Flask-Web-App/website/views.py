from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)
sellers = [
        {"name": "Seller 1", "image": "BUYERS/IMAGE 1.jpeg", "type": 0, "number":1},
        {"name": "Seller 2", "image": "BUYERS/IMAGE 2.jpeg", "type": 0, "number":2},
        {"name": "Seller 3", "image": "BUYERS/IMAGE 3.jpeg", "type": 0, "number":3},
        {"name": "Seller 4", "image": "BUYERS/IMAGE4.webp", "type": 0, "number":4},
    ]
    
buyers = [
        {"name": "Buyer 1", "image": "SELLERS/IMAGE1.jpeg", "type": 1, "number":5},
        {"name": "Buyer 1", "image": "SELLERS/IMAGE2.webp", "type": 1, "number":6},
        {"name": "Buyer 2", "image": "SELLERS/IMAGE3.jpeg", "type": 1, "number":7},
        {"name": "Buyer 3", "image": "SELLERS/IMAGE4.webp", "type": 1, "number":8},
    ]

@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    current_time = datetime.now()
    greeting = "Good Morning!" if current_time.hour < 12 else "Good Afternoon!" if current_time.hour < 18 else "Good Evening!"
    return render_template('index.html', greeting=greeting, sellers=sellers, buyers=buyers, user = current_user)

BUSINESS_DATA = {
    "1": {
        "id": "1",
        "name": "Sample Business 1",
        "image": "/static/images/sample1.jpg",
        "address": "123 Sample St, Sample City",
        "contact_number": "(123) 456-7890",
        "contact_email": "contact@samplebusiness1.com",
        "brochure_link": "/static/brochures/sample_brochure1.pdf",
        "deals": [
            {"title": "Deal 1", "description": "Discount on Product 1", "price": "$10"},
            {"title": "Deal 2", "description": "Special Price for Service A", "price": "$20"},
        ]
    },
    "2": {
        "id": "2",
        "name": "Sample Business 2",
        "image": "/static/images/sample2.jpg",
        "address": "456 Another St, Another City",
        "contact_number": "(987) 654-3210",
        "contact_email": "contact@samplebusiness2.com",
        "brochure_link": "/static/brochures/sample_brochure2.pdf",
        "deals": [
            {"title": "Deal A", "description": "Discount on Product A", "price": "$15"},
            {"title": "Deal B", "description": "Special Price for Service B", "price": "$25"},
        ]
    }
}

@views.route('/businesses/<business_id>')
def business_list(business_id):
    business_id = int(business_id)
    if business_id < 4: mode = sellers
    else:   mode = buyers; business_id -= 4;
    businesses = [{"id": data["id"], "name": data["name"], "image": data["image"]} for data in BUSINESS_DATA.values()]
    return render_template('business_list.html', businesses=businesses, entity = mode, ID = business_id - 1)
