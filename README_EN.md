# Hotel Management System 
<img src="Image\hotel4.png">
  
<!-- <img src="Image\hotel5.png">  
<img src="Image\hotel.png"> 
<img src="Image\hotel1.png"> 
<img src="Image\hotel2.png"> 
<img src="Image\hotel3.png">  -->

# Run the application instructions

* For run You must be genrate the database 
* after that you should be give the star in github .
* go to the github repository and take the following command for  create the database go to database file .
* In customer table 11 columns are created for each customer and the customer table columns name are given in the README file upper.
  


  # SuiteSpot Hotel Management System

SuiteSpot is a comprehensive Hotel Management System built using Python and Tkinter. It provides an intuitive graphical user interface (GUI) for managing hotel operations, including customer details, room bookings, and detailed reports.

---

## Features

* **User Authentication**: Secure login and registration system with password reset functionality.
* **Customer Management**: Add, update, and manage customer details.
* **Room Booking**: Manage room bookings and availability.
* **Detailed Reports**: View and generate detailed reports for hotel operations.
* **Intuitive GUI**: User-friendly interface built with Tkinter.

---

## Prerequisites

* **Python Version**: Ensure Python 3.8 or higher is installed.
* **Database**: MySQL server for storing hotel data.
* **Dependencies**: Install required Python packages using:

  ```bash
  pip install -r requirements.txt
  ```

---

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/SuiteSpot.git
   cd SuiteSpot
   ```

2. **Set Up the Database**:
   * Import the `hotel.sql` file located in the `database/` folder into your MySQL database.
   * Update the database credentials in `login.py` if necessary.

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```bash
   python login.py
   ```

---

## File Structure

```
SuiteSpot/
├── config.py
├── CONTRIBUTING.md
├── customer.py
├── Deatail.py
├── HOWTOUSE.md
├── LICENSE
├── login.py
├── Main.py
├── PULL_REQUEST_TEMPLATE.md
├── README.md
├── README_EN.md
├── requirements.txt
├── room.py
├── database/
│   └── hotel.sql
├── Image/
│   ├── login_background.jpg
│   ├── register_background.jpg
│   ├── ... (other images)
├── report/
│   ├── Gantt Chart.xlsx
│   ├── Hotelproject1.docx
├── test/
│   ├── customer.py
│   ├── Deatail.py
│   ├── ... (other test files)
├── utils/
│   └── helper.py
```

---

## Usage

1. **Login**:
   * Run `login.py` to open the login window.
   * Use the default admin credentials:
     * Username: `admin`
     * Password: `root`

2. **Main Dashboard**:
   * Navigate through the menu to manage customers, rooms, and view reports.

3. **Register New Users**:
   * Click the `REGISTER` button on the login screen to create a new account.

4. **Forgot Password**:
   * Use the `FORGOT PASSWORD` option to reset your password.

---

## Contribution

We welcome contributions! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or support, please contact the project maintainers or open an issue in the repository.
