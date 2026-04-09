# Pet Vet - Pet Management & Service Platform

Pet Vet is a comprehensive Django-based web application designed to bridge the gap between pet owners and professional pet service providers.

## 🐾 Features

- **For Customers**:
  - Book **Veterinary Doctors** at clinics.
  - Book **Professional Dog Walkers** with specific hourly services (e.g., Morning Walk, Park Run).
  - Book **Pet Care Centers** for boarding and services.
  - Adopt pets from verified shops.
  - Purchase pet products online.
  - Track booking history and status.
  - Provide feedback to service providers.

- **For Service Providers (Dog Walkers, Clinics, Shops, Care Centers)**:
  - Register and manage profiles (subject to admin approval).
  - List personalized services and rates.
  - Manage incoming booking requests (Accept/Reject).
  - Track completed walks and paid services.

- **For Admin**:
  - Approve or Reject new health/service providers.
  - Manage user accounts and content.
  - Monitor complaints and feedback.

## 🛠️ Technology Stack

- **Backend**: Django (Python)
- **Database**: SQLite (Development)
- **Frontend**: HTML5, Vanilla CSS, JavaScript, Bootstrap
- **Icons**: Font Awesome

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Django 5.x

### Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VishnuSuresh0204/Pet_Vet.git
   cd Pet_Vet
   ```

2. **Database Setup**:
   ```bash
   python manage.py makemigrations petvetapp
   python manage.py migrate
   ```

3. **Running the Application**:
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.

## 🛤️ Recent Updates

- **Service Selection**: Customers can now choose specific service types when booking dog walkers.
- **Dynamic Pricing**: Booking costs are automatically calculated based on duration and chosen service rates.
- **Visibility Control**: Only admin-approved providers are visible to customers in their dashboards.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
