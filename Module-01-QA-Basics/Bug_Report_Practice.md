# Bug Report: Login button is not responding

**ID:** BUG-001  
**Status:** New  
**Severity:** Critical  
**Priority:** High

## Description
User is unable to log in to the application. After clicking the "Login" button with valid credentials, nothing happens.

## Steps to Reproduce
1. Open https://www.saucedemo.com/
2. Enter `standard_user` in the Username field.
3. Enter `secret_sauce` in the Password field.
4. Click the "Login" button.

## Expected Result
User should be redirected to the inventory page (`/inventory.html`).

## Actual Result
Nothing happens. The user stays on the login page, and no error message is displayed.

## Environment
- Browser: Microsoft Edge Version 146.0.3856.97
- OS: Windows 11