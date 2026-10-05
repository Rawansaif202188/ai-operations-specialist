# Browser Security Demo

A simple Flask web application demonstrating an important web security principle:

> **Hidden does not mean protected.**

The project shows why sensitive features, permissions, and data should not rely only on browser-side controls and must be verified by the server.

This demo was created as part of **Week 3 of the AI Operations Specialist Practicum**.

---

## Project Objective

The goal of this demo is to answer a simple question:

**Can we trust the browser to protect sensitive features?**

The answer is **no**.

Anything sent to the browser can potentially be inspected or modified by the user using browser developer tools.

The demo compares two approaches:

```text
❌ Client-Side Hiding

vs.

✅ Server-Side Authorization
```

---

## How the Demo Works

The application contains an **Advanced Analytics** feature intended for Pro users.

The demo starts with a Free user:

```python
current_user = {
    "name": "Rawan",
    "plan": "free"
}
```

Two different implementations are demonstrated.

---

# 1. Insecure Example — Client-Side Hiding

In the first example, the Pro data is already included in the HTML but hidden using CSS.

```html
<div id="pro-content" class="hidden">
```

The CSS rule is:

```css
.hidden {
    display: none;
}
```

The page appears to protect the feature:

```text
🔒 This feature requires a Pro subscription.
```

However, the sensitive content has already been sent to the browser.

### Bypassing the UI

Open browser DevTools:

```text
Ctrl + Shift + I
```

Then:

```text
Elements
→ Ctrl + F
→ Search: pro-content
```

Find:

```html
<div id="pro-content" class="hidden">
```

Remove:

```text
hidden
```

The browser immediately reveals:

```text
💎 PRO FEATURE UNLOCKED

Revenue Insights

Monthly Revenue: $48,250
Growth Rate: +18.4%
```

The user did not actually become a Pro user.

Only the interface was modified.

### Result

```text
Hidden ≠ Protected
```

The browser already had the data, so CSS could only hide it visually.

---

# 2. Secure Example — Server-Side Authorization

The second example does not rely on the browser to decide whether access should be allowed.

Instead, JavaScript requests the protected data from the Flask server:

```javascript
fetch("/api/pro-data")
```

The server checks the user's plan:

```python
if current_user["plan"] != "pro":
    return jsonify({
        "error": "Forbidden",
        "message": "Pro subscription required."
    }), 403
```

The authorization decision therefore happens on the **server**, not in the browser.

---

## Free User — 403 Forbidden

With the server-side user configured as:

```python
current_user = {
    "name": "Rawan",
    "plan": "free"
}
```

click:

```text
Request Secure Pro Data
```

The server rejects the request:

```text
❌ 403 FORBIDDEN

Access denied by the server.

Pro subscription required.
```

### Demo Result — Free User

When the user is on the Free plan, the server rejects the request with **403 Forbidden**.

![403 Forbidden — Server denied access](assets/403-forbidden.png)

The request can also be inspected using:

```text
DevTools
→ Network
→ pro-data
```

The HTTP response shows:

```text
Status Code: 403 Forbidden
```

Changing HTML or CSS in DevTools does not change this server decision.

---

## Pro User — 200 OK

For the second test, change the demo user's plan in `app.py`:

```python
current_user = {
    "name": "Rawan",
    "plan": "pro"
}
```

Save the file and request the secure data again
