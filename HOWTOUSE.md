# HOWTOUSE.md

## How to Use the SuiteSpot Hotel Management System

### Prerequisites

1. **Python Version**: Ensure you have Python 3.8 or higher installed.
2. **Dependencies**: Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   - Import the `hotel.sql` file located in the `database/` folder into your MySQL database.
   - Update the database credentials in the `login.py` file if necessary.

### Running the Application

1. **Login Window**:
   - Run the application by executing the `login.py` file:

     ```bash
     python login.py
     ```

   - Enter the username and password to log in. Default admin credentials:
     - Username: `admin`
     - Password: `root`

2. **Register New Users**:
   - Click the `REGISTER` button on the login screen to open the registration window.
   - Fill in the required details and agree to the terms and conditions to register.

3. **Forgot Password**:
   - Click the `FORGOT PASSWORD` button on the login screen.
   - Enter your email and answer the security question to reset your password.

4. **Main Dashboard**:
   - After logging in, the main dashboard will open.
   - Use the menu on the left to navigate:
     - `CUSTOMER`: Manage customer details.
     - `ROOM`: Manage room bookings.
     - `DETAIL`: View detailed reports.
     - `LOGOUT`: Exit the application.

### File Structure

- **`login.py`**: Handles user authentication and login functionality.
- **`main.py`**: Main dashboard for hotel management.
- **`customer.py`**: Manages customer-related operations.
- **`room.py`**: Handles room booking operations.
- **`Deatail.py`**: Displays detailed reports.
- **`database/hotel.sql`**: SQL file to set up the database schema.
- **`Image/`**: Contains images used in the application.

### Notes

- Ensure the `Image/` folder is in the same directory as the Python files.
- Update the database credentials in `login.py` if your MySQL setup differs.

### Troubleshooting

- **Missing Dependencies**: Run `pip install -r requirements.txt` to install missing packages.
- **Database Connection Issues**: Verify your MySQL server is running and the credentials in `login.py` are correct.
- **Image Loading Issues**: Ensure the `Image/` folder contains all required images.

### Contact

For further assistance, contact the developer or refer to the `README.md` file.
