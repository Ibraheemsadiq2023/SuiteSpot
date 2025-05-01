# CONTRIBUTING.md

## Contributing to SuiteSpot Hotel Management System

Thank you for considering contributing to SuiteSpot! We welcome contributions from the community to improve and enhance the project. Please follow the guidelines below to ensure a smooth contribution process.

### How to Contribute

1. **Fork the Repository**:
   - Click the "Fork" button on the top-right corner of the repository page to create your own copy of the project.

2. **Clone the Repository**:
   - Clone your forked repository to your local machine:

     ```bash
     git clone https://github.com/your-username/SuiteSpot.git
     ```

3. **Set Up the Development Environment**:
   - Navigate to the project directory:

     ```bash
     cd SuiteSpot
     ```

   - Install the required dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Set up the database by importing the `hotel.sql` file located in the `database/` folder into your MySQL database.

4. **Create a New Branch**:
   - Create a new branch for your feature or bug fix:

     ```bash
     git checkout -b feature-or-bugfix-name
     ```

5. **Make Changes**:
   - Implement your changes in the appropriate files.
   - Ensure your code follows the project's coding standards and is well-documented.

6. **Test Your Changes**:
   - Run the application to ensure your changes work as expected:

     ```bash
     python login.py
     ```

   - If applicable, add or update tests in the `test/` directory and run them.

7. **Commit Your Changes**:
   - Stage your changes:

     ```bash
     git add .
     ```

   - Commit your changes with a descriptive message:

     ```bash
     git commit -m "Add feature or fix bug: description of changes"
     ```

8. **Push Your Changes**:
   - Push your branch to your forked repository:

     ```bash
     git push origin feature-or-bugfix-name
     ```

9. **Create a Pull Request**:
   - Go to the original repository and click the "New Pull Request" button.
   - Select your branch and provide a clear description of your changes.

### Contribution Guidelines

- **Code Style**: Follow Python's PEP 8 guidelines for code style.
- **Documentation**: Ensure all new features and changes are well-documented.
- **Testing**: Add or update tests for your changes and ensure all tests pass.
- **Commit Messages**: Use clear and descriptive commit messages.

### Reporting Issues

If you encounter any issues or bugs, please report them by creating a new issue in the repository. Provide as much detail as possible, including steps to reproduce the issue and any relevant screenshots or logs.

### Contact

If you have any questions or need further assistance, feel free to contact the project maintainers or open a discussion in the repository.

Thank you for contributing to SuiteSpot!
