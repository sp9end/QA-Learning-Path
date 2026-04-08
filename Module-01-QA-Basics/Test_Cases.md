# Test Cases: SauceDemo - Authentication

| ID | Title | Steps | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC-001** | Successful Login | 1. Open https://www.saucedemo.com/ <br> 2. Enter `standard_user` <br> 3. Enter `secret_sauce` <br> 4. Click Login | User is redirected to `/inventory.html` and sees the "Products" title. |
| **TC-002** | Login with Locked User | 1. Open SauceDemo <br> 2. Enter `locked_out_user` <br> 3. Enter `secret_sauce` <br> 4. Click Login | Error message is displayed: "Epic sadface: Sorry, this user has been locked out." |
| **TC-003** | Login with Invalid Password | 1. Open SauceDemo <br> 2. Enter `standard_user` <br> 3. Enter `wrong_password` <br> 4. Click Login | Error message is displayed regarding invalid credentials. |